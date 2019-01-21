from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from ccm.settings import Base


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship('Patient')
    date = Column(Date, nullable=False)

    def __repr__(self):
        return '<Appointment(id={id}, patient={patient}, date={date})>'.format(
            id=self.id,
            patient=self.patient_id,
            date=self.date
        )
