# Set a password 
password = "mysecret"

# Function to check the password
def check_password(input_password):
    if input_password == password:
        return True
    else:
        return False

# Main program
while True:
    user_input = input("Enter the password: ")
    if check_password(user_input):
        print("Access granted!")
        break
    else:
        print("Access denied. Try again.")
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
print("===========================")
print("PROJECT:DATA VISUALISATION")
print("===========================")
print("TOPIC:Productions Of Different Cereals By Indian States" )
print("Developed by:1.Amit Shukla 2.Aman Maddheshiya 3.Ansh Shukla")

for n in range(0,9):
    print("---------------------------------------")
    print("1.For checking the data.")
    print("2.Read the file without index.")
    print("3.Line Chart")
    print("4.Bar Graph")
    print("5.To Modify the specific existence data.")
    print("6.To Add New ROW In CSV.")
    print("7.To Delete a Record From CSV.")
    print("8.For Exit")
    print("---------------------------------------")
    choice=int(input('Enter Your Choice as 1,2,3,4,5,6,7 or 8:'))

    if choice==1:
       print("The Data")
       df=pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv")
       print(df)

    elif choice==2:
        print("Reading the file without index")
        df=pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv", index_col=0)
        print(df)


#FOR LINE CHART:)
    elif choice==3:
        df=pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv")
        States=df["States"]
        Wheat=df["Wheat"]
        Rice=df["Rice"]
        Maize=df["Maize"]
        Pulses=df["Pulses"]
        plt.xlabel("States")
        for k in range(0,6):
            print("Press 1 to print Wheat Production as per the state.")
            print("Press 2 to print Rice Production as per the state.")
            print("Press 3 to print for Maize Production as per the state.")
            print("Press 4 to print for Pulses Production as per the state.")
            print("Press 5 to print All data.")
            print("Press 6 to move NEXT. ")
            YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
        
            if YC == 1:
                plt.ylabel("Wheat")
                plt.title("State wise Production List ")
                plt.plot(States, Wheat, color='b')
                plt.show()
            elif YC == 2:
                plt.ylabel("Rice")
                plt.title("State wise Production List")
                plt.plot(States, Rice, color='g')
                plt.show()
            elif YC == 3:
                plt.ylabel("Maize")
                plt.title("State wise Production List")
                plt.plot(States, Maize, color='r')
                plt.show()
            elif YC == 4:
                plt.ylabel("Pulses")
                plt.title("State wise Production List")
                plt.plot(States, Pulses, color='c')
                plt.show()
            elif YC == 5:
                plt.ylabel("Production")
                plt.plot(States,Wheat, color='b', label = "State wise Wheat Production")
                plt.plot(States, Rice, color='g', label = "State wise Rice Production")
                plt.plot(States,Maize, color='r', label = "State wise Maize Production")
                plt.plot(States,Pulses, color='c', label = "State wise Pulses Production")
                plt.legend()
                plt.show()
            elif YC==6:
                break
            else:
                print("Enter valid input")
        

#FOR BAR GRAPH:)
    elif choice==4:
        df = pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv")
        States = df["States"]
        Wheat = df["Wheat"]
        Rice = df["Rice"]
        Maize = df["Maize"]
        Pulses = df["Pulses"]
        plt.xlabel("States")
        for k in range(0,7):
            print("Press 1 to print the Wheat Production as per the state.")
            print("Press 2 to print the Rice Production as per the state.")
            print("Press 3 to print the Maize Production as per the state")
            print("Press 4 to print the Pulses Production as per the state.")
            print("Press 5 to print the data in form of stack bar chart")
            print("Press 6 to print the data in form of multi bar chart")
            print("Press 7 to move NEXT ")
            YC = int(input("Enter the number representing your preferred bar graph from the above choices:"))
            if YC == 1:
                plt.ylabel("Wheat")
                plt.title("States wise Wheat Production")
                plt.bar(States, Wheat, color='b', width = 0.5)
                plt.show()
            elif YC == 2:
                plt.ylabel("Rice")
                plt.title("States wise Rice Production")
                plt.bar(States,Rice, color='g', width = 0.5)
                plt.show()
            elif YC == 3:
                plt.ylabel("Maize")
                plt.title("States wise Maize Production")
                plt.bar(States, Maize, color='r', width = 0.5)
                plt.show()
            elif YC == 4:
                plt.ylabel("Pulses")
                plt.title("States wise Pulses Production")
                plt.bar(States, Pulses, color='c', width = 0.5)
                plt.show()
            elif YC == 5:
                plt.bar(States,Wheat, color='b', width = 0.5, label = "States wise Wheat Production")
                plt.bar(States, Rice, color='g', width = 0.5, label = "States wise Rice Production")
                plt.bar(States,Maize, color='r', width = 0.5, label = "States wise Maize Production")
                plt.bar(States, Pulses, color='c',width = 0.5, label = "States wise Pulses Production")
                plt.legend()
                plt.show()
            elif YC == 6:
                D=np.arange(len(States))
                width=0.25
                plt.bar(D,Wheat, width, color='b', label = "States wise Wheat Production")
                plt.bar(D+0.25,Rice, width, color='g', label = "States wise Rice Production")
                plt.bar(D+0.50,Maize, width, color='r', label = "States wise Maize Production")
                plt.bar(D+0.75, Pulses ,width, color='c', label = "States wise Pulses Production")
                plt.legend()
                plt.show()
            elif YC==7:
                break
            else:
                print("Enter valid input")
    elif choice==5:
        #TO MODIFY A SPECIFIC  DATA BY ASSIGNING INDEX AND COLUMN NUMBER
        df = pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv")
        print(df)
       
        i=int(input("Provide the index of the SPECIFIC ROW WHOSE RECORD TO MODIFIED(0,1,2,..):"))
        j=int(input("Provide the COLUMN Number of the SPECIFIC COLUMN WHOSE RECORD TO MODIFIED(1,2,3,..):"))
        l=int(input("Provide the new DATA TO BE ADDED AT THAT PLACE:"))
        
        df.iloc[i,j] = l
        df.to_csv(r"C:\Users\anshs\Downloads\ProductionList.csv", index=False)
        print(df)

    elif choice ==6:
        #TO ADD NEW RECORD INTO CSV FILE
        import csv
        u=input("Provide the State's Name:")
        v=input("Provide the Wheat Production:")
        w=input("Provide the Rice Production:")
        x=input("Provide the Maize Production:")
        y=input("Provide the Pulses Production:")
        data_to_append = [[u,v,w,x,y]]
        file=open(r"C:\Users\anshs\Downloads\ProductionList.csv",'a',newline='')
        writer=csv.writer(file)
        writer.writerows(data_to_append)
        file.close()
        df = pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv")
        print(df)
    elif choice==7:
        #TO DELETE A RECORD FROM CSV FILE
        m=int(input("Provide the index of row to be deleted:"))
        df = pd.read_csv(r"C:\Users\anshs\Downloads\ProductionList.csv")
        df = df.drop(df.index[m])
        df.to_csv(r"C:\Users\anshs\Downloads\ProductionList.csv", index=False)
        print(df)
    elif choice ==8:
           print("Thank You for using...")
           break






