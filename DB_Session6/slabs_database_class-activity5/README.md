Author Lemart
An entity is a real world object about where data is stored. Example: book is an entity
A relationship decribes how two entities are connected, eample: a Customer places an Order, the relationship is places.
An attribute is a property or a characteristic of an entity, example: online bookstore. For the book entity
* BookID
* Title
* Author
* Price
Title and Price are the attributes of the book entity.

2. Data Module Levels
----------------------------------------------------------------------------------------------------------------------------------
-Conceptual Data Model-------------------------------------+------Physical Data Model--------------------------------------------+
-High-level representation of the business requirements.---+------Detailed implementation of the database in a DBMS.-------------+
-Created by business analysts and database designers.------+------Created by database administrs and developers.-----------------+
-Focuses on entities, relationships, and business rules.---+------Focuses on tables, columns, data types, keys, and constraints.-+
-Independent of any database software.---------------------+------Specific to a database system such as PostgreSQL.--------------+
----------------------------------------------------------------------------------------------------------------------------------
ER Mapping
Customer Entity

Attributes:

CustomerID (Primary Key)
FirstName
LastName
Email
PhoneNumber
Order Entity

Attributes:

OrderID (Primary Key)
OrderDate
TotalAmount
CustomerID (Foreign Key)
Relationship
One Customer can place many Orders.
Each Order belongs to one Customer.

Relationship:
Customer (1) --------- (M) Order
        places
