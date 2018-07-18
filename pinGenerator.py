from __future__ import print_function
import sys
import string
import random
import time
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QApplication
from librouteros import connect
from escpos.printer import Network
from datetime import datetime


class PINGenerator(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()


	def Generador(self, size = 6, chars = string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))


	def Print(self):
		pin = self.Generador()
		api = connect(username='api', password='eior48nr', host='168.227.22.136')

		parametros = {
			'name': pin,
			'password': pin,
			'profile': 'default',
			'server': 'all'
		}

		api(cmd='/ip/hotspot/user/add', **parametros)
		api.close()


		###############################################
		#					IMPRIMIR
		###############################################
		#impresora = Network("192.168.1.99")
		#today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		#time.sleep(1)
		#impresora.set(
		#	font='a',
		#	height=2,
		#	align='left',
		#	bold=False,
		#	double_height=False
		#)
		#impresora.text('Hotel Florencia \n')
		#impresora.text('\n')
		#impresora.text('Clave De Acceso Wifi \n')
		#impresora.text('\n')
		#impresora.text(pin)
		#impresora.text('\n')
		#impresora.text('Fecha/Hora Generado \n')
		#impresora.text(today)
		#impresora.text('Gracias Por Preferirnos \n')

		self.lbl_a.setText(pin)
		self.lbl_a.adjustSize()


	def initUI(self):
		self.lbl_a = QLabel(self)
		self.lbl_a.move(120, 30)
		self.lbl_a.setText('------')


		lbl = QLabel(self)
		lbl.move(10, 10)
		lbl.setText('PIN De Acceso')

		gbtn = QPushButton('Generar', self)
		gbtn.resize(gbtn.sizeHint())
		gbtn.move(30, 65)
		gbtn.clicked.connect(self.Print)

		qbtn = QPushButton('Cerrar', self)
		qbtn.clicked.connect(QApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(180, 65)

		self.setGeometry(300, 300, 280, 100)
		self.setWindowTitle('Hotel Florencia')
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = PINGenerator()
	sys.exit(app.exec_())
