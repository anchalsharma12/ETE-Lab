import pandas as pd
from pandas import DataFrame 
df_tennis = pd.read_csv('DS.csv')
print( df_tennis)

def entropy(probs):  
    import math
	return sum( [-prob*math.log(prob, 2) for prob in probs] )

def entropy_of_list(a_list):
	from collections import Counter
    cnt = Counter(x for x in a_list) #Count the positive and negative ex
	num_instances = len(a_list)
	probs = [x / num_instances for x in cnt.values()] 
	return entropy(probs)

total_entropy = entropy_of_list(df_tennis['PT'])

print("\n Total Entropy of PlayTennis Data Set:",total_entropy)
