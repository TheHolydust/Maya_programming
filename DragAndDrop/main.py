import maya.cmds as cmds 
from PySide2 import QtWidgets, QtCore, QtGui

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

from option_window import OptiondWindow


class MianCostomWindow(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    
    def __init__(self):
        super(MianCostomWindow, self).__init__()

        self.setupUI()

    def setupUI(self):
        
        self.setObjectName("MianCostomWindowID")
        self.setWindowTitle("Main Window")

        self.setMinimumSize(500, 400)

        
        # create main layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainLayout.setContentsMargins(5,5,5,5)

        # create buttion
        self.optBtn = QtWidgets.QPushButton('Options')

        # crate left layout
        group_box1 = QtWidgets.QGroupBox()
        group_box1.setStyleSheet("background-color: rgb(100, 100, 100);")
        group_box1.setContentsMargins(10,10,10,10)
        
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setAlignment(QtCore.Qt.AlignTop)
        self.leftLayout.setContentsMargins(0,0,0,0)
        group_box1.setLayout(self.leftLayout)

        # crate rigt layout
        group_box2 = QtWidgets.QGroupBox()
        group_box2.setStyleSheet("background-color: rgb(100, 100, 100);")
        group_box2.setFixedWidth(100)
        group_box2.setContentsMargins(10,10,10,10)

        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setAlignment(QtCore.Qt.AlignBottom)
        self.rightLayout.setContentsMargins(0,0,0,0)
        group_box2.setLayout(self.rightLayout)

        # create top righ layout
        self.rightopLayout = QtWidgets.QVBoxLayout()
        self.rightopLayout.setAlignment(QtCore.Qt.AlignBottom)
        self.rightLayout.addLayout ( self.rightopLayout, stretch = 3 )

        self.righBotLayout = QtWidgets.QVBoxLayout()
        self.righBotLayout.setAlignment(QtCore.Qt.AlignBottom)
        self.righBotLayout.addWidget ( self.optBtn )
        self.rightLayout.addLayout ( self.righBotLayout, stretch = 0 )

        # set
        self.mainLayout.addWidget(group_box1)
        self.mainLayout.addWidget(group_box2)

        # self.mainLayout.addLayout( self.leftLayout, stretch = 3  ) 
        # self.mainLayout.addLayout( self.rightLayout, stretch = 0  ) 

        # set layouts
        self.setLayout( self.mainLayout )



        self.optBtn.clicked.connect ( self.opt_window)

    
    def opt_window(self):
        
        self.opt_win = OptiondWindow()
        self.opt_win.show()







def main():

    if cmds.window('MianCostomWindowID', q=1, exists=1):
        cmds.deleteUI('MianCostomWindowID')
    
    if cmds.windowPref('MianCostomWindowID', exists = 1):
        cmds.windowPref('MianCostomWindowID', remove = 1)


    global myUi
    myUI = MianCostomWindow()
    myUI.show()



if __name__ == "__main__":
    main()
