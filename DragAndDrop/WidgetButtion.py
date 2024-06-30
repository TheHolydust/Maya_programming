import maya.cmds as cmds 
from PySide2 import QtWidgets, QtCore, QtGui


class WidgetButtMimeData(QtCore.QMimeData):
    """
    This class holds all the info that we need to transfer with a widget Drag
    """

    def __init__(self):
        super(WidgetButtMimeData,  self).__init__()
        self.someText = "none"
        self.fromWidget = None

    def setText(self, text = None):
        self.someText = text

    def getText(self):
        return self.someText




class WidgetButtion(QtWidgets.QWidget):
    """
    The button that we gonna Click | Drag | Drop
    When we click - our cursor carries MimeData that we need to feed with some custom info
    """
    
    def __init__(self, parent = None, label = "TEST"):

        super(WidgetButtion, self).__init__()

        self.setFixedHeight(40)

        # Background Color
        self.setAutoFillBackground(True)
        color = 80
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), QtGui.QColor(color,color,color))
        self.setPalette(self.p)

        # main layout
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainLayout)

        # label
        self.label = QtWidgets.QLabel(label)
        self.mainLayout.addWidget(self.label)

    def set_label(self, text = ""):
        self.label.setText(text) # for Drag and Drop


    def mouseMoveEvent(self, event):

        if event.buttons() != QtCore.Qt.LeftButton:
            return

        mimeData = WidgetButtMimeData() #create mimeData class | nothing too much happes here

        # Feed mimeData
        mimeData.setText(self.label.text())

        #Create Ghosty image behind the moving mouse cursor
        self.pixmap = self.grab()
        painter = QtGui.QPainter(self.pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(self.pixmap.rect(), QtGui.QColor(80, 80, 80, 127))
        painter.end()

        #Here we create the actual Drag class that does Dragging
        drag = QtGui.QDrag(self) # create Drag class to copy information between applications
        drag.setMimeData(mimeData) # data to be sent with Drag
        drag.setPixmap(self.pixmap) # set widget image
        drag.setHotSpot(event.pos()) #
        drag.exec_(QtCore.Qt.LinkAction | QtCore.Qt.MoveAction) # starts the Drag and Drop operation

        """
        Qt::MoveAction          0x2  (2)    Move the data from the source to the target.
        Qt::LinkAction          0x4  (4)    Create a link from the source to the target.
        """