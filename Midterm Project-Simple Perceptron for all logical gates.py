#This program makes/trains perceptron neural network for any given gate by the user except for 'NOT'.
#Student Name: Maral Dezfoulizadeh
#Email: maraldezfoulizadeh78@gmail.com

import random

exit_flag = False
print("------------------------------------------------------------------------------------------------")
while (exit_flag == False):
    #getting the gate from user
    gate = input("Please Enter the gate(AND, OR, NAND, NOR, XOR, XNOR) or type 'exit' to exit the program: ")
    print("------------------------------------------------------------------------------------------------")
    target = []                              #setting targets based on the given gate by user
    if gate == "AND":
        target.append(0)
        target.append(0)
        target.append(0)
        target.append(1)
    elif gate == "NAND":
        target.append(1)
        target.append(1)
        target.append(1)
        target.append(0)
    elif gate == "OR":
        target.append(0)
        target.append(1)
        target.append(1)
        target.append(1)
    elif gate == "NOR":
        target.append(1)
        target.append(0)
        target.append(0)
        target.append(0)
    elif gate == "XOR":
        target.append(0)
        target.append(1)
        target.append(1)
        target.append(0)
    elif gate == "XNOR":
        target.append(1)
        target.append(0)
        target.append(0)
        target.append(1)
    elif gate == "exit":
        break

    #getting the alpha value from user
    alpha = float(input("Now Please Enter the Alpha value: "))
    if alpha>1 or alpha<0:
        while(True):
            alpha = float(input("The Alpha you entered is either very big or very small. Please enter a value between 0 and 1: "))
            if alpha <1 and alpha>0:
                break

    print("--------------------------------------------------------------------------------------------------")
    Answer = input("Would you like to Enter W1 and W2 yourself(if no it will be randomly generated)? |y/n| : ")
    print("___________________________________________________________________________________________________")



    x1x2 = [0,0,0,1,1,0,1,1]                 #setting input values for the table                            
    

    y = 0                   #calculation relust. Will be put into the functionand if it was greater than 1, it'll be 1. Else it'll be 0.
                            #Bios memory space(b) is assumed to have the value of 0
    if Answer == "y":
        w1 = float(input("Please Enter W1: "))
        print("-------------------------------")
        w2 = float(input("Please Enter W2: " ))
        print("___________________________________________________________________________________________________")
    elif Answer == "n":
        print("___________________________________________________________________________________________________")
        w1 = random.random()
        w2 = random.random()

    Error = 0               #Error value. If result matches the target value Error is 0. Else it's 1.
    result = 0              #we calculate y and put it in f and this value will be the result which is either 0 or 1 depending on y. 
    i=0                     #counter for the input list
    j=0                     #counter for the target list
    counter = 0

    nochange_round = 0   
    """
        if  'nochange_round' value is equal to 4 it means that 1 round of calculation has been done
        without any changes to w1 and w2 which means that the learning is done.
    """
    while(counter in range(101)):
        while(i in range(8)):
            y = (w1*x1x2[i]) + (w2*x1x2[i+1])
            print("Y is : "+ str(w1)+ " * |" + str(x1x2[i]) + "| + " + str(w2) + " * |" + str(x1x2[i+1]) + "| = " + str(y))
            #calculating f(y)
            if y>1:
                result = 1
            else:
                result = 0
            
            if result == target[j]:
                print("No Error, no need for change.")
                Error = 0
                nochange_round =  nochange_round + 1
                if  nochange_round == 4:
                    counter = 101
                    exit_flag = True
                    print("| DONE! |")
                    break
                j=j+1
                
            else:
                Error = 1
                print(" -----------------------------------------")
                print("| We have Error. Need to change W1 and W2 |")
                print(" -----------------------------------------")
                print()
                w1 = w1 + (x1x2[i] * Error * alpha)
                print("W1 is now: " + str(w1))
                w2 = w2 + (x1x2[i+1] * Error * alpha)
                print("W2 is now: " + str(w2))
                nochange_round = 0
                j=j+1
            
            if j == 4:
                j=0
            
            y = 0
            i=i+2
            if i==8 and nochange_round < 4:
                nochange_round = 0
                i=0
                print("_______________________________________________________________________________________________")
            counter = counter + 1
            if counter>100:
                print("-----------------------------------------------------------------")
                print("I tried 100 rounds and I DON'T THINK I'M EVER GOING TO BE DONE...")
                print("-----------------------------------------------------------------")
                break

