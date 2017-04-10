from __future__ import print_function

import sys
import re

from pyspark import SparkContext
#from pyspark.ml.clustering import KMeans
#from pyspark.accumulators import AccumulatorParam
#@author Srikanth

if __name__ == "__main__":
	
	#np.set_printoptions(threshold='nan')

	if len(sys.argv) !=2:
		print("Input format is not correct")
	sc = SparkContext(appName="Q2: sessions of user 'achille'")
	#read file
	raw = sc.textFile(sys.argv[1],4)
	#filter user 'achiller' who starting session
	filterline = raw.filter(lambda x: x.find('Starting Session') != -1 and x.find('user achille') != -1)

	#count line that include starting session .. user achille
	countline = filterline.count()
	print('  + '+sys.argv[1]+': '+str(countline))

	sc.stop()
