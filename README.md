# 20260601-DE5M5

Scenario:

User Stories or Backlog:

Solutions Diagram:
Hint - Use something like draw.io and add the image into this ReadMe.md file. 


# PM Task

1. Load the two datasets
2. Clean the them (thoroughly)
3. Measure at least 1 data engineering metric in the data cleaning process (ie dropped rows)
4. MVP: Output the cleaned files as a local csv.

Stretch: 

5. Output the cleaned files into the local SSMS (use SQLAlchemy); create a new DB for this.
6. Refactor your code into modular functions.

# Day 2

## AM Task:

- Focus on having at least one function like:
    - dataEnrich():
        - Calculate the days between the two date columns and add it as a new col. 
    - fileLoader
    - duplicateCheck
    - naCheck
    - dataCleaner
    - addToSQL

# Day 3 AM:

Level 1: 
Create your docker container with your cleaner app and data files. Your data must be saved in the volume. 

Level 2: 
Look into the concept of Docker Compose

Level 3:
Look at the difference between Docker Swarm and Kubernetes 

Stretch: 
Discuss with Nirosh