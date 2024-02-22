# Homework

The [linked colab notebook](https://colab.research.google.com/drive/1Te-AT0lfh0GpChg1Rbd0ByEKOHYtWXfm#scrollTo=wLF4iXf-NR7t&forceEdit=true&sandboxMode=true) offers a few exercises to practice what you learned today.


#### Question 1: What is the sum of the outputs of the generator for limit = 5?
- **A**: 10.23433234744176
- **B**: 7.892332347441762
- **C: 8.382332347441762 answer**
- **D**: 9.123332347441762

#### Question 2: What is the 13th number yielded by the generator?
- **A**: 4.236551275463989
- **B: 3.605551275463989 answer**
- **C**: 2.345551275463989
- **D**: 5.678551275463989

##### code for Q1,Q2
```
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13
generator = square_root_generator(limit)
sum = 0 
for x,sqrt_value in enumerate(generator):
    sum = sum + sqrt_value
    print("n : ",x)
    print(sqrt_value)
    print("sum", sum)
```


#### Question 3: Append the 2 generators. After correctly appending the data, calculate the sum of all ages of people.
- **A: 353 answer**
- **B**: 365
- **C**: 378
- **D**: 390

#### Question 4: Merge the 2 generators using the ID column. Calculate the sum of ages of all the people loaded as described above.
- **A**: 205
- **B**: 213
- **C**: 221
- **D: 230 answer**

##### code for Q3,Q4
```
import dlt 
import duckdb

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


person_pipeline = dlt.pipeline(destination='duckdb', dataset_name='person_generator')

conn.sql("DELETE FROM person")
info = person_pipeline.run(people_1(),
										table_name="person",
										write_disposition="merge",
                    primary_key = "id")
print(info)

# connect to duckDB 
print("pipeline name : ",person_pipeline.pipeline_name)
conn = duckdb.connect(f"{person_pipeline.pipeline_name}.duckdb")
conn.sql(f"SET search_path = '{person_pipeline.dataset_name}'")

print('Loaded tables: ')
display(conn.sql("show tables"))
print("\n\n\n Person table before update :")

person = conn.sql("SELECT * FROM person ORDER BY id").df()
display(person)


#append from person2 
info = person_pipeline.run(people_2(),
										table_name="person",
										write_disposition="append",)
print(info)
person = conn.sql("SELECT * FROM person ORDER BY id").df()
display(person)
print(conn.sql("SELECT SUM(age) FROM person"))
print(conn.sql("SELECT SUM(age) FROM person").df())


#merge from person2
info = person_pipeline.run(people_2(),
										table_name="person",
										write_disposition="merge",
                    primary_key = "id")
print(info)

person = conn.sql("SELECT * FROM person ORDER BY id").df()
display(person)
print(type(conn.sql("SELECT SUM(age) FROM person")))
print(conn.sql("SELECT SUM(age) FROM person").df())
```
Submit the solution here: https://courses.datatalks.club/de-zoomcamp-2024/homework/workshop1

--- 
# Next steps