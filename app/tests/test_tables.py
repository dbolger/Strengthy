from tables import User, Workout


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check that the email, hashed_password, and role fields are defined correctly
    """
    user = User("gymdude99", "bench400soon!", "gymdude99@gmail.com")
    assert user.email == "gymdude99@gmail.com"
    assert user.password != "bench400soon!"
    # assert user.role == "user"


def test_new_workout():
    """
    GIVEN a Workout model
    WHEN a new Workout is created
    THEN check that the email, hashed_password, and role fields are defined correctly
    """

    # TODO other way to generate new user?
    user = User("gymdude99", "bench400soon!", "gymdude99@gmail.com")
    workout = Workout(
        user, "Leg Day", [{"name": "Leg Press", "sets": 4, "units": 8, "type": "reps"}]
    )

    assert workout.user_id == user.id
    assert workout.name == "Leg Day"
    # assert len(workout.exercises) == 1 TODO: how to use sqlalchemy with tests
    assert workout.exercises[0].name == "Leg Press"
