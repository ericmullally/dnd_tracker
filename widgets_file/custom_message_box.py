from PyQt5 import QtCore, QtGui, QtWidgets, uic


Ui_message_box_form, message_box_baseClass = uic.loadUiType("widgets_file\custom_message.ui")

class Custom_message_box(message_box_baseClass):
    chossen = QtCore.pyqtSignal(bool)
    """  button names : ok_button, cancel_button  """
    def __init__(self,message, *args, **kwargs):

        super().__init__( *args, **kwargs)
        self.ui = Ui_message_box_form()
        self.ui.setupUi(self)
        self.ui.message_label.setText(message)
        self.ui.message_label.adjustSize()
       
        self.ui.cancel_button.clicked.connect(self.send_cancel)
        self.ui.ok_button.clicked.connect(self.send_ok)
    
    def send_cancel(self):
         self.chossen.emit(False)
         self.close()
    
    def send_ok(self):
        self.chossen.emit(True)
        self.close()