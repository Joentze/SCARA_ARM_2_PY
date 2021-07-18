import math as m

ARM_ONE = 100
ARM_TWO = 100

#Get Arm Node Length
def getArmNode(coordX, coordY):
    xSq = coordX**2
    ySq = coordY**2
    return m.sqrt(xSq + ySq)

def ArmNodeAngSurface(coordX, coordY):
    return m.atan(coordY/coordX)

def angleBtwArmOneTwo(ARM_NODE, ARM_ONE, ARM_TWO):
    #USE COSINE RULE
    sqAN = ARM_NODE**2
    sqAO = ARM_ONE**2
    sqAT = ARM_TWO**2
    numerator = sqAN - sqAO - sqAT
    denominator = -2 * ARM_ONE * ARM_TWO
    cosNode = numerator/denominator
    return m.acos(cosNode)

def servoOneANG(ARM_TWO, ARM_NODE, ARM_NODE_ANGLE):
    firstSINRule = ARM_NODE/m.sin(ARM_NODE_ANGLE)
    sinNode = ARM_TWO/firstSINRule
    PART_ONE = m.asin(sinNode)
    return PART_ONE + ARM_NODE_ANGLE

def returnServoAngOneTwo(coordX, coordY):
    ARM_NODE = getArmNode(coordX, coordY)
    SERVO_TWO = angleBtwArmOneTwo(ARM_NODE,ARM_ONE,ARM_TWO)
    ARM_NODE_ANGLE = SERVO_TWO
    SERVO_ONE = servoOneANG(ARM_TWO, ARM_NODE, ARM_NODE_ANGLE)
    return m.degrees(SERVO_ONE), m.degrees(SERVO_TWO)

if __name__ == "__main__":
    s1, s2 = returnServoAngOneTwo(50,50)
    print(s1)
    print(s2)