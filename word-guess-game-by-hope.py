import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt

class KelimeOyunu(QWidget):
    def __init__(self):
        super().__init__()

        self.sehir_listesi = [
            ("adana", "Türkiye'nin güneyinde yer alan bir il."),
            ("adıyaman", "Nemrut Dağı ile ünlü bir il."),
            ("afyonkarahisar", "Termal suları ve sucukları ile meşhur bir il."),
            ("ağrı", "Doğubayazıt ilçesi ve İshak Paşa Sarayı ile bilinen bir il."),
            ("amasya", "Elması ve tarihi evleri ile ünlü bir il."),
            ("ankara", "Türkiye'nin başkenti."),
            ("antalya", "Turizm cenneti olan bir il."),
            ("artvin", "Yeşil doğası ve Karadeniz'e kıyısı olan bir il."),
            ("aydın", "Efeler diyarı olarak bilinen bir il."),
            ("balıkesir", "Marmara ve Ege bölgelerinde kıyısı olan bir il."),
            ("bartın", "Karadeniz kıyısında yer alan bir il."),
            ("batman", "Hasankeyf antik kenti ile bilinen bir il."),
            ("bayburt", "Tarihi Bayburt Kalesi ile ünlü bir il."),
            ("bilecik", "Osmanlı İmparatorluğu'nun doğduğu topraklar."),
            ("bingöl", "Yüzen adaları ile bilinen bir il."),
            ("bitlis", "Nemrut Krater Gölü ve tarihi yapıları ile bilinen bir il."),
            ("bolu", "Abant ve Yedigöller gibi doğal güzellikleri ile ünlü bir il."),
            ("burdur", "Salda Gölü ile ünlü bir il."),
            ("bursa", "Osmanlı İmparatorluğu'nun ilk başkenti ve ipek üretimi ile ünlü bir il."),
            ("çanakkale", "Tarihi Gelibolu Yarımadası ve Truva Antik Kenti ile bilinen bir il."),
            ("çankırı", "Tuz Mağarası ve kaya tuzu ile ünlü bir il."),
            ("çorum", "Hitit medeniyetine ev sahipliği yapmış bir il."),
            ("denizli", "Pamukkale travertenleri ile ünlü bir il."),
            ("diyarbakır", "Tarihi surları ve kültürel zenginlikleri ile bilinen bir il."),
            ("düzce", "Doğal güzellikleri ve yaylaları ile ünlü bir il."),
            ("edirne", "Osmanlı İmparatorluğu'nun ikinci başkenti ve tarihi yapıları ile ünlü bir il."),
            ("elazığ", "Harput Kalesi ve Hazar Gölü ile bilinen bir il."),
            ("erzincan", "Doğa sporları ve Kemaliye ilçesi ile ünlü bir il."),
            ("erzurum", "Kış sporları merkezi Palandöken ile ünlü bir il."),
            ("eskişehir", "Modern yapıları ve Porsuk Çayı ile bilinen bir il."),
            ("gaziantep", "Baklavası ve tarihi yapıları ile ünlü bir il."),
            ("giresun", "Fındığı ve Karadeniz kıyıları ile ünlü bir il."),
            ("gümüşhane", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("hakkari", "Dağları ve doğal güzellikleri ile ünlü bir il."),
            ("hatay", "Tarihi ve kültürel zenginlikleri ile bilinen bir il."),
            ("ığdır", "Ağrı Dağı'nın eteklerinde yer alan bir il."),
            ("ısparta", "Gülleri ve lavanta bahçeleri ile ünlü bir il."),
            ("istanbul", "Türkiye'nin en büyük şehri ve kültür başkenti."),
            ("izmir", "Ege'nin incisi olarak bilinen bir il."),
            ("kahramanmaraş", "Dondurması ve tarihi yapıları ile ünlü bir il."),
            ("karabük", "Safranbolu evleri ile ünlü bir il."),
            ("karaman", "Tarihi ve kültürel zenginlikleri ile bilinen bir il."),
            ("kars", "Ani Harabeleri ve Kars Kalesi ile ünlü bir il."),
            ("kastamonu", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("kayseri", "Erciyes Dağı ve pastırması ile ünlü bir il."),
            ("kırıkkale", "Sanayi ve askeri tesisleri ile bilinen bir il."),
            ("kırklareli", "Bağları ve üzüm festivali ile ünlü bir il."),
            ("kırşehir", "Tarihi ve kültürel zenginlikleri ile bilinen bir il."),
            ("kilis", "Suriye sınırında yer alan ve tarihi yapıları ile bilinen bir il."),
            ("kocaeli", "Sanayi ve ticaret merkezi olan bir il."),
            ("konya", "Mevlana Müzesi ve geniş tarım arazileri ile ünlü bir il."),
            ("kütahya", "Çinileri ve termal kaynakları ile ünlü bir il."),
            ("malatya", "Kayısısı ile ünlü bir il."),
            ("manisa", "Tarihi yapıları ve üzüm bağları ile bilinen bir il."),
            ("mardin", "Tarihi taş evleri ve kültürel zenginlikleri ile ünlü bir il."),
            ("mersin", "Akdeniz kıyısında yer alan ve limanı ile bilinen bir il."),
            ("muğla", "Bodrum, Marmaris ve Fethiye gibi turistik ilçeleri ile ünlü bir il."),
            ("muş", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("nevşehir", "Kapadokya bölgesi ve peri bacaları ile ünlü bir il."),
            ("niğde", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("ordu", "Fındığı ve yaylaları ile ünlü bir il."),
            ("osmaniye", "Karatepe-Aslantaş Milli Parkı ile bilinen bir il."),
            ("rize", "Çayı ve yaylaları ile ünlü bir il."),
            ("sakarya", "Sapanca Gölü ve doğal güzellikleri ile bilinen bir il."),
            ("samsun", "Karadeniz'in önemli liman şehirlerinden biri."),
            ("siirt", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("sinop", "Karadeniz'in en kuzey noktası ve doğal limanı ile ünlü bir il."),
            ("sivas", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("şanlıurfa", "Peygamberler şehri olarak bilinen ve Göbeklitepe ile ünlü bir il."),
            ("şırnak", "Tarihi ve kültürel zenginlikleri ile bilinen bir il."),
            ("tekirdağ", "Üzüm bağları ve rakısı ile ünlü bir il."),
            ("tokat", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("trabzon", "Sümela Manastırı ve doğal güzellikleri ile ünlü bir il."),
            ("tunceli", "Munzur Vadisi Milli Parkı ile bilinen bir il."),
            ("uşak", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("van", "Van Gölü ve Akdamar Adası ile ünlü bir il."),
            ("yalova", "Termal kaynakları ve doğal güzellikleri ile bilinen bir il."),
            ("yozgat", "Tarihi yapıları ve doğal güzellikleri ile bilinen bir il."),
            ("zonguldak", "Kömür madenleri ve doğal güzellikleri ile bilinen bir il.")
        ]
        self.harf_basi_para = 50
        self.yanlis_tahmin_cezasi = 10
        self.tahmin_sayisi = 5
        self.harf_isteme_hakki = 5
        self.dogru_tahmin_puani = 75
        self.ekstra_harf_hakki = 2
        self.oyuncular = []
        self.para = []
        self.harf_hakki = []
        self.ipucu_hakki = []
        self.sira = 0

        self.initUI()

    def initUI(self):
        QFontDatabase.addApplicationFont(":/Users/ahmetberkayayhan/Downloads/Montserrat-Regular.ttf")
        self.setFont(QFont("Montserrat"))

        self.setWindowTitle('Kelime Oyunu')
        self.setGeometry(100, 100, 500, 400)

        self.layout = QVBoxLayout()

        self.oyuncu_label = QLabel('Oyuncu Adı:', self)
        self.oyuncu_label.setFont(QFont('Montserrat', 14))
        self.layout.addWidget(self.oyuncu_label)

        self.oyuncu_input = QLineEdit(self)
        self.oyuncu_input.setPlaceholderText('Oyuncu Adı Giriniz')
        self.oyuncu_input.setFont(QFont('Montserrat', 14))
        self.oyuncu_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #8c8c8c;
                border-radius: 10px;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
        """)
        self.layout.addWidget(self.oyuncu_input)

        self.ekle_button = QPushButton('Oyuncu Ekle', self)
        self.ekle_button.setFont(QFont('Montserrat', 14))
        self.ekle_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.ekle_button.clicked.connect(self.oyuncu_ekle)
        self.layout.addWidget(self.ekle_button)

        self.baslat_button = QPushButton('Oyunu Başlat', self)
        self.baslat_button.setFont(QFont('Montserrat', 14))
        self.baslat_button.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #007bb5;
            }
        """)
        self.baslat_button.clicked.connect(self.oyunu_baslat)
        self.layout.addWidget(self.baslat_button)

        self.kelime_label = QLabel('', self)
        self.kelime_label.setFont(QFont('Montserrat', 24))
        self.layout.addWidget(self.kelime_label)
        self.kelime_label.hide()

        self.harf_input = QLineEdit(self)
        self.harf_input.setPlaceholderText('Bir Harf Giriniz')
        self.harf_input.setFont(QFont('Montserrat', 14))
        self.harf_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #8c8c8c;
                border-radius: 10px;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
        """)
        self.layout.addWidget(self.harf_input)
        self.harf_input.hide()

        self.tahmin_button = QPushButton('Tahmin Et', self)
        self.tahmin_button.setFont(QFont('Montserrat', 14))
        self.tahmin_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
        """)
        self.tahmin_button.clicked.connect(self.tahmin_et)
        self.layout.addWidget(self.tahmin_button)
        self.tahmin_button.hide()

        self.harf_iste_button = QPushButton('Harf İste', self)
        self.harf_iste_button.setFont(QFont('Montserrat', 14))
        self.harf_iste_button.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #fb8c00;
            }
        """)
        self.harf_iste_button.clicked.connect(self.harf_iste)
        self.layout.addWidget(self.harf_iste_button)
        self.harf_iste_button.hide()

        self.kelime_tahmin_button = QPushButton('Kelimeyi Tahmin Et', self)
        self.kelime_tahmin_button.setFont(QFont('Montserrat', 14))
        self.kelime_tahmin_button.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #8e24aa;
            }
        """)
        self.kelime_tahmin_button.clicked.connect(self.kelimeyi_tahmin_et)
        self.layout.addWidget(self.kelime_tahmin_button)
        self.kelime_tahmin_button.hide()

        self.ipucu_button = QPushButton('İpucu İste', self)
        self.ipucu_button.setFont(QFont('Montserrat', 14))
        self.ipucu_button.setStyleSheet("""
            QPushButton {
                background-color: #607D8B;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #546E7A;
            }
        """)
        self.ipucu_button.clicked.connect(self.ipucu_iste)
        self.layout.addWidget(self.ipucu_button)
        self.ipucu_button.hide()

        self.oyuncular_label = QLabel('Oyuncular:', self)
        self.oyuncular_label.setFont(QFont('Montserrat', 14))
        self.layout.addWidget(self.oyuncular_label)

        self.sira_label = QLabel('Sıra: ', self)
        self.sira_label.setFont(QFont('Montserrat', 14))
        self.layout.addWidget(self.sira_label)
        self.sira_label.hide()

        self.puan_label = QLabel('Puanlar:', self)
        self.puan_label.setFont(QFont('Montserrat', 14))
        self.layout.addWidget(self.puan_label)
        self.puan_label.hide()

        self.harf_hakki_label = QLabel('Harf İsteme Hakları:', self)
        self.harf_hakki_label.setFont(QFont('Montserrat', 14))
        self.layout.addWidget(self.harf_hakki_label)
        self.harf_hakki_label.hide()

        self.ipucu_hakki_label = QLabel('İpucu Hakları:', self)
        self.ipucu_hakki_label.setFont(QFont('Montserrat', 14))
        self.layout.addWidget(self.ipucu_hakki_label)
        self.ipucu_hakki_label.hide()

        self.setLayout(self.layout)

    def oyuncu_ekle(self):
        oyuncu_adi = self.oyuncu_input.text()
        if oyuncu_adi:
            self.oyuncular.append({"isim": oyuncu_adi})
            self.para.append(0)
            self.harf_hakki.append(self.harf_isteme_hakki)
            self.ipucu_hakki.append(1)
            self.oyuncu_input.clear()
            self.guncelle_oyuncular_label()
        else:
            QMessageBox.warning(self, 'Uyarı', 'Lütfen oyuncu adı giriniz.')

    def guncelle_oyuncular_label(self):
        oyuncu_isimleri = ', '.join([oyuncu["isim"] for oyuncu in self.oyuncular])
        self.oyuncular_label.setText(f'Oyuncular: {oyuncu_isimleri}')

    def guncelle_sira_label(self):
        siradaki_oyuncu = self.oyuncular[self.sira]["isim"]
        self.sira_label.setText(f"Sıra: {siradaki_oyuncu}")

    def guncelle_puan_label(self):
        puanlar = ', '.join([f"{oyuncu['isim']}: {puan}" for oyuncu, puan in zip(self.oyuncular, self.para)])
        self.puan_label.setText(f'Puanlar: {puanlar}')

    def guncelle_harf_hakki_label(self):
        haklar = ', '.join([f"{oyuncu['isim']}: {hak}" for oyuncu, hak in zip(self.oyuncular, self.harf_hakki)])
        self.harf_hakki_label.setText(f'Harf İsteme Hakları: {haklar}')

    def guncelle_ipucu_hakki_label(self):
        haklar = ', '.join([f"{oyuncu['isim']}: {hak}" for oyuncu, hak in zip(self.oyuncular, self.ipucu_hakki)])
        self.ipucu_hakki_label.setText(f'İpucu Hakları: {haklar}')

    def oyunu_baslat(self):
        if not self.oyuncular:
            QMessageBox.warning(self, 'Uyarı', 'Lütfen önce oyuncu ekleyiniz.')
            return

        self.sira = random.randint(0, len(self.oyuncular) - 1)

        self.oyuncu_label.hide()
        self.oyuncu_input.hide()
        self.ekle_button.hide()
        self.baslat_button.hide()

        self.kelime_label.show()
        self.harf_input.show()
        self.tahmin_button.show()
        self.harf_iste_button.show()
        self.kelime_tahmin_button.show()
        self.ipucu_button.show()
        self.sira_label.show()
        self.puan_label.show()
        self.harf_hakki_label.show()
        self.ipucu_hakki_label.show()

        self.guncelle_sira_label()
        self.guncelle_puan_label()
        self.guncelle_harf_hakki_label()
        self.guncelle_ipucu_hakki_label()

        self.yeni_kelime()

    def yeni_kelime(self):
        self.secili_kelime, self.ipucu = random.choice(self.sehir_listesi)
        self.harfler = []
        self.z = list('_' * len(self.secili_kelime))
        self.tahmin_sayisi = 5
        self.kelime_label.setText(' '.join(self.z))
        self.kelime_tahmin_button.show()

    def tahmin_et(self):
        oyuncu = self.oyuncular[self.sira]
        harf = self.harf_input.text().lower()
        self.harf_input.clear()

        if not harf or len(harf) > 1:
            QMessageBox.warning(self, 'Uyarı', 'Lütfen sadece bir harf giriniz.')
            return

        if harf in self.harfler:
            QMessageBox.warning(self, 'Uyarı', 'Bu harfi daha önce tahmin ettiniz.')
            return

        if harf not in self.secili_kelime:
            self.para[self.sira] -= self.yanlis_tahmin_cezasi
            self.tahmin_sayisi -= 1
            QMessageBox.information(self, 'Bilgi', f"Girdiğiniz harf bu kelimede yok! {self.tahmin_sayisi} tane tahmin hakkınız kaldı.")
            if self.tahmin_sayisi == 0:
                QMessageBox.information(self, 'Oyun Bitti', f"Tahmin hakkınız kalmadı. Kaybettiniz! Seçilen kelime: {self.secili_kelime}")
                self.yeni_kelime()
            self.sira = (self.sira + 1) % len(self.oyuncular)
            self.guncelle_sira_label()
            self.guncelle_puan_label()
            return

        harf_sayisi = self.secili_kelime.count(harf)
        self.para[self.sira] += self.harf_basi_para * harf_sayisi
        for i in range(len(self.secili_kelime)):
            if harf == self.secili_kelime[i]:
                self.z[i] = harf
        self.harfler.append(harf)
        self.kelime_label.setText(' '.join(self.z))

        if '_' not in self.z:
            QMessageBox.information(self, 'Tebrikler', f"Tebrikler Kazandınız! Seçilen kelime: {self.secili_kelime}")
            self.yeni_kelime()
            return

        self.guncelle_sira_label()
        self.guncelle_puan_label()
        self.guncelle_harf_hakki_label()

    def kelimeyi_tahmin_et(self):
        tahmin, ok = QInputDialog.getText(self, 'Tahmin', 'Kelimenin tamamını yazabilirsiniz:')
        if ok and tahmin.lower() == self.secili_kelime:
            if not self.harfler:  # Eğer oyuncu hiçbir harf açılmadan doğru tahmin ederse
                self.para[self.sira] += 500
                self.harf_hakki[self.sira] += 10
                QMessageBox.information(self, 'Tebrikler', f"Tebrikler! Hiç harf açılmadan doğru bildiniz. 500 puan ve 10 ekstra harf isteme hakkı kazandınız.")
            else:
                self.para[self.sira] += self.dogru_tahmin_puani
                self.harf_hakki[self.sira] += self.ekstra_harf_hakki
                QMessageBox.information(self, 'Tebrikler', f"Tebrikler Kazandınız! {self.dogru_tahmin_puani} puan ve {self.ekstra_harf_hakki} ekstra harf isteme hakkı kazandınız.")
            self.guncelle_puan_label()
            self.guncelle_harf_hakki_label()
            self.yeni_kelime()
        else:
            self.para[self.sira] -= self.yanlis_tahmin_cezasi
            self.tahmin_sayisi -= 1
            QMessageBox.information(self, 'Yanlış Tahmin', f"Yanlış tahmin ettiniz.. {self.tahmin_sayisi} tane tahmin hakkınız kaldı.")
            if self.tahmin_sayisi == 0:
                QMessageBox.information(self, 'Oyun Bitti', f"Tahmin hakkınız kalmadı. Kaybettiniz! Seçilen kelime: {self.secili_kelime}")
                self.yeni_kelime()
            self.sira = (self.sira + 1) % len(self.oyuncular)
            self.guncelle_sira_label()
            self.guncelle_puan_label()
            return

    def harf_iste(self):
        if self.harf_hakki[self.sira] > 0:
            self.harf_hakki[self.sira] -= 1
            self.guncelle_harf_hakki_label()
            acilmamis_harfler = [harf for harf in self.secili_kelime if harf not in self.harfler]
            if acilmamis_harfler:
                acilacak_harf = random.choice(acilmamis_harfler)
                for i in range(len(self.secili_kelime)):
                    if acilacak_harf == self.secili_kelime[i]:
                        self.z[i] = acilacak_harf
                self.harfler.append(acilacak_harf)
                self.kelime_label.setText(' '.join(self.z))

                if '_' not in self.z:
                    QMessageBox.information(self, 'Tebrikler', f"Tebrikler Kazandınız! Seçilen kelime: {self.secili_kelime}")
                    self.yeni_kelime()
                    return

                self.guncelle_sira_label()
                self.guncelle_puan_label()
                self.guncelle_harf_hakki_label()
            else:
                QMessageBox.information(self, 'Bilgi', 'Açılmamış harf kalmadı.')
        else:
            QMessageBox.warning(self, 'Uyarı', 'Harf isteme hakkınız kalmadı.')

    def ipucu_iste(self):
        if self.ipucu_hakki[self.sira] > 0:
            self.ipucu_hakki[self.sira] -= 1
            self.guncelle_ipucu_hakki_label()
            QMessageBox.information(self, 'İpucu', self.ipucu)
        else:
            QMessageBox.warning(self, 'Uyarı', 'İpucu isteme hakkınız kalmadı.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KelimeOyunu()
    ex.show()
    sys.exit(app.exec_())