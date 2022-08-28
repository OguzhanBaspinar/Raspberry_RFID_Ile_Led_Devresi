# Raspberry_RFID_Ile_Led_Devresi

Raspberyy GPIO pinlerinin hepsini kullanabilmek için aşağıdaki adımları uygulayınız; <br>
Raspberyy Pi konsolunu açınız. <br>
𝙨𝙪𝙙𝙤 𝙖𝙥𝙩-𝙜𝙚𝙩 𝙪𝙥𝙙𝙖𝙩𝙚 <br>
𝙨𝙪𝙙𝙤 𝙖𝙥𝙩-𝙜𝙚𝙩 𝙞𝙣𝙨𝙩𝙖𝙡𝙡 𝙥𝙮𝙩𝙝𝙤𝙣-𝙙𝙚𝙫 <br>
komutlarını yazarak yüklemeleri yapınız. (Rasperry PI gerekli güncellemeler) <br>

𝙂𝙋𝙄𝙊 𝙆𝙪̈𝙩𝙪̈𝙥𝙝𝙖𝙣𝙚𝙨𝙞𝙣𝙞𝙣 𝘾̧𝙖𝙜̆ı𝙧ı𝙡𝙢𝙖𝙨ı :  <br>
Raspberry Pi kartınızda GPIO kütüphanesinin ismi RPi.GPIO olarak kullanılmaktadır. Python programında bu kütüphaneyi eklemek için aşağıdaki komut kullanılmaktadır.
>> import RPi.GPIO

GPIO kütüphanesini programda daha sonra GPIO ismiyle çağırmak için aşağıdaki kod kullanılmaktadır.

>> import RPi.GPIO as GPIO

𝙂𝙋𝙄𝙊 𝙋𝙞𝙣 𝙏𝙪̈𝙧𝙪̈𝙣𝙪̈𝙣 𝘼𝙮𝙖𝙧𝙡𝙖𝙣𝙢𝙖𝙨ı : <br> 
Raspberry Pi’ın GPIO pinlerini isimlendirirken iki farklıdizilimle karşılaşırız. Bunlar BCM dizilimi ve BOARD dizilimidir. BCM dizilimi pinlere verilen GPIO numaralarından oluşmaktadır. Bunlar sıralı numaralar değildir. BOARD dizilimi ise pinlerin fiziksel numaralandırılmasıdır. 1’den başlayıp 40’a kadar devam eden sıralı sayılardan oluşur.
Resimde Raspberry Pi'nin pin girişleri ve isimleri yer almaktadır. <br>
![gpio-pinout-diagram](https://user-images.githubusercontent.com/106193850/187070778-c4f0181f-84a5-4524-9053-1717bb102509.png)
