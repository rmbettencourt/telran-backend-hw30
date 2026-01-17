# HW30: Car Model Prediction

## 🧩 Task Definition

The goal of this homework is to create a predictive model that estimates the car model based on customer attributes. Specifically, we use **Gender** and **Color** as input features (`X`) and the **car model** as the output (`y`).

Additional tasks include:

- Computing model accuracy.
- Persisting the trained model for future use.
- Performing pandas data analysis on the dataset:
    - Filter only Hyundai cars.
    - Filter Toyota cars with price greater than 40,000.
    - Identify the three most popular car models.
- Implementing categorical encoding using a custom converter module.

The solution leverages **scikit-learn** for machine learning and **pandas** for data processing. The full solution is available in this repository.

---

## 📝 Description

This project demonstrates the use of **decision tree classification** to predict car models based on user attributes. It also illustrates:

- Handling and cleaning datasets with pandas.
- Encoding categorical variables into numerical values.
- Splitting data into training and test sets to evaluate model accuracy.
- Saving and loading machine learning models using `joblib`.
- Performing simple data analysis tasks with pandas.

The model is trained on a cleaned car sales dataset containing attributes such as **Gender, Company, Model, Transmission, Color, Price, Annual Income**, and more.

---

## 🎯 Purpose

- Learn to preprocess categorical data for machine learning.
- Build a classification model to predict car models.
- Understand how to evaluate model performance using test sets.
- Persist trained models for production or further analysis.
- Apply pandas techniques for real-world data analysis tasks.

---

## ✨ Features

- Predict car model based on **Gender** and **Color**.
- Encode categorical columns into numerical format for modeling.
- Compute **accuracy** of predictions.
- Persist the trained model for reuse.
- Filter dataset for specific companies and price ranges.
- Identify the most popular car models.

---

## 🏗️ Architecture Overview

- `src/converter.py` — helper module for categorical encoding.
- `car_sales.ipynb` — main notebook with data processing, model training, and analysis.
- `tests/` — unit tests for the converter module.
- `joblib` — used for saving and loading trained models.
- `pandas` — data manipulation and analysis.
- `scikit-learn` — machine learning model implementation.

---

## 🔍 How It Works

1. **Load and clean data**: Remove duplicates and missing values.
2. **Encode categorical data**: Convert string columns like Gender, Color, Model into numerical values.
3. **Define input (`X`) and output (`Y`)**: Use Gender and Color as features; Model as target.
4. **Split data**: Divide into training and testing sets.
5. **Train model**: Use `DecisionTreeClassifier` on training data.
6. **Evaluate**: Predict on test data and calculate accuracy.
7. **Retrain and save model**: Fit model on full dataset and persist using `joblib`.
8. **Data analysis tasks**: Filter Hyundai and Toyota cars, and compute top 3 popular models.

---

## 📜 Output Example

- Model prediction for a new customer:

```python
CUSTOMER = mapper["Gender"]["Female"]
COLOR = mapper["Color"]["Pale White"]

prediction = model.predict([[CUSTOMER, COLOR]])
print("Predicted Car Model:", prediction)
```

- Filter Hyundai cars:

```python
dfHyundai = df[df["Company"] == "Hyundai"].reset_index()
print(dfHyundai)
```

- Filter Toyota cars with price > 40,000:

```python
dfToyotaExp = df.query('Company == "Toyota" and `Price ($)` > 40000').reset_index()
print(dfToyotaExp)
```

- Top 3 most popular car models:

```python
mostPopularCars = df[["Model", "Company"]].value_counts().head(3).reset_index()
print(mostPopularCars)
```

---

## 📦 Usage

1. Install required packages:

```bash
pip install pandas scikit-learn joblib
```

2. Run `car_sales.ipynb` notebook to train model and perform analysis.

3. Load persisted model for predictions:

```python
import joblib
model = joblib.load("gender-color-model.joblib")
```

---

## 🧪 Running Tests

Unit tests for the converter module:

```bash
python -m unittest discover tests -v
```

Tests cover:

- Enumerator function
- Column mapping
- DataFrame conversion to numeric values

---

## ✅ Dependencies

- Python 3.10+
- pandas
- scikit-learn
- joblib

---

## 🗂 Project Structure

```
.
├── car_sales.ipynb
├── main.py
├── README.md
├── src
│   └── converter.py
├── tests
│   └── test_converter.py
├── car_sales_cleaned1.csv
└── gender-color-model.joblib
```

---

## 📊 Project Status

**Status:** Completed ✅

- Model trains successfully.
- Accuracy evaluated.
- Data analysis tasks implemented.
- Converter module tested.

---

## 📄 License

MIT License

---

## 🧮 Conclusion

This project illustrates end-to-end **predictive modeling** using Python. It combines **data preprocessing**, **categorical encoding**, **model training**, and **data analysis** in a practical scenario.

---

Made with ❤️ and Python by **Sam Malikin** 🎓
