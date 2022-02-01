#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex_gridb.py
#
#  
import tkinter as tk
from platform import python_version

class MinhaCalculadora:

	def __init__(self, parent):

		self.nValorAtual=0

		top = self.top = parent

		display = tk.Text(top,height = 1,width =20)
		display.tag_config('justified', justify="right")
		display.insert('insert',self.nValorAtual, 'justified')

		btn1= tk.Button(top, text="1", command=self.p1)
		btn2= tk.Button(top, text="2", command=self.p2)
		btn3= tk.Button(top, text="3", command=self.p3)
		btn4= tk.Button(top, text="4", command=self.p4)
		btn5= tk.Button(top, text="5", command=self.p5)
		btn6= tk.Button(top, text="6", command=self.p6)
		btn7= tk.Button(top, text="7", command=self.p7)
		btn8= tk.Button(top, text="8", command=self.p8)
		btn9= tk.Button(top, text="9", command=self.p7)
		btn0= tk.Button(top, text="0", command=self.p8)

		btnCLR = tk.Button(top, text="C", command=self.pCLR)
		btnPonto = tk.Button(top, text=".", command=self.pPonto)

		btnDivide = tk.Button(top, text="/", command=self.equal)
		btnMultiplica = tk.Button(top, text="x", command=self.multiplica)
		btnSoma= tk.Button(top, text="+", command=self.soma)
		btnSubtrai= tk.Button(top, text="-", command=self.subtrai)
		btnEqual = tk.Button(top, text="=", command=self.equal)


		btn1.grid(row=1,column=0, padx= 1, pady=10)
		btn2.grid(row=1,column=1, padx= 1, pady=10)
		btn3.grid(row=1,column=2, padx= 1, pady=10)
		btn4.grid(row=2,column=0, padx= 1, pady=10)
		btn5.grid(row=2,column=1, padx= 1, pady=10)
		btn6.grid(row=2,column=2, padx= 1, pady=10)
		btn7.grid(row=3,column=0, padx= 1, pady=10)
		btn8.grid(row=3,column=1, padx= 1, pady=10)
		btn9.grid(row=3,column=2, padx= 1, pady=10)
		btn0.grid(row=4,column=1, padx= 1, pady=10)

		btnPonto.grid(row=4,column=2, padx= 1, pady=10)
		btnCLR.grid(row=4,column=0, padx= 1, pady=10)

		btnDivide.grid(row=1,column=3, padx= 5, pady=10)
		btnMultiplica.grid(row=2,column=3, padx= 5, pady=10)
		btnSoma.grid(row=3,column=3, padx= 5, pady=10)
		btnSubtrai.grid(row=4,column=3, padx= 5, pady=10)
		btnEqual.grid(row=5,column=3, padx= 5, pady=10)


		display.grid(row=0,column=0,columnspan=4)

	def pCLR(self):
		pass

	def pPonto(self):
		pass


	def p1(self):
		pass

	def p2(self):
		pass

	def p3(self):
		pass

	def p4(self):
		pass

	def p5(self):
		pass

	def p6(self):
		pass

	def p7(self):
		pass

	def p8(self):
		pass

	def p9(self):
		pass

	def p0(self):
		pass


	def multiplica(self):
		pass

	def divide(self):
		pass

	def soma (self):
		pass

	def subtrai(self):
		pass

	def equal(self):
		print ("Para você: Implemente as funções da calculadora")
		self.top.destroy()



def main(args):
	root = tk.Tk()

	calc = MinhaCalculadora(root)
	root.wait_window(calc.top)

	return 0

if __name__ == '__main__':
	print (python_version())   #somente para verificar que estamos no ambiente virtual python 3.5
	import sys
	sys.exit(main(sys.argv))