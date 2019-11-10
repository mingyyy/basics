All Interview Questions
-----------------------

The interview questions are roughly structured like the sections in the
\"Basic data engineering skills\" part. This makes it easier to navigate
this document. I still need to sort them accordingly.

### SQL DBs

-   What are windowing functions?

According to PostgreSQL v.9 documentation, an SQL Window function performs a calculation across a set of table rows that are somehow related to the current row, in a way similar to aggregate functions.
A window function call always contains an OVER clause.

-   What is a stored procedure?

-   Why would you use them?

-   What are atomic attributes?

-   Explain ACID props of a database

*Atomicity* means that either the entire transaction takes place at once or doesn’t happen at all. There is no midway i.e. transactions do not occur partially. 
Each transaction is considered as one unit and either runs to completion or is not executed at all. It involves following two operations.

*Consistency* means that integrity constraints must be maintained so that the database is consistent before and after the transaction. It refers to correctness of a database. 

*Isolation* ensures that multiple transactions can occur concurrently without leading to inconsistency of database state. 
Transactions occur independently without interference. 
Changes occurring in a particular transaction will not be visible to any other transaction until that particular change in that transaction is written to memory or has been committed. 
This property ensures that the execution of transactions concurrently will result in a state that is equivalent to a state achieved these were executed serially in some order.

*Durability* ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if system failure occurs. 
These updates now become permanent and are stored in a non-volatile memory. The effects of the transaction, thus, are never lost.

-   How to optimize queries?

-   What are the different types of JOIN (CROSS, INNER, OUTER)?

-   What is the difference between Clustered Index and Non-Clustered
    Index - with examples?
    
*Clustered Index*

Only one per table
Faster to read than non clustered as data is physically stored in index order

In an RDBMS, usually, the primary key allows you to create a clustered index based on that specific column.
 
*Non Clustered Index*

Can be used many times per table
Quicker for insert and update operations than a clustered index
Both types of index will improve performance when select data with fields that use the index but will slow down update and insert operations.

Because of the slower insert and update clustered indexes should be set on a field that is normally incremental ie Id or Timestamp.

### The Cloud

-   What is serverless?

-   What is the difference between IaaS, PaaS and SaaS?

-   How do you move from the ingest layer to the Cosumption layer? (In
    Serverless)

-   What is edge computing?

-   What is the difference between cloud and edge and on-premise?

### Linux

-   What is crontab?

### Big Data

-   What are the 4 V's?

-   Which one is most important?

### Kafka

-   What is a topic?

-   How to ensure FIFO?

-   How do you know if all messages in a topic have been fully consumed?

-   What are brokers?

-   What are consumergroups?

-   What is a producer?

### Coding

-   What is the difference between an object and a class?

-   Explain immutability

-   What are AWS Lambda functions and why would you use them?

-   Difference between library, framework and package

-   How to reverse a linked list

-   Difference between args and kwargs

-   Difference between OOP and functional programming

### NoSQL DBs

-   What is a key-value (rowstore) store?

-   What is a columnstore?

-   Diff between Row and col.store

-   What is a document store?

-   Difference between Redshift and Snowflake

### Hadoop

-   What file formats can you use in Hadoop?

-   What is the difference between a name and a datanode?

-   What is HDFS?

-   What is the purpose of YARN?

### Lambda Architecture

-   What is streaming and batching?

-   What is the upside of streaming vs batching?

-   What is the difference between lambda and kappa architecture?

-   Can you sync the batch and streaming layer and if yes how?

### Python

-   Difference between list tuples and dictionary

### Data Warehouse & Data Lake

-   What is a data lake?

-   What is a data warehouse?

-   Are there data lake warehouses?

-   Two data lakes within single warehouse?

-   What is a data mart?

-   What is a slow changing dimension (types)?

-   What is a surrogate key and why use them?

### APIs (REST)

-   What does REST mean?

-   What is idempotency?

-   What are common REST API frameworks (Jersey and Spring)?

### Apache Spark

-   What is an RDD?

-   What is a dataframe?

-   What is a dataset?

-   How is a dataset typesafe?

-   What is Parquet?

-   What is Avro?

-   Difference between Parquet and Avro

-   Tumbling Windows vs. Sliding Windows

-   Difference between batch and stream processing

-   What are microbatches?

### MapReduce

-   What is a use case of mapreduce?

-   Write a pseudo code for wordcount

-   What is a combiner?

### Docker & Kubernetes

-   What is a container?

-   Difference between Docker Container and a Virtual PC

-   What is the easiest way to learn kubernetes fast?

### Data Pipelines

-   What is an example of a serverless pipeline?

-   What is the difference between at most once vs at least once vs
    exactly once?

-   What systems provide transactions?

-   What is a ETL pipeline?

### Airflow

-   What is a DAG (in context of airflow/luigi)?

-   What are hooks/is a hook?

-   What are operators?

-   How to branch?

### DataVisualization

-   What is a BI tool?

### Security/Privacy

-   What is Kerberos?

-   What is a firewall?

-   What is GDPR?

-   What is anonymization?

### Distributed Systems

-   How clusters reach consensus (the answer was using consensus
    protocols like Paxos or Raft). Good I didnt have to explain paxos

-   What is the cap theorem / explain it (What factors should be
    considered when choosing a DB?)

-   How to choose right storage for different data consumers? It's
    always a tricky question

### Apache Flink

-   What is Flink used for?

-   Flink vs Spark?

### GitHub

-   What are branches?

-   What are commits?

-   What's a pull request?

### Dev/Ops

-   What is continuous integration?

-   What is continuous deployment?

-   Difference CI/CD

### Development / Agile

-   What is Scrum?

-   What is OKR?

-   What is Jira and what is it used for?