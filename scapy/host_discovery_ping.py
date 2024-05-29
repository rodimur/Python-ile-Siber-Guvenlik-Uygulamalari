from scapy.all import * # scapy kütüphanesini import ediyoruz

ip = IP() # scapyde kullandığımı IP() için bir ip değişkeni tanımlıyoruz
icmp = ICMP() # scapy de kullandığımız ICMP() için bir değişken tanımlıyoruz

pingPckt = ip/icmp # ping ve icmp paketlerini birleştiriyoruz

addr = "10.0.2." # burda tarama ping taraması yapıcağımız adresi giriyoruz

ipList = [] # açık olan ip leri tutmak için bir list tanımladık

for i in range(256): # tarama yapmak istediğimiz aralığı for döngüsü ile belirledik
	pingPckt[IP].dst=addr+str(i) # burda destination ip adresini for döngüsünden aldığımız değer ile değiştiriyoruz
	# print(pingPckt[IP].dst)
	responce = sr1(pingPckt,timeout=0.5 , verbose = False) # burda responce ile geri dönüş alıyoruz
	# print(responce)
	if(responce):
		# print(pingPckt[IP].dst," is up") # geri dönüş değerini eğer ip kullanılıyor ise bu ip açık demesini sağladık
		ipList.append(pingPckt[IP].dst) # burda açık ipleri listin içine attık
	else:
		pass

print(ipList) 

