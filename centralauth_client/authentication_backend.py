from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

import json
import urllib2

from centralauth_client import *

class CentralAuthenticationBackend(ModelBackend):

    def authenticate(self, session_key):
        """
        Return User record if central auth cookie is valid.
        Return None if no match.
        """

        # Get all the info from the central auth provider
        centralauth_provider_response = urllib2.urlopen(CENTRALAUTH_PROVIDER + 'authenticate/?session_key=' + session_key + '&service=' + CENTRALAUTH_SERVICE )

        centralauth_provider_datadict = json.loads(centralauth_provider_response.read())

        #response brought back an error
        if not "Success" in centralauth_provider_datadict['status']:
            return None

        # select the user
        user, created = User.objects.get_or_create(username=centralauth_provider_datadict['username'])

        if created:
            # Get data and save to new user
            centralauth_provider_response = urllib2.urlopen(CENTRALAUTH_PROVIDER + 'get_attributes/?session_key=' + session_key + '&service=' + CENTRALAUTH_SERVICE )
            centralauth_provider_datadict = json.loads(centralauth_provider_response.read())

            for key, value in centralauth_provider_datadict['attributes'].items():
                user.__setattr__(CENTRALAUTH_USER_ATTRIBUTES[key], value)

            user.set_unusable_password()
            user.save()

        return user
    # authenticate
# class CentralAuthenticationBackend
