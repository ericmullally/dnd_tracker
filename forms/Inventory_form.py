from PyQt5 import QtCore, QtGui, QtWidgets, uic

Ui_inventory_form, inventory_baseClass = uic.loadUiType("forms\inventory_form.ui")

class Inventory_from(inventory_baseClass):
    submit_inventory = QtCore.pyqtSignal(object)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_inventory_form()
        self.ui.setupUi(self)
        self.ui.add_atk_button.clicked.connect(self.add_atk_input)
        self.ui.add_equipment_button.clicked.connect(self.add_equipment_input)
        self.ui.add_feat_button.clicked.connect(self.add_feats_input)
        self.ui.submit_button.clicked.connect(self.submit_form)
        self.show()

    def add_atk_input(self):
        row_num = self.ui.atks_layout.rowCount()
        atk_field_list = []
        for i in range(0,3):
            atk_field = QtWidgets.QLineEdit("", self) 
            atk_field.setObjectName(f"atk_feild_{i}_row_{row_num}")
            atk_field_list.append(atk_field)
            atk_field.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            atk_field.setMinimumHeight(15)
            atk_field.setMaximumWidth(70)
        delete_button = QtWidgets.QPushButton("delete_button", self)
        delete_button.setText("X")
        delete_button.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        delete_button.setMinimumHeight(15)
        delete_button.setFixedWidth(32)
        atk_field_list.append(delete_button)
        
        
        
        for i in range(0,4):
            self.ui.atks_layout.addWidget(atk_field_list[i],row_num, i )

    def add_equipment_input(self):
        equipment_title = QtWidgets.QLineEdit("", self.ui.equipment_contents)
        count_button = QtWidgets.QSpinBox( self.ui.equipment_contents)
        
        count_button.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        count_button.setMinimumHeight(15)
        count_button.setFixedWidth(32)
        
        equipment_title.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        equipment_title.setMinimumHeight(15)
        equipment_title.setFixedWidth(200)

        self.ui.equipment_layout.addRow(equipment_title, count_button)
        
    def add_feats_input(self):
        feat_title = QtWidgets.QLineEdit("", self.ui.equipment_contents)
        delete_button = QtWidgets.QPushButton( "X",self.ui.equipment_contents)
        
        delete_button.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        delete_button.setMinimumHeight(15)
        delete_button.setFixedWidth(32)
        
        feat_title.setSizePolicy(
                        QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        feat_title.setMinimumHeight(15)
        feat_title.setFixedWidth(250)

        self.ui.feats_layout.addRow(feat_title, delete_button)

    def submit_form(self):
        """row starts at 1"""
        from_data = {"attacks":{}, }
        for atk in self.ui.atks_content.children():
           if isinstance(atk, QtWidgets.QLineEdit):
               if "0" in atk.objectName():
                   print(atk.objectName())
                   from_data["attacks"][atk.text()] = []
                
       
                   