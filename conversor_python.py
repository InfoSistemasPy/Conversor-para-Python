#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Desenvolvido por: @Thiago.leandro.py Intagram.
#      Portifólio: https://infosistemaspy.github.io/portal/
#         Git Hub: https://github.com/InfoSistemasPy


# Importar as Bibliotecas e Dependencias
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout, QMainWindow, QProgressBar
from PyQt5.QtWidgets import QMessageBox
import time
import os
import sys
import sip

def funcao_principal():
    valor = 0
    caminho = os.getcwd()
    extensao = ".py"
    nome_arquivo = tela.lineEdit.text()
    
    #Loop de verificação
    if extensao in nome_arquivo:
        pos = nome_arquivo.find('.')
        print(pos)
        
        # Barra de Progresso
        tela.progressBar.setValue(valor)
        tela.progressBar.setRange(0, 100)
        valor = valor + 15
        tela.progressBar.setValue(valor)
        time.sleep(1)
        valor = valor + 10
        tela.progressBar.setValue(valor)
        time.sleep(1)
        valor = valor + 20
        tela.progressBar.setValue(valor)
        time.sleep(1)
        valor = valor + 15
        tela.progressBar.setValue(valor)
        time.sleep(1)
        valor = valor + 25
        tela.progressBar.setValue(valor)
        time.sleep(1)
        valor = valor + 15
        tela.progressBar.setValue(valor)
        time.sleep(1)
    
        # Codigo da Conversão
        os.system('cd ' + caminho)
        # Não sei se precisa instalar
        os.system('pip install cx_freeze')
        time.sleep(5)
        os.system('cxfreeze {}'.format(nome_arquivo))
     
        # Teste do app
        print('py_to_exe')
        #Mensagen de conclusão popup
        mgs_py_to_exe = "Conversão 100% Concluida!!!"
        QMessageBox.about(tela,"py_to_exe",mgs_py_to_exe)
    
        #Limpar LineEdit e o progressBar
        time.sleep(1)
        tela.lineEdit.clear()
        tela.progressBar.setValue(0)
    else:
        print("erro")
        msg_else ="Por favor escreva o nome do programa + " + ".py"
        QMessageBox.about(tela,"alerta",msg_else)
    
app=QtWidgets.QApplication([])
tela=uic.loadUi('janela.ui')

tela.pushButton_3.clicked.connect(funcao_principal)

tela.show()
app.exec()
sys.exit(app.exec())


# In[ ]:




