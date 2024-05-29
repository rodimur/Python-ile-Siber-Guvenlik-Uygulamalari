import socket # socket kütüphanesini import ettik 


ip = "10.0.2.5"

# bir try except bloğu tanımladık çünkü eğer port kapalı ise kod çalışmıyor connection refused hatası alıyorduk bizde bu hata alındağında port kapalı mesajı bastırmak için try except bloğu kullandık
for port in range(1,100):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket nesnesi tanımladık ipv4 gönderiyoruz isteklerimizi tcp istekleri
		s.connect((ip,port))
		print(str(port)," open")
	except Exception as e:
		print(str(port)," closed")
		pass
	finally:
		s.close()

# her seferinde socketi tekrardan oluşturuyoruz ve kapatıyoruz çünkü böyle yapmazsak socket açık kalıyor ve hataya düşüyor ilk açık portu buluyo diğerlerini kapalı gösteriyor
