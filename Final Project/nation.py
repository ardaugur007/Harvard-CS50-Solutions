import random

class Nation:
    def __init__(self, name):
        self.name = name
        # Başlangıç kaynakları
        self.gold = 300
        self.food = 500
        self.population = 50
        self.soldiers = 0

        # Binalar
        self.buildings = {
            "farm": 1,
            "barrack": 0,
            "wall": 0
        }

    def collect_resources(self):
        # Tur sonu kaynak toplama mantığı

        # Her çiftlik 50 yiyecek üretir
        food_gain = self.buildings["farm"] * 50
        # Nüfus kişi başı 1 altın vergi öder
        gold_gain = self.population * 1

        # Eğer yemek stoğu varsa nüfus her tur %10 büyür
        if self.food > 0:
            growth = self.population // 10
            self.population += growth

        self.food += food_gain
        self.gold += gold_gain
        # Nüfus kişi başı 1 yemek yer
        self.food -= (self.population * 1)

        return food_gain, gold_gain

    def build(self, building_type, amount):
        # Bina inşa mantığı
        costs = {"farm": 50, "barrack": 100, "wall": 200}

        if building_type not in costs:
            raise ValueError(f"Invalid building type: {building_type}")

        total_cost = costs[building_type] * amount

        # Para yetiyor mu diye kontrol
        if self.gold < total_cost:
            raise ValueError(f"Insufficient gold! You need {total_cost - self.gold} more.")

        # Sorun yoksa parayı düşüp binayı ekle
        self.gold -= total_cost
        self.buildings[building_type] += amount
        return True

    def __str__(self):
        # Düzgün gözüksün diye
        return f"{self.name} Empire | Gold: {self.gold} | Food: {self.food} | Pop: {self.population}"
