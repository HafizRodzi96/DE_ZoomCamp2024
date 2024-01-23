## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--delete`
- `--rc`
- `--rmc`
- `--rm`

### Hafiz Answer:
`--rm Automatically remove the container when it exits `

## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- 0.42.0
- 1.0.0
- 23.0.1
- 58.1.0

### Hafiz Answer:
Command used
`docker run -it --entrypoint=bash python:3.9` \
then `pip list`
 answer is ``` wheel      0.42.0 ```



# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612
- 15859
- 89009

### Hafiz Answer:
`15612`
```
select count(*) from yellow_taxi_data
where date(lpep_pickup_datetime) = TO_DATE('2019-09-18','YYYY-MM-DD') and date(lpep_dropoff_datetime) = TO_DATE('2019-09-18','YYYY-MM-DD')

```

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.


- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

### Hafiz Answer:
`2019-09-26`
```
SELECT date(lpep_pickup_datetime), trip_distance from yellow_taxi_data
where trip_distance = (select max(trip_distance) from yellow_taxi_data) 
```
## Question 5. The number of passengers

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
 
- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"

### Hafiz Answer:
`"Brooklyn" "Manhattan" "Queens"`
```
create table joined_table as (
select "PULocationID", total_amount, "LocationID", "Borough" from yellow_taxi_data 
Left join zone_data ON "PULocationID" ="LocationID" );

select sum(total_amount) as total,"Borough" from joined_table group by "Borough" 
having sum(total_amount) > 50000 
ORDER BY total DESC;

```

- 2619378 Brooklyn 
- 2460386  Queens 
- 2427880 Manhattan 
- 818158 Bronx 

## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza

### Hafiz Answer:

`JFK Airport`

```
create table joined_table as (
select "PULocationID", "DOLocationID" ,total_amount, "LocationID", "Borough",tip_amount,"Zone"  from yellow_taxi_data 
Left join zone_data ON "PULocationID" ="LocationID")

select * from joined_table 
where "Zone" = 'Astoria' 
order by tip_amount desc

```


## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.

### Hafiz Answer:
```
  # google_storage_bucket.Homework-Bucket-testingTerra will be created
  + resource "google_storage_bucket" "Homework-Bucket-testingTerra" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "unified-surfer-405214-testing_homework"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_storage_bucket.Homework-Bucket-testingTerra: Creating...
google_storage_bucket.Homework-Bucket-testingTerra: Creation complete after 2s [id=unified-surfer-405214-testing_homework]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

## Submitting the solutions

* Form for submitting: 
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 29 January, 23:00 CET