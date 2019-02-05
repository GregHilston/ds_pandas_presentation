# Validation Works
# Below is the code needed to perform validation on the work above.

import pandas as pd

INPUT_FILE = "train.csv"

validation_df = df = pd.read_csv(INPUT_FILE)

def validate(expected, actual, message):
    print(f"expected type {type(expected)}")
    print(f"actual type {type(actual)}")

    if ((isinstance(expected, pd.DataFrame) or isinstance(expected, pd.Series)) and not expected.equals(actual)) or ((isinstance(expected, float) or isinstance(expected, int) or isinstance(expected, str)) and expected != actual):
        print("Incorrect!")
        print("Expected:")
        display(expected)
        print("Actual:")
        
        if actual:
            display(actual)
        else:
            print("None")
        
        if message is not "":
            print(message)
    else:
        print("Correct!")
        
def validate_first_row_of_df(df):
    validate(validation_df.head(1), df, "Hint: There are multiple ways to do this. Look into the data frame function `head`.")
    
def validate_fare_greater_than_30(df):
    hint = "Hint: Make sure you're doing > 30 and not >=. Additionally look up the function `loc` and how we used it to make a conditional on age previously."
    
    validate(validation_df.loc[validation_df.Fare > 30.0], df, hint)
    
def validate_everyones_age(age_sum):
    hint = "Hint: You can either loop over every row and sum the age of each row, look into the `sum` function, look into the Pandas' `apply' function or perform a `groupby` and a `sum` aggregation. All are acceptible."
    
    validate(validation_df.Age.sum(), age_sum, hint)
    
def validate_only_cabin_series(cabin_series):
    hint = "Hint: You should be able to access the series of the data frame either with dot notation like `df.COLUMN_NAME` or dictionary notation like `df['COLUMN_NAME']"
    
    validate(validation_df.Cabin, cabin_series, hint)

def validate_value_of_sex_column_first_row(value):
    hint = "Hint: Look up the Pandas function `at`"

    validate(validation_df.at[0, "Sex"], value, hint)