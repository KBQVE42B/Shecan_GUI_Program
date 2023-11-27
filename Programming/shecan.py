# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pickle

class Ui_Shecan(object):
	# the auto screen sizing for qt with os code
	os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    
	# the setup ui function
	def setupUi(self, Shecan):
		global active
		global mint, bg_color, white_color, black, soft_green, soft_pink

		# colors
		mint = "#4CD3C2"
		bg_color = "#363636"
		white_color = "#EEEEEE"
		black = "#252525"
		soft_green = "#B7EFCD"
		soft_pink = "#FFBCBC"

		Shecan.setObjectName("Shecan")
		Shecan.resize(285, 330)
		Shecan.setMinimumSize(QtCore.QSize(285, 330))
		Shecan.setMaximumSize(QtCore.QSize(285, 330))

		# defining active variable
		active_file = open('active.dat', 'rb')
		active = pickle.load(active_file)
		
		self.centralwidget = QtWidgets.QWidget(Shecan)
		self.centralwidget.setObjectName("centralwidget")
		
		self.title = QtWidgets.QLabel(self.centralwidget)
		self.title.setGeometry(QtCore.QRect(-3, 0, 291, 61))
		self.title.setObjectName("title")

		self.active_btn = QtWidgets.QPushButton(self.centralwidget)
		self.active_btn.setGeometry(QtCore.QRect(28, 190, 231, 61))
		self.active_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.active_btn.setObjectName("active_btn")

		self.status = QtWidgets.QLabel(self.centralwidget)
		self.status.setGeometry(QtCore.QRect(10, 70, 91, 16))
		self.status.setStyleSheet("color: #FF5722;")
		self.status.setObjectName("status")

		Shecan.setCentralWidget(self.centralwidget)
		self.retranslateUi(Shecan)

		if active:
			# main window background
			Shecan.setStyleSheet(f"background-color: {mint};\n"
			"color: rgb(238, 238, 238);")

			# title
			self.title.setStyleSheet(f"color: {soft_pink};\n"
			"font: 20pt \"Jokerman\";\n"
			"background-color: #252525;\n"
			"padding-left: 100px;\n"
			"border-radius: 7px;\n"
			f"border-bottom: 2px solid {soft_pink};")

			# Active Button
			self.active_btn.setStyleSheet("border-radius: 30px;\n"
			f"border: 2px solid {black};\n"
			f"background-color: {soft_pink};\n"
			"color: #252525;\n"
			"font: 16pt \"Jokerman\";")

			self.active_btn.setText("DeActive")

			# change status color to green and change its text
			self.status.setText('Status : Active')
			self.status.setStyleSheet(f"color: {soft_green};")

		else:
			# main window background
			Shecan.setStyleSheet("background-color: #363636;\n"
			"color: rgb(238, 238, 238);\n"
			"")

			# title
			self.title.setStyleSheet("color: rgb(183, 239, 205);\n"
			"font: 20pt \"Jokerman\";\n"
			"background-color: #252525;\n"
			"padding-left: 100px;\n"
			"border-radius: 7px;\n"
			"border-bottom: 2px solid rgb(76, 211, 194);")

			# Active button
			self.active_btn.setStyleSheet("border-radius: 30px;\n"
			"border: 2px solid #B7EFCD;\n"
			"background-color: #4CD3C2;\n"
			"color: 252525;\n"
			"font: 16pt \"Jokerman\";")

			self.active_btn.setText("Active")

			# change status color to green and change its text
			self.status.setText('Status : DeActive')
			self.status.setStyleSheet("color: #FF5722;")
		
		self.active_btn.clicked.connect(self.activate_deactivate) # call the activate_deactivate function when the button clicked
		QtCore.QMetaObject.connectSlotsByName(Shecan)
	
	
	def activate_deactivate(self):
		global active

		if not active:
			# main window background
			Shecan.setStyleSheet(f"background-color: {mint};\n"
			"color: rgb(238, 238, 238);")

			# title
			self.title.setStyleSheet(f"color: {soft_pink};\n"
			"font: 20pt \"Jokerman\";\n"
			"background-color: #252525;\n"
			"padding-left: 100px;\n"
			"border-radius: 7px;\n"
			f"border-bottom: 2px solid {soft_pink};")

			# Active Button
			self.active_btn.setStyleSheet("border-radius: 30px;\n"
			f"border: 2px solid {black};\n"
			f"background-color: {soft_pink};\n"
			"color: #252525;\n"
			"font: 16pt \"Jokerman\";")

			self.active_btn.setText("DeActive")

			# change status color to green and change its text
			self.status.setText('Status : Active')
			self.status.setStyleSheet(f"color: {soft_green};")

			# changing the dns to shecan DNSes
			os.system('netsh interface ip set dns "Wi-Fi 3" static 178.22.122.100')
			os.system('netsh interface ip add dns "Wi-Fi 3" 185.51.200.2 index=2')

			# change the active var to true and dump it to our active.dat file with pickle lib
			active = True
			active_file = open('active.dat', 'wb')
			pickle.dump(active, active_file)
			
		else:
			# main window background
			Shecan.setStyleSheet("background-color: #363636;\n"
			"color: rgb(238, 238, 238);\n"
			"")

			# title
			self.title.setStyleSheet("color: rgb(183, 239, 205);\n"
			"font: 20pt \"Jokerman\";\n"
			"background-color: #252525;\n"
			"padding-left: 100px;\n"
			"border-radius: 7px;\n"
			"border-bottom: 2px solid rgb(76, 211, 194);")

			# Active button
			self.active_btn.setStyleSheet("border-radius: 30px;\n"
			"border: 2px solid #B7EFCD;\n"
			"background-color: #4CD3C2;\n"
			"color: 252525;\n"
			"font: 16pt \"Jokerman\";")

			self.active_btn.setText("Active")

			# change status color to green and change its text
			self.status.setText('Status : DeActive')
			self.status.setStyleSheet("color: #FF5722;")
						
			# changing the dns to dhpc
			os.system('netsh interface ip set dns "Wi-Fi 3" dhcp')
			# change the active var to false and dump it to our active.dat file with pickle lib
			active = False
			active_file = open('active.dat', 'wb')
			pickle.dump(active, active_file)
			


	def retranslateUi(self, Shecan):
		_translate = QtCore.QCoreApplication.translate
		Shecan.setWindowTitle(_translate("Shecan", "Shecan"))
		self.title.setText(_translate("Shecan", "Shecan"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Shecan = QtWidgets.QMainWindow()
	ui = Ui_Shecan()
	ui.setupUi(Shecan)
	Shecan.show()
	sys.exit(app.exec_())