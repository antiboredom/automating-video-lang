import requests

TOKEN = '3424366.3d395e3.20c74391d2904f2e963f9b687051e3fe'


curl -F 'client_id=[clientID]' -F 'client_secret=[clientSecret]' -F 'grant_type=authorization_code' -F 'redirect_uri=[redirectURI]' -F 'code=[code]' https://api.instagram.com/oauth/access_token

