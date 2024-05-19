import pandas as pd
import sys

def process_csv(file_path: str, username: str, required_columns: int) -> None:
    """Reads a CSV file and allows the user to select the best translator for the questions.

    This method is used to allow the user to validate the translations of the CSV file.
    It gets the path of the csv file containing the translations and the name of the user
    It will then create a column for the user to select the best translator for each row.
    The user can input the numbers 1, 2, 3, or a combination of them separated by commas.
    Those values will be mapped to the translator equivalent and then stored in the appropriate row.
    The user can also input -1 to exit the validation process.
    
    Args:
        file_path (str): The path of the CSV file containing the translations.
        username (str): The name of the user that will validate the translations.
        required_columns (int): The number of columns that should be printed for each row, starting from the first one.

    Returns:
        None
    """
    mappings = {
        1: "Gpt",
        2: "Meltemi",
        3: "Llama3",
        0: "No one"
    }

    # Open the file as a dataframe
    df = pd.read_csv(file_path)

    # fix the name of the column corresponding to the user
    column_name = f'{username.upper()}_Validation'

    # Create the column if it does not exist
    if column_name not in df.columns:
        df.insert(len(df.columns), column_name, [pd.NA]*len(df))

    # Iterate the dataframe, starting from the first None row of the validation column
    # This allows the user to continue from where they left off
    for index, row in df.iterrows():

        # Skip the rows that have already been validated
        if not pd.isna(row[column_name]):
            continue

        print(f"Row {index+1}:")
        # For each line print all columns
        for col in df.columns[0: required_columns]:
            clean_text = row[col].strip().replace('\n', '. ')
            print(f"{col}: {clean_text}")

        # Input from the user
        user_input = input("-----------------------------------------\nEnter the number of the best translator(s) separated by commas (1: GPT, 2: Meltemi, 3: Lamma3, 0: None): ")
        # exit the loop if the user enters -1
        if user_input == "-1":
            break

        try:
            user_input = "/".join([mappings[int(num.strip())] for num in user_input.split(",")])
        except KeyError:
            print("Invalid input. Next time, enter the numbers 1, 2, 3, or a combination of them separated by commas.")
            continue

        print(f'Will update row {index+1} with "{user_input}"')
        # Add this user input as the row value of the column "Username_Validation"
        df.at[index, column_name] = user_input

        print("\n\n")

    # Save the dataframe back to the CSV file
    df.to_csv(file_path, index=False)

if __name__ == "__main__":

    # get the file path from the arguments
    try:
        file_path = sys.argv[1]
        username = sys.argv[2]
        required_columns = int( sys.argv[3] )
    except IndexError:
        print("Please provide the file path as an argument.")
        sys.exit(1)

    # Call the method to allow the user to easier validate the translations
    process_csv(file_path=file_path, username=username, required_columns=required_columns)