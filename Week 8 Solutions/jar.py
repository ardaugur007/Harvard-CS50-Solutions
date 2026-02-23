class Jar:
    def __init__(self, capacity = 12):
        # Kapasite negatif olamaz
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        # Değişkenleri tanımla
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Mevcut kurabiye kadar emoji döndür
        return "🍪" * self.size

    def deposit(self, n):
        # Kapasiteden fazla ekleyemesin
        if self.size + n > self.capacity:
            raise ValueError("Exceeds capacity")

        self._size += n

    def withdraw(self, n):
        # Mevcut miktardan fazla çıkarılamasın
        if self.size < n:
            raise ValueError("Not enough cookies")

        self._size -= n

    @property
    def capacity(self):
        # Kapasiteyi döndür
        return self._capacity

    @property
    def size(self):
        # Mevcut sayıyı döndür
        return self._size
