import falcon
from falcon_autocrud.middleware import Middleware

from ccm import settings
from ccm.appointments.resources import AppointmentListResource
from ccm.auth.resources import AuthenticateResource
from ccm.middlewares import AuthMiddleware
from ccm.patients.resources import PatientsCreateListResource, PatientsDetailResource


def create_app(db_engine):
    api = falcon.API(middleware=[
        Middleware(),
        AuthMiddleware()
    ])

    api.add_route('/patients', PatientsCreateListResource(db_engine))
    api.add_route('/patient/{id:int}', PatientsDetailResource(db_engine))

    api.add_route('/appointments', AppointmentListResource(db_engine))
    api.add_route('/appointments/patient/{patient_id:int}', AppointmentListResource(db_engine))

    api.add_route('/auth', AuthenticateResource())

    return api


def get_app():
    db_engine = settings.db_engine
    return create_app(db_engine)
