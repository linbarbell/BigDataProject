
#Computing w/ Large Data Sets - NYU Courant Institute - Fall 2014

A Look at NYC Taxi Data and How We Tip

<b>Project By:</b>

- Lin, Emily  
- Liu, Thomas  
- Shaw Susanto, Billy

<h3><u>Data</u></h3>
This project uses data by <a href="http://chriswhong.com/open-data/foil_nyc_taxi/">Chris Whong</a>, who has
requested all 2013 NYC taxi rides data from NYC Taxi & Limousine Commission. Bless his heart.

We took all trip information, as well as all the fare rides. </br>

</br>
We sampled about 75 million rides (>= 30GB) to make the following analysis. 

<h3><u>Data Analysis</u></h3>

<b>Basic Information</b>

  - Which neighborhood takes the cab the most (pickup)  
  - Which is the most popular neighborhood for cab rides (dropoff) 
  - At which time do New Yorkers take cab ride the most? 
  - At which time do New Yorkers take cab rides the least? 
  - Which time has the lowest avg speed (distance/ time travelled) 
  - Which time has the highest avg speed (distance/ time travelled) 
  
<b>Payments & Tip </b>

  - Average in New York CRD - 0.20200465239853405
  - Which neighborhood tips the most - make a histogram, possibly using visual map of NYC OK
  - Which neighborhood uses credit card vs neighborhoods that don’t use credit cards - histogram, possibly using visual map of NYC
  - Does time of the day affect tip?
  
  
<b>Analytics</b>

  - Prediction: predicting tip based on neighborhood and time -> lm, simplified lasso. compare two methods by comparing mse. 
