from seasons import get_minutes, convert
from datetime import date

def test_get_minutes():
    date1 = date(2022, 1, 1)
    date2 = date(2023, 1, 1)
    assert get_minutes(date1, date2) == 525600

    date3 = date(2021, 1, 1)
    assert get_minutes(date3, date2) == 1051200

def test_convert():
    # Rent şarkısındaki sayı
    assert convert(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(1051200) == "One million, fifty-one thousand, two hundred minutes"
