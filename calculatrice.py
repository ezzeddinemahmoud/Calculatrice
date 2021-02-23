# ---------- Importations ---------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


from Main import Ui_MainWindow
# ------------ Initialisations -----------------------------
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# +++++++++++++ Logique de l'application ++++++++++++++++++++
# Déclaration des variables globales ---------
check = True
res =None
# Les fonctions (Les slots)
# fonction zero ------------
def zero():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "0")
    else:
        ui.lineEdit.setText("0")
    check = True
# fonction one ------------
def one():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "1")
    else:
        ui.lineEdit.setText("1")
        check = True
# fonction tow ------------
def tow():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "2")
    else:
        ui.lineEdit.setText("2")
        check = True
# fonction three ------------
def three():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "3")
    else:
        ui.lineEdit.setText("3")
        check = True
# fonction fore ------------
def fore():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "4")
    else:
        ui.lineEdit.setText("4")
        check = True
# fonction five ------------
def five():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "5")
    else:
        ui.lineEdit.setText("5")
        check = True
# fonction six ------------
def six():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "6")
    else:
        ui.lineEdit.setText("6")
        check = True
# fonction seven ------------
def seven():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "7")
    else:
        ui.lineEdit.setText("7")
        check = True
# fonction eight ------------
def eight():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "8")
    else:
        ui.lineEdit.setText("8")
        check = True
# fonction nine ------------
def nine():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "9")
    else:
        ui.lineEdit.setText("9")
        check = True
# fonction virgule ------------
def virgule():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + ".")
    else:
        ui.lineEdit.setText(".")
        check = True
# fonction mult ------------
def mult():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "*")
    check = True
# fonction plus ------------
def plus():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "+")
    check = True
# fonction minus ------------
def minus():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "-")
    check = True
# fonction diviser ------------
def diviser():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "/")
    check = True
# fonction parenttg ------------
def parentg():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + "(")
    else:
        ui.lineEdit.setText("(")
        check = True
# fonction parentd ------------
def parentd():
    global check
    if check:
        ui.lineEdit.setText(ui.lineEdit.text() + ")")
    else:
        ui.lineEdit.setText(")")
        check = True
# fonction clear ------------
def clear():
    ui.lineEdit.setText("")
# fonction memoriser ------------
def memoriser():
    if res is not None:
        ui.lineEdit.setText(ui.lineEdit.text() + str(res))
    else:
        pass
# fonction equal ------------
def equal():
    global res
    global check
    try:
        ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
        res=ui.lineEdit.text()
    except ZeroDivisionError:
        ui.lineEdit.setText("Division par zero impossible")
    except SyntaxError:
        ui.lineEdit.setText("Opération invalide")
    except:
        ui.lineEdit.setText("Error")
    check = False


# ------------ Connection ----------- (Relier les boutons aux fonctions)
ui.pushButton.clicked.connect(memoriser)
ui.pushButton_8.clicked.connect(zero)
ui.pushButton_7.clicked.connect(virgule)
ui.pushButton_9.clicked.connect(one)
ui.pushButton_11.clicked.connect(tow)
ui.pushButton_10.clicked.connect(three)
ui.pushButton_12.clicked.connect(fore)
ui.pushButton_14.clicked.connect(five)
ui.pushButton_13.clicked.connect(six)
ui.pushButton_15.clicked.connect(seven)
ui.pushButton_17.clicked.connect(eight)
ui.pushButton_16.clicked.connect(nine)
ui.pushButton_19.clicked.connect(clear)
ui.pushButton_22.clicked.connect(mult)
ui.pushButton_21.clicked.connect(diviser)
ui.pushButton_23.clicked.connect(minus)
ui.pushButton_24.clicked.connect(plus)
ui.pushButton_18.clicked.connect(parentg)
ui.pushButton_20.clicked.connect(parentd)
ui.pushButton_25.clicked.connect(equal)

# -------- Fin du programme --------------------------------
sys.exit(app.exec_())
