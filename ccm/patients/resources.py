import falcon
from falcon_autocrud.resource import CollectionResource, SingleResource

from ccm.patients.forms import validate_patient_create
from ccm.patients.models import Patient


class PatientsCreateListResource(CollectionResource):
    model = Patient
    methods = ['GET', 'POST']

    @falcon.before(validate_patient_create)
    def on_post(self, req, resp, *args, **kwargs):
        return super(PatientsCreateListResource, self).on_post(req, resp, *args, **kwargs)


class PatientsDetailResource(SingleResource):
    model = Patient
    methods = ['GET']
