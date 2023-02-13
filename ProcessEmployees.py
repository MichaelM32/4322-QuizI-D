'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

employee_dat = open("employee_data.csv", 'r')
empfile = csv.reader(employee_dat, delimiter=',')


#create an empty dictionary

empdict = {}

#use a loop to iterate through the csv file

for employee in empfile:
    CustID = employee[0]
    FName = employee[1]
    LName = employee[2]
    Dep = employee[3]
    Title = employee[4]
    Sal = employee[5]
    Hire = employee[6]
    Birth = employee[7]
    Gend = employee[8]
    Clear = employee[9]

    if employee[4] == "Marketing":
        raise_pay = float(employee[5]) * 1.1
        

    #check if the employee fits the search criteria



print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout



          
        

        
    
