#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Desenvolvido por: @Thiago.leandro.py Intagram.
#      Portifólio: https://infosistemaspy.github.io/portal/
#         Git Hub: https://github.com/InfoSistemasPy


# Importar as Bibliotecas e Dependencias
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QMainWindow, QProgressBar
import time
import os
import sys

# Variaveis globais
valor = 0
caminho = os.getcwd()

def funcao_principal():
    global valor
    global caminho
    
     # Barra de Progresso
    tela.progressBar.setValue(valor)
    tela.progressBar.setRange(0, 100)
    valor = valor + 15
    time.sleep(1)
    tela.progressBar.setValue(valor)
    valor = valor + 10
    time.sleep(1)
    tela.progressBar.setValue(valor)
    valor = valor + 15
    time.sleep(1)
    
    # Entrada de dados do nome do Arquivo
    nome_arquivo = tela.lineEdit.text()
    
     # Barra de Progresso
    tela.progressBar.setValue(valor)
    tela.progressBar.setRange(0, 100)
    valor = valor + 10
    time.sleep(1)
    tela.progressBar.setValue(valor)
    valor = valor + 20
    time.sleep(1)
    tela.progressBar.setValue(valor)
    valor = valor + 10
    time.sleep(1)
    
    # Codigo da Conversão
    os.system('cd ' + caminho)
    # Não sei se precisa instalar
    #os.system('pip install pyinstaller')
    os.system('pyinstaller --onefile -w {}'.format(nome_arquivo))
    
    # Barra de Progresso
    tela.progressBar.setValue(valor)
    tela.progressBar.setRange(0, 100)
    valor = valor + 20
    time.sleep(1)
    
    # Teste do app
    print('py_to_exe')
    
    #Limpar LineEdit e o progressBar
    time.sleep(1)
    tela.lineEdit.clear()
    tela.progressBar.setValue(0)
    
app=QtWidgets.QApplication([])
tela=uic.loadUi('janela.ui')

tela.pushButton_3.clicked.connect(funcao_principal)

tela.show()
app.exec()


# In[ ]:




