import pytest

from pms import APP
from pms.models import Doctor, attach_db
from pms.utils import insert_dummy_data, get_database_path


@pytest.fixture
def setup():
    attach_db(app=APP, database_path=get_database_path(testing=True))
    insert_dummy_data()


def test_doctor_get_all(setup):
    all_doctors = Doctor.query.all()
    print(all_doctors[0].to_json())
    assert len(all_doctors) == 4
