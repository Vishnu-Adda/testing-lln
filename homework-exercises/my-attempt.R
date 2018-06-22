
totalBetween <- 0
counter <- 1
for(i in rnorm(100)) {
  if(i > -1 & i < 1) {
    totalBetween <- totalBetween + 1
  }
  mean <- totalBetween / counter
  print(mean)
  counter <- counter + 1
}