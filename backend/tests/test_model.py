import sys

sys.path.append('.')
from backend.model.submarine import Submarine
import pytest

def test_instance_submarine():
    submarine = Submarine()
    assert isinstance(submarine, Submarine)


# ATRIBUTOS
def test_latitude_attr():
    submarine = Submarine()
    assert isinstance(submarine.latitude, int)
    assert isinstance(submarine.longitude, int)
    assert isinstance(submarine.heigth, int)
    assert isinstance(submarine.direction, str)


def test_value_attr():
    submarine = Submarine()
    assert submarine.longitude == 0
    assert submarine.latitude == 0
    assert submarine.heigth == 0
    assert submarine.direction == 'NORTE'
