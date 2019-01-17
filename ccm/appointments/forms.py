import falcon
from wtforms import Form, ValidationError
from wtforms.ext.sqlalchemy.orm import model_form

from ccm.appointments.models import Appointment
from ccm.patients.models import Patient

from ccm.settings import session


def validate_patient(form, field):
    patient = session.query(Patient).get(field.data)
    if not patient:
        raise ValidationError('Patient with id={id} not found'.format(id=field.data))


AppointmentForm = model_form(
    Appointment,
    Form,
    field_args={
        'patient_id': {
            'validators': [
                validate_patient
            ]
        }
    },
    exclude_fk=False
)


def validate_appointment_create(req, resp, resource, params):
    data = req.context.get('doc')
    appointment_form = AppointmentForm(data=data)

    if not appointment_form.validate():
        raise falcon.HTTPBadRequest(
            'Form Validation Error',
            appointment_form.errors
        )
