from __future__ import print_function

import sys
import re
from pyspark import SparkContext
#from pyspark.ml.clustering import KMeans
#from pyspark.accumulators import AccumulatorParam
#@author Srikanth

def detectuser(lw):
	if 'user' in lw and 'Starting' in lw:
		i = lw.index('user')
		return str(lw[i+1]).translate(None,".,?!@()*&<>''[]{}")
	else:
		return 'null'

if __name__ == "__main__":
	
	#np.set_printoptions(threshold='nan')

	if len(sys.argv) !=2:
		print("Input format is not correct")
	sc = SparkContext(appName="Q3: unique user names")
	raw = sc.textFile(sys.argv[1],4)
	#split adata with space as deliminator
	splitdata = raw.map(lambda x:x.split())
	#detect user that starting the session
	userdata = splitdata.map(lambda x:(str(detectuser(x)),1)) #ex:('achille',1)
	filterdata = userdata.filter(lambda x:x[0] != 'null')
	# count line of unique user using reducebykey
	countdata = filterdata.reduceByKey(lambda x,y: x+y)
	collectdata = countdata.collect()
	print('  + '+sys.argv[1]+': '+str(collectdata))
	
	sc.stop()
