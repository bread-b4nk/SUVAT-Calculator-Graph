# ==============================================================================
# SUVAT Graph Maker
# ==============================================================================
#stoke's law frictional force on a sphere is equal to 6 pi times coefficient of viscosity times the radius and its velocity
# cSpell:ignore stoke's, pyplot, xlabel, ylabel
import matplotlib.pyplot as plt
def data_input():
    print("Horizontal Components\n")
    print("Hit return/enter nothing if the quantity is unknown")
    s_horizontal = input("Please enter s (displacement in m): ")
    u_horizontal = input("Please enter u (initial velocity in m/s): ")
    v_horizontal = input("Please enter v (final velocity in m/s): ")
    a_horizontal = input("Please enter a (acceleration in m/s^2): ")
    t_horizontal = input("Please enter t (time in s): ")

    if s_horizontal != "":
        s_h_presence = 1
        s_horizontal = float(s_horizontal)
    else:
        s_h_presence = 0
    if u_horizontal != "":
        u_h_presence = 1
        u_horizontal = float(u_horizontal)
    else:
        u_h_presence = 0
    if v_horizontal != "":
        v_h_presence = 1
        v_horizontal = float(v_horizontal)
    else:
        v_h_presence = 0
    if a_horizontal != "":
        a_h_presence = 1
        a_horizontal = float(a_horizontal)
    else:
        a_h_presence = 0
    if t_horizontal != "":
        t_h_presence = 1
        t_horizontal = float(t_horizontal)
    else:
        t_h_presence = 0

    horizontal_presence = s_h_presence+u_h_presence+v_h_presence+a_h_presence+t_h_presence

    print("\nVertical Components (ASSUMING UP IS POSITIVE)\n")
    print("Hit return/enter nothing if the quantity is unknown")
    s_vertical = input("Please enter s (displacement in m): ")
    u_vertical = input("Please enter u (initial velocity in m/s): ")
    v_vertical = input("Please enter v (final velocity in m/s): ")
    a_vertical = input("Please enter a (acceleration in m/s^2), if nothing is entered, -9.8 will be used: ")
    t_vertical = input("Please enter t (time in s): ")

    #checking for presence of variables
    if s_vertical != "":
        s_v_presence= 1
        s_vertical = float(s_vertical)
    else:
        s_v_presence = 0
    if u_vertical != "":
        u_v_presence = 1
        u_vertical = float(u_vertical)
    else:
        u_v_presence = 0
    if v_vertical != "":
        v_v_presence = 1
        v_vertical = float(v_vertical)
    else:
        v_v_presence = 0
    if a_vertical != "":
        a_v_presence = 1
        a_vertical = float(a_vertical)
    else:
        a_vertical = -9.8
        a_v_presence = 1
    if t_vertical != "":
        t_v_presence = 1
        t_vertical = float(t_vertical)
    else:
        t_v_presence = 0

    vertical_presence = s_v_presence+u_v_presence+v_v_presence+a_v_presence+t_v_presence

    return (horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence)

def calculation(horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence):
    if t_horizontal != t_vertical and t_horizontal != "" and t_vertical != "":
        print("Error, horizontal and vertical times must be the same")
        exit()
    elif t_horizontal == "" and t_vertical != "":
        print("Error, the time should be the same for horizontal and vertical components, setting them to be the same")
        t_horizontal = float(t_vertical)
        t_h_presence = 1
    elif t_vertical == "" and t_horizontal != "":
        print("Error, the time should be the same for horizontal and vertical components, setting them to be the same")
        t_vertical = float(t_horizontal)
        t_v_presence = 1
    if s_v_presence + u_v_presence + v_v_presence +a_v_presence+t_v_presence <= 2 and s_v_presence == 0:
        s_v_presence = 1
        s_vertical = float(0)
        print("Error, not enough vertical variables, assuming vertical displacement as 0")



    # ==============================================================================
    # Horizontal Components
    # ==============================================================================
    for i in range(2): #calculation is here
        #v = u + at 
        if u_h_presence+v_h_presence+a_h_presence == 3 and t_h_presence == 0:
            t_horizontal = (v_horizontal - u_horizontal)/a_horizontal
            t_vertical = t_horizontal
            t_h_presence = 1
            t_v_presence = 1
            print("BOX 1")
        if u_h_presence+v_h_presence+t_h_presence == 3 and a_h_presence == 0:
            a_horizontal = (v_horizontal - u_horizontal)/t_horizontal
            a_h_presence = 1
            print("BOX 2")
        if v_h_presence+a_h_presence+t_h_presence == 3 and u_h_presence == 0:
            u_horizontal = v_horizontal - a_horizontal * t_horizontal
            u_h_presence = 1
            print("BOX 3")
        if u_h_presence+a_h_presence+t_h_presence == 3 and v_h_presence == 0:
            v_horizontal = u_horizontal + a_horizontal * t_horizontal
            v_h_presence = 1
            print("BOX 4")

        #s = (u+v)t / 2
        if s_h_presence+u_h_presence+v_h_presence == 3 and t_h_presence == 0:
            t_horizontal = s_horizontal * 2/(u_horizontal+v_horizontal)
            t_h_presence = 1
            print("BOX 5")
        if t_h_presence+u_h_presence+v_h_presence == 3 and s_h_presence == 0:
            s_horizontal = t_horizontal * (u_horizontal+v_horizontal)/2
            s_h_presence = 1
            print("BOX 6")
        if s_h_presence+t_h_presence+v_h_presence == 3 and u_h_presence == 0:
            u_horizontal = 2 * s_horizontal/t_horizontal - v_horizontal
            u_h_presence = 1
            print("BOX 7")
        if s_h_presence+t_h_presence+u_h_presence == 3 and v_h_presence == 0:
            v_horizontal = 2 * s_horizontal/t_horizontal - u_horizontal
            v_h_presence = 1
            print("BOX 8")

        #v^2 = u^2 + 2as
        if u_h_presence+a_h_presence+s_h_presence == 3 and v_h_presence == 0:
            v_horizontal = ((u_horizontal**2) + 2 * a_horizontal * s_horizontal)**0.5
            v_h_presence = 1
            print("BOX 9")
        if v_h_presence+a_h_presence+s_h_presence == 3 and u_h_presence == 0:
            u_horizontal = (v_horizontal**2-2*a_horizontal*s_horizontal)**0.5
            u_h_presence = 1
            print("BOX 10")
        if v_h_presence+u_h_presence+s_h_presence == 3 and a_h_presence == 0:
            a_horizontal = (v_horizontal**2-u_horizontal**2)/(2*s_horizontal)
            a_h_presence = 1
            print("BOX 11")
        if v_h_presence+u_h_presence+a_h_presence == 3 and s_h_presence == 0:
            s_horizontal = (v_horizontal**2-u_horizontal**2)/(2*a_horizontal)
            s_h_presence = 1
            print("BOX 12")

        #s = ut + 1/2at^2
        if u_h_presence+t_h_presence+t_h_presence == 3 and s_h_presence == 0:
            s_horizontal = u_horizontal*t_horizontal + 0.5 * a_horizontal * t_horizontal**2
            s_h_presence = 1
            print("BOX 13")
        if a_h_presence+t_h_presence+s_h_presence == 3 and u_h_presence == 0:
            u_horizontal = (0.5 * a_horizontal*t_horizontal**2-s_horizontal)/t_horizontal
            u_h_presence = 1
            print("BOX 14")
        if s_h_presence+u_h_presence+t_h_presence == 3 and a_h_presence == 0:
            a_horizontal = (2*(s_horizontal-u_horizontal*t_horizontal))/(t_horizontal**2)
            a_h_presence = 1
            print("BOX 15")
        if s_h_presence+u_h_presence+a_h_presence == 3 and t_h_presence == 0:
            temp1 = (u_horizontal * -1 + (u_horizontal ** 2 + 2 * a_horizontal * s_horizontal))/a_horizontal
            temp2 = (u_horizontal * -1 - (u_horizontal ** 2 + 2 * a_horizontal * s_horizontal))/a_horizontal
            if temp1 <= 0:
                t_horizontal = temp2
                t_h_presence = 1
            else:
                t_horizontal = temp1
                t_h_presence = 1
            print("BOX 16")

        # s = vt - 1/2at^2
        if v_h_presence+t_h_presence+t_h_presence == 3 and s_h_presence == 0:
            s_horizontal = v_horizontal*t_horizontal - 0.5 * a_horizontal * t_horizontal**2
            s_h_presence = 1
            print("BOX 17")
        if a_h_presence+t_h_presence+s_h_presence == 3 and v_h_presence == 0:
            v_horizontal = (0.5 * a_horizontal*t_horizontal**2+s_horizontal)/t_horizontal
            v_h_presence = 1
            print("BOX 18")
        if s_h_presence+v_h_presence+t_h_presence == 3 and a_h_presence == 0:
            a_horizontal = (2*(s_horizontal-v_horizontal*t_horizontal))/(t_horizontal**2)
            a_h_presence = 1
            print("BOX 19")
        if s_h_presence+v_h_presence+a_h_presence == 3 and t_h_presence == 0:
            temp1 = (v_horizontal + (v_horizontal ** 2 - 2 * a_horizontal * s_horizontal))/a_horizontal
            temp2 = (v_horizontal - (v_horizontal ** 2 - 2 * a_horizontal * s_horizontal))/a_horizontal
            if temp1 <= 0:
                t_horizontal = temp2
                t_h_presence = 1
            else:
                t_horizontal = temp1
                t_h_presence = 1
            print("BOX 20")



    # ==============================================================================
    # VERTICAL COMPONENTS
    # ==============================================================================

        #v = u + at 
        # if u_v_presence+v_v_presence+a_v_presence == 3 and t_v_presence == 0:
        #     t_vertical = (v_vertical - u_vertical)/a_vertical
        #     t_v_presence = 1
        #     t_h_presence = 1 
        #     print("BOX A")
        if u_v_presence+v_v_presence+t_v_presence == 3 and a_v_presence == 0:
            a_vertical = (v_vertical - u_vertical)/t_vertical
            a_v_presence = 1
            print("BOX B")
        if v_v_presence+a_v_presence+t_v_presence == 3 and u_v_presence == 0:
            u_vertical = v_vertical - a_vertical * t_vertical
            u_v_presence = 1
            print("BOX C")
        if u_v_presence+a_v_presence+t_v_presence == 3 and v_v_presence == 0:
            v_vertical = u_vertical + a_vertical * t_vertical
            v_v_presence = 1
            print("BOX D")

        #s = (u+v)t / 2
        # if s_v_presence+u_v_presence+v_v_presence == 3 and t_v_presence == 0:
        #     t_vertical = s_vertical * 2/(u_vertical+v_vertical)
        #     t_v_presence = 1
        #     print("BOX E")
        if t_v_presence+u_v_presence+v_v_presence == 3 and s_v_presence == 0:
            s_vertical = t_vertical * (u_vertical+v_vertical)/2
            s_v_presence = 1
            print("BOX F")
        if s_v_presence+t_v_presence+v_v_presence == 3 and u_v_presence == 0:
            u_vertical = 2 * s_vertical/t_vertical - v_vertical
            u_v_presence = 1
            print("BOX G")
        if s_v_presence+t_v_presence+u_v_presence == 3 and v_v_presence == 0:
            v_vertical = 2 * s_vertical/t_vertical - u_vertical
            v_v_presence = 1
            print("BOX H")

        #v^2 = u^2 + 2as
        if u_v_presence+a_v_presence+s_v_presence == 3 and v_v_presence == 0:
            v_vertical = ((u_vertical**2) + 2 * a_vertical * s_vertical)**0.5
            v_v_presence = 1
            print("BOX I")
        if v_v_presence+a_v_presence+s_v_presence == 3 and u_v_presence == 0:
            u_vertical = (v_vertical**2-2*a_vertical*s_vertical)**0.5
            u_v_presence = 1
            print("BOX J")
        if v_v_presence+u_v_presence+s_v_presence == 3 and a_v_presence == 0:
            a_vertical = (v_vertical**2-u_vertical**2)/2*s_vertical
            a_v_presence = 1
            print("BOX K")
        if v_v_presence+u_v_presence+a_v_presence == 3 and s_v_presence == 0:
            s_vertical = (v_vertical**2-u_vertical**2)/2*a_vertical
            s_v_presence = 1
            print("BOX L")

        #s = ut + 1/2at^2
        if u_v_presence+t_v_presence+t_v_presence == 3 and s_v_presence == 0:
            s_vertical = u_vertical*t_vertical + 0.5 * a_vertical * t_vertical**2
            s_v_presence = 1
            print("BOX M")
        if a_v_presence+t_v_presence+s_v_presence == 3 and u_v_presence == 0:
            u_vertical = (0.5 * a_vertical*t_vertical**2-s_vertical)/t_vertical
            u_v_presence = 1
            print("BOX N")
        if s_v_presence+u_v_presence+t_v_presence == 3 and a_v_presence == 0:
            a_vertical = (2*(s_vertical-u_vertical*t_vertical))/t_vertical**2
            a_v_presence = 1
            print("BOX O")
        if s_v_presence+u_v_presence+a_v_presence == 3 and t_v_presence == 0:
            temp1 = (u_vertical * -1 + (u_vertical ** 2 - 2 * a_vertical * s_vertical*-1)**0.5)/a_vertical
            temp2 = (u_vertical * -1 - (u_vertical ** 2 - 2 * a_vertical * s_vertical*-1)**0.5)/a_vertical
            if temp1 <= 0:
                t_vertical = temp2
                t_v_presence = 1
            else:
                t_vertical = temp1
                t_v_presence = 1
            print("BOX P")

        # s = vt - 1/2at^2
        if v_v_presence+t_v_presence+t_v_presence == 3 and s_v_presence == 0:
            s_vertical = v_vertical*t_vertical- 0.5 * a_vertical * t_vertical**2
            s_v_presence = 1
            print("BOX Q")
        if a_v_presence+t_v_presence+s_v_presence == 3 and v_v_presence == 0:
            v_vertical = (0.5 * a_vertical*t_vertical**2+s_vertical)/t_vertical
            v_v_presence = 1
            print("BOX R")
        if s_v_presence+v_v_presence+t_v_presence == 3 and a_v_presence == 0:
            a_vertical = (2*(s_vertical-v_vertical*t_vertical))/t_vertical**2
            a_v_presence = 1
            print("BOX S")
        if s_v_presence+v_v_presence+a_v_presence == 3 and t_v_presence == 0:
            temp1 = (v_vertical + (v_vertical ** 2 - a_vertical * s_vertical*-1))/a_vertical
            temp2 = (v_vertical - (v_vertical ** 2 - a_vertical * s_vertical*-1))/a_vertical
            if temp1 <= 0:
                t_vertical = temp2
                t_v_presence = 1
            else:
                t_vertical = temp1
                t_v_presence = 1
            print("BOX T")

    horizontal_presence = s_h_presence+u_h_presence+v_h_presence+a_h_presence+t_h_presence
    vertical_presence = s_v_presence+u_v_presence+v_v_presence+a_v_presence+t_v_presence

    
    print("\n------------------ Values: ------------------")
    print("NUMBER OF HORIZONTAL COMPONENTS " + str(horizontal_presence))
    print("NUMBER OF VERTICAL COMPONENTS " + str(vertical_presence))
    print("\nHorizontal Components:")
    if s_h_presence == 0:
        print("Displacement couldn't be calculated")
    else:
        print(str("Displacement: " + str(s_horizontal)))
    if u_h_presence == 0:
        print("Initial Velocity couldn't be calculated")
    else:
        print(str("Initial Velocity: " + str(u_horizontal)))
    if v_h_presence == 0:
        print("Final Velocity couldn't be calculated")
    else:
        print(str("Final Velocity: " + str(v_horizontal)))
    if a_h_presence == 0:
        print("Acceleration couldn't be calculated")
    else:
        print(str("Acceleration: " + str(a_horizontal)))
    if t_h_presence == 0:
        print("Time couldn't be calculated")
    else:
        print("Time: " + str(t_horizontal))
    print("\nVertical Components")
    if s_v_presence == 0:
        print("Displacement couldn't be calculated")
    else:
        print(str("Displacement: " + str(s_vertical)))
    if u_v_presence == 0:
        print("Initial Velocity couldn't be calculated")
    else:
        print(str("Initial Velocity: " + str(u_vertical)))
    if v_v_presence == 0:
        print("Final Velocity couldn't be calculated")
    else:
        print(str("Final Velocity: " + str(v_vertical)))
    if a_v_presence == 0:
        print("Acceleration couldn't be calculated")
    else:
        print(str("Acceleration: " + str(a_vertical)))
    if t_v_presence == 0:
        print("Time couldn't be calculated")
    else:
        print("Time: " + str(t_vertical))

    return (horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence)

def graph(horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence):
    import matplotlib.pyplot as plt
# ==========================================================================
# Horizontal Graphs
# ==========================================================================
    if horizontal_presence >= 4:
        t_h_graph = []
        number_of_points = int(float(t_horizontal) + 1.0) * 10
        for i in range(0,number_of_points):
            t_h_graph.append(i * 0.1)

        #displacement graph
        s_h_graph = []
        
        for i in range(0,number_of_points):
            s_h_graph.append(float(u_horizontal*i*0.1 + .5*a_horizontal*((0.1*i)**2)))
        
        plt.plot(t_h_graph,s_h_graph)
        plt.xlabel("Time (s)")
        plt.ylabel("Displacement (m)")
        plt.title("Horizontal Displacement Graph")
        plt.show()
        
        #velocity graph
        v_h_graph = []
        for i in range(0,number_of_points):
            v_h_graph.append(float(u_horizontal + a_horizontal*i*0.1))
        
        plt.plot(t_h_graph,v_h_graph)
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.title("Horizontal Velocity Graph")
        plt.show()

        #acceleration graph
        a_h_graph = []
        for i in range(0,number_of_points):
            a_h_graph.append(float((v_horizontal**2-u_horizontal**2)/2*s_horizontal))
        
        plt.plot(t_h_graph,a_h_graph)
        plt.xlabel("Time (s}")
        plt.ylabel("Acceleration (m/s^2)")
        plt.title("Horizontal Acceleration Graph")
        plt.show()
        
    else:
        print("Error, more horizontal components are needed to create horizontal graphs")
# ==============================================================================
# Vertical Graphs
# ==============================================================================
    if vertical_presence >= 4:
        t_v_graph = []
        number_of_points = int(float(t_vertical) + 1) * 10
        print(number_of_points)
        for i in range(0,number_of_points):
            t_v_graph.append(i * 0.1)

        #displacement graph
        s_v_graph = []
        
        for i in range(0,number_of_points):
            s_v_graph.append(float(u_vertical*i*0.1 + .5*a_vertical*((0.1*i)**2)))
        plt.plot(t_v_graph,s_v_graph)
        plt.xlabel("Time (s)")
        plt.ylabel("Displacement (m)")
        plt.title("Vertical Displacement Graph")
        plt.show()
        
        #velocity graph
        v_v_graph = []
        for i in range(0,number_of_points):
            v_v_graph.append(float(u_vertical + a_vertical*i*0.1))
        
        plt.plot(t_v_graph,v_v_graph)
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.title("Vertical Velocity Graph")
        plt.show()

        #acceleration graph
        a_v_graph = []
        for i in range(0,number_of_points):
            a_v_graph.append(a_vertical)
           
        
        plt.plot(t_v_graph,a_v_graph)
        plt.xlabel("Time (s}")
        plt.ylabel("Acceleration (m/s^2)")
        plt.title("Vertical Acceleration Graph")
        plt.show()
    else:
        print("Error, more vertical components are needed. Some graphs may not be created.")

    
def main():
    print("-------------------------------------------------------------------------")
    print("\nSUVAT Graph Maker\n")
    print("-------------------------------------------------------------------------\n\n")

    print("Please input values first.")
    horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence = data_input()
    while True:
        print("\n\nOptions:\n1. Calculating more values\n2. Graphing\nAnything Else. Exit Program")
        user_input = input("What would you like to do?")
        if user_input == "1":
            horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence = calculation(horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence)
        elif user_input == "2":
            graph(horizontal_presence,s_horizontal,u_horizontal,v_horizontal,a_horizontal,t_horizontal,s_h_presence,u_h_presence,v_h_presence,a_h_presence,t_h_presence,vertical_presence,s_vertical,u_vertical,v_vertical,a_vertical,t_vertical,s_v_presence,u_v_presence,v_v_presence,a_v_presence,t_v_presence)
        else:
            print("Goodbye.")
            exit()

main()