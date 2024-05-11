import maya.cmds as cmds


class Rocket(object):

    def __init__(self, name = "My rocket", bodyParts = 4, noseConeHeight = 10, fuelTanks = 6, radius=1):

        self.bodyParts = int(bodyParts)
        self.noseConeHeight = int(noseConeHeight)
        self.fuelTanks = int(fuelTanks)
        self.radius  = radius
        self.mainName = name

        #if not self.bodyParts >= 1 or self.noseConeHeight >= 1 or self.fuelTanks >= 1:
            #cmds.error("Wrong arguments. It most >=1")

    
    def moveCone(self , name = "Default"):
        '''
        create and move cone
        '''
        self.fuelCone = cmds.polyCone(n=name, r = self.radius, h=self.radius)[0]
        coneBB = cmds.xform (self.fuelCone, q = 1, boundingBox =1, ws=1) 
        coneMid = (coneBB[4] - coneBB[1])/2

        cmds.xform (self.fuelCone, t = [0, coneMid, 0])

    def crateCyl(self, name = "step1"):
        '''
        create and move first cylinder
        '''
        coneBB = cmds.xform (self.fuelCone, q = 1, boundingBox =1, ws=1)
        self.bodyCyl = cmds.polyCylinder(n = name, r = self.radius)
        cylBB = cmds.xform (self.bodyCyl, q = 1, boundingBox =1, ws=1)
        cylMid = (cylBB[4] - cylBB[1])/2
        
        
        #move on top of cone
        cmds.xform (self.bodyCyl, t = [0, coneBB[4] + cylMid, 0])

       
       
    def generateModel(self):
                
        # [x_min, y_min, z_min, x_max, y_max, z_max]
        
        if self.fuelTanks == 1: 
            
            self.moveCone(name = "fuelCone")
            
        else:            
            
            self.moveCone(name = "fuelCone")

            newrad = 2*3.14*self.radius/self.fuelTanks/2.4
            print (newrad)
            cmds.polyCone(self.fuelCone, e = 1, r = newrad)

            coneRot = 360/self.fuelTanks
            cmds.xform(self.fuelCone, r=1, t = [self.radius, 0, 0])
            cmds.xform(self.fuelCone, ws=1, a=1, rp = [0,0,0], sp = [0,0,0])

            for i in range(self.fuelTanks-1):
                
                copyCone = cmds.duplicate(self.fuelCone)
                cmds.xform(copyCone, relative = 1, ro = [0, coneRot, 0])

                self.fuelCone = copyCone

        if self.bodyParts == 1:
            self.crateCyl()
        
        else:
            self.crateCyl()

            for i in range(self.bodyParts-1):
                cylBB = cmds.xform (self.bodyCyl, q = 1, boundingBox =1, ws=1)
                cylMid = (cylBB[4] - cylBB[1])/2

                copyCyl = cmds.polyCylinder(r = self.radius)
                cmds.xform(copyCyl, r=1, t= [0, cylBB[4] + cylMid, 0])

                self.bodyCyl = copyCyl

        
        cylBB = cmds.xform (self.bodyCyl, q = 1, boundingBox =1, ws=1)
        

        self.moveCone(name = "noseCone")
        
        cmds.xform(self.fuelCone, r=1, t = [0, cylBB[4], 0])


        cmds.ls(type = )


                
                
cone1 = Rocket(bodyParts = 2, fuelTanks = 10, radius = 2)
cone1.generateModel()
