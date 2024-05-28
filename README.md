# Flights Dataset Analysis

## About Dataset

### Research Questions
The aim of our study is to answer the following research questions:
- Does the price vary with Airlines?
- How is the price affected when tickets are bought just 1 or 2 days before departure?
- How does the price change with different Source and Destination cities?
- How does the ticket price vary between Economy and Business class?

## Dataset
The dataset contains information about flight booking options from the Ease My Trip website for flights between India's top 6 metro cities. There are 300,261 data points and 11 features in the cleaned dataset.

### Features
The various features of the cleaned dataset are explained below:

1. **Airline**: The name of the airline company. This is a categorical feature with 6 different airlines.
2. **Flight**: Information regarding the plane's flight code. This is a categorical feature.
3. **Source City**: The city from which the flight takes off. This is a categorical feature with 6 unique cities.
4. **Departure Time**: A derived categorical feature created by grouping time periods into bins. It contains 6 unique time labels for the departure time.
5. **Stops**: A categorical feature with 3 distinct values that indicates the number of stops between the source and destination cities.
6. **Arrival Time**: A derived categorical feature created by grouping time intervals into bins. It has 6 distinct time labels for the arrival time.
7. **Destination City**: The city where the flight will land. This is a categorical feature with 6 unique cities.
8. **Class**: A categorical feature that contains information on seat class, with two distinct values: Business and Economy.
9. **Duration**: A continuous feature that shows the total travel time between cities in hours.
10. **Days Left**: A derived feature calculated by subtracting the booking date from the trip date.
11. **Price**: The target variable that stores information on the ticket price.

[Link to the dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
## How to Run the Dashboard
### Clone the Repository
```bash
git clone https://github.com/melllinia/FlightPriceDashboard.git
cd FlightPriceDashboard
```

### Install the Requirements
```bash
pip install -r requirements.txt
```

### Run the Dashboard
```bash
python3 src/app.py
```

## Dashboard Deployment
The dashboard is available online with subsampled data for demonstration purposes.  
You can access it here: [Flight Price Dashboard](https://flightpricedashboard.onrender.com/)
