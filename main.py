#MAIN FOR SCARA
#Python Modules
import math as m

#other python modules
from trigoCal import returnServoAngOneTwo as getAngles


if __name__ == "__main__":
   s1, s2 = getAngles(50,50)
   
