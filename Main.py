from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from metody_main import wykres
from hirvonen import hirvonen 
from moje_metody import decimalDeg2dms

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'App'
        self.initInterface()
        self.initWidgets()
        
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(500, 500, 310, 120)
        self.show()
        
    def initWidgets(self):
        self.btn = QPushButton("Połozenie punktu P",self)
        self.btn2 = QPushButton("Metoda Hirvonena",self)
        
        grid = QGridLayout()
        grid.addWidget(self.btn, 0, 0)
        grid.addWidget(self.btn2, 1, 0)
        self.setLayout(grid)
        self.btn.clicked.connect(self.P_window)
        self.btn2.clicked.connect(self.H_window)
        
    def P_window(self):
        self.close()
        self.next=AppWindow()
    
    def H_window(self):
        self.close()
        self.next=MetodaHirvonena()
        
        
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Położenie punktu P"
        self.initInterface()
        self.initWidgets()
        
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(500, 500, 410, 280)
        self.show()
    
    def initWidgets(self):
        #Punkt A
        P_A_Label = QLabel("<b>Punkt A :</b>", self)
        AxLabel = QLabel("X:", self)
        AyLabel = QLabel("Y:", self)
        self.AxEdit = QLineEdit()
        self.AyEdit = QLineEdit()
        
        #Punkt B
        P_B_Label = QLabel("<b>Punkt B :</b>", self)
        BxLabel = QLabel("X:", self)
        ByLabel = QLabel("Y:", self)
        self.BxEdit = QLineEdit()
        self.ByEdit = QLineEdit()
        
        #Punkt C
        P_C_Label = QLabel("<b>Punkt C :</b>", self)
        CxLabel = QLabel("X:", self)
        CyLabel = QLabel("Y:", self)
        self.CxEdit = QLineEdit()
        self.CyEdit = QLineEdit()
        
        #Punkt D
        P_D_Label = QLabel("<b>Punkt D :</b>", self)
        DxLabel = QLabel("X:", self)
        DyLabel = QLabel("Y:", self)
        self.DxEdit = QLineEdit()
        self.DyEdit = QLineEdit()
        
        
        P_P_Label = QLabel("<b>Punkt P :</b>", self)
        PxLabel = QLabel("X:", self)
        PyLabel = QLabel("Y:", self)
        self.PxEdit = QLineEdit()
        self.PyEdit = QLineEdit()
        self.PxEdit.setReadOnly(True)
        self.PyEdit.setReadOnly(True)
        self.P_polozenie = QLabel("", self)

        btn = QPushButton("Współrzędne P | Położenie P | Wykres", self)
        btn.setToolTip("Nacisnij, aby policzyć współrzędne punktu P, jego położenie orazy aby wygenerować wykres")
        btnClear = QPushButton("Clear", self)
        self.btnBack = QPushButton("Wróć", self)
        
        grid = QGridLayout()
        

        
        grid.addWidget(P_A_Label, 0, 0)
        grid.addWidget(AxLabel, 0, 1)
        grid.addWidget(AyLabel, 1, 1)       #Dla A
        grid.addWidget(self.AxEdit, 0, 2)
        grid.addWidget(self.AyEdit, 1, 2)
        
        grid.addWidget(P_B_Label, 0, 3)
        grid.addWidget(BxLabel, 0, 4)
        grid.addWidget(ByLabel, 1, 4)       #Dla B
        grid.addWidget(self.BxEdit, 0, 5)
        grid.addWidget(self.ByEdit, 1, 5)
        
        grid.addWidget(P_C_Label, 2, 0)
        grid.addWidget(CxLabel, 2, 1)
        grid.addWidget(CyLabel, 3, 1)       #Dla C
        grid.addWidget(self.CxEdit, 2, 2)
        grid.addWidget(self.CyEdit, 3, 2)
        
        grid.addWidget(P_D_Label, 2, 3)
        grid.addWidget(DxLabel, 2, 4)
        grid.addWidget(DyLabel, 3, 4)       #Dla D
        grid.addWidget(self.DxEdit, 2, 5)
        grid.addWidget(self.DyEdit, 3, 5)
        
        grid.addWidget(P_P_Label, 4, 0)
        grid.addWidget(PxLabel, 4, 1)
        grid.addWidget(PyLabel, 5, 1)       #Dla P
        grid.addWidget(self.PxEdit, 4, 2)
        grid.addWidget(self.PyEdit, 5, 2)
        grid.addWidget(self.P_polozenie, 6, 0, 1, 7)

        
        
        grid.addWidget(btn, 7, 0, 1, 7)
        grid.addWidget(btnClear, 8, 0, 1, 7)
        grid.addWidget(self.btnBack, 9, 0, 1, 7)
        
        self.setLayout(grid)
        
        btn.clicked.connect(self.dzialanie)
        btnClear.clicked.connect(self.clear)
        self.btnBack.clicked.connect(self.back)
        
    def dzialanie(self):
        
        nadawca = self.sender()

        try:
            A_X = float(self.AxEdit.text())
            A_Y = float(self.AyEdit.text())
            B_X = float(self.BxEdit.text())
            B_Y = float(self.ByEdit.text())
            C_X = float(self.CxEdit.text())
            C_Y = float(self.CyEdit.text())
            D_X = float(self.DxEdit.text())
            D_Y = float(self.DyEdit.text())

            if nadawca.text() == "Współrzędne P | Położenie P | Wykres":
                bx1,txt,P_X,P_Y = wykres(A_X,A_Y,B_X,B_Y,C_X,C_Y,D_X,D_Y)
            
            self.PxEdit.setText(str(P_X))
            self.PyEdit.setText(str(P_Y))
            self.P_polozenie.setText(str(txt))
            
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Złe typy danych!", QMessageBox.Ok)
            self.xEdit().clear()
            self.yEdit().clear()
    
    def clear(self):
        
        self.AxEdit.clear()
        self.AyEdit.clear()
        self.BxEdit.clear()
        self.ByEdit.clear()
        self.CxEdit.clear()
        self.CyEdit.clear()
        self.DxEdit.clear()
        self.DyEdit.clear()
        self.PxEdit.clear()
        self.PyEdit.clear()
        self.P_polozenie.clear()
    
    def back(self):
        self.close()
        self.next=MainWindow()
        
        
class MetodaHirvonena(QWidget):
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.setGeometry(500,500,150,130)          # miejsce wyswietlenia się na ekranie oraz szerokość i wysokość okna;
        self.setWindowIcon(QIcon('H.png'))         
        self.setWindowTitle("Metoda Hirvonena")   
        self.show()

    def interfejs_widgets(self):
        # umieszczenie i rozmieszczenie widżetów
        e1 = QLabel("X :", self)
        e2 = QLabel("Y :", self)
        e3 = QLabel("Z :", self)
        e7 = QLabel("Minuty :", self)
        e8 = QLabel("Stopnie :", self)
        e9 = QLabel("Sekundy :", self)
        e10 = QLabel("H :", self)
        
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        
        self.fistopnie = QLineEdit()
        self.fiminuty  = QLineEdit()
        self.fisekundy = QLineEdit()
        self.lambdastopnie = QLineEdit()
        self.lambdaminuty  = QLineEdit()
        self.lambdasekundy = QLineEdit()
        self.wysokosc = QLineEdit()
        
        self.fistopnie.setReadOnly(True)
        self.fiminuty.setReadOnly(True)
        self.fisekundy.setReadOnly(True)
        self.lambdastopnie.setReadOnly(True)
        self.lambdaminuty.setReadOnly(True)
        self.lambdasekundy.setReadOnly(True)
        self.wysokosc.setReadOnly(True)
        
        
        
        self.button = QPushButton(" ", self)
        self.button.setIcon(QIcon("strzalka w prawo.jpg"))
        self.clearbutton = QPushButton("Clear", self)
        self.clearbutton.setToolTip("Po nacisnięciu wszystkie pola zostaną <b>wyczyszczone</b>") # wskazówka
        self.btnBack = QPushButton("Wróć", self)

        fi      = QPixmap("fi.png") # symbol współrzędnej fi
        lambdaa =  QPixmap("lambda.png") # symbol współrzędnej lambda
        hirv     = QPixmap("metoda hirvonena.png") # rysunek
        
        filbl = QLabel(self)
        filbl.setPixmap(fi) # dodanie rysunku do widgetu
        
        lambdalbl = QLabel(self)
        lambdalbl.setPixmap(lambdaa) 
        
        hirvlbl = QLabel(self)
        hirvlbl.setPixmap(hirv) 
        
        grid  = QGridLayout()
        
        grid.addWidget(e1, 1, 0)
        grid.addWidget(e2, 2, 0)
        grid.addWidget(e3, 3, 0)
        
        grid.addWidget(self.l1, 1, 1)
        grid.addWidget(self.l2, 2, 1)
        grid.addWidget(self.l3, 3, 1)
        
        grid.addWidget(self.button, 2, 2)
        
        grid.addWidget(filbl, 1, 3)
        grid.addWidget(lambdalbl, 2, 3)
        grid.addWidget(e10, 3, 3)
        
        grid.addWidget(self.fistopnie, 1, 4)
        grid.addWidget(self.fiminuty, 1, 5)
        grid.addWidget(self.fisekundy, 1, 6)
        
        grid.addWidget(self.lambdastopnie, 2, 4)
        grid.addWidget(self.lambdaminuty, 2, 5)
        grid.addWidget(self.lambdasekundy, 2, 6)
        grid.addWidget(self.wysokosc, 3, 4, 1, 3)
        
        grid.addWidget(e7, 0, 4)
        grid.addWidget(e8, 0, 5)
        grid.addWidget(e9, 0, 6)
        grid.addWidget(self.clearbutton, 4, 0, 1, 7)
        grid.addWidget(hirvlbl, 6, 0, 1, 7)
        grid.addWidget(self.btnBack, 5, 0, 1, 7)
        
        
        self.setLayout(grid)
        
        self.button.clicked.connect(self.dzialanie)

        self.clearbutton.clicked.connect(self.clear)
        self.btnBack.clicked.connect(self.back)
        
    def dzialanie(self):
        
        nadawca = self.sender()
        
        try:
            # pobranie współrzędnych
            X = float(self.l1.text()) 
            Y = float(self.l2.text())
            Z = float(self.l3.text())
            
            if nadawca.text() == " ":
                B, L, H = hirvonen(X, Y, Z, a = 6378137., e2 = 0.00669438002290) 
                fi = decimalDeg2dms(B)
                la = decimalDeg2dms(L)
           
            #wyswietlenie wynikow   
            self.fistopnie.setText(str(fi[0]))
            self.fiminuty.setText(str(fi[1]))
            self.fisekundy.setText(str(round(fi[2],5)))
            
            self.lambdastopnie.setText(str(la[0]))
            self.lambdaminuty.setText(str(la[1]))
            self.lambdasekundy.setText(str(round(la[2],5)))
            
            self.wysokosc.setText(str(round(H,3)))
            
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Brak danych!", QMessageBox.Ok)
            
    def clear(self):
        self.fistopnie.clear()
        self.fiminuty.clear()
        self.fisekundy.clear()
        self.lambdastopnie.clear()
        self.lambdaminuty.clear()
        self.lambdasekundy.clear()
        self.wysokosc.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        
    def closeEvent(self, event):
        #  wyświetlamy użytkownikowi prośbę o potwierdzenie zamknięcia
        # dziala po kliknieciu close
        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno chcesz zakończyć?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
            
    def back(self):
        self.close()
        self.next=MainWindow()
        
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = MainWindow()
    sys.exit(app.exec_())