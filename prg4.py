import pandas as pd

def explore_dataset(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            print("Unsupported file format. Please provide a CSV or Excel file.")
            return

        print("Dataset Information:")
        print(df.info())
        print("\nFirst few rows of the dataset:")
        print(df.head())
        print("\nSummary statistics:")
        print(df.describe())
        print("\nUnique values for categorical columns:")
        for column in df.select_dtypes(include='object').columns:
            print(f"{column}: {df[column].unique()}")

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with a proper file path
file_path = r'C:\Users\Lenovo\OneDrive\Desktop\IRIS.csv'
explore_dataset(file_path)

