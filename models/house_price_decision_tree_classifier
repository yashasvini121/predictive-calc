from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

price_bins = [0, 100000, 200000, 300000, 400000, float('inf')] 
price_labels = ['low', 'medium', 'high', 'very_high']
df['price_category'] = pd.cut(df[target], bins=price_bins, labels=price_labels)

target_classification = 'price_category'
features_classification = df.drop(columns=[target, target_classification])  # Remove numerical price
Train_X_class, Test_X_class, Train_Y_class, Test_Y_class = train_test_split(
    features_classification, df[target_classification], train_size=0.8, test_size=0.2, random_state=100
)

dt_classifier = DecisionTreeClassifier(random_state=100)

# Train the model
dt_classifier.fit(Train_X_class, Train_Y_class)
pred_train_class = dt_classifier.predict(Train_X_class)
pred_test_class = dt_classifier.predict(Test_X_class)

# Evaluate the model
train_accuracy = accuracy_score(Train_Y_class, pred_train_class)
test_accuracy = accuracy_score(Test_Y_class, pred_test_class)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")
print("Classification Report:")
print(classification_report(Test_Y_class, pred_test_class))

def save_decision_tree_model():
    with open("models/house_price/saved_models/decision_tree_model.pkl", "wb") as file:
        pickle.dump(dt_classifier, file)

# Call the save function where appropriate
# save_decision_tree_model()
