import os
from github import Github
import time
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMainWindow
import sys


def start_download():
    token = token_field.text()
    main_window.close()
    try:
        g = Github(token)
        links = []
        g.get_organization('LARS-409').get_repos()
        for r in g.get_organization('LARS-409').get_repos():
            links.append(r.clone_url)

        git_dir = str(time.asctime()).replace(" ", "_").replace(":", ".")
        os.system("md " + git_dir)
        os.chdir(git_dir)
        os.system("git init")
        for link in links:
            cmd = "git clone " + link
            os.system(cmd)
    except Exception as e:
        print(e)


app = QApplication(sys.argv)
main_window = QWidget()
main_window.resize(500, 40)
main_window.setWindowTitle("Git start")
button = QPushButton('start download')
label = QLabel("input token: ")
button.clicked.connect(start_download)
token_field = QLineEdit()

box = QHBoxLayout()
box.addWidget(label)
box.addWidget(token_field)
box.addWidget(button)
main_window.setLayout(box)
main_window.show()
sys.exit(app.exec())
