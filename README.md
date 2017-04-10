<<<<<<< HEAD
### Big-Data

##Assymetric Friend Recommendation Implementation using Hadoop MapReduce. 

#Run: 

Import to Eclipse and run there. 

or 

open terminal -- hadoop jar <path to Maven generated jar> <path to class> <input file> <temp folder> <output folder>
=======
#Big-Data
--------------------------------

##Log Analysis

###Files Contained: 
README.txt
log_analyzer script (Starts Spark job - Spark Submit)
q1 to q9.py 
Iliad and Odyssey log files 
Iliad and Odyssey anonymous-11 log files

###Run: 
  Assuming proper hadoop and Spark installation 
Copy log files into hadoop file system with $ hadoop dfs -copyFromLocal <local folder> <hdfs location>
                                            ie: hadoop dfs -copyFromLocal /home/Srikanth/iliad /hadoop/iliad

Copy the log_analysis (contains log_analyzer script + q1-9.py) folder into home directory. 

Open Terminal -- 

cd in log_analysis folder
$ ./log_analyzer -q # <log location in dfs> <log location in dfs>
ie : $ ./log_analyzer -q 1 /hadoop/iliad /hadoop/odyssey
//only difference is the # between runs

//Results appear in terminal and see dfs contents for anonymized-11 (iliad/odyssey)

Incase you need to delete from dfs (for example to rerun q9).  Run 
$hadoop dfs -rmr <file in dfs to remove>
ie: $hadoop dfs -rmr /hadoop/iliad-anonymized-10
ie: $hadoop dfs -rmr /hadoop/odyssey-anonymized-10

----------------------------------------------------------------------------

##Assymetric Friend Recommendation Implementation using Hadoop MapReduce. 

###Files Contained: 

README.txt
WhoToFollow.java
pom.xml
mapreduce-0.0.1-SNAPSHOT.jar
test.txt


###Run: 
  Assuming proper Hadoop installation
Import to Eclipse and run there by importing external jars to project folder. 

or 

open terminal -- 

$ javac WhoToFollow.java

//exclude ">" & current input file is test.txt

$ hadoop jar >path to + Maven generated jar> >path to  + class> >input file> >temp folder> -output folder>

####ASSUMING RUN FROM HOME DIRECTORY
ie: hadoop jar mapreduce-0.0.1-SNAPSHOT.jar com.srikanth.mapreduce.WhoToFollow test.txt temp output 

//intermediary results will be put into temp folder 

//final results will be put into output folder
>>>>>>> 8f6179ac4bc692ac39938685f5840e1ac6049f01
