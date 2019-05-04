import pandas as pd
budget_data = pd.read_csv('Resources/budget_data.csv')
budget_data.head()

date = budget_data['Date'].values
#print(date)

profit_losses = budget_data['Profit/Losses'].values
#print(profit_losses)

#find the total number of months (length of date list)
total_number_months = len(date)
#print(total_number_months)

#find the net total amount of "Profit/Losses" over the entire period (sum of profit_losses list)
sum_of_profit_losses = sum(profit_losses)
#print(sum_of_profit_losses)

# find the average of the changes in "Profit/Losses" over the entire period (take the second value in profit_losses list and subtract the first value then third - second and so on down the list, then take the average of all of those values)
list_of_profit_losses_differences = []
for i in range(1, len(profit_losses)):
     difference = profit_losses[i] - profit_losses[i-1]
     list_of_profit_losses_differences.append(float(difference))    
    
 #print(list_of_profit_losses_differences)

from statistics import mean
average_change_profit_losses = mean(list_of_profit_losses_differences)
average_change_profit_losses_round =float(round(average_change_profit_losses, 2))
#print(average_change_profit_losses_round)


# find the greatest increase in profits (date and amount) over the entire period (find max of list_of_profit_losses_differences)
max_profit = max(list_of_profit_losses_differences)
int_max_profit = int(max_profit)
#print(int_max_profit)
index_max_profit = list_of_profit_losses_differences.index(max_profit)
#print(index_max_profit)
date_index_max = date[index_max_profit + 1]
#print(date_index_max)


# find the greatest decrease in losses (date and amount) over the entire period (find min of list_of_profit_losses_differences)
min_profit = min(list_of_profit_losses_differences)
int_min_profit = int(min_profit)
#print(int_min_profit)
index_min_profit = list_of_profit_losses_differences.index(min_profit)
#print(index_min_profit)
date_index_min = date[index_min_profit + 1]
#print(date_index_min)

#print out all values as requested
print('Financial Analysis')
print('-------------------------------')
print(f"Total Months: {total_number_months}")
print(f"Total: ${str(sum_of_profit_losses)}")
print(f"Average Change: ${str(average_change_profit_losses_round)}")
print(f"Greatest Increase in Profits: {date_index_max} (${str(int_max_profit)})")
print(f"Greatest Decrease in Profits: {date_index_min} (${str(int_min_profit)})")

print 
import sys
sys.stdout = open('main.txt', 'w')
print('Financial Analysis')
print('-------------------------------')
print(f"Total Months: {total_number_months}")
print(f"Total: ${str(sum_of_profit_losses)}")
print(f"Average Change: ${str(average_change_profit_losses_round)}")
print(f"Greatest Increase in Profits: {date_index_max} (${str(int_max_profit)})")
print(f"Greatest Decrease in Profits: {date_index_min} (${str(int_min_profit)})")
sys.stdout.close()





