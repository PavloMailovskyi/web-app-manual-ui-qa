## https://www.sql-practice.com/ ##


### SQL-01: List all patients admitted after a specific date

Scenario:
Verify that the system correctly returns patients admitted after 2018-01-01

SQL Query:
SELECT patient_id, first_name, last_name, admission_date
FROM admissions
JOIN patients USING (patient_id)
WHERE admission_date > '2018-01-01';

Validation:
All returned records must have admission_date strictly later than 2018-01-01
No records with earlier dates should appear

---

### SQL-02: Patients older than 40 years

Scenario:
Verify that the system correctly returns patients older than 40 years.

SQL Query:
select * from patients
where birth_date < '1986-01-12'

Validation:
All returned patients must have birthdate earlier than 1986-01-12
No patient with birthdate later than 1986-01-12

---

### SQL-03: Count total number of admissions

Scenario:
Verify that the total number of admissions can be calculated correctly.

SQL Query:
select COUNT(*) AS TOTAL_ADMISSIONS
FROM ADMISSIONS

Validation:
Result contains exactly one row
total_admissions value is greater than or equal to 0

---

### SQL-04: Unique birth years by order

Scenario:
Show unique birth years from patients and order them by ascending.

SQL Query:
SELECT year(birth_date)
FROM patients
GROUP BY year(birth_date)

Validation:
All years are unique
All returned records are real years
There is no NULL records returned

---

### SQL-05: Female patients only

Scenario:
Verify that only female patients are returned.

SQL Query:
SELECT * FROM patients
WHERE gender = 'F'

Validation:
All returned records have gender = 'F'
No male patients are included

---

### SQL-06: Admissions with diagnosis

Scenario:
Verify that admissions with a specified diagnosis are returned

SQL Query:
SELECT * FROM admissions
WHERE diagnosis is not null

Validation:
All returned records have a non-null diagnosis
No admissions with NULL diagnosis are included