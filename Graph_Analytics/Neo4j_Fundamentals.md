# Getting Started with Graph Database and Neo4j

![Neo4j icon](http://neo4j-org-dev.herokuapp.com/)

## Neo4j

* **Neo4j** is a **Graph Database**
* Neo4j's data model is a **Graph**, in particular a **Property Graph**
* **Cypher** is Neo4j's graph query language (SQL for graphs!)
* Cypher is a declarative query language
* You describe what you you are interested in, not how it is acquired.
* Cypher is meant to be very readable and expressive


## Graph Database

* A **Graph Database** stores data in a **Graph**, the most generic of data structures, capable of elegantly representing any kind of data in a highly accessible way.
* The records in a graph database are called **Nodes**.
* Nodes are connected through typed, directed **Relationships**.
* Each single Node and Relationship can have named attributes referred to as **Properties**.
* A **Label** is a name that organises nodes into **groups**.
* A **Property-Graph** consists of labeled nodes and relationships each with properties.
* Nodes are just data records, usually used for an entity (label). Besides properties they also contain their relationships to other nodes.
* Relationships connect two nodes. They are also an explicit data record in the graph database. Think of them as containing shared information between two entities (direction, type, properties) and representing the connection to both nodes.
* Properties are simple key:value pairs. There is no schema, just structure.

## Describing a Graph: an Introduction to Cypher

Let's see how we describe elements of a graph using the basic syntax of Cypher, Neo4j's query language.



**Nodes**

`(a)` actors

`(m)` movies

`( )` some anonymous node


**Relationships**


`-[r]->` a relationship referred to as "r"

`(a)-[r]->(m)` actors having a relationship referred to as "r" to movies

`-[:ACTED_IN]->` the relationship type is ACTED_IN

`(a)-[:ACTED_IN]->(m)` actors that ACTED_IN some movie

`(d)-[:DIRECTED]->(m)` directors that DIRECTED some movie


**Properties**
*Nodes with Properties*

`(m {title:"The Matrix"})` Movie with a title property

`(a {name:"Keanu Reeves",born:1964})` Actor with name and born property

*Relationship with Properties*

`(a)-[:ACTED_IN {roles:["Neo"]}]->(m)` Relationship ACTED_IN with roles property (an array of character names)


**Labels**

`(a:Person)` a Person

`(a:Person {name:"Keanu Reeves"})` a Person with properties

`(a:Person)-[:ACTED_IN]->(m:Movie)` a Person that ACTED_IN some movie


