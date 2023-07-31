from time import time # Zamanı ölçmek için time modülünü ekliyoruz

# Şimdi giriş paragrafının doğruluğunu hesaplamak için bir fonksiyon tanımlayalım

def tperror(prompt):
    global inwords

    words = prompt.split() # Giriş paragrafını kelimelere bölelim
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords) - 1): # İlk ve son kelimeyi kontrol ediyoruz
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1

        else: # Diğer kelimeleri kontrol ediyoruz
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1

    return errors 

# Şimdi dakikada yazılan kelime hızını hesaplamak için bir fonksiyon tanımlayalım

def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split() # Giriş metnini kelimelere bölelim
    twords = len(inwords) # Toplam kelime sayısını bulalım
    speed = twords / time # Hızı hesaplayalım (dakikada kaç kelime yazıldığını gösterir)

    return speed

# Toplam geçen süreyi hesaplamak için bir fonksiyon tanımlayalım

def elapsedtime(stime, etime):
    time = etime - stime # etime bitiş zamanı, stime başlangıç zamanı
    return time 

if __name__ == '__main__':
    prompt = "Python is an interpreted, high-level, general-purpose programming language.Created by Guido van Rossum and first released in 1991,  "
    # Bu paragraf, hızınızı kontrol etmek için yazmanız gereken metin

    print("Aşağıdakini yazın: ", prompt)

    # Kullanıcının hazır olduğunu kontrol etmek için Enter tuşuna basmasını bekliyoruz

    input("Hızınızı ölçmek için hazır olduğunuzda Enter tuşuna basın!")

    # Giriş için zaman kaydediyoruz
    stime = time()
    inprompt = input()
    etime = time()

    # Fonksiyonların döndürdüğü tüm bilgileri toplayalım

    time = round(elapsedtime(stime, etime), 2) # Süreyi yuvarlayalım
    speed = speed(inprompt, stime, etime)
    errors = tperror(prompt)

    # Sonuçları görmek için gerekli tüm verileri yazdıralım

    print("######################################")
    print("Toplam geçen süre: ", time, "saniye")
    print("Ortalama yazma hızınız", speed, "kelime/dakika")
    print("Toplam", errors, "hata ile")
    print("#########################################")
