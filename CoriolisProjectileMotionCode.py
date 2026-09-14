## Here, we modify the original code and add in additional variables to make this more complex,
## while ensuring it runs smoothly.

import math ## For operations of sin, cos, and pi
import matplotlib.pyplot as plt ## Used for creating graphs

## Define gravity constant
g = 9.8 ## Earth's surface gravity in units of m/s^2

## Define omega constant
omega = 7.27E-5 ## Earth's rotational speewd in units of rad/s

print("\n")
option = input("Would you like to include the Coriolis effect [Type 1 for YES or 2 (or anything else for that matter) for NO]: ")

## Compute the acceleration assuming gravity and drag force
def acceleration(v_x, v_y, v_z, C, m, option):

    ## Calculate total speed for 3D drag force calculation
    v_total = math.sqrt(v_x*v_x + v_y*v_y + v_z*v_z)

    ## Drag acts opposite to velocity in all three dimensions
    a_x = -C*v_x*v_total/m
    a_y = -g - C*v_y*v_total/m ## Assuming y is the vertical axis
    a_z = -C*v_z*v_total/m

    if (option=="1"):
        a_x += -v_z*omega_y
        a_y += v_z*omega_x
        a_z += v_x*omega_y - v_y*omega_x
    return a_x, a_y, a_z

## Update the position and velocity of the projectile
def update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    z = z + v_z*dt + 0.5*a_z*dt*dt

    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    v_z = v_z + a_z*dt

    return x, y, z, v_x, v_y, v_z

## Get the initial input
v_0 = float(input("What is the magnitude of the initial velocity?: ")) ## Units in m/s
print ("\n")
theta = float(input("What is your current latitude?: ")) ## The function is now a latitude function; Units in degrees.
print ("\n")
dt = float(input("What is the size of the time step?: ")) ## Units in seconds
print ("\n")
m = float(input("What is the projectile mass?: ")) ## golf ball ~ 0.04593 kg
print ("\n")
C = float(input("What is the drag coefficient?: ")) ## golf ball ~ 4E-4 kg/m


if (option=="1"):
    print("\n")
    print("Implementing the Coriolis effect")
    print("\n")
    print("This may take a few moments...")

    ## Break the initial velocity into components
    v_x = v_0*math.cos((90-theta)*math.pi/180.0)
    v_y = v_0*math.sin((90-theta)*math.pi/180.0)
    v_z = 0

    ## Break the Earth's angular speed into components
    omega_x = -omega*math.cos((theta)*math.pi/180.0)
    omega_y = omega*math.sin((theta)*math.pi/180.0)
    omega_z = 0
    
    print("\n")
    ## Open file for output
    outFile = open("coriolisProjectileDragData.txt", "w")
    ## Set some initial values
    t = 0
    x = 0
    y = 0
    z = 0
    y_max = 0
    inFlight = True
    ## Run the loop for the desired number of time steps, output to file at each step
    ## Write down the distance it went and the maximum height.
    
    ## Create empty arrays for graphs
    x_array = []
    y_array = []
    z_array = []

    while (inFlight):
            a_x, a_y, a_z = acceleration(v_x, v_y, v_z, C, m, option)
            x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt)
            t += dt

            ## Add the values to the array
            x_array.append(x)
            y_array.append(y)
            z_array.append(z)
            
            if (y >= 0):
                outFile.write(f"{t: .4f}" + " " + f"{x: .4f}" + " " + f"{y: .4f}" + " " + f"{z: .4f}" + " " + 
                              f"{v_x: .4f}" + " " + f"{v_y: .4f}" + " " + f"{v_z: .4f}" + " " + 
                              f"{a_x: .4f}" + " " + f"{a_y: .4f}" + " " + f"{a_z: .4f}" +"\n")
                if (y > y_max):
                    y_max = y
            else:
                inFlight = False
    
    ## Close the file
    outFile.close()

    ## Print some summary statistics
    print("\n")
    print(f"The maximum height was {y_max: .4f} meters")
    print(f"The horizontal x-range was {x: .4f} meters")
    print(f"The horizontal z-range was {z: .4f} meters")

else:
    print("\n")
    print("Proceeding as normal.")
    print("\n")
    print("This may take a few moments...")

    ## Break the initial velocity into components
    v_x = v_0*math.cos((90-theta)*math.pi/180.0)
    v_y = v_0*math.sin((90-theta)*math.pi/180.0)
    v_z = 0

    ## Open file for output
    outFile = open("coriolisProjectileDragData.txt", "w")

    ## Set some initial values
    t = 0
    x = 0
    y = 0
    z = 0
    y_max = 0
    inFlight = True
    ## Run the loop for the desired number of time steps, output to file at each step
    ## Write down the distance it went and the maximum height.
    
    ## Create empty arrays for graphs
    x_array = []
    y_array = []
    z_array = []
    
    while (inFlight):
        a_x, a_y, a_z = acceleration(v_x, v_y, v_z, C, m, option)
        x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt)
        t += dt

        ## Add the values to the array
        x_array.append(x)
        y_array.append(y)
        z_array.append(z)
                   
        if (y >= 0):
            outFile.write(f"{t: .4f}" + " " + f"{x: .4f}" + " " + f"{y: .4f}" + " " + f"{z: .4f}" + " " + 
                          f"{v_x: .4f}" + " " + f"{v_y: .4f}" + " " + f"{v_z: .4f}" + " " + 
                          f"{a_x: .4f}" + " " + f"{a_y: .4f}" + " " + f"{a_z: .4f}" +"\n")
            if (y > y_max):
                y_max = y
        else:
            inFlight = False

    ## Close the file
    outFile.close()
    
    ## Print some summary statistics
    print("\n")
    print(f"The maximum height was {y_max: .4f} meters")
    print(f"The horizontal x-range was {x: .4f} meters")
    print(f"The horizontal z-range was {z: .4f} meters")

## Create the x vs y plot
plt.xlabel ("$x$ (m)")
plt.ylabel ("$y$ (m)")
plt.plot (x_array, y_array)
plt.savefig("X_vs_Y_graph.pdf")

plt.clf() ## This helps clears the previous graph and make room for the second graph

## Create the x vs z plot
plt.xlabel ("$x$ (m)")
plt.ylabel ("$z$ (m)")
plt.plot (x_array, z_array)
plt.savefig("X_vs_Z_graph.pdf")