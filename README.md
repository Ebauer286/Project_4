PROJECT 4 - EDIBLE VS POISONOUS MUSHROOM CLASSIFICATION

---

REPOSITORY Guide:
1) Data used to train and test the classifiers can be found at MushroomDataset/secondary_data.csv.
2) To instantiate and populate a NoSQL database using MongoDB and Pymongo, run populate_db.py.
3) Preprocessing, training and evaluation of the KNN model is stored in Model_training/KNN_model.ipynb.
4)  Preprocessing, training and evaluation of the Random Forest model is stored in Model_Training/RandomForest_model.ipynb.

---

PROJECT OVERVIEW

Objective: train a machine learning model to classify mushrooms as either poisonous or edible.

The project utilized both K-nearest neighbor (KNN) and Random Forest algorithms for classification.

---

DATASET 

This dataset includes 61069 hypothetical mushrooms with caps based on 173 species (353 mushrooms
per species). This dataset was created by D. Wagner, D. Heider and G. Hattab, and obtained from UC Irvine's Machine Learning Repository (https://archive.ics.uci.edu/dataset/848/secondary+mushroom+dataset). The dataset includes metadata columns such as:
  * cap-diameter
  * cap-shape
  * does-bruise-bleed
  * gill-attachment
  * gill-spacing
  * gill-color
  * stem-height



---

METHODOLOGY

The project follows these key steps (Note: the preprocessing, model training and evaluation follows the same steps for both the KNN and Random Forest models):
1. Create and populate a noSQL database, using MongoDB and Pymongo
2. Generate data frame with all records from database.
3. Remove al columns with empty values.
4. Split the data into training and testing batches.
5. Scale the training and test features.
6. Train the model using scaled training batch.
7. Generate predictions using the test batch.
8. Evaluate the model, looking at accuracy, precision and recall.
9. Return to the preprocessing stage to optimize the training data.
10. Starting with the complete raw data, fill all empty values (in all columns) with 'n/a' string value, to create a new distinct categorical value. No columns are dropped.
11. Repeat steps 4 to 8. 


   
---

RESULTS

Training of both the KNN and Random Forest classifiers was successful.

* The KNN model was trained to achieve: 0.999 accuracy, 0.999 recall and 0.999 precision.
* The Random Forest model was able to achieve: 1.0 accuracy, 1.0 recall and 1.0 precision.


---

TECHNOLOGIES USED
  * Python
  * Pandas
  * SKLearn: Random Forest Classifier
  * SKLearn: K-Nearest Neighbor 
  * Jupyter Notebook
* MongoDB

  ---


  
