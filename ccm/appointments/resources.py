import falcon
from falcon_autocrud.resource import CollectionResource

from ccm.appointments.forms import validate_appointment_create
from ccm.appointments.models import Appointment


class AppointmentListResource(CollectionResource):
    model = Appointment
    methods = ['GET', 'POST']

    @falcon.before(validate_appointment_create)
    def on_post(self, req, resp, *args, **kwargs):
        return super(AppointmentListResource, self).on_post(req, resp, *args, **kwargs)
