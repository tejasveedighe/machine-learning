# the percentile of data is a number which describes as the number which the given percentage of values are lower than or equal to 
import numpy as np

# the 75 percentile of ages is 43 that means that 75% of values are less that or equal to 43
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

print(np.percentile(ages, 75))