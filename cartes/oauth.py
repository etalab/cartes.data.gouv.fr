from social_core.backends.oauth import BaseOAuth2


class DataGouvOAuth2(BaseOAuth2):
    """DataGouv OAuth authentication backend"""
    name = 'datagouv'
    ACCESS_TOKEN_URL = 'https://www.data.gouv.fr/oauth/token'
    AUTHORIZATION_URL = 'https://www.data.gouv.fr/oauth/authorize'
    SCOPE_SEPARATOR = ','
    REDIRECT_STATE = False
    DEFAULT_SCOPE = ['default']
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        """Return user details from DataGouv account"""
        return {'username': response.get('first_name'),
                'email': response.get('email') or '',
                'first_name': response.get('first_name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('https://www.data.gouv.fr/api/1/me/', params={
            'access_token': access_token})
