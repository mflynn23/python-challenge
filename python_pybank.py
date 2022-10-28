#import csv module 
import csv
import os 

#declaring csv path
csvpath = os.path.join('budget_data.csv') 

with open (csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)

    #Variables
    months=[]
    outcomes=[]

    # Conditions
    total_pl= 0
    m_count=0
    m_change=0
    change=0
    revenue = 0
    min_revenue = 0
    max_revenue = 0
    sum_revenue = 0
    avg_revenue = 0
    avg_revenue_change = 0
    sum_revenue_change = 0
    prev_revenue = 0
    line_num = 1

    # Reading the rows
    for row in csvreader:
        m_count = m_count + 1
        revenue = float(row[1])
        sum_revenue = sum_revenue + revenue
        revenue_change = revenue - prev_revenue
        sum_revenue_change = sum_revenue_change + revenue_change
        if revenue_change < min_revenue:
            min_month = row[0]
            min_revenue = revenue_change
        if revenue_change > max_revenue:
            max_month = row[0]
            max_revenue = revenue_change
        prev_revenue = revenue

avg_revenue = sum_revenue/m_count
avg_revenue_change = round(sum_revenue_change/(m_count - 1), 2)
    #sum_revenue_change/(m_count-1)

#Generating Outputs
analysis=f'\
    Financial Analysis\n\
    Total Months: {m_count}\n\
    Total: ${round(sum_revenue,0)}\n\
    Average Change: {avg_revenue_change}\n\
    Greatest Increase in Profits: {max_month} (${max_revenue})\n\
    Greatest Decrease in Profits: {min_month} (${min_revenue})'

print(analysis)

#Write into text file

pybankfile=open("pybank.txt","w") #Open or create a new file 
pybankfile.writelines(analysis) #Print analysis
pybankfile.close() #Close file