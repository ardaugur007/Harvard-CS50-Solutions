from jar import Jar
import pytest

def test_init():
    # Varsayılan kapasite 12 mi?
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0 # Başlangıçta boş mu?

    # Farklı kapasite ile başlat
    jar2 = Jar(5)
    assert jar2.capacity == 5

    # Negatif kapasite hatası
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == "" # Boşken boş gelmeli

    jar.deposit(1)
    assert str(jar) == "🍪" # 1 kurabiyeye 1 emoji mi?

    jar.deposit(11)
    assert str(jar) == "🍪" * 12 # 12 kurabiyeye 12 emoji mi?

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5 # 5 eklendi mi?
    # Kapasite aşımı testi
    with pytest.raises(ValueError):
        jar.deposit(6) # 11 kapasiteyi aşıyor hata verdi mi?

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3 # 3 kaldı mı?

    # Yetersiz bakiye testi
    with pytest.raises(ValueError):
        jar.withdraw(4) # 3 varken 4 çekememeli
