#imports
import math
pi=math.pi

#variables
P=(8050)#density(kg/m^3)
UTS=(2693)#ultimate Tensile strenth(MPA)
r=(0.5)#Radius (M)
h=(0.005)#height of disk(M)
RPM=(100)#rotation per minuite
#extra info
m=(P*pi*r**2*h)#mass(KG)
print("mass of disk is " + str(m) + " kg")
I=(1/2*m*r**2)# moment of inertia
print("moment of inertia "+str(I))
w=(RPM/9.549297)# angular velocity(radians per second)
print('angular velocity '+str(w)+' rad/s')

#the Disks useing fly wheel mathmatics
EK= 1/2*I*w**2#EK is the stored kinetic energy(joules)
print('stored kinetic energy '+str(EK)+' J')
#Increasing amounts of rotation energy can be stored in the flywheel until the rotor shatters.
sigt=((P*r**2*w**2)/1*10**-6)#tensile stress in (MPA)
def bp():
    if sigt>UTS:
        print('the Hoop stress in the disk is '+str(sigt)+' Warning it will break')
    elif sigt<UTS:
        print('the Hoop stress in the disk is '+str(sigt))
bp()
