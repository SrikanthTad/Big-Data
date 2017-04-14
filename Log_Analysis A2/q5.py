from __future__ import print_function

import sys
import re
from pyspark import SparkContext
#from pyspark.ml.clustering import KMeans
#from pyspark.accumulators import AccumulatorParam
#@author Srikanth

def detecterror(lw):
	if lw.find('error') != -1:
		return 1
	else:
		return 0

if __name__ == "__main__":
	
	#np.set_printoptions(threshold='nan')

	if len(sys.argv) !=2:
		print("Input format is not correct")
	sc = SparkContext(appName="Q5: detect error")
	raw = sc.textFile(sys.argv[1],4)

	# detect line that contain word 'error'
	errordata = raw.filter(lambda x:detecterror(x.lower()))
	
	#countdata = filterdata.reduceByKey(lambda x,y: x+y)
	collectdata = errordata.count()
	print('  + '+sys.argv[1]+': '+str(collectdata))
	
	sc.stop()
