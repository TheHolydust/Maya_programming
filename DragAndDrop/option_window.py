import maya.cmds as cmds 
from PySide2 import QtWidgets, QtCore, QtGui
import json
import os

from DragAndDrop.widget_field import WidgetField
from DragAndDrop.WidgetButtion import WidgetButtion

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin




root = r"C:/Users/Holydust/Desktop"


class OptiondWindow(MayaQWidgetBaseMixin, QtWidgets.QDialog):

    def __init__(self, parent = None):
        super(OptiondWindow, self).__init__()

        self.setupUI()

    def setupUI(self):
        
        self.setObjectName("OptionWindowID")
        self.setWindowTitle("Options")

        self.setFixedSize(300, 390)
        
        # create main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainLayout.setContentsMargins(5,5,5,5)

        self.setLayout( self.mainLayout )


        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.setAlignment(QtCore.Qt.AlignTop)
        self.topLayout.setContentsMargins(0,0,0,0)
        
        self.botLayout = QtWidgets.QHBoxLayout()
        self.botLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.botLayout.setContentsMargins(0,0,0,0)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.botLayout)

        # add widgets
        self.obj1 = WidgetField()
        self.obj1.add_test_buttions()
        self.topLayout.addWidget(self.obj1)
        # self.obj1.add_dict()

        self.obj2 = WidgetField()
        self.topLayout.addWidget(self.obj2)


        #add button
        self.saveBtn = QtWidgets.QPushButton('Save')
        self.saveBtn.setFixedWidth(100)
        self.botLayout.addWidget(self.saveBtn)
        self.saveBtn.clicked.connect(self.save_data)


        
    # def save_data(self):
        
    #     data = {}

        
    #     data['obj1'] = self.obj1.count_buttons()
    #     data['obj2'] = self.obj2.count_buttons()

       
    #     json_data = json.dumps(data)

        
    #     with open(os.path.join(root, 'data.json'), 'w') as file:
    #         file.write(json_data)

    #     self.close()

    def save_data(self):
        
        buttons_names = []

        
        widgets = QtWidgets.QApplication.instance().findChildren(WidgetButtion)

        buttons_names = [widget.text() for widget in widgets]
        # for widget in widgets:
        #     if widget.parent() == self.obj1 or widget.parent() == self.obj2:
        #         buttons_names.append(widget.label.text())

        
        with open("buttons.json", "w") as file:
            json.dump(buttons_names, file)

        
        self.close()