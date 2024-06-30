"""
This is widget from drag and drop
"""
import maya.cmds as cmds 
from PySide2 import QtWidgets, QtCore, QtGui

from DragAndDrop.WidgetButtion import WidgetButtion




class WidgetField(QtWidgets.QWidget):

    def __init__(self):
        super(WidgetField, self).__init__()

        self.setFixedSize(143, 350)
        self.setAcceptDrops(True)

        #bg color
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(40,40,40))
        self.setPalette(self.p)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setContentsMargins(2,2,2,2)
        self.setLayout(self.mainLayout)
        

        #* scroll area-----------------------------------------------------------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(340)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(130)
     
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)

        self.scroll_layout = QtWidgets.QGridLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,3,0)
        self.scroll_layout.setSpacing(3) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)

        self.mainLayout.addWidget(self.scrollArea) #add to main layout   
        #*-----------------------------------------------------------------------     

    def add_test_buttions(self):
        for i in range(4):
            self.btn = WidgetButtion(label = "bution_" + str(i))
            self.scroll_layout.addWidget(self.btn)

    def count_buttons(self):
        return self.scroll_layout.count()



    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        #! add drop event script
        
        mimeData = event.mimeData()
        text = mimeData.getText()
        event.source().deleteLater()

        button = WidgetButtion()
        button.set_label(text)
        self.scroll_layout.addWidget(button)


