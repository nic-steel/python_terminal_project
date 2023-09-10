import matplotlib.pyplot as plt

print("Welcome to my beam analysis calculator!")
print("Please note the following:")
print("This is an LRFD analysis for a simply supported beam ONLY")

def error_check(prompt):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            if num >= 0:
                return num
                break
            else:
                print("Load must be a positive number")
        except ValueError or TypeError:
            print("Please enter a valid number")

max_span = error_check("Please enter the beam span (in ft): ")
dead_load = error_check("Please enter the unfactored dead load (in K/ft): ")
live_load = error_check("Please enter the unfactored live load (in K/ft): ")

#Plotting variables
x = []
y1 = []
y2 = []

def moment_calc(dead_load, live_load, location):
    moment = ((1.2*dead_load + 1.6*live_load)*(location)/2)*(max_span-location)
    return moment

def shear_calc(dead_load, live_load, location):
    shear = (1.2*dead_load + 1.6*live_load)*((max_span/2)-location)
    return shear

def graph_plot(span):
    num = 0
    while num <= span:
        num = float(num)
        x.append(num)
        y1.append(moment_calc(dead_load, live_load, num))
        y2.append(shear_calc(dead_load, live_load, num))
        num += 0.5  

def calculations():
        #Moment Calc
        print("Max Moment = {} K-ft".format(moment_calc(dead_load, live_load, max_span/2)))
        print("Location of max moment = {} ft".format(max_span/2))
        graph_plot(max_span)
        plt.plot(x,y1)
        plt.show()
        #Shear Calc
        print("Max Shear = {} K".format(shear_calc(dead_load, live_load, 0)))
        print("Location of max shear = 0 ft, {} ft".format(max_span))
        graph_plot(max_span)
        plt.plot(x,y2)
        plt.show()
     
calculations()