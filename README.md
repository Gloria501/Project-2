**Employee Data Scraper**


This Python script scrapes employee data from the SlingAcademy API, normalizes it, and prepares it for data warehouse ingestion.

Features

* Fetches and parses employee JSON data

* Extracts key fields: ID, Name, Email, Phone, etc.

--Normalizes:

  *Full Name = First + Last Name

  *Designation by experience

  *Invalid phone numbers ('x' marked as "Invalid Number")

 *Hire Date to YYYY-MM-DD

 *Ensures correct data types for all fields

 *Error handling with retries
 
 *(Optional) Salary currency conversion
 

  *Test Cases*

  
  
* API reachable and JSON valid

* Data fields correctly extracted

* Data types and structure validated

* Handles missing/invalid values
