'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

#[your code here]
import csv
with open("chipotle.tsv", mode="rU") as f: 
    file_nested_list = [row for row in csv.reader(f, delimiter="\t")]

#WITHOUT csv.reader()
#with open("chipotle.tsv", mode="rU") as f:
#    file_nested_list = [row.split("\t") for row in f]


'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

#[your code here]
header = file_nested_list[0]
data = file_nested_list[1:]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps 
and then code each step
'''

ANSWER == 18.81

#slice the data list to include only the order_id column (sublist)
order_id = []
for row in data: 
    row[0]
    order_id.append(row[0])
print order_id[0:5] #check to make sure the loop sliced the correct column

number_orders = len(set(order_id)) #count distinct of order numbers are store it in a variable
print number_orders #print out order number should be 1834

#create a list of item prices from the item_price column (list).
#First remove"$" character and then converting the string into a float 
#need to convert to float because of decimals
#Can all be accomplished in a single for loop
price = []
for row in data: 
    row[-1][1:6]
    price.append(float(row[-1][1:6]))

type(price) #confirm that this is a list
type(price[0]) #confirm that values in list are floats 
print price

#Create a list of order quantities and convert the strings into integers
#quantity = []
#for row in data: 
#    row[1]
#    quantity.append(int(row[1]))
    
#type(quantity) #confirm that this is a list
#type(quantity[0]) #confirm that values in list are integers 

#Get total price by doing elementwise multiplication to our two lists: quantity and price
#total_price = [a*b for a,b in zip(price,quantity)] 

#use sum function to create a single flaot value
#we can use the sum function without multiplying price by the quantit column 
#because the price column/var already reflects the quantity multiplier   
sum_total_price = sum(price)
print sum_total_price

avg_order_price = (sum_total_price/number_orders)
print avg_order_price


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

soda_list = []
for row in data: 
    if (row[2] == "Canned Soda"  or row[2] == "Canned Soft Drink"):
        soda_list.append(row[3])

unique_sodas = set(soda_list)
print unique_sodas

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

ANSWER == 5.40
'''
NOTE: much more complicated code below, below is the condensed version
'''
http://stackoverflow.com/questions/823561/what-does-mean-in-python

burrito_orders = 0 
toppings_number = 0 
for row in data: 
    if "Burrito" in row[2]:
        burrito_orders += 1
        toppings_number += (row[3].count(',') + 1)
        
avg_toppings = (round(toppings_number/float(burrito_orders), 2))
print avg_toppings


##create a list that contains only burrito toppings
#toppings_list = []
#for row in data: 
#    if (row[2] == "Steak Burrito" or row[2] == "Chicken Burrito" or row[2] == "Veggie Burrito" or row[2] == "Carnitas Burrito" or row[2] == "Barbacoa Burrito" or row[2] == "Burrito"):
#        toppings_list.append(row[3])
#print toppings_list #1172
#
##find the number of burritos
##check this using excel...bad I know....but I don't trust other ways of checking. 
##plus it's probably more defensible to tell your stakeholder you checked this way rather
##than some complex other logic using code...
#number_burrito_orders = len(toppings_list)
#print number_burrito_orders
#
##find the total number of toppings using list comprehension but only works for lists with 
##one level of nesting 
#num_toppings = [item for sublist in toppings_list for item in sublist].count(",")
#print num_toppings #number of burrito toppings = 5151, this number is too low 
##a visual inspection of the data suggests that there are closer to 7-10 toppings per order
##thus the order number should be somewhere around 9-10K
#
##create a function to flatten the list, pulled shamelessly from stack exchange
#def flatten(x):
#    result = []
#    for el in x:
#        if hasattr(el, "__iter__") and not isinstance(el, basestring):
#            result.extend(flatten(el))
#        else:
#            result.append(el)
#    return result
#
##store flattened list in var
#flat_toppings_list = flatten(toppings_list)
#print flat_toppings_list
#
##loop through flattened list and count each comma and add 1
#number_toppings = []
#for item in flat_toppings_list:
#        item.count(",")        
#        number_toppings.append(item.count(",") + 1)
#
##create a var with the sum of toppings
#sum_number_toppings = sum(number_toppings)
#print sum_number_toppings
#
#avg_toppings = (round(sum_number_toppings / float(number_burrito_orders), 2))
#print avg_toppings

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

from collections import defaultdict
chips = defaultdict(int)
for row in data:
    if "Chips" in row[2]: 
        chips[row[2]] += int(row[1])

        
