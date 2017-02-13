#Big-Data

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
