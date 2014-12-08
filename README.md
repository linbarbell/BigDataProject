
#A Look at NYC Taxi Data and How We Tip

<h3>Computing w/ Large Data Sets - NYU Courant Institute - Fall 2014</h3>

<b>Project By:</b>

- Lin, Emily  
- Liu, Thomas  
- Shaw Susanto, Billy

<b>Main Tools</b>

- Python (main language)
- iPython Notebook (main platform)
- GeoPy (for reverse geocoding)
- Pandas (for data analysis)
- Tableau (for data visualization)

<h3><u>Data</u></h3>
This project uses data by <a href="http://chriswhong.com/open-data/foil_nyc_taxi/">Chris Whong</a>, who has
requested all 2013 NYC taxi rides data from NYC Taxi & Limousine Commission. Bless his heart.

We took all trip information, as well as all the fare rides. </br>

</br>
We sampled about 75 million rides (>= 30GB) to make the following analysis. 

<h3><u>Data Analysis</u></h3>

<b>Basic Information</b> (1 slide per point)

  - Which neighborhood takes the cab the most (pickup): 1) List of top 10 2) Pie Chart - "top neighborhood.csv"
  - Which is the most popular neighborhood for cab rides (dropoff) 1) List of top 10 2) Pie - chart - "top_drop_neighborhood.csv"
  - At which time do New Yorkers take cab ride the most? 1) List of percentage 2) Bar chart - "count_by_hour.csv"
  - At which time do New Yorkers take cab rides the least? 
  - Which time has the lowest avg speed (distance/ time travelled) 
  - Which time has the highest avg speed (distance/ time travelled) 
  
<b>Payments & Tip </b>

  - Average in New York CRD - 0.20200465239853405

  Specific areas of interest:
  - Tip percentage (avg, top)
  - Credit card vs. cash
  - Total fare
  
  Factors to analyze:
  - Average
  - Neighborhood: does pick up area/ drop off area affect tip or payment methods (for the top list: only pick with more than 10,000 rides)
  - Time of the day
  - Distance travelled
  
<b>Analytics</b>

  - Prediction: predicting tip based on neighborhood and time -> lm, simplified lasso. compare two methods by comparing mse. 
