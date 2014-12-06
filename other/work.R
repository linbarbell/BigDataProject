trip.data <- read.csv(file = "trip_data_example.csv")
time <- trip.data[,9]
distance <- trip.data[,10]

trip.data["hour"] <- NA
pickup <- as.vector(trip.data[,6])
for (i in 1:length(trip.data[,"hour"])) {
  timesplit <- strsplit(pickup[i], " ")[[1]]
  timesplit <- strsplit(timesplit[2], ":")[[1]][1]
  trip.data[i, "hour"] <- timesplit
}
#lms <- lm(time ~ distance)

#anova(lms)
#summary(lms)
#plot(distance, time)
#abline(lms)
trip.data[2, "hour"] <- 0