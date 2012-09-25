from django.contrib.auth import authenticate, login

from centralauth_client import *

class AuthenticationMiddleware(object):
    def process_request(self, request):
        """ 
        This function tries to login the given user using the central 
        authentication system, before the actual view is called.

        The authentication will happen only once, as soon as the user
        is logged in, authentication is no longer performed
        """

        # User is already logged in
        if request.user.is_authenticated():
            return None
            
        # User does not have central auth cookie
        if not CENTRALAUTH_COOKIE_NAME in request.COOKIES:
            return None
        
        # Get user data
        session_key = request.COOKIES.get(CENTRALAUTH_COOKIE_NAME)

        # Authenticate user
        user = authenticate(session_key = session_key)

        #Check if authenticated succesfully
        if user is None:
            return None

        # Login the user
        login(request, user)

    def process_response(self, request, response):
        """
        This function checks if the user is still logged in and
        makes sure the user is not logged in again unwanted
        """
        try:
            if not request.user.is_authenticated():
                response.delete_cookie(CENTRALAUTH_COOKIE_NAME)
        except AttributeError:
            pass

        return response