# Udacity Data Streaming Nanodegree
## Spark Streaming

This project includes all the files required in the description of the task.

### Step 1

Screenshot of the output console for the Kafka consumer:

![Console output 1](/media/console.png)

### Step 2

Screenshot of console when executing spark streaming application:

![Console output 2](/media/job.png)


### Step 3

Screenshot of Spark UI for measuring time per task

![Console output 3](/media/time.png)

The next parameters have been modified within the Spark Session:

![Console output 4](/media/parameters.PNG)


The results of the comparison are presented in the next graph, that represents the seconds required per task for each configuration:

![Console output 4](/media/comparison.PNG)

The combinations that present lower times are:
* 1GB 1core
* 2GB 2cores
* 2GB 3cores