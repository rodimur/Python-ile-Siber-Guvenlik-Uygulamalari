import random # rastgele mac adresi oluşturmak istediğimiz için random kütüphanesini import ettik
import subprocess # komut çalıştırmak için subprocess kütüphanesini import ettik 
import re # bu kütüphanenin internet sitesi var çıktı içinden almak istediğimiz değeri bastırmamıza yarıyor

charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] # burda bir mac adresinde bulanan karakterleri listeledik

newMac = "" 
for i in range(12):
	newMac = newMac+random.choice(charList)
#print(newMac)
 
#08:00:27:21:b1:d0
#16323BCC4356

ifconfigResult = subprocess.check_output("ifconfig eth0", shell= True).decode() # ifconfig eth0 komutunu çalıştırdık
#print(ifconfigResult)

oldMac = re.search("ether(.*?)txqueuelen",ifconfigResult).group(1).strip() # burda ifconfig komutudnan bize sadece mac adresi kısmı lazım o yüzden re kütüphanesini kullanarak sadece mac adresi kısmını bastırdık
#print(oldMac)

subprocess.check_output("ifconfig eth0 down ",shell = True)
subprocess.check_output("ifconfig eth0 hw ether "+newMac,shell = True)
subprocess.check_output("ifconfig eth0 up ",shell = True)

print("Old Mac :",oldMac)
print("new mac :",newMac)
