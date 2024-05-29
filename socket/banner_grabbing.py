import socket # socket kütüphanesini import ettik 


ip = "10.0.2.5"

# bir try except bloğu tanımladık çünkü eğer port kapalı ise kod çalışmıyor connection refused hatası alıyorduk bizde bu hata alındağında port kapalı mesajı bastırmak için try except bloğu kullandık
for port in range(1,100):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket nesnesi tanımladık ipv4 gönderiyoruz isteklerimizi tcp istekleri
		s.settimeout(5.0) # bir timeout değeri belirledik çünkü cevap gelene kadar öyle takılı bekliyor bunu engellemek için timeout değeri ekledik
		s.connect((ip,port))
		response = s.recv(1024) # karşıda hangi servis çalıştığını öğrenmek için bi geri dönüş alıyoruz 

		print(str(port),": open : Banner :",response.decode()) # burda aldığımız geri dönüşü decode ediyoruz 
	except socket.timeout as t: # timeout yiyen yani hiç cevap alamadığımız portları farklı bi method kullan diye hata mesajı yaptık
		if(port==80):
			httpMessage = "GET / HTTP/1.0\r\n\r\n" # 80 portu http olduğunu biliyoruz ama timeout a düşüyordu bizde bi telnet bağlantısı yaptık get ile iki kere enter a bastığında geliyordu \r\n\r\n iki kere enter a basma komutu 
			s.send(httpMessage.encode()) # mesajı encode edip gönderdik
			httpRcv = s.recv(1024)	# mesaj geri döndü
			print(str(port),": open : Banner :",httpRcv.decode()) # mesajı decode edip yazdırdık
		else:
			print(str(port)," : use diffrent method")

	except Exception as e:
		#print(str(port),": closed : reason :",str(e)) # kapalı olan portların sebeplerini görelim dedik bağlantı sağlanamadı timeout yedi gibi sebebi ne
		pass
	finally:
		s.close()

# her seferinde socketi tekrardan oluşturuyoruz ve kapatıyoruz çünkü böyle yapmazsak socket açık kalıyor ve hataya düşüyor ilk açık portu buluyo diğerlerini kapalı gösteriyor
