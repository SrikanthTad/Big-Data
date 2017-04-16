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
	sc = SparkContext(appName="Q8")
	#read first file
	raw = sc.textFile(sys.argv[1],4)
	#save name of file/host using broadcast
	f1 = sc.broadcast(sys.argv[1])	

	splitdata = raw.map(lambda x:x.split())
	# detect user
	userdata1 = splitdata.map(lambda x:str(detectuser(x))).filter(lambda x:x != 'null').distinct()
	
	#read second file
	raw2 = sc.textFile(sys.argv[2],4)
	# save name of file/host using broadcast
	f2 = sc.broadcast(sys.argv[2])

	splitdata2 = raw2.map(lambda x:x.split())
	#detect user
	userdata2 = splitdata2.map(lambda x:str(detectuser(x))).filter(lambda x:x != 'null').distinct()

	#remove user that appear in another file/host using subtract
	#map user with their file/host 
	collectdata1 = userdata1.subtract(userdata2).flatMap(lambda x:[(x,f1.value)]).collect() #ex: ('hector','iliad')
	collectdata2 = userdata2.subtract(userdata1).flatMap(lambda x:[(x,f2.value)]).collect() #ex: ('achille','odyssey')
	
	#collectdata1 = userdata1.subtract(userdata2).collect()
    #collectdata2 = userdata2.subtract(userdata1).collect()

	print('  + : '+str(collectdata1+collectdata2))
	
	sc.stop()
