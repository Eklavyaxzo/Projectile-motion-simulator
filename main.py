# imports modules
import  numpy as np
import matplotlib.pyplot as plt


# constants

g= 9.8 # gravity

# user inputs

theta = float(input("Enter the angle (dregree) :"))
v0 = float(input("enter the velocity (m/s):"))

# angle to radian 
theta_radian= np.radians(theta)

# time of flight ( how much time it will in air)
t_filght= 2*v0*np.sin(theta_radian)/g

# time steps
t = np.linspace(0,t_filght, num=1000)

# calculation of position

x = v0*np.cos(theta_radian)*t
y =  v0*np.sin(theta_radian)*t - 0.5*g*t**2



max_height= max(y)
range_distancs = max(x)

print("Maximum Height : " , round(max_height,2),"m")
print("Maximum distance : " , round(range_distancs,2),"m")



# ploting the trajectory

plt.plot(x,y)
plt.title(f"Projectile trajectory velocity{v0}m/s angle{theta}")
plt.xlabel("Distance (m)")
plt.ylabel("height(m)")
#  control x and y axis limit
# plt.xlim(0, max(x)*0.9) 
# plt.ylim(0, max(y)*0.9)
plt.annotate(f"Max Height = {round(max_height,2)} m",
             xy= (range_distancs/2 , max_height),
             xytext=(range_distancs/2 , max_height +1 ),
             arrowprops=dict(facecolor = 'green' , shrink=0.05)
             )


plt.grid()
plt.show()
