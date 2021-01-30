import pytest
import sys
sys.path.append('.')

from backend.model.submarine import Submarine

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


# METHODS
def test_update_direction_method_invalid_parameter():
    with pytest.raises(ValueError):
        submarine = Submarine()
        submarine.update_direction('D')


def test_update_direction_method_empty_string_parameter():
    with pytest.raises(ValueError):
        submarine = Submarine()
        submarine.update_direction('')


def test_update_direction_method_int_parameter():
    with pytest.raises(ValueError):
        submarine = Submarine()
        submarine.update_direction(1)


def test_update_direction_method_without_parameter():
    with pytest.raises(ValueError):
        submarine = Submarine()
        submarine.update_direction(None)


def test_update_direction_logic_east():
    submarine = Submarine()
    submarine.update_direction('R')
    assert submarine.direction == 'LESTE'


def test_update_direction_logic_west():
    submarine = Submarine()
    submarine.update_direction('L')
    assert submarine.direction == 'OESTE'


def test_update_direction_south():
    submarine = Submarine()
    submarine.update_direction('L')
    submarine.update_direction('L')
    assert submarine.direction == 'SUL'


def test_update_direction_north():
    submarine = Submarine()
    submarine.update_direction('R')
    submarine.update_direction('L')
    assert submarine.direction == 'NORTE'
