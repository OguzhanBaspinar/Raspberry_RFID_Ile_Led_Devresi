from pirc522 import RFID
import signal
import time
import RPi.GPIO as GPIO
GPIO.setwarnings (False)

yesilled = 7     # yeşil led 7 numaralı BOARD pinine atanmıştır
kirmiziled=13    # kırmızı led 13 numaralı BOARD pinine atanmıştır
sariled=11       # sarı led 11 numaralı BOARD pinine atanmıştır
 

GPIO.setmode(GPIO.BOARD)      # 1..40 olarak board dizilimini kullanılacaktır. 
GPIO.setup(yesilled, GPIO.OUT)
GPIO.setup(sariled, GPIO.OUT)
GPIO.setup(kirmiziled, GPIO.OUT)
oku = RFID()                     
util = oku.util()                    # RFID haberleşmeyi başlat. 
util.debug = True
GPIO.output(yesilled, False)
while True:
    try:
        GPIO.output(yesilled, True)
        print("1")
        oku.wait_for_tag()
        print("2")
        (error, data) = oku.request()
        if not error:
            print("\nKart Algilandi!")
            (error, kartid) = oku.anticoll()    # doğru okunan RFID kart bilgisini kartid değişkenine aktar
            if not error:
                kart= str(kartid[0])+" "+str(kartid[1])+" "+str(kartid[2])+" "+str(kartid[3])+" "+str(kartid[4])
            print(kart)
            
            kirmiziled=13
            sariled=11
            yesilled = 7
            
            if kart == "171 195 128 13 229":
                print("YEŞİL LED ON")
                GPIO.output(yesilled, True)
                GPIO.output(kirmiziled, False)
                GPIO.output(sariled, False)
                GPIO.output(kirmiziled, True)
                time.sleep(0.5)
                GPIO.output(kirmiziled, False)
                time.sleep(0.5)
                GPIO.output(kirmiziled, True)
                GPIO.output(yesilled, False)
            if kart != "171 195 128 13 229":
                print("YEŞİL LED OFF")
                GPIO.output(yesilled, False)
                GPIO.output(kirmiziled, True)
                time.sleep(0.5)
                GPIO.output(kirmiziled, False)
                time.sleep(0.5)
            
    except KeyboardInterrupt(): 
        GPIO.cleanup()
        break
