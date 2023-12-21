# Big-Data-Final-Project-News-Sentiment-Analysis-with-Spark

# Zookeeper and Kafka Installation Guide on GCP

This guide provides step-by-step instructions for installing and configuring Zookeeper and Kafka on Google Cloud Platform (GCP), along with setting up HDFS paths and installing Python libraries for data handling and analysis.

## Zookeeper Installation Guide

### Step 1: Downloading Zookeeper
```bash
wget https://archive.apache.org/dist/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz
```

### Step 2: Extracting the Package
```bash
tar -xzf zookeeper-3.4.14.tar.gz
```

### Step 3: Cleaning Up
```bash
rm zookeeper-3.4.14.tar.gz
```

### Step 4: Configuring Zookeeper
```bash
cd zookeeper-3.4.14/conf/
cp zoo_sample.cfg zoo.cfg
vi zoo.cfg
# Append server.0=127.0.0.1:2888:3888 and modify dataDir
```

### Step 5: Preparing Data Directory
```bash
sudo mkdir /var/zookeeper
sudo chown [YOUR_GCP_USERNAME]:[YOUR_GCP_USERNAME] /var/zookeeper
```

### Step 6: Setting Up 'myid' File
```bash
vi /var/zookeeper/myid
# Add '0' in the file
```

### Step 7: Starting Zookeeper
```bash
# From Zookeeper directory
bin/zkServer.sh start
# Or from Home Directory
zookeeper-3.4.14/bin/zkServer.sh start
```

## Kafka Installation Guide

### Step 1: Begin in the Home Directory
```bash
cd
```

### Step 2: Downloading Kafka
```bash
wget https://packages.confluent.io/archive/4.1/confluent-4.1.4-2.11.tar.gz
```

### Step 3: Extracting Kafka
```bash
tar -xzf confluent-4.1.4-2.11.tar.gz
```

### Step 4: Removing the Downloaded Archive
```bash
rm confluent-4.1.4-2.11.tar.gz
```

### Step 5: Configuring Kafka
```bash
cd confluent-4.1.4/
vi etc/kafka/zookeeper.properties
# Change dataDir to /var/zookeeper
```

### Step 6: Starting the Kafka Server
```bash
bin/kafka-server-start etc/kafka/server.properties
# For background execution
nohup bin/kafka-server-start etc/kafka/server.properties > /dev/null 2>&1 &
```

## Setting Up HDFS Path and Installing Python Libraries in GCP

### Creating Directories in HDFS for Data Storage
```bash
hadoop fs -mkdir /BigData/
hadoop fs -mkdir /BigData/FinalProject/
```

### Installing Python Libraries in GCP
```bash
pip install newsapi newsapi-python kafka-python hdfs
```

## Uploading Python Scripts to GCP

- Navigate to GCP interface and upload 'producer.py' and 'consumer.py'.
- Edit 'producer.py' to include your API key and desired keywords.
- Edit 'consumer.py' to include your GCP username.

## Final Steps for Running Your Project

### Running Zookeeper and Kafka
Start Zookeeper and Kafka as mentioned in the installation guide.

### Running the Producer and Consumer Scripts
```bash
# In separate terminal connections
python producer.py
python consumer.py
```

### Verifying Data Storage in HDFS
```bash
hadoop fs -ls /BigData/FinalProject/
# To view file contents
hdfs dfs -cat /BigData/FinalProject/news_data.txt
```

## Data Analysis and Model Prediction using Spark

### Starting Spark
```bash
spark-shell --master yarn
```

### Data Analysis Steps
- Import libraries and read data from HDFS.
- Perform various queries and data manipulations as per your project needs.

### Training ML Model
- Utilize Spark ML to train and evaluate models based on your dataset.

