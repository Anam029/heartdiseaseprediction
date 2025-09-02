import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset
df = pd.read_csv('heart.csv')

# Preprocess the data (refer to the Medium article for detailed preprocessing steps)

# Split the data into features and target
X = df.drop('condition', axis=1)
y = df['condition']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save the model to a file
with open('logmod.pkl', 'wb') as f:
    pickle.dump(model, f)
