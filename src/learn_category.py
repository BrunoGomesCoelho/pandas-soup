import pandas as pd
import xgboost as xgb

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


WASHER_FILE = "washers.csv"
REFRIGERATORS_FILE = "refrigerators.csv"
TEST_SIZE = 0.3

def load_files():
    washers = pd.read_csv(WASHER_FILE)
    refrigerators = pd.read_csv(REFRIGERATORS_FILE)

    washers["Category"] = 0
    refrigerators["Category"] = 1

    return washers, refrigerators


def main():
    categorical_labels = ["Title", "Brand", "Model", "Category"]
    washers, refrigerators = load_files()
    all_data = pd.concat([washers, refrigerators])

    # Transform categorical data to numeric for xgboost
    for label in categorical_labels:
        washers.loc[washers[label].isnull(), label] = "nullo"
        refrigerators.loc[refrigerators[label].isnull(), label] = "nullo"
        all_data.loc[all_data[label].isnull(), label] = "nullo"

        encoding = LabelEncoder()
        encoding.fit(all_data[label])
        washers[label] = encoding.transform(washers[label])
        refrigerators[label] = encoding.transform(refrigerators[label])

    # Deal with None price
    label = "Price"
    washers.loc[washers[label] == "None"] = 0
    refrigerators.loc[refrigerators[label] == "None"] = 0

    # Convert string price to float
    washers["Price"] = washers["Price"].astype(float)
    refrigerators["Price"] = refrigerators["Price"].astype(float)

    # Free some RAM due to my laptop lagging
    del all_data

    # Shuffle data
    washers = washers.sample(frac=1)
    refrigerators = refrigerators.sample(frac=1)

    # We split data into train/test
    washer_train, washer_test = train_test_split(washers, test_size=TEST_SIZE)
    refrigerators_train, refrigerators_test = train_test_split(refrigerators, test_size=TEST_SIZE)

    # Merge the differents products
    train = pd.concat([washer_train, refrigerators_train])
    test = pd.concat([washer_test, refrigerators_test])

    # Laptop limitations
    del washers, refrigerators, washer_train, washer_test,\
        refrigerators_train, refrigerators_test

    # Get prediction
    y_train = train["Category"].copy()
    train.drop("Category", axis=1, inplace=True)

    y_test = test["Category"].copy()
    test.drop("Category", axis=1, inplace=True)

    """
    We use small number of estimators and high learning rate due
       to runtime restrictions of my laptop

     Also, ideally we would be running a gridSearch or something similiar
       to otimize parameters using K-Folds
    """
    clf = xgb.XGBClassifier(
        max_depth=4,
        n_estimators=10,
        learning_rate=1,
        subsample=1.0,
        seed=1301)

    # A better idea would be having a validation to use as a eval set.
    #   Since the problem is quite easy, we skipped this
    clf.fit(train, y_train, early_stopping_rounds=5, eval_metric="error",
            eval_set=[(train, y_train)])

    # make predictions for test data
    y_pred = clf.predict(test)
    predictions = [round(value) for value in y_pred]

    # evaluate predictions
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))

if __name__ == "__main__":
    main()
