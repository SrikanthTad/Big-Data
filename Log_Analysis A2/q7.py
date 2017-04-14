from __future__ import print_function

import sys
import re
from pyspark import SparkContext
#from pyspark.ml.clustering import KMeans
#from pyspark.accumulators import AccumulatorParam
#@author Srikanth

def detectuser(lw):
	if 'Starting' in lw and 'user' in lw:
		i = lw.index('user')
		return str(lw[i+1]).translate(None,".,?!@()*&<>''[]{}")
	else:
		return 'null'
if __name__ == "__main__":
	
	#np.set_printoptions(threshold='nan')

	if len(sys.argv) !=3:
		print("Input format is not correct")
	sc = SparkContext(appName="Q7")
	#read first file
	raw = sc.textFile(sys.argv[1],4)

	splitdata = raw.map(lambda x:x.split())
	#detect user from file 1
	userdata1 = splitdata.map(lambda x:str(detectuser(x))).filter(lambda x:x != 'null')
	
	#read second file
	raw2 = sc.textFile(sys.argv[2],4)
	
	splitdata2 = raw2.map(lambda x:x.split())
	#detect user from file 2
	userdata2 = splitdata2.map(lambda x:str(detectuser(x))).filter(lambda x:x != 'null')
	# find user that appear in both of file using intersection
	collectdata = userdata1.intersection(userdata2).collect()
	print('  + : '+str(collectdata))
	
	sc.stop()
