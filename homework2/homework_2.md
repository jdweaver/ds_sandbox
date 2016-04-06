#Homework For Class 2: Command Line Fun


1) Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo.
- DIRECTORY:/c/Users/joshuaw/Documents/data science class/class 4 git and git hub

	- CODE: tail chipotle.tsv
	- CODE: head chipotle.tsv
	- DATA DESCRIPTION: flat file structure, in a wide format, with attributes/variables as columns and observations as rows,     where each row is a single item in a single order, hence order number repeats for each item. COLUMN NAME (DESCRIPTION):      order_id (unique identifier per order), quantity (number of item purchased), choice_description (describes attributes of      item e.g. fresh tomato salsa, rice, cheese etc.), item_price (price of the item)
- Other thoughts: it would really interesting if there was a date/time stamp and geo location so you could correlate time and location with demand and forecast stockouts. Also since Chipotle has a "burrito" app, if you could associate a person's info in the POS machine to the app you could proactively anticipate their order based on their location via Passbook for example. 

2) Number of orders? 
- CODE: tail chipotle.tsv
	- ANSWER: 1834
	- CODE RATIONALE: sort of hacky...but since I know that there is one line per item and multiple items, I can look at the last lines of the file and grab the order ID #

3) Number of items ordered (or number of lines)
- CODE: wc -l chipotle.tsv
	- ANSWER: 4623
	
4) Burrito Popularity: chicken or beef
- CODE: grep "Steak Burrito" chipotle.tsv | wc -l
	- CODE: grep "Chicken Burrito" chipotle.tsv | wc -l 
	- ANSWER: Chicken (N = 553 v. N = 368)
 
5) Do chicken burritos more often have black beans or pinto beans?
- CODE: grep "Chicken Burrito" chipotle.tsv | grep "Pinto Beans" | wc -l
- CODE: grep "Chicken Burrito" chipotle.tsv | grep "Black Beans" | wc -l
- ANSWER: black beans (N = 282) are paired with chicken burritos more often than pinto beans (N = 105)
- CODE RATIONALE: I thought of this as a nested loop. My thinking was find every instance of "Chicken Burrito" then in that result set count the number of times that "Black Beans" or "Pinto Beans" shows up in this set and since you can choose one or the other I could count the number of lines.

6) List the files that end in .csv or .tsv 
- CODE: find /c/Users/Joshuaw/Documents/GA_Data_Science -name "*.?sv"
	- ANSWER: 
				./GA-SEA-DAT2-master/data/airlines.csv
				./GA-SEA-DAT2-master/data/Airline_on_time_west_coast.csv
				./GA-SEA-DAT2-master/data/bank-additional.csv
				./GA-SEA-DAT2-master/data/bikeshare.csv
				./GA-SEA-DAT2-master/data/chipotle.tsv
				./GA-SEA-DAT2-master/data/citibike_feb2014.csv
				./GA-SEA-DAT2-master/data/drinks.csv
				./GA-SEA-DAT2-master/data/drones.csv
				./GA-SEA-DAT2-master/data/hitters.csv
				./GA-SEA-DAT2-master/data/icecream.csv
				./GA-SEA-DAT2-master/data/imdb_1000.csv
				./GA-SEA-DAT2-master/data/mtcars.csv
				./GA-SEA-DAT2-master/data/NBA_players_2015.csv
				./GA-SEA-DAT2-master/data/ozone.csv
				./GA-SEA-DAT2-master/data/pronto_cycle_share/2015_station_data.csv
				./GA-SEA-DAT2-master/data/pronto_cycle_share/2015_trip_data.csv
				./GA-SEA-DAT2-master/data/pronto_cycle_share/2015_weather_data.csv
				./GA-SEA-DAT2-master/data/sms.tsv
				./GA-SEA-DAT2-master/data/syria.csv
				./GA-SEA-DAT2-master/data/titanic.csv
				./GA-SEA-DAT2-master/data/ufo.csv
				./GA-SEA-DAT2-master/data/vehicles_test.csv
				./GA-SEA-DAT2-master/data/vehicles_train.csv
				./GA-SEA-DAT2-master/data/yelp.csv


7) Number of occurance of "dictionary" (upper or lower case)
- CODE: grep -r -i dictionary | wc -w
	- ANSWER: 1227

8) Find something interesting: 
- of 4623, 901 items were coca-cola, representing 19% of the total items 
