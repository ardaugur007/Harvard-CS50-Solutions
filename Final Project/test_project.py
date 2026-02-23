from nation import Nation
from project import parse_command, calculate_defense, calculate_enemy_power
import pytest

def test_parse_command():
    assert parse_command("build 5 farms") == ("build", 5, "farm")
    assert parse_command("TRAIN 10 SOLDIERS") == ("train", 10, "soldier")
    assert parse_command("build 1 farm") == ("build", 1, "farm")
    assert parse_command("build 1 barracks") == ("build", 1, "barrack")
    assert parse_command("next") == ("next", None, None)
    assert parse_command("attack") == (None, None, None)

def test_nation_mechanics():
    n = Nation("TestLand")

    food_gain, gold_gain = n.collect_resources()
    assert n.population == 55
    assert food_gain == 50
    assert gold_gain == 50

def test_build_success():
    n = Nation("Builder")
    n.gold = 100
    n.buildings["farm"] = 0

    assert n.build("farm", 1) == True
    assert n.gold == 50
    assert n.buildings["farm"] == 1

def test_build_error():
    n = Nation("PoorLand")
    n.gold = 10

    with pytest.raises(ValueError):
        n.build("wall", 1)

    with pytest.raises(ValueError):
        n.build("skyscraper", 1)

def test_calculate_defense():
    assert calculate_defense(0, 0) == 0
    assert calculate_defense(1, 0) == 10
    assert calculate_defense(0, 1) == 50
    assert calculate_defense(2, 2) == 120

def test_calculate_enemy_power():
    assert calculate_enemy_power(50) == 100
    assert calculate_enemy_power(0) == 0
    assert calculate_enemy_power(10) == 20
