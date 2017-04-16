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
	sc = SparkContext(appName="Q6: 5 most frequent error massage")
	raw = sc.textFile(sys.argv[1],4)

	splitdata = raw.map(lambda x:x.split(None, 4))
	
	#errordata = splitdata.filter(lambda x:(x[3],detecterror(x[3].lower())))

	#filter line that contain word 'error'
	errordata = splitdata.filter(lambda x:detecterror(x[4].lower()))
	#map the message. ex:('Error ...',1)
	tupledata = errordata.map(lambda x:(x[4],1))
	#count the error based on message
	countdata = tupledata.reduceByKey(lambda x,y: x+y)
	#sort by error count number
	collectdata = countdata.sortBy(lambda x:x[1],False).map(lambda x:(x[1],str(x[0]))).collect()
	#collectdata = splitdata.sortBy(lambda x:len(x)).collect()
	i = 0
	print('  + '+sys.argv[1]+':')
	for s in collectdata:
		if i < 5:
			print('    - '+str(s))
		else:
			break
		i=i+1

	sc.stop()
