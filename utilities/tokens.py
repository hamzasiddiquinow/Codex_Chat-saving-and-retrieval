# # generate token and send it to the user in the response
#import simplejwt as simplejwt
#from rest_framework_simplejwt import Accesstoken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from jwt.exceptions import InvalidTokenError
# import jwt
#
# from CODEX.settings import SECRET_KEY
#
#
# def generate_jwt_tokens(user):
#     # Generate access token
#     access_token = AccessToken.for_user(user)
#
#     # Generate refresh token
#     refresh_token = RefreshToken.for_user(user)
#
#     return {
#         'access_token': str(access_token),
#         'refresh_token': str(refresh_token),
#     }
#
#
# def parse_jwt_token(token):
#     try:
#         # Decode the JWT token
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS512'])
#         user_id = decoded_token['user_id']
#
#         return user_id
#     except InvalidTokenError as e:
#         return e
