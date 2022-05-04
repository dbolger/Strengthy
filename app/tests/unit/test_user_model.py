import tables
def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check that the email, hashed_password, and role fields are defined correctly
    """
    user = User('gymdude99', 'bench400soon!', 'gymdude99@gmail.com')
    assert user.email == 'gymdude99@gmail.com'
    assert user.hashed_password != 'bench400soon!'
    assert user.role == 'user'
