import pandas as pd
from urllib.request import urlretrieve

class CSVDataManipulator:
    def __init__(self, csv_url):
        self.csv_url = csv_url

    def import_and_manipulate(self):
        # Download the CSV file and save it locally
        local_file, _ = urlretrieve(self.csv_url, "data.csv")
        
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(local_file)

        type(df)

        # Perform data manipulation (for demonstration, let's print the first few rows)
        print("First 5 rows of the DataFrame:")
        print(df.head())

# Example usage
if __name__ == "__main__":
    # Instantiate the class with the URL of the CSV file
    data_manipulator = CSVDataManipulator("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv")
    
    # Call the method to import and manipulate the data
    data_manipulator.import_and_manipulate()
