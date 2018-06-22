
# Kind of like a forEach loop, where i is a num from rnorm()
# The bigger N is, the closer it will print to 68.2
N <- 1000
counter <- 0
for(i in rnorm(N)) {
  if(i > -1 & i < 1) {
    counter <- counter + 1
  }
}
counter / N

# Compare the last statement to: 68.2% ( our theoretical value )