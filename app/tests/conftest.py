import pytest
import tables
@pytest.fixture(scope='module')
def new_user():
    user = User('gymdude99', 'bench400soon!', 'gymdude99@gmail.com')
    return user
