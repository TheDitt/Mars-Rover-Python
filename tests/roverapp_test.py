from mars_rover_python.app import RoverApp


def test_answer_failure():
    assert RoverApp.inc(3) == 5

def test_answer_pass():
    assert RoverApp.inc(4) == 5