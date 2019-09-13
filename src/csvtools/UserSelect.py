#For statistical analyses the user may specify certain rows and columns within the rows, 
#or columns and rows within the columns to perform the analyses on. 
# The selection must be appropriate for the type of statistic to be calculated.

#As a user, I want to be able to select the rows and columns to be analyzed and graphed so I can better understand my data.

def Selection():
    row=input("Enter row ")
    column=input("Enter column ")
    return row,column


