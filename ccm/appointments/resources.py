import falcon
from falcon_autocrud.resource import CollectionResource

from ccm.appointments.forms import validate_appointment_create
from ccm.appointments.models import Appointment


class AppointmentListView(CollectionResource):
    model = Appointment

    @falcon.before(validate_appointment_create)
    def on_post(self, req, resp, *args, **kwargs):
        return super(AppointmentListView, self).on_post(req, resp, *args, **kwargs)
