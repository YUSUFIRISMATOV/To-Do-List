import json
import os
from datetime import datetime

class TodoListesi:
    def __init__(self):
        self.dosya_adi = "todo_listesi.json"
        self.gorevler = self.gorevleri_yukle()
    
    def gorevleri_yukle(self):
        if os.path.exists(self.dosya_adi):
            try:
                with open(self.dosya_adi, 'r', encoding='utf-8') as dosya:
                    return json.load(dosya)
            except:
                return []
        return []
    
    def gorevleri_kaydet(self):
        with open(self.dosya_adi, 'w', encoding='utf-8') as dosya:
            json.dump(self.gorevler, dosya, ensure_ascii=False, indent=2)
    
    def gorev_ekle(self):
        gorev = input("Yeni görev: ")
        tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
        self.gorevler.append({
            "gorev": gorev,
            "tamamlandi": False,
            "tarih": tarih
        })
        self.gorevleri_kaydet()
        print("✅ Görev eklendi!")
    
    def gorevleri_listele(self):
        if not self.gorevler:
            print("📝 Henüz görev yok.")
            return
        
        print("\n📋 GÖREV LİSTESİ:")
        for i, gorev in enumerate(self.gorevler, 1):
            durum = "✅" if gorev["tamamlandi"] else "⏳"
            print(f"{i}. {durum} {gorev['gorev']} ({gorev['tarih']})")
    
    def gorev_tamamla(self):
        self.gorevleri_listele()
        if not self.gorevler:
            return
        
        try:
            numara = int(input("\nTamamlanan görev numarası: ")) - 1
            if 0 <= numara < len(self.gorevler):
                self.gorevler[numara]["tamamlandi"] = True
                self.gorevleri_kaydet()
                print("🎉 Görev tamamlandı!")
            else:
                print("Geçersiz görev numarası!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
    
    def gorev_sil(self):
        self.gorevleri_listele()
        if not self.gorevler:
            return
        
        try:
            numara = int(input("\nSilinecek görev numarası: ")) - 1
            if 0 <= numara < len(self.gorevler):
                silinen = self.gorevler.pop(numara)
                self.gorevleri_kaydet()
                print(f"🗑️ '{silinen['gorev']}' silindi!")
            else:
                print("Geçersiz görev numarası!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
    
    def calistir(self):
        while True:
            print("\n📝 TO-DO LİSTESİ")
            print("1. Görev ekle")
            print("2. Görevleri listele")
            print("3. Görev tamamla")
            print("4. Görev sil")
            print("5. Çıkış")
            
            secim = input("Seçiminiz (1-5): ")
            
            if secim == "1":
                self.gorev_ekle()
            elif secim == "2":
                self.gorevleri_listele()
            elif secim == "3":
                self.gorev_tamamla()
            elif secim == "4":
                self.gorev_sil()
            elif secim == "5":
                print("Güle güle!")
                break
            else:
                print("Geçersiz seçim!")

if __name__ == "__main__":
    todo = TodoListesi()
    todo.calistir()
