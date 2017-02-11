


import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.function.Predicate;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


/**
 * Whom to Follow Implementation using People you may know.
 * @author srikanth
 *
 */
public class Pymk3 {


    //Mapper-1
    public static class Mapper1 extends Mapper<Object, Text, IntWritable, IntWritable> {

        public void map(Object key, Text values, Context context) throws IOException, InterruptedException {
            StringTokenizer st = new StringTokenizer(values.toString());
            IntWritable user = new IntWritable(Integer.parseInt(st.nextToken()));

            // Go through the list of all followers of user 'user' and emit (follower,user)
            IntWritable follower = new IntWritable();
            while (st.hasMoreTokens()) {
                Integer friend = Integer.parseInt(st.nextToken());
                follower.set(friend);
                context.write(follower, user);
            }
        }
    }


    //(Identity) Reducer-1
    public static class Reducer1 extends Reducer<IntWritable, IntWritable, IntWritable, Text> {

        // The reduce method
        public void reduce(IntWritable key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            IntWritable user = key;

            String valuesString = "";
            while (values.iterator().hasNext()) {
                int value = values.iterator().next().get();
                valuesString+=Integer.valueOf(value)+"\t";
            }
            Text result = new Text(valuesString);
            context.write(user, result);
        }
    }

    //Mapper-2
    public static class Mapper2 extends Mapper<Object, Text, IntWritable, IntWritable> {

        public void map(Object key, Text values, Context context) throws IOException, InterruptedException {
            StringTokenizer st = new StringTokenizer(values.toString());
            IntWritable user = new IntWritable(-Integer.parseInt(st.nextToken()));

            ArrayList<Integer> friends = new ArrayList<Integer>();

            IntWritable friend1 = new IntWritable();
            while (st.hasMoreTokens()) {
                Integer friend = Integer.parseInt(st.nextToken());
                friend1.set(friend);
                context.write(friend1, user);
                friends.add(friend);
            }

            ArrayList<Integer> seenFriends = new ArrayList<Integer>();
            // The element in the pairs that will be emitted.
            IntWritable friend2 = new IntWritable();
            for (Integer friend : friends) {
                friend1.set(friend);
                for (Integer seenFriend : seenFriends) {
                    friend2.set(seenFriend);
                    context.write(friend1, friend2);
                    context.write(friend2, friend1);
                }
                seenFriends.add(friend1.get());
            }
        }
    }

}