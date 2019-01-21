import jwt
import falcon


class AuthMiddleware(object):
    def process_request(self, req, resp):
        token = req.get_header('Authorization')

        if not token:
            raise falcon.HTTPUnauthorized(
                'No Authentication Token Provided',
                ''
            )

        jwt_token = token.split(' ')[1]
        try:
            jwt_decoded = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            raise falcon.HTTPUnauthorized(
                'Authentication Failed',
                ''
            )
        user = jwt_decoded.get('user')
        password = jwt_decoded.get('password')

        if self.validate_user(user, password):
            # Add the user to the request and response
            setattr(req, 'user', user)
            setattr(resp, 'user', user)

    def validate_user(self, user, password):
        # We will need to add extra logic here.
        # i.e. Query the database for this user with this password
        return True
