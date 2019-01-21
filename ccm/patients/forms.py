import falcon
from wtforms import Form, validators
from wtforms.ext.sqlalchemy.orm import model_form

from ccm.patients.models import Patient

PatientForm = model_form(
    Patient,
    Form,
    field_args={
        'first_name': {
            'validators': [
                validators.DataRequired()
            ]
        },
        'birth_date': {
            'validators': [
                validators.DataRequired()
            ]
        }
    }
)


def validate_patient_create(req, resp, resource, params):
    data = req.context.get('doc')
    patient_form = PatientForm(data=data)

    if not patient_form.validate():
        raise falcon.HTTPBadRequest(
            'Form Validation Error',
            patient_form.errors
        )
