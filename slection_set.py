import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin # use it to keep UI on top of Maya UI



class SelectionSetWgt(QtWidgets.QWidget,):
    def __init__(self, selection):
        super(SelectionSetWgt, self).__init__()

        self.selection = selection
        self.state = True

        self.setupUI()

      
    
    def setupUI(self):


        self.setMinimumSize(260,40)
        self.setMaximumHeight(40)

        self.setAutoFillBackground(True)
        self.set_bacground(100, 100, 100) #emit 'set_bacground' function
        
        #setup mainLayout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setContentsMargins(5,5,5,5)
        self.setLayout( self.mainLayout )

              
        #
        
        
        #check obj type
        if  self.selection == cmds.ls(sl=1, type = 'transform'):
            self.selection = cmds.sets(self.selection, n = "set_1")
            
        # create label
        self.annotLabel = QtWidgets.QLabel(self.selection) 
        
        # set_label
        self.annotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget( self.annotLabel )

        #* Context menu
        self.popMenu = QtWidgets.QMenu(self)

        self.popMenuAdd = QtWidgets.QAction('Add object', self)
        self.popMenu.addAction(self.popMenuAdd)
        self.popMenuAdd.triggered.connect(self.testA)

        self.popMenuDel = QtWidgets.QAction('Delete object', self)
        self.popMenu.addAction(self.popMenuDel)
        self.popMenuDel.triggered.connect(self.testB)    

        # attributes
        self.setMouseTracking(True)  
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)
        #*______________________________________


        
    # set bacground to funcion    
    def set_bacground(self, r=100, g=100, b=100):
        self.p = QtGui.QPalette() # crate  palitra class
        
        self.color = QtGui.QColor(r,g,b) #crate color variable
        
        self.p.setColor(self.backgroundRole(), self.color) # set color
        self.setPalette(self.p) # instal palette in space


    # events

    def mouseReleaseEvent(self, event):
        self.set_bacground(100,100,100)
        
        if self.state == True:
            cmds.select(self.selection)


    def enterEvent(self, event):
        self.set_bacground(120,120,120)
        
    def leaveEvent(self, event):
        self.set_bacground(100,100,100)

    def mousePressEvent(self, event):
        self.set_bacground(130,130,130)
        
        if event.buttions() == QtCore.Qt.LeftButton:
            self.state = True
        elif event.buttions() == QtCore.Qt.RightButton:
            self.state = False

    


    
    
    def onContextMenu(self, point):

        self.popMenu.exec_(self.mapToGlobal(point))

    
    
    
    
    def testA(self):
        sel = cmds.ls(sl = 1, l = 1 )
        cmds.sets(sel, add = 'set_1')
        print ("TEST A")

    def testB(self):
        print ("TEST B")





class MyCostomWidget(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    def __init__(self):
        super(MyCostomWidget, self).__init__()

        self.i = 1
        self.selection = None
        
        self.setupUI()
        

    def setupUI(self):
        
        self.setObjectName('MyCostomWidgetUIId')
        self.setWindowTitle('My Test UI')
        self.setMinimumSize(300, 500) # Width , Height in pixels 
        
        #create main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.mainLayout.setContentsMargins(5,5,5,5)
        
        #set main layout
        self.setLayout( self.mainLayout )


        #* scroll area-----------------------------------------------------------
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(290)
     
        self.scrollArea.setFocusPolicy( QtCore.Qt.NoFocus )
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)

        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,0,0)
        self.scroll_layout.setSpacing(4) #layout
        self.scroll_area_widget.setLayout(self.scroll_layout)

        self.mainLayout.addWidget(self.scrollArea) #add to main layout   
        #*-----------------------------------------------------------------------           

       
        # create buttion plus
        self.button_Create = QtWidgets.QPushButton('+')
        self.mainLayout.addWidget(self.button_Create)
        
        # crate connection
        self.button_Create.clicked.connect( self.crate_set )

                

    def crate_set(self):

        selection = cmds.ls(sl = 1,) 

        if not selection:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Please, select objects')
            return
        
        #add exist sets
        if selection == cmds.ls(sl = 1, type = 'objectSet'):
            for i in selection:
                self.set_wgt = SelectionSetWgt(i)
                self.scroll_layout.addWidget( self.set_wgt )
        
        else:
            self.set_wgt = SelectionSetWgt(selection)
            self.scroll_layout.addWidget( self.set_wgt )

        



def main():

    if cmds.window('MyCostomWidgetUIId', q=1, exists=1):
        cmds.deleteUI('MyCostomWidgetUIId')
    
    if cmds.windowPref('MyCostomWidgetUIId', exists = 1):
        cmds.windowPref('MyCostomWidgetUIId', remove = 1)


    global myUi
    myUI = MyCostomWidget()
    myUI.show()


if __name__ == "__main__":
    main()
