import os
import csv

#create list to store data for months, profit and profit changes
months = []
profits = []
change_list = []
greatest_increase = 0
greatest_decrease = 0


#create a path for file (check this later)
csv_path = os.path.join('Resources', 'budget_data.csv')

#open and read csv
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Read the header row first 
    next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        #Add the months and profits in the created list
        months.append(row[0])
        profits.append(int(row[1]))

        #Create variable to store the total number of months and total profit in the dataset
        total_months = len(months)
        total_profits = sum(profits)

    # Using for loop through profits to calculate change_list
    for i in range(len(profits)):
        if i < (len(profits)-1):
            change = (profits[i+1] - profits[i])
            change_list.append(change)
            
    
    #Calculate the average change and round upto 2 decimal
    average_change = round(sum(change_list)/len(change_list), 2)

    #Calculate the greatest_increase and greatest_decrease and their respective months
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)
    greatest_increase_month = change_list.index(greatest_increase)
    greatest_decrease_month = change_list.index(greatest_decrease)
    max_month = months[greatest_increase_month + 1]
    min_month = months[greatest_decrease_month + 1]

    summary = (
            f'Financial Analysis\n'
            f'--------------------------- \n'
            f'Total Months: {total_months} \n'
            f'Total: ${total_profits} \n'
            f'Average Change: $ {average_change} \n'
            f'Greatest Increase in Profits: {max_month} $ {greatest_increase} \n'
            f'Greatest Decrease in Profits: {min_month} $ {greatest_decrease} \n'
     )
    print(summary)

#Specify a path for output file named pybank_output
output_path = os.path.join("Analysis","pybank_output.txt") 

#Open the file using "write" mode
with open(output_path, 'w') as text:
    text.write(summary)
