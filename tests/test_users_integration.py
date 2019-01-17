from falcon import testing
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ccm import app

from ccm.patients.models import Patient
from ccm.settings import TEST_DB_URL, Base


class TestClass(object):
    session = None

    @pytest.fixture(autouse=True)
    def client(self, request):
        db_engine = create_engine(TEST_DB_URL)
        Base.metadata.create_all(db_engine)

        Session = sessionmaker(bind=db_engine)
        self.session = Session()

        def fin():
            Base.metadata.drop_all(db_engine)

        request.addfinalizer(fin)
        return testing.TestClient(app.create_app(db_engine))

    def test_no_patients(self, client):
        expected_json = {'data': []}

        result = client.simulate_get('/patients')

        assert result.json == expected_json

    def test_patients_success(self, client):
        expected_json = {
            "data": [
                {
                    "id": 1,
                    "first_name": "Jose",
                    "last_name": "Giron",
                    "birth_date": "1989-08-04"
                }
            ]
        }

        self.session.add(
            Patient(
                first_name='Jose',
                last_name='Giron',
                birth_date='1989-08-04'
            )
        )
        self.session.commit()
        self.session.close()

        result = client.simulate_get('/patients')

        assert result.json == expected_json

    def test_patients_form_error(self, client):
        expected_json = {
            "title": "Form Validation Error",
            "description": {
                "first_name": [
                    "This field is required."
                ]
            }
        }

        result = client.simulate_post('/patients', json={
            "first_name": "",
            "last_name": "Giron",
            "birth_date": "1989-08-04"
        })

        assert result.json == expected_json
