from statistics import mode
from scipy import stats
import numpy as np

data = [99,86,87,88,111,86,103,87,94,78,77,85,86]

meanOfData = np.mean(data)

modeOfData = stats.mode(data)

medainOfData = np.median(data)

print(meanOfData, modeOfData, medainOfData)