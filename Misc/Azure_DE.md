## Azure for the Data Engineer

#### Some tasks Azure data engineer:

- Design and develop data storage and data processing solutions for the enterprise.
- Set up and deploy cloud-based data services such as blob services, databases, and analytics.
- Secure the platform and the stored data. Make sure only the necessary users can access the data.
- Ensure business continuity in uncommon conditions by using techniques for high availability and disaster recovery.
- Monitor to ensure that the systems run properly and are cost-effective.

#### How a data engineer differs from a database administrator

The data engineer's role overlaps with the role of the database administrator (DBA) in terms of broad tasks. 
The differences are in scope and focus. Data engineers work with more than just databases, 
and they focus on cloud implementations rather than on-premises servers.

#### Extract, Transform, and Load (ETL) process

- **Extract**

Define the data source: Identify source details such as the resource group, subscription, 
and identity information such as a key or secret.

Define the data: Identify the data to be extracted. Define data by using a database query, a set of files, 
or an Azure Blob storage name for blob storage.

- **Transform**

Define the data transformation: Data transformation operations can include splitting, 
combining, deriving, adding, removing, or pivoting columns. Map fields between the data source and the data destination. 
You might also need to aggregate or merge data.

- **Load**

Define the destination: During a load, many Azure destinations can accept data formatted as a 
JavaScript Object Notation (JSON), file, or blob. You might need to write code to interact with application APIs.
Azure Data Factory offers built-in support for Azure Functions. You'll also find support for many programming languages, 
including Node.js, .NET, Python, and Java. 
Although Extensible Markup Language (XML) was common in the past, 
most systems have migrated to JSON because of its flexibility as a semistructured data type.

Start the job: Test the ETL job in a development or test environment. 
Then migrate the job to a production environment to load the production system.

Monitor the job: ETL operations can involve many complex processes. 
Set up a proactive and reactive monitoring system to provide information when things go wrong. 
Set up logging according to the technology that will use it.

#### Five phases of data engineering project design
1. source
2. inject
3. prepare
4. analyze
5. consume
