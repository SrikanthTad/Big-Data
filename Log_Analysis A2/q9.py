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

def detectalluser(lw):
        if 'user' in lw:
                i = lw.index('user')
                return str(lw[i+1]).translate(None,".,?!@()*&<>''[]{}")
        else:
                return 'null'

def changeuser(tp,idx):
	for user in idx:
		if user[0] in tp:
			tp = tp.replace(user[0],user[1])
	return tp

if __name__ == "__main__":
	#np.set_printoptions(threshold='nan')
	if len(sys.argv) !=2:
		print("Input format is not correct")
	sc = SparkContext(appName="Q9")
	raw = sc.textFile(sys.argv[1])

	splitdata = raw.map(lambda x:(x,x.split()))
	#detect user
	detectdata = splitdata.map(lambda x:(x[0],detectuser(x[1])))
	userdata = detectdata.filter(lambda x:x[1] != 'null')
	#sort user by ascending sort and index user using zipWithIndex
	#ex: ('achille','user-0')
	indexdata = userdata.map(lambda x:str(x[1])).distinct().sortBy(lambda x:x).zipWithIndex().map(lambda x:(x[0],'user-'+str(x[1]))).repartition(1)
	# store index using broadcast so all of machine can access this value
	indexbc = sc.broadcast(indexdata.collect())
	#change user to anonym
	anonimdata = raw.map(lambda x:changeuser(x,indexbc.value))

	collectdata = indexdata.collect()

	print('  + '+sys.argv[1])
	print('  User name mapping: '+str(collectdata))
	# save data to hdfs
	anonimdata.saveAsTextFile(sys.argv[1]+'-anonymized-10')
	print('  Anonymized files: '+sys.argv[1]+'-anonymized-10')
	#collectdata2= joindata.collect()
	#print(sys.argv[1]+': '+str(collectdata))
	#print()
	#print(collectdata2)	
	sc.stop()
