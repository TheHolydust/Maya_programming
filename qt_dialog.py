import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui




class MyDialog(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super(MyDialog, self).__init__() # Инициализация всех свойств и настроек класса QDialog
        
        self.seup_UI()
    
        
    def seup_UI(self):    
        # становится частью окна Maya
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        # задать уникальный идентификатор окна
        self.setObjectName('myTestWindow')
        
        # установить видимое название окна
        self.setWindowTitle('My Test UI')
        
        # размер окна (меньше окно сделать нельзя)
        self.setMinimumSize(300, 160) # Width , Height in pixels
        self.setMaximumSize (400, 200)

        # create main layout
        self.mainLayout = QtWidgets.QVBoxLayout()

        self.setLayout(self.mainLayout) # установить в наш QDialog главный layout

        # создаем поле ввода
        self.mainLine = QtWidgets.QLineEdit()
        self.mainLine.setPlaceholderText("Enter object name")
        
        self.mainLayout.addWidget(self.mainLine) # размещаем его в главном Layout

        self.create_radButtions()
        self.crate_slider()
        self.create_mainButtions()
        
        
    def create_radButtions(self):
        # создаем группу кнопок
        self.radioButGrp = QtWidgets.QGroupBox()
        self.radioButGrp.setMaximumHeight(50)

        # создаём лайоут под эти кнопки
        self.radio_groupLayout = QtWidgets.QHBoxLayout()

        # создаем кнопки
        self.radio_Sphere = QtWidgets.QRadioButton('Sphere')
        self.radio_Sphere.setChecked( True ) # включаем галочку
        self.radio_Cube = QtWidgets.QRadioButton('Cube')
        self.radio_Cone = QtWidgets.QRadioButton('Cone')

        # Помещаем их в соответсвующий layout
        self.radio_groupLayout.addWidget( self.radio_Sphere )
        self.radio_groupLayout.addWidget( self.radio_Cube )
        self.radio_groupLayout.addWidget( self.radio_Cone )

        # Устанавливаем в группу - layout
        self.radioButGrp.setLayout( self.radio_groupLayout)

        # add layout to mainLayout
        self.mainLayout.addWidget( self.radioButGrp )

        
    def crate_slider(self):
        # создаем горизонтальный лайоут для полоски и окна
        self.slider_Layout = QtWidgets.QHBoxLayout()

        # создаем анниацию к слайдеру
        self.annotSlder = QtWidgets.QLabel("X :")

        #создать слайдер
        self.mainSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.mainSlider.setMinimum(0)
        self.mainSlider.setMaximum(100)
        self.mainSlider.valueChanged.connect(self.update_lineText)
        
        
        # создать текстовое поле
        self.sliderText = QtWidgets.QLineEdit()
        self.sliderText.setAlignment(QtCore.Qt.AlignHCenter)
        
        
        self.sliderText.setText(str(self.mainSlider.value()))
        self.sliderText.setFixedWidth(35)
        self.sliderText.setMaxLength(3) 
        self.sliderText.setInputMask(' 000')
       
        

        self.sliderText.returnPressed.connect( self.change_slider )

        # добавляем в лайоут слайдера слайдер и окно отображения
        self.slider_Layout.addWidget( self.annotSlder )
        self.slider_Layout.addWidget( self.mainSlider )
        self.slider_Layout.addWidget( self.sliderText )

        # add layout to mainLayout
        self.mainLayout.addLayout(self.slider_Layout)


    def create_mainButtions(self):
        # Создадим отдельный горизонтальный layout для кнопок
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        
        # Создадим сами кнопки
        self.button_Create = QtWidgets.QPushButton('Create')
        self.button_Apply = QtWidgets.QPushButton('Apply')
        self.button_Close = QtWidgets.QPushButton('Close')
        
        # Поместим кнопки в соответствующий layout
        self.buttonsLayout.addWidget( self.button_Create )
        self.buttonsLayout.addWidget( self.button_Apply )
        self.buttonsLayout.addWidget( self.button_Close )
        
        # add layout to mainLayout
        self.mainLayout.addLayout(self.buttonsLayout)

        self.button_Create.clicked.connect( self.create )
        self.button_Apply.clicked.connect( self.apply )
        self.button_Close.clicked.connect( self.close )
        
        
    def create(self):
        # Creates a polygonal object and closes UI
        # check which radio button is selected
        self.apply()
        
        # close our UI
        self.close()
        
    def apply(self):
        # Creates an object and keeps UI opened
        
        # check which radio button is selected
        obj_name = self.mainLine.text()
        
        if obj_name.isdigit():
            QtWidgets.QMessageBox.warning(self, 'Error', 'You cannot enter only numbers')
            return

        if self.radio_Sphere.isChecked():
            obj = cmds.polySphere(n=obj_name)[0]
        elif self.radio_Cube.isChecked():
            obj = cmds.polyCube(n=obj_name)[0]
        else:
            obj = cmds.polyCone(n=obj_name)[0]

        # перемещаем объект на X
        cmds.setAttr(obj + "." + "translateX", self.mainSlider.value())


    def update_lineText (self, value):
        self.sliderText.setText(str(value))

    def change_slider(self):
        self.mainSlider.setValue( int(self.sliderText.text()))


        
# проверить если наш UI уже создан
if cmds.window('myTestWindow', q=1, exists=1):
    cmds.deleteUI('myTestWindow')
    
# проверить если Maya хранит в себе настройки отображения нашего UI
if cmds.windowPref('myTestWindow', exists = 1):
    cmds.windowPref('myTestWindow', remove = 1)




myUI = MyDialog()
myUI.show() 
