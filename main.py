from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QHBoxLayout, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def open_files():
    global filenames #change to get rid of global variable
    filenames, _ = QFileDialog().getOpenFileNames(window, 'Select files')
    message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Destruction successful')

app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')

layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setToolTip('Destroy File')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignHCenter)

window.setLayout(layout)
window.show()
app.exec()


"""
    from pathlib import Path
    
    root_dir = Path('destination')
    
    for path in root_dir.glob("*.csv"):
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
"""