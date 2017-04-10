#!/usr/bin/python
#@author Srikanth

from __future__ import print_function

import sys

from pyspark import SparkContext
#from pyspark.ml.clustering import KMeans
#from pyspark.accumulators import AccumulatorParam

if __name__ == "__main__":
	
	#np.set_printoptions(threshold='nan')

	if len(sys.argv) !=2:
		print("Input format is not correct")
	sc = SparkContext(appName="Q1: line counts")
	#read file
	raw = sc.textFile(sys.argv[1],4)
	#count line in file
	countline = raw.count()
	print('  + '+sys.argv[1]+': '+str(countline))

	sc.stop()
