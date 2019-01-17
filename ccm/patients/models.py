from sqlalchemy import Column, Integer, String, Date
from sqlalchemy_utils import ChoiceType

from ccm.settings import Base


class Patient(Base):
    GENDER = [
        (1, 'M'),
        (2, 'F'),
        (3, '')
    ]

    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    birth_date = Column(Date, nullable=False)
    # gender = Column(ChoiceType(GENDER))

    def fullname(self):
        return u'{first_name} {last_name}}'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def __repr__(self):
        return u'<Patient(id={id}, fullname={fullname})>'.format(
            id=self.id,
            fullname=self.fullname
        )
