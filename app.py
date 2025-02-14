import sys
import pandas as pd
from PyQt5.QtWidgets import QAbstractButton, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class CadastroAluno(QWidget):
    def __init__(self):
        super().__init__()

        self.alunos = []
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Cadastro de Alunos')

        layout = QGridLayout()
        self.setLayout(layout)

        label_nome = QLabel('Nome do aluno:')
        self.input_nome = QlineEdit()
        layout.addWidget(self.input_nome, 0, 0)
        layout.addWidget(self.input_nome, 0, 1)

        label_turma = QLabel('Turma:')
        self.input_turma = QLineEdit()
        layout.addWidget(self.input_turma, 1, 0)
        layout.addWidget(self.input_turma, 1, 1)

