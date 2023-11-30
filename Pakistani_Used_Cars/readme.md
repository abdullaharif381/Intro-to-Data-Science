# PakWheels Used Cars Dataset Analysis and Machine Learning

## Dataset Overview

- **Dataset Link:** [PakWheels Used Cars](https://www.kaggle.com/datasets/muhammadwaqargul/pakwheels-used-car-dataset-october-2022)
- **Roll Numbers:** `22L-7764` and `22L-7484`

## Project Part A

### Part 1: Describing the Dataset

The dataset contains information about used cars in Pakistan, including details like model year, location, engine type, fuel type, transmission, engine capacity, mileage, and features. The dataset has a total of 89,955 rows and 16 columns.

### Part 2: Data Wrangling, Preprocessing, and Transformation

- Data cleaning, handling missing values, and outlier detection.
- Feature engineering, creating new columns for efficient preprocessing.
- Encoding categorical variables using one-hot encoding and target encoding.
- Scaling with normalization and standardization.
- Storing the prepared dataset in a CSV file.

### Part 3: Exploratory Data Analysis (EDA)

- Analysis of various attributes such as price, mileage, engine capacity, and features.
- Visualization of patterns and distributions.
- Machine learning model development for predicting the value of used cars.

## Introduction

1. **Problem Statement:**
   - Develop a machine learning model to predict the value of used cars in Pakistan based on various attributes.
   - Facilitate better negotiation for buyers and sellers, preventing fraud.

2. **Source of the Dataset:**
   - Uploaded by Muhammad Waqar Gul on Kaggle in October 2022.

3. **Brief Description of the Dataset:**
   - Contains details about used cars, including model year, location, engine type, and more.
   - Total rows: 89,955, Total columns: 16.

4. **Attributes/Variables/Columns:**

   | Column Name          | Description                                       |
   |----------------------|---------------------------------------------------|
   | ad_url               | Webpage URL where the car is/was listed           |
   | title                | Title of the car (make, model, variant)            |
   | location             | Place of sale of the car                          |
   | price                | Price of the car in Pakistani Rupees              |
   | mileage              | Total kilometers the car has traveled             |
   | engine_type          | Engine type of the car (petrol/diesel/none)       |
   | transmission         | Type of transmission used by the car              |
   | ... (and more)       | Other attributes of the cars                     |

## Data Wrangling

- Importing libraries, reading the dataset, and dropping unnecessary columns.
- Handling missing values and removing duplicate rows.
- Features manipulation, outlier detection, and handling.
- Encoding categorical variables using one-hot encoding and target encoding.

## Conclusion

This project aims to create a robust machine learning model for predicting the value of used cars in Pakistan, contributing to transparency and fairness in the used car market.

Feel free to explore the complete code for a detailed understanding of each step and contribute to further enhancements!

