## Section Data Modeling (AEiE0703)

## 📖 1. Introduction
Data modeling and database design are critical for building scalable, reliable software systems. This section covers the conceptual models (like ER diagrams) and theoretical foundations (like normalization) required to design relational databases correctly. This is heavily tested in the NEC exams.

## 2. Basic Concept: Abstraction, Schema, and Instances

### Data Abstraction
Database systems hide complex implementation details from users using three levels of abstraction:
1. **Physical Level**: Describes how data is actually stored.
2. **Logical Level**: Describes what data is stored and relationships among data.
3. **View Level**: Describes only part of the entire database relevant to a specific user.

### Data Independence
- **Logical Data Independence**: Ability to modify the logical schema without altering the view schema or applications.
- **Physical Data Independence**: Ability to modify the physical schema without altering the logical schema.

### Schema and Instances
- **Schema**: The overall design of the database (rarely changes).
- **Instance**: The actual content (data) stored in the database at a specific moment in time (changes frequently).

## 3. Entity-Relationship (E-R) Model

> [!NOTE] Definition
> **E-R Model**: A high-level conceptual data model used to define the data elements and relationships for a specified system.

### Strong and Weak Entity Sets
- **Strong Entity Set**: Has a primary key that uniquely identifies its entities.
- **Weak Entity Set**: Lacks a primary key of its own. It depends on an identifying (strong) entity set and uses a partial key (discriminator).

### Attributes and Keys
- **Attributes**: Properties describing an entity (e.g., Simple, Composite, Single-valued, Multi-valued, Derived).
- **Super Key**: A set of one or more attributes that uniquely identifies an entity.
- **Candidate Key**: A minimal super key.
- **Primary Key**: A candidate key chosen by the database designer.
- **Foreign Key**: An attribute in one table that uniquely identifies a row of another table.

### E-R Diagram Components
- **Rectangles**: Entity sets.
- **Ellipses**: Attributes. (Dashed ellipses for derived attributes, double ellipses for multi-valued).
- **Diamonds**: Relationships.
- **Double Rectangles**: Weak entity sets.

## 4. Normalization and Normal Forms
Normalization organizes data to reduce redundancy and improve data integrity.

### Functional Dependencies (FD)
If $A \rightarrow B$, then attribute $B$ is functionally dependent on attribute $A$. For any two tuples, if their $A$ values are equal, their $B$ values must also be equal.

### Different Normal Forms
1. **First Normal Form (1NF)**: All attributes contain atomic (indivisible) values. No multi-valued attributes.
2. **Second Normal Form (2NF)**: It is in 1NF, and all non-key attributes are fully functionally dependent on the primary key (no partial dependencies).
3. **Third Normal Form (3NF)**: It is in 2NF, and there is no transitive dependency of non-key attributes on the primary key.
4. **Boyce-Codd Normal Form (BCNF)**: A stricter version of 3NF. For every non-trivial functional dependency $X \rightarrow Y$, $X$ must be a super key.

## 5. Constraints and Relations

### Integrity and Domain Constraints
- **Domain Constraints**: Specifies the set of valid values for an attribute (e.g., Age must be an integer > 0).
- **Integrity Constraints**: Rules applied to enforce data consistency (Entity Integrity: PK cannot be null, Referential Integrity: FK must match a valid PK).

### Relations (Joined, Derived)
- Relational algebra forms the basis for SQL.
- **Joins**: Natural join, outer joins (left, right, full).
- **Derived Relations**: Creating temporary result sets or views from base relations.

## 6. SQL Commands: DDL, DML, and Views

### Data Definition Language (DDL)
Defines schema and structure.
```sql
CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Salary DECIMAL(10,2)
);
ALTER TABLE Employee ADD DepartmentId INT;
DROP TABLE Employee;
```

### Data Manipulation Language (DML)
Manipulates the actual data.
```sql
INSERT INTO Employee (ID, Name) VALUES (1, 'John Doe');
UPDATE Employee SET Salary = 50000 WHERE ID = 1;
DELETE FROM Employee WHERE ID = 1;
SELECT * FROM Employee;
```

### Views
A virtual table based on the result-set of an SQL statement.
```sql
CREATE VIEW HighEarners AS
SELECT Name, Salary FROM Employee WHERE Salary > 80000;
```

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> BCNF is stricter than 3NF. A relation in BCNF is always in 3NF, but a relation in 3NF is not necessarily in BCNF.

> [!TIP]
> When asked about ER Diagram conversions to tables: An M:N relationship always requires a separate table bridging the two entity tables.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - Normalization progression: 1NF (Atomic) -> 2NF (No partial dependency) -> 3NF (No transitive dependency) -> BCNF (LHS is superkey).
> - Strong Entity = Primary Key; Weak Entity = Identifying Relationship + Partial Key.

## ✏️ Practice Problems
1. Define a schema $R(A, B, C, D)$ with FDs: $A \rightarrow B$, $B \rightarrow C$. Determine the highest normal form of $R$.
   - *Sketch:* The key is $A$ (or part of it). $B \rightarrow C$ is a transitive dependency. Thus, it's not in 3NF. If $A$ is the sole key, it's in 2NF.
2. Differentiate between logical and physical data independence.
3. Draw an E-R diagram for a hospital system where a Doctor treats many Patients, but a Patient can also be treated by multiple Doctors. Include a weak entity 'Medical History' dependent on Patient.
</Section 7.3: Data Modeling (AEiE0703)>
