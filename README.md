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
<br>
**Deneyde Kullanılacak Malzemeler:** <br>
- Bread Board <br>
- 3 Adet Led <br>
- Raspberyy Pi <br>
- RFID Kart Okuyucu <br>
- Jumper Kablo (d-e, e-e) <br>
- 3 Adet 220 Ohm Direnç <br>

RFID sistemi temel olarak 2 bileşenden oluşmaktadır. Bunlar; <br>
• RFID Tag (RFID Etiketi) <br>
• RFID Reader/Writer (RFID Okuyucu/Yazıcı) <br>
Etiket, içinde nesneye ait bilgilerin depolandığı bir yonga (çip seti) ve okuyucu ile iletişime geçebilmek için bir anten barındıran bileşenlerdir. Okuyucu ile iletişime geçebilmek için RF sinyallerini kullanırlar. Etiketlerin yüzeyleri farklı türde malzemelerle kaplanabilir. Her etiketin benzersiz bir tanımlayıcı (id) numarası vardır. Etiketlerin hafıza kapasiteleri 64 bit – 8 MB arasında değişebilir. RFID etiketler okuyucu ile temas etmeden iletişime geçebilirler. <br>
RFID bağlantılarını aşağıdaki tablodaki pinlere göre ayarlayınız.
![RFID Pin](https://user-images.githubusercontent.com/106193850/187072547-7abcecb5-0354-4e02-8572-3ec40427d761.png) <br>
RFID kartını kullanabilmek için gerekli kütüphaneyi raspberry de console üzerinden yükleyiniz. RC522 (RFID kartın kütüphanesi) <br>

>> sudo pip install pi-rc522
<br>
Python kodlarına kodlarım sekmesinden ulaşabilirsiniz.

