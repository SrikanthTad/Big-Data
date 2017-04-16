
### Big-Data

--------------------------------
Log Analysis

Run:

{Assuming proper hadoop and Spark installation} 

1. Copy log files into hadoop file system with $ hadoop dfs -copyFromLocal <local file locaiton> <destination dfs>

(ie: hadoop dfs -copyFromLocal /home/Srikanth/iliad /hadoop/iliad)

2. Copy the log_analysis (contains log_analyzer script + q1 …. q9.py) folder into home directory.

3. Open Terminal --
cd in log_analysis folder and run $ ./log_analyzer -q # <iliad dfs location> <odyssey dfs location> 

(ie : $ ./log_analyzer -q 1 /hadoop/iliad /hadoop/odyssey) //only difference is the # between runs

//Results appear in terminal and see dfs contents for anonymized-11 (iliad/odyssey)

NOTE: Incase you need to delete from dfs (for example to rerun q9). Run $hadoop dfs -rmr <dfs path to file>

(ie: $hadoop dfs -rmr /hadoop/iliad-anonymized-10) 
(ie: $hadoop dfs -rmr /hadoop/odyssey-anonymized-10)


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




