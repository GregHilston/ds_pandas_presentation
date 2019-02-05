# Validation Works
# Below is the code needed to perform validation on the work above.

import pandas as pd

INPUT_FILE = "train.csv"

validation_df = pd.read_csv(INPUT_FILE)

def validate(expected, actual, message):
    print(f"expected type {type(expected)}") # TODO remove
    print(f"actual type {type(actual)}") # TODO remove

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

def validate_min_age(value):
    hint = "Hint: Look into the Pandas function `min` that can be called on a Series"

    validate(validation_df["Age"].min(), value, hint)

def validate_max_age(value):
    hint = "Hint: Look into the Pandas function `max` that can be called on a Series"

    validate(validation_df["Age"].max(), value, hint)

def validate_pivot_table_pclass_sex_survived(df):
    hint = "Hint: Look into the Pandas function `pivot_table`"

    pivot_table = validation_df.pivot_table(index='Pclass', columns='Sex', 
                    values='Survived', aggfunc='sum')

    validate(pivot_table, df, hint)

def validate_pivot_table_pclass_sex_fare(df):
    hint = "Hint: Look into the Pandas function `pivot_table`"

    pivot_table = validation_df.pivot_table(index='Pclass', columns='Sex', 
                    values='Fare', aggfunc='mean')

    validate(pivot_table, df, hint)

def validate_transpose(df):
    hint = "Look into the Pandas function `T`"

    validate(validation_df.T, df, hint)

def validate_age_removed(df_without_age):
    hint = "Look into the Pandas function `remove`. Note, this doesn't modify the dataframe by default and instead returns a new modified data frame. Also take note of the axis parameter (hint you want it to be set to 1, for columns)"

    validate(validation_df.drop("Age", axis=1), df_without_age, hint)

def validate_age_column_renamed_to_how_old(df_age_renamed_df):
    hint = "Look into the Pandas function called `rename`"

    validate(validation_df.rename(columns={'Age': 'How Old'}), df_age_renamed_df, hint)

def validate_last_five_rows(last_five_rows_df):
    hint = "Look into the Pandas function `tail`"

    validate(validation_df.tail(), last_five_rows_df, hint)

def validate_only_age_and_sex_columns(age_and_sex_columns_df):
    hint = "Look into indexing into the dataframe by providing a list of rows of interest. Super duper hint: `df[['some column', 'some other column']]`"

    validate(validation_df[['Age', 'Sex']], age_and_sex_columns_df, hint)

def validate_males_over_50_in_pclass_3(males_over_50_pclass_3):
    hint = "Look into indexing the original data frame and combing conditionals with the `&` operator. This may be challenging the first time you do this. Here's an example of getting the teenages`df[(df['Age'] <= 18) & (df['Age'] >= 13)]`. Modify this to your need!"

    validate(validation_df[(validation_df['Age'] > 50) & (validation_df['Sex'] == 'male') & (validation_df['Pclass'] == 3)], males_over_50_pclass_3, hint)

def new_wealthy_column(x):
    if x.Pclass == 1:
        return True
    else:
        return False

def validate_new_wealhty_column(df):
    hint = "Look into the `apply` function. This is an incredibly useful took to use with Pandas. I reccommend really ensuring you understand this challenge, as it will save you much time in the future."

    copy_validation_df = validation_df.copy()
    copy_validation_df["Wealthy"] = df.apply(new_wealthy_column, axis=1)

    validate(copy_validation_df, df, hint)