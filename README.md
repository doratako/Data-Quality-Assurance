##  Data validation and data cleansing

The dataset used in the restaurant recommender system consists of 9 CSV files, each containing various features related to restaurants, consumers, and consumer preferences </br> https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data# </br>

The project aims to establish predefined validation rules covering various aspects of data quality, including checks for referential integrity, uniqueness, completeness, data types, ranges, and values. The initial step involves data validation to identify any quality issues. Once the issues are identified, data cleansing tasks are performed to resolve the identified problems and improve the overall data quality. The cleansing process focuses on correcting errors, inconsistencies, and inaccuracies </br>

To achieve this, a script file contains common and reusable functions that are invoked in individual script files. These individual scripts are designed to handle specific tasks related to each CSV file, allowing for a modular and organized approach to data processing.</br>

In order to handle potential data processing errors, the project incorporates exception handling. When errors occur, relevant information is logged in a text file, providing a record of encountered errors for troubleshooting.



