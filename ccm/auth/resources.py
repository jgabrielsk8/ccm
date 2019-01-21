import jwt
import falcon
import os
import base64

SECRET = os.environ.get('JWT_SECRET', 'secret')


class AuthenticateResource(object):

    def on_post(self, req, resp, *args, **kwargs):
        auth_data = req.auth.split(' ') if req.auth else None

        if not auth_data:
            raise falcon.HTTPBadRequest

        auth_data_decoded = base64.b64decode(auth_data[1]).decode('utf-8').split(':')

        user = auth_data_decoded[0]
        pwd = auth_data_decoded[1]

        token = jwt.encode({'user': user, 'password': pwd}, SECRET, algorithm='HS256')

        resp.status = falcon.HTTP_OK
        resp.media = {
            'data': {
                'token': token.decode('utf-8')
            }
        }
