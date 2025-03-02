We are developing a program with User Interface to find the Earliest Arrival Time and scheduling the Airline Flights.
It provides an agenda of flights for the users. The Agent of the Airline company can have access to the database of all the flights and airports. Along with the Flight Number, Origin Airport and Destination Airport. The Flights also have departure and arrival time.
The main objective of the project is to determine the earliest Arrival Time for the   Destination from a Source Origin and the Start Time.

We are going to solve this using the Shortest Path Algorithm.








As we need to calculate the earliest arrival time given with a start time. We can take the problem to be a Digraph where all the airports are nodes, and the flights are the Diedges with the weight of time interval (i.e., 
the time difference between arrival time of destination Airport and the Source Airport).
We need to take into consideration that while going from the Origin Airport to Destination Airport and while taking flights from one airport to another, we will consider only the flights that can be caught.
Thus, TIME plays an important role in our Algorithm, as we can take only the flights whose departure time from the airport is later than the Arrival time at the airport.
We are taking the help of Dijkstra’s Algorithm
