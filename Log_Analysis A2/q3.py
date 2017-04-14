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

	if len(sys.argv) !=2:
		print("Input format is not correct")
	sc = SparkContext(appName="Q3: unique user names")
	raw = sc.textFile(sys.argv[1],4)

	#split line with space as deliminator
	splitdata = raw.map(lambda x:x.split())
	#detect user that starting session using function detectuser
	userdata = splitdata.map(lambda x:str(detectuser(x))).filter(lambda x:x != 'null')
	# distinct users
	collectdata = userdata.distinct().collect()
	print('  + '+sys.argv[1]+': '+str(collectdata))
	
	sc.stop()
