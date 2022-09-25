# family_budget
This projects is a test task

# Task
1.	Description
The application should allow for creating several users. Each user can create a list of any number of budgets and share it with any number of users. 
The budget consists of income and expenses. They are grouped into categories. It is required to create REST or GraphQL API and a database. 
The project should contain authorisation, tests, fixtures, filtering and pagination.

2.	Technologies
Any. Whatever would be best in your opinion (including JS frameworks).

3.	Requirements
Entire project should be available as an open source project on GitHub. Please commit your work on a regular basis (rather than one huge commit). 
The project should contain a README file with information how to install the application in a local environment.

4.	Deploy
Please use Docker for orchestration (docker-compose).

# Comments
1. The project is made exclusively for users, but not for guests

2. Added model Family. If, say, the father - superuser wants to create a separation of families due to the large number of users. Then, in connection with this separation, refine the functionality for showing the budget exclusively to your family.

3. Filtering and fixtures (located in each application folder in a folder with the same name). Made in test mode for demonstration purposes. I didn't do detailed filtering.

4. When running not through a docker container, I advise you to make a virtual environment and install all dependencies from the requirements.txt file.

# Docker
docker build .

docker-compose up
