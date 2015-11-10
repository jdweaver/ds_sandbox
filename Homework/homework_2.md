#Homework For Class 2: Command Line Fun


1) Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo.
- DIRECTORY: C:\Users\joshuaw\Documents\GA_Data_Science\data\chipotle.tsv
	- CODE: tail chipotle.tsv
	- CODE: head chipotle.tsv
	- DATA DESCRIPTION: flat file structure, in a wide format, with attributes/variables as columns and observations as rows,     where each row is a single item in a single order, hence order number repeats for each item. COLUMN NAME (DESCRIPTION):      order_id (unique identifier per order), quantity (number of item purchased), choice_description (describes attributes of      item e.g. fresh tomato salsa, rice, cheese etc.), item_price (price of the item)
- Other thoughts: it would really interesting if there was a date/time stamp and geo location so you could correlate time and location with demand and forecast stockouts. Also since Chipotle has a "burrito" app, if you could associate a person's info in the POS machine to the app you could proactively anticipate their order based on their location via Passbook for example. 

2) Number of orders? 
- CODE: uniq chipotle.tsv | wc -l
	- ANSWER: 4589
	- CODE RATIONALE: combine the uniq and wc -l commands using the pipe command (side note: always wondered what that symbol     was used for) to obtain a count distinct of the rows. This only tell us the number of orders in the file it doesn't tell     us the number of items. 

3) Number of items ordered (or number of lines)
- CODE: wc -l chipotle.tsv
	- ANSWER: 4623
	- CODE RATIONALE: this makes sense that we have 34 more lines indicated here than in our count distinct code. However, in         thinking about the data it seems like we should have many more items, at least 2x; the assumption being that most             people order more than one item.
	
4) Burrito Popularity: chicken or beef (Question: Is there a way do this with a single command?)
- CODE: grep "Steak Burrito" chipotle.tsv | wc -l
	- CODE: grep "Chicken Burrito" chipotle.tsv | wc -l 
	- ANSWER: Chicken (N = 553 v. N = 368)
 
5) Do chicken burritos more often have black beans or pinto beans?
- CODE: grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | wc -l
	- CODE: grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" | wc -l
	- ANSWER: black beans (N = 282) are paired with chicken burritos more often than pinto beans (N = 105)
- CODE RATIONALE: I thought of this as a nested loop. My thinking was find every instance of "Chicken Burrito" then in        that result set count the number of times that "Black Beans" or "Pinto Beans" shows up in this set and since you can         choose one or the other I could count the number of lines.

6) List the files that end in .csv or .tsv 
- CODE: find /c/Users/Joshuaw/Documents/GA_Data_Science -name "*.?sv"
	- ANSWER: 
		- GA_Data_Science/data/airlines.csv
		- GA_Data_Science/data/bank-additional.csv
		- GA_Data_Science/data/bikeshare.csv
		- GA_Data_Science/data/chipotle.tsv
		- GA_Data_Science/data/drinks.csv
		- GA_Data_Science/data/hitters.csv
		- GA_Data_Science/data/imdb_1000.csv
		- GA_Data_Science/data/sms.tsv
		- GA_Data_Science/data/titanic.csv
		- GA_Data_Science/data/ufo.csv
		- GA_Data_Science/data/vehicles_test.csv
		- GA_Data_Science/data/vehicles_train.csv
		- GA_Data_Science/data/yelp.csv

7) Number of occurance of "dictionary" (upper or lower case)
- CODE: grep -r -i dictionary /c/Users/Joshuaw/Documents/GA_Data_Science | wc -w
	- ANSWER: 864

8) Find something interesting: 
- In set of transactions, for people who drink Coca-Cola products, Coke is by far the most popular accounting for over           half of all coke products consumed (N = 257, 52%) compared to Diet Coke (N = 134, 27%).   
