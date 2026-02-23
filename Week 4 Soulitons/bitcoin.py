import sys # Terminal ile konuşmak için
import requests # İnternet sitelerine bağlanıp veri çekebilmek için

if len(sys.argv) != 2: # Kullanıcı python bitcoin.py haricinde bir giriş yaptı mı kontrolü
    sys.exit("Missing command-line argument") # Giriş yapmadıysa hata mesajı ver ve kapat

try:
    bitcoin = float(sys.argv[1]) # Terminalden gelen her şey string olduğundan burada sayıya çeviriyoruz
except ValueError: # Kullanıcı sayı yerine kelime girerse hata mesajıyla kapıyoruz
    sys.exit("Command-line argument is not a number")

API = "b33e0e70a149c8d94be087f35c21fbc53378a93e100d3cd2ea5cf2730e12d33c" # CoinCap sitesinden aldığımız özel şifremiz
url = "https://rest.coincap.io/v3/assets/bitcoin" # Veriyi çekeceğimiz adres
params = {"apiKey": API} # Anahtarı adrese yapıştırmak yerine parametre olarak paketliyoruz

try:
    response = requests.get(url, params = params) # request.get ile siteye alo diyoruz, params ile kimliğimizi gösteriyoruz
    data = response.json() # Site cevabı java script dilinde göndereceğinden bunu pythonun anlayacağı sözlük yapısına çeviriyoruz
    price = data["data"]["priceUsd"] # Gelen verinin içinden fiyatı çekiyoruz, datanın içinde priceUsd etiketini buluyoruz
    price_num = float(price) # Siteden gelen yazıyı sayıya çeviriyoruz

except requests.RequestException: # İnternet kesintisi veya site çöküntüsü varsa hata mesajı
    sys.exit("API request error")

except (KeyError, ValueError): # Gelen veride priceUsd etiketi yoksa veya veri bozuksa hata mesajı
    sys.exit("Data parsing error")

cost = bitcoin * price_num # Elimizdeki miktar ile güncel fiyatı çarpıyoruz
print(f"${cost:,.4f}") # Sonucu ekrana yaz, binlik ayracı koy, virgülden sonra 4 basamak göster
