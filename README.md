# Raspberry_RFID_Ile_Led_Devresi

Raspberyy GPIO pinlerinin hepsini kullanabilmek için aşağıdaki adımları uygulayınız;
Raspberyy Pi konsolunu açınız.
sudo apt-get update
sudo apt-get install python-dev
komutlarını yazarak yüklemeleri yapınız. (Rasperry PI gerekli güncellemeler)

^*GPIO Kütüphanesinin Çağırılması*^
Raspberry Pi kartınızda GPIO kütüphanesinin ismi RPi.GPIO olarak kullanılmaktadır. Python programında bu kütüphaneyi eklemek için
aşağıdaki komut kullanılmaktadır.
>> import RPi.GPIO

GPIO kütüphanesini programda daha sonra GPIO ismiyle çağırmak için
aşağıdaki kod kullanılmaktadır.

>> import RPi.GPIO as GPIO

GPIO Pin Türünün Ayarlanması
Raspberry Pi’ın GPIO pinlerini isimlendirirken iki farklıdizilimle karşılaşırız. Bunlar BCM dizilimi ve BOARD
dizilimidir. BCM dizilimi pinlere verilen GPIO numaralarından oluşmaktadır. Bunlar sıralı numaralar değildir.
BOARD dizilimi ise pinlerin fiziksel numaralandırılmasıdır. 1’den başlayıp 40’a kadar devam eden sıralı sayılardan oluşur.
Resimde Raspberry Pi'nin pin girişleri ve isimleri yer almaktadır.
![gpio-pinout-diagram](https://user-images.githubusercontent.com/106193850/187070778-c4f0181f-84a5-4524-9053-1717bb102509.png)
