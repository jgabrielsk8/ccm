import falcon
from falcon_autocrud.middleware import Middleware

from ccm import settings
from ccm.patients.resources import PatientsCreateListView
from ccm.appointments.resources import AppointmentListView


def create_app(db_engine):
    api = falcon.API(middleware=[Middleware()])
    api.add_route('/patients', PatientsCreateListView(db_engine))
    api.add_route('/appointments', AppointmentListView(db_engine))
    return api


def get_app():
    db_engine = settings.db_engine
    return create_app(db_engine)
