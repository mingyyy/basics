All Interview Questions
-----------------------

The interview questions are roughly structured like the sections in the
\"Basic data engineering skills\" part. This makes it easier to navigate
this document. I still need to sort them accordingly.

### SQL DBs

-   *What are windowing functions?*

According to PostgreSQL v.9 documentation, an SQL Window function performs a calculation across a set of table rows that are somehow related to the current row, in a way similar to aggregate functions.
A window function call always contains an OVER clause.

-   *What is a stored procedure?*

-   Why would you use them?

-   What are atomic attributes?

-   *Explain ACID props of a database*

*Atomicity* means that either the entire transaction takes place at once or doesn’t happen at all. There is no midway i.e. transactions do not occur partially. 
Each transaction is considered as one unit and either runs to completion or is not executed at all. It involves following two operations.

*Consistency* means that integrity constraints must be maintained so that the database is consistent before and after the transaction. It refers to correctness of a database. 

*Isolation* ensures that multiple transactions can occur concurrently without leading to inconsistency of database state. 
Transactions occur independently without interference. 
Changes occurring in a particular transaction will not be visible to any other transaction until that particular change in that transaction is written to memory or has been committed. 
This property ensures that the execution of transactions concurrently will result in a state that is equivalent to a state achieved these were executed serially in some order.

*Durability* ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if system failure occurs. 
These updates now become permanent and are stored in a non-volatile memory. The effects of the transaction, thus, are never lost.

-   *How to optimize queries?*

You can use `Explain Analyze` to study the details of each query. 
Some best practice you should follow:

1. Index all the predicates in JOIN, WHERE, ORDER BY and GROUP BY clauses. It is recommended that all predicate columns be indexed. The exception being where column data has very low cardinality.

2. Avoid using functions in predicates.
The index is not used by the database if there is a function on the column.
For example, `SELECT * FROM TABLE1 WHERE UPPER(COL1)='ABC'`

3. Avoid using wildcard (`%`) at the beginning of a predicate.
The predicate LIKE `%abc` causes full table scan. This is a known performance limitation in all databases.

4. Avoid unnecessary columns in SELECT clause. e.g. `SELECT *`
Specify the columns in the SELECT clause instead of using SELECT *.

5. Use inner join, instead of outer join if possible.
The outer join should only be used if it is necessary. 
Using outer join limits the database optimization options which typically results in slower SQL execution.

6. DISTINCT and UNION should be used only if it is necessary.
DISTINCT and UNION operators cause sorting, which slows down the SQL execution. 
Use UNION ALL instead of UNION, if possible, as it is much more efficient.

7. The ORDER BY clause is mandatory in SQL if the sorted result set is expected. Sorting is expensive.

-   *What are the different types of JOIN (CROSS, INNER, OUTER)?*

-   *What is the difference between Clustered Index and Non-Clustered
    Index - with examples?*
  
    
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

REST is acronym for REpresentational State Transfer. 
It is architectural style for distributed hypermedia systems and was first presented by Roy Fielding in 2000

Guiding Principles of REST

Client–server – By separating the user interface concerns from the data storage concerns, we improve the portability of the user interface across multiple platforms and improve scalability by simplifying the server components.
Stateless – Each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.
Cacheable – Cache constraints require that the data within a response to a request be implicitly or explicitly labeled as cacheable or non-cacheable. If a response is cacheable, then a client cache is given the right to reuse that response data for later, equivalent requests.
Uniform interface – By applying the software engineering principle of generality to the component interface, the overall system architecture is simplified and the visibility of interactions is improved. In order to obtain a uniform interface, multiple architectural constraints are needed to guide the behavior of components. REST is defined by four interface constraints: identification of resources; manipulation of resources through representations; self-descriptive messages; and, hypermedia as the engine of application state.
Layered system – The layered system style allows an architecture to be composed of hierarchical layers by constraining component behavior such that each component cannot “see” beyond the immediate layer with which they are interacting.
Code on demand (optional) – REST allows client functionality to be extended by downloading and executing code in the form of applets or scripts. This simplifies clients by reducing the number of features required to be pre-implemented.

-   What is idempotency?

-   What are common REST API frameworks (Jersey and Spring)?

### Apache Spark

-   What is an RDD?

RDD (Resilient Distributed Dataset) is the fundamental data structure of Apache Spark which are an immutable collection of objects which computes on the different node of the cluster. 
Each and every dataset in Spark RDD is logically partitioned across many servers so that they can be computed on different nodes of the cluster.

-   What is a dataframe?

A DataFrame is a distributed collection of data organized into named columns. 
It is conceptually equal to a table in a relational database.

-   What is a dataset?

It is an extension of DataFrame API that provides the functionality of type-safe, 
object-oriented programming interface of the RDD API and performance benefits of the Catalyst query optimizer and off heap storage mechanism of a DataFrame API.
Only Scala and Java API supported.

-   How is a dataset typesafe?

-   What is Parquet?

columnar file format, fast read (slower writing), compatible with Spark
compressible well

-   What is Avro?
row file format, 

-   Difference between Parquet and Avro

-   Tumbling Windows vs. Sliding Windows

-   Difference between batch and stream processing

-   What are microbatches?


### MapReduce

-   What is a use case of mapReduce?

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
Directed Acyclic Graph

-   What are hooks/is a hook?

-   What are operators?

-   How to branch?

### DataVisualization

-   What is a BI tool?
Business Intelligent tool

### Security/Privacy

-   What is Kerberos?

-   What is a firewall?

-   What is GDPR?
Guideline data protection rules?

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