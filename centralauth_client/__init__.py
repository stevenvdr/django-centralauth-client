import settings

# Name of the centralauth cookie
CENTRALAUTH_COOKIE_NAME_DEFAULT = 'centralauth_session_key_new'
CENTRALAUTH_COOKIE_NAME = getattr(settings, 'CENTRALAUTH_COOKIE_NAME', CENTRALAUTH_COOKIE_NAME_DEFAULT)

# The fields that should be sent when a request is made
CENTRALAUTH_USER_ATTRIBUTES_DEFAULT = {
    'username':'username',
    'first_name':'first_name',
    'last_name':'last_name',
    'email':'email',
}
CENTRALAUTH_USER_ATTRIBUTES = getattr(settings, 'CENTRALAUTH_USER_ATTRIBUTES', CENTRALAUTH_USER_ATTRIBUTES_DEFAULT)

# Sites that have access to this central authentication system
CENTRALAUTH_PROVIDER_DEFAULT = "http://localhost:8000/centralauth_provider/"
CENTRALAUTH_PROVIDER = getattr(settings, 'CENTRALAUTH_PROVIDER', CENTRALAUTH_PROVIDER_DEFAULT)

# Sites that have access to this central authentication system
CENTRALAUTH_SERVICE_DEFAULT = "http://localhost:8001/"
CENTRALAUTH_SERVICE = getattr(settings, 'CENTRALAUTH_SERVICE', CENTRALAUTH_SERVICE_DEFAULT)