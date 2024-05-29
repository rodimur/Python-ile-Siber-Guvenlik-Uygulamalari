from scapy.all import *

# host discovery yapmak için iki adet pakete ihtiyacımız var ethernet ve arp onları tanımladık 

eth = Ether() 
arp = ARP()

# layer 2 seviyesinde broadcast yapmak istiyorsak ff:ff:ff:ff:ff:ff olarak mac adresi vermemiz gerekiyor
eth.dst = "ff:ff:ff:ff:ff:ff"
arp.pdst = "10.0.2.1/24" # destination adresi olarak subnetinimizi veriyoruz

bpckt = eth/arp # ethernet ve arp paketlerini birleştirdik

# bpckt.show()

ans,unans = srp(bpckt,timeout=5) # paket gönderiyoruz send and recive packet 

#srp layer 2
#sr layer 3
#send layer 3
#sendp layer 2
#yani eğer paketin için ip varsa send yada sr yi kullanıcaz eğer layer 2 de kullanıcaksak sonuna p yi eklemeyi unutmıycaz

#ans.summary() # burda dönen cevabın özet bilgisine bakıyoruz
print("#"*30)
#unans.summary() # burda dönmeyen cevabın özet bilgisine bakıyoruz

for snd,rcv in ans: 
	#rcv.show() # geri dönen değerleri gösterdi
	print(rcv.psrc , " : " , rcv.src) # açık olan ip adresilerni ve mac adreslerini yazdırdık
