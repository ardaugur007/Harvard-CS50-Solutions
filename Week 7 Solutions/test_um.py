from um import count

def test_single_um():
    # Basit testler
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um") == 1

def test_embedded_um():
    # Kelime içinde geçen um'lar
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("dummy") == 0

def test_sentences():
    # Cümle içi karışık testler
    assert count("Um, thanks, um...") == 2
    assert count("hello, um, world") == 1
    assert count("Um, thanks for the album.") == 1
