# Ana hesaplamalar ve fonksiyonlar burada.
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QDoubleValidator
import numpy as np
from OtherClasses import *


# Ana pencere/işlemlerin yapıldığı yer
class AnaIslemler(QMainWindow):

    def __init__(self):
        super().__init__()



        loadUi("..\GUIPages\DevreArayuz.ui", self)

        self.setWindowTitle("Devre Hesapları & Grafikler")

        # Qt Designer yerine kodla uyguladığımız bazı style durumları
        self.ItInfoBtn.setStyleSheet("""QToolTip { 
                                                   background-color: black; 
                                                   color: white; 
                                                   border: none;
                                                   }""")

        self.VtInfoBtn.setStyleSheet("""QToolTip { 
                                           background-color: black; 
                                           color: white; 
                                           border: none;
                                           }""")
        self.GraphBtn.setStyleSheet("""
        QPushButton{
        font: 15pt "MS Shell Dlg 2";
        background-color: #fffde7;
        border:2px solid;
        border-color:#414141;
        border-radius:15px;}
        
        QPushButton:pressed{
        background-color: #afbfff;        
        }""")

        self.HesaplaBtn.setStyleSheet("""
                QPushButton{
                font: 15pt "MS Shell Dlg 2";
                background-color: #fffde7;
                border:2px solid;
                border-color:#414141;
                border-radius:15px;}

                QPushButton:pressed{
                background-color: #afbfff;        
                }""")

        self.InfoBtn.setStyleSheet("""
                QPushButton{
                font: 12pt "MS Shell Dlg 2";
                background-color: #fffde7;
                border:2px solid;
                border-color:#414141;
                border-radius:15px;}

                QPushButton:pressed{
                background-color: #afbfff;        
                }""")

        self.FormulBtn.setStyleSheet("""
                        QPushButton{
                        font: 8pt "MS Shell Dlg 2";
                        background-color: #fffde7;
                        border:2px solid;
                        border-color:#414141;
                        border-radius:15px;}

                        QPushButton:pressed{
                        background-color: #afbfff;        
                        }""")

        self.GraphBox.setStyleSheet("""
        background-color: rgb(255,255,255);
        border:2px solid;
        border-color: #ffefcb;
        border-radius:15px;
        background-color: rgb(255, 255, 255);
        """)

        # Butonların fonksiyonlar ile bağlantıları ve diğer pencereleri çağırmada kullanılan classların tanımlanması
        self.GraphBtn.clicked.connect(self.update_graph)
        self.HesaplaBtn.clicked.connect(self.update_gui)
        self.InfoBtn.clicked.connect(self.open_InfoWindow)
        self.InfoWindow = InfoWindow()
        self.FormulBtn.clicked.connect(self.open_MatGosterim)
        self.MatGosterim = MatGosterim()
        self.KisaltmaBtn.clicked.connect(self.open_Kisaltma)
        self.Kisaltma = Kisaltma()
        self.SemaBtn.clicked.connect(self.open_Sema)
        self.DevreSemasi = DevreSemasi()

        # Inputları alan widgetler yalnızca sayı girdisine izin veriyor
        self.VoltInput.setValidator(QDoubleValidator())
        self.AciInput.setValidator(QDoubleValidator())
        self.DirencInput.setValidator(QDoubleValidator())
        self.VoltInput_2.setValidator(QDoubleValidator())

    def update_gui(self):  # Hesaplamaları yapan fonksiyon

        # Inputların tamamının girildiğinden emin ol/Değilse uyarı mesajı verilsin
        if len(self.VoltInput.text()) < 1:
            self.Eksik_PopUp()
        elif len(self.AciInput.text()) < 1:
            self.Eksik_PopUp()
        elif len(self.DirencInput.text()) < 1:
            self.Eksik_PopUp()
        elif len(self.VoltInput_2.text()) < 1:
            self.Eksik_PopUp()
        else:

            # Alınan inputlarda virgül kullanıldıysa onun yerine nokta kullanılmasını iste
            # Veri girişi alırken kullandığımız validator virgül kullanıldığında çalışmayı durduruyor
            girdiler = []
            girdi1 = self.VoltInput.text()
            girdiler.append(girdi1)
            girdi2 = self.AciInput.text()
            girdiler.append(girdi2)
            girdi3 = self.DirencInput.text()
            girdiler.append(girdi3)
            girdi4 = self.VoltInput_2.text()
            girdiler.append(girdi4)

            if "," in girdiler[0]:
                self.Virgül_PopUp()
            elif "," in girdiler[1]:
                self.Virgül_PopUp()
            elif "," in girdiler[2]:
                self.Virgül_PopUp()
            elif "," in girdiler[3]:
                self.Virgül_PopUp()
            else:

                Gerilim = round(float(self.VoltInput.text()), 2)
                Aci = round(float(self.AciInput.text()), 2)
                Direnc = round(float(self.DirencInput.text()), 2)
                Frekans = round(float(self.VoltInput_2.text()), 2)

                # Inputların geçerli değerlere sahip olduğundan emin ol/Değilse uyarı mesajı verilsin
                if (Aci < 0 or Aci > 180):
                    self.Aci_PopUp()
                elif Gerilim < 0:
                    self.Gerilim_PopUp()
                elif Direnc < 0:
                    self.Direnc_PopUp()
                elif Frekans <= 0:
                    self.Frekans_PopUp()


                else:

                    # Bu listeyi hesaplamanın sonunda verilmesi gerekebilecek bir mesaj için kullan.
                    CikisDegerleri = []

                    Vm = round(Gerilim * (2 ** (0.5)), 3)
                    self.VmValue.setText(str(Vm))
                    CikisDegerleri.append(str(Vm))

                    Vdc = round((Vm / (2 * np.pi)) * (1 + np.cos(Aci * np.pi / 180)), 3)
                    self.VdcValue.setText(str(Vdc))
                    CikisDegerleri.append(str(Vdc))

                    Im = round((Vm / Direnc), 3)
                    self.ImValue.setText(str(Im))
                    CikisDegerleri.append(str(Im))

                    Idc = round(((Im / 2 / np.pi) * (1 + np.cos(Aci * np.pi / 180))), 3)
                    self.IdcValue.setText(str(Idc))
                    CikisDegerleri.append(str(Idc))

                    Pdc = round(((Idc * Vdc) / 1000), 3)
                    self.PdcValue.setText(str(Pdc))
                    CikisDegerleri.append(str(Pdc))

                    Is = round((Im / 2) * ((1 - (Aci / 180) + np.sin(2 * Aci * np.pi / 180) / (2 * np.pi)) ** (0.5)), 3)
                    self.IsValue.setText(str(Is))
                    CikisDegerleri.append(str(Is))

                    Ps = round(((Is * Gerilim) / 1000), 3)
                    self.PsValue.setText(str(Ps))
                    CikisDegerleri.append(str(Ps))

                    Vt = round((Vm * (13 / 10)), 3)
                    self.VtValue.setText(str(Vt))
                    CikisDegerleri.append(str(Ps))

                    It = round((Im * (13 / 10)), 3)
                    self.ItValue.setText(str(It))
                    CikisDegerleri.append(str(It))

                    T = round((1 / Frekans*1000), 3)
                    self.VtValue_2.setText(str(T))
                    CikisDegerleri.append(str(T))

                    # nan çıktısı verildiğinde kullanıcıyı ne olduğuna dair bilgilendir
                    if "nan" in CikisDegerleri:
                        self.nanBox()

    def update_graph(self):  # Grafikleri çizdiren fonksiyon

        # Inputların tamamının girildiğinden emin ol/Değilse uyarı mesajı verilsin
        if len(self.VoltInput.text()) < 1:
            self.Eksik_PopUp()
        elif len(self.AciInput.text()) < 1:
            self.Eksik_PopUp()
        elif len(self.DirencInput.text()) < 1:
            self.Eksik_PopUp()
        elif len(self.VoltInput_2.text()) < 1:
            self.Eksik_PopUp()
        else:
            # Alınan inputlarda virgül kullanıldıysa onun yerine nokta kullanılmasını iste
            girdiler = []
            girdi1 = self.VoltInput.text()
            girdiler.append(girdi1)
            girdi2 = self.AciInput.text()
            girdiler.append(girdi2)
            girdi3 = self.DirencInput.text()
            girdiler.append(girdi3)
            girdi4 = self.VoltInput_2.text()
            girdiler.append(girdi4)

            if "," in girdiler[0]:
                self.Virgül_PopUp()
            elif "," in girdiler[1]:
                self.Virgül_PopUp()
            elif "," in girdiler[2]:
                self.Virgül_PopUp()
            elif "," in girdiler[3]:
                self.Virgül_PopUp()
            else:

                Gerilim = round(float(self.VoltInput.text()), 2)
                Aci = round(float(self.AciInput.text()), 2)
                Direnc = round(float(self.DirencInput.text()), 2)
                fre = round(float(self.VoltInput_2.text()), 2)

                # Inputların geçerli değerlere sahip olduğundan emin ol/Değilse uyarı mesajı verilsin
                if (Aci < 0 or Aci > 180):
                    self.Aci_PopUp()
                elif Gerilim < 0:
                    self.Gerilim_PopUp()
                elif Direnc < 0:
                    self.Direnc_PopUp()
                elif fre <= 0:
                    self.Frekans_PopUp()
                else:

                    Aci = round(float(self.AciInput.text()), 2)
                    R = round(float(self.DirencInput.text()), 2)
                    Gerilim = round(float(self.VoltInput.text()), 2)
                    fre = round(float(self.VoltInput_2.text()), 2)
                    t = 1 / fre

                    # Grafik çizim işlemleri
                    Vmax = Gerilim * (2 ** (1 / 2))
                    a = Aci * np.pi / 180
                    w = 2 * np.pi * fre

                    x1 = np.linspace(a / w * 1000, 1 / (2 * fre) * 1000, 100)
                    x2 = np.linspace(0, a / w * 1000, 100)
                    x3 = np.linspace(np.pi / w * 1000, 2 * np.pi / w * 1000, 100)
                    x4 = np.linspace(a / w * 1000 + (2 * np.pi) / w * 1000, 3 * np.pi / w * 1000, 100)
                    x5 = np.linspace(2 * np.pi / w * 1000, 1000 * (a / w + 2 * np.pi / w), 100)
                    x6 = np.linspace(3 * np.pi / w * 1000, 4 * np.pi / w * 1000, 100)
                    x7 = np.linspace(0, 2 * 1 / fre * 1000, 100)
                    x8 = np.linspace(np.pi / w * 1000, (2 * np.pi / w + a / w) * 1000, 100)

                    self.MplWidget.canvas.axes.clear()
                    self.MplWidget.canvas.axes.set_facecolor("#fffde7")
                    self.MplWidget.canvas.axes.set_xticks(np.linspace(0, 2 * t * 1000, 9))
                    self.MplWidget.canvas.axes.set_yticks(np.linspace(Vmax, -Vmax, 5))
                    self.MplWidget.canvas.axes.plot(x7, np.linspace(0, 0, 100), linewidth=1, color="black")
                    self.MplWidget.canvas.axes.plot(x7, Vmax * np.sin(2 * np.pi * x7 * fre / 1000), linewidth=3,
                                                    color="#109D57")
                    self.MplWidget.canvas.axes.set_title('Kaynak Gerilimi-Zaman')
                    self.MplWidget.canvas.axes.grid(color="black", linestyle="--")
                    self.MplWidget.canvas.draw()

                    self.MplWidget_2.canvas.axes.clear()
                    self.MplWidget_2.canvas.axes.set_facecolor("#fffde7")
                    self.MplWidget_2.canvas.axes.set_xticks(np.linspace(0, 4 * np.pi / w * 1000, 9))
                    self.MplWidget_2.canvas.axes.set_yticks(np.linspace(Vmax, -Vmax, 5))
                    self.MplWidget_2.canvas.axes.plot(x7, np.linspace(0, 0, 100), linewidth=1, color="black")
                    self.MplWidget_2.canvas.axes.axvline(a / w * 1000, 0.5, 0.45 * np.sin(a) + 0.5, lw=3,
                                                         color="#0091D5")
                    self.MplWidget_2.canvas.axes.axvline(a / w * 1000 + 2 * np.pi / w * 1000, 0.5,
                                                         0.45 * np.sin(a) + 0.5,
                                                         lw=3,
                                                         color="#0091D5")
                    self.MplWidget_2.canvas.axes.set_title('Ortalama Çıkış Gerilimi-Zaman')
                    self.MplWidget_2.canvas.axes.plot(x1, Vmax * np.sin(2 * np.pi * fre * x1 / 1000), linewidth=3,
                                                      color="#0091D5")
                    self.MplWidget_2.canvas.axes.plot(x7, Vmax * np.sin(2 * np.pi * x7 * fre / 1000), ":",
                                                      color="#0091D5")
                    self.MplWidget_2.canvas.axes.plot(x3, np.linspace(0, 0, 100), linewidth=3, color="#0091D5")
                    self.MplWidget_2.canvas.axes.plot(x4, Vmax * np.sin(2 * np.pi * x4 * fre / 1000), linewidth=3,
                                                      color="#0091D5")
                    self.MplWidget_2.canvas.axes.plot(x6, np.linspace(0, 0, 100), linewidth=3, color="#0091D5")
                    self.MplWidget_2.canvas.axes.plot(x2, np.linspace(0, 0, 100), linewidth=3, color="#0091D5")
                    self.MplWidget_2.canvas.axes.plot(x5, np.linspace(0, 0, 100), linewidth=3, color="#0091D5")
                    self.MplWidget_2.canvas.axes.grid(color="black", linestyle="--")
                    self.MplWidget_2.canvas.draw()

                    self.MplWidget_3.canvas.axes.clear()
                    self.MplWidget_3.canvas.axes.set_facecolor("#fffde7")
                    self.MplWidget_3.canvas.axes.set_xticks(np.linspace(0, 4 * np.pi / w * 1000, 9))
                    self.MplWidget_3.canvas.axes.set_yticks(np.linspace(Vmax, -Vmax, 5))
                    self.MplWidget_3.canvas.axes.plot(x7, np.linspace(0, 0, 100), linewidth=1, color="black")
                    self.MplWidget_3.canvas.axes.set_title('Tristör Gerilimi-Zaman')
                    self.MplWidget_3.canvas.axes.axvline(a / w * 1000, 0.5, 0.45 * np.sin(a) + 0.5, lw=3,
                                                         color="#D9482B")
                    self.MplWidget_3.canvas.axes.axvline(a / w * 1000 + 2 * np.pi / w * 1000, 0.5,
                                                         0.45 * np.sin(a) + 0.5,
                                                         lw=3,
                                                         color="#D9482B")
                    self.MplWidget_3.canvas.axes.plot(x2, Vmax * np.sin(2 * np.pi * fre * x2 / 1000), linewidth=3,
                                                      color="#D9482B")
                    self.MplWidget_3.canvas.axes.plot(x1, np.linspace(0, 0, 100), linewidth=3, color="#D9482B")
                    self.MplWidget_3.canvas.axes.plot(x8, Vmax * np.sin(2 * np.pi * fre * x8 / 1000), linewidth=3,
                                                      color="#D9482B")
                    self.MplWidget_3.canvas.axes.plot(x4, np.linspace(0, 0, 100), linewidth=3, color="#D9482B")
                    self.MplWidget_3.canvas.axes.plot(x7, Vmax * np.sin(2 * np.pi * fre * x7 / 1000), ":",
                                                      color="#D9482B")
                    self.MplWidget_3.canvas.axes.plot(x6, Vmax * np.sin(2 * np.pi * fre * x6 / 1000), linewidth=3,
                                                      color="#D9482B")
                    self.MplWidget_3.canvas.axes.grid(color="black", linestyle="--")
                    self.MplWidget_3.canvas.draw()

                    self.MplWidget_4.canvas.axes.clear()
                    self.MplWidget_4.canvas.axes.set_facecolor("#fffde7")
                    self.MplWidget_4.canvas.axes.set_xticks(np.linspace(0, 4 * np.pi / w * 1000, 9))
                    self.MplWidget_4.canvas.axes.set_yticks(np.linspace(Vmax / R, -Vmax / R, 5))
                    self.MplWidget_4.canvas.axes.plot(x7, np.linspace(0, 0, 100), linewidth=1, color="black")
                    self.MplWidget_4.canvas.axes.axvline(a / w * 1000, 0.5, 0.45 * np.sin(a) + 0.5, lw=3,
                                                         color="#ff0073")
                    self.MplWidget_4.canvas.axes.axvline(a / w * 1000 + 2 * np.pi / w * 1000, 0.5,
                                                         0.45 * np.sin(a) + 0.5,
                                                         lw=3,
                                                         color="#ff0073")
                    self.MplWidget_4.canvas.axes.set_title('Kaynak Akımı-Zaman')
                    self.MplWidget_4.canvas.axes.plot(x1, Vmax / R * np.sin(2 * np.pi * fre * x1 / 1000), linewidth=3,
                                                      color="#ff0073")
                    self.MplWidget_4.canvas.axes.plot(x7, Vmax / R * np.sin(2 * np.pi * fre * x7 / 1000), ":",
                                                      color="#ff0073")
                    self.MplWidget_4.canvas.axes.plot(x3, np.linspace(0, 0, 100), linewidth=3, color="#ff0073")
                    self.MplWidget_4.canvas.axes.plot(x4, Vmax / R * np.sin(2 * np.pi * fre * x4 / 1000), linewidth=3,
                                                      color="#ff0073")
                    self.MplWidget_4.canvas.axes.plot(x6, np.linspace(0, 0, 100), linewidth=3, color="#ff0073")
                    self.MplWidget_4.canvas.axes.plot(x2, np.linspace(0, 0, 100), linewidth=3, color="#ff0073")
                    self.MplWidget_4.canvas.axes.plot(x5, np.linspace(0, 0, 100), linewidth=3, color="#ff0073")
                    self.MplWidget_4.canvas.axes.grid(color="black", linestyle="--")
                    self.MplWidget_4.canvas.draw()

                    self.MplWidget_5.canvas.axes.clear()
                    self.MplWidget_5.canvas.axes.set_facecolor("#fffde7")
                    self.MplWidget_5.canvas.axes.set_xticks(np.linspace(0, 4 * np.pi / w * 1000, 9))
                    self.MplWidget_5.canvas.axes.set_yticks(np.linspace(Vmax / R, -Vmax / R, 6))
                    self.MplWidget_5.canvas.axes.plot(x7, np.linspace(0, 0, 100), linewidth=1, color="black")
                    self.MplWidget_5.canvas.axes.axvline(a / w * 1000, 0.5, 0.45 * np.sin(a) + 0.5, lw=3,
                                                         color="#cc00ff")
                    self.MplWidget_5.canvas.axes.axvline(a / w * 1000 + 2 * np.pi / w * 1000, 0.5,
                                                         0.45 * np.sin(a) + 0.5,
                                                         lw=3,
                                                         color="#cc00ff")
                    self.MplWidget_5.canvas.axes.set_title('Ortalama Çıkış Akımı-Zaman')
                    self.MplWidget_5.canvas.axes.plot(x1, Vmax / R * np.sin(2 * np.pi * fre * x1 / 1000), linewidth=3,
                                                      color="#cc00ff")
                    self.MplWidget_5.canvas.axes.plot(x7, Vmax / R * np.sin(2 * np.pi * fre * x7 / 1000), ":",
                                                      color="#cc00ff")
                    self.MplWidget_5.canvas.axes.plot(x3, np.linspace(0, 0, 100), linewidth=3, color="#cc00ff")
                    self.MplWidget_5.canvas.axes.plot(x4, Vmax / R * np.sin(2 * np.pi * fre * x4 / 1000), linewidth=3,
                                                      color="#cc00ff")
                    self.MplWidget_5.canvas.axes.plot(x6, np.linspace(0, 0, 100), linewidth=3, color="#cc00ff")
                    self.MplWidget_5.canvas.axes.plot(x2, np.linspace(0, 0, 100), linewidth=3, color="#cc00ff")
                    self.MplWidget_5.canvas.axes.plot(x5, np.linspace(0, 0, 100), linewidth=3, color="#cc00ff")
                    self.MplWidget_5.canvas.axes.grid(color="black", linestyle="--")
                    self.MplWidget_5.canvas.draw()

                    self.MplWidget_6.canvas.axes.clear()
                    self.MplWidget_6.canvas.axes.set_facecolor("#fffde7")
                    self.MplWidget_6.canvas.axes.set_xticks(np.linspace(0, 4 * np.pi / w * 1000, 9))
                    self.MplWidget_6.canvas.axes.set_yticks(np.linspace(Vmax / R, -Vmax / R, 5))
                    self.MplWidget_6.canvas.axes.plot(x7, np.linspace(0, 0, 100), linewidth=1, color="black")
                    self.MplWidget_6.canvas.axes.axvline(a / w * 1000, 0.5, 0.45 * np.sin(a) + 0.5, lw=3,
                                                         color="#702E52")
                    self.MplWidget_6.canvas.axes.axvline(a / w * 1000 + 2 * np.pi / w * 1000, 0.5,
                                                         0.45 * np.sin(a) + 0.5,
                                                         lw=3,
                                                         color="#702E52")
                    self.MplWidget_6.canvas.axes.set_title('Tristör Akımı-Zaman')
                    self.MplWidget_6.canvas.axes.plot(x1, Vmax / R * np.sin(2 * np.pi * fre * x1 / 1000), linewidth=3,
                                                      color="#702E52")
                    self.MplWidget_6.canvas.axes.plot(x7, Vmax / R * np.sin(2 * np.pi * fre * x7 / 1000), ":",
                                                      color="#702E52")
                    self.MplWidget_6.canvas.axes.plot(x3, np.linspace(0, 0, 100), linewidth=3, color="#702E52")
                    self.MplWidget_6.canvas.axes.plot(x4, Vmax / R * np.sin(2 * np.pi * fre * x4 / 1000), linewidth=3,
                                                      color="#702E52")
                    self.MplWidget_6.canvas.axes.plot(x6, np.linspace(0, 0, 100), linewidth=3, color="#702E52")
                    self.MplWidget_6.canvas.axes.plot(x2, np.linspace(0, 0, 100), linewidth=3, color="#702E52")
                    self.MplWidget_6.canvas.axes.plot(x5, np.linspace(0, 0, 100), linewidth=3, color="#702E52")
                    self.MplWidget_6.canvas.axes.grid(color="black", linestyle="--")
                    self.MplWidget_6.canvas.draw()

    # ....._PopUp fonksiyonları çeşitli message box tanımlamaları
    def Aci_PopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Dikkat!")
        msg.setText("""Geçersiz açı değeri girdiniz.
Lütfen doğru bir değer girip tekrar deneyin.""")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def Gerilim_PopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Dikkat!")
        msg.setText("""Geçersiz gerilim değeri girdiniz.
Gerilim sıfırdan küçük olamaz.""")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def Direnc_PopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Dikkat!")
        msg.setText("""Geçersiz direnç değeri girdiniz.
Direnç sıfırdan küçük olamaz!""")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def Eksik_PopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Dikkat!")
        msg.setText("""Eksik değer girdiniz.""")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def Virgül_PopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Dikkat!")
        msg.setText('''Lütfen ondalıklı sayı girişi için virgül(,) yerine nokta(.) kullanın! ''')
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    # "nan" çıktısının türüyle alakalı bilgi mesajı
    def nanBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("nan Ne Anlama Geliyor?")
        msg.setText('''"nan" tanımlanmamış veya sunulamayan bir değer anlamına gelmektedir!
Detaylı bilgi için "show details" butonuna tıklayın.''')
        msg.setIcon(QMessageBox.Question)
        msg.setDetailedText('''“nan” tanımsız veya belirsiz herhangi bir değeri temsil etmek için kullanılan sayısal bir veri türüdür. Örneğin. 0/0 bir gerçek sayı değildir ve bu nedenle nan ile temsil edilir.''')
        msg.exec_()

    def Frekans_PopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Dikkat!")
        msg.setText("""Geçersiz frekans değeri girdiniz.
Frekans sıfırdan küçük veya sıfıra eşit olamaz!.""")
        msg.icon = QIcon("..\GUIPages\warningIcon.png")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()




    # open_.... diğer pencereleri çağırmak için fonksiyonlar
    def open_WelcomePage(self):
        self.Welcome.show()
    def open_InfoWindow(self):
        self.InfoWindow.show()

    def open_MatGosterim(self):
        self.MatGosterim.show()

    def open_Kisaltma(self):
        self.Kisaltma.show()

    def open_Sema(self):
        self.DevreSemasi.show()


