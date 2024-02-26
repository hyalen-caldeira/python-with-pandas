import pandas as pd
from urllib.request import urlretrieve

class CSVDataManipulator:
    def __init__(self, csv_url):
        self.csv_url = csv_url

    def import_and_read_csv_file(self):
        # Download the CSV file and save it locally
        local_file, _ = urlretrieve(self.csv_url, "data.csv")
        
        # Read the CSV file into a Pandas DataFrame
        self.df = pd.read_csv(local_file)

    def describe_csv_file(self):
        print("\nView basic infomation about rows, columns & data types: " + "\n" + str(self.df.info()))
        print("\nView statistical information about numeric columns: " + "\n" + str(self.df.describe()))
        print("\nGet the list of column names: " + "\n" + str(self.df.columns))
        print("\nGet the number of rows & columns as a tuple: " + "\n" + str(self.df.shape))

    def retrieve_data_from_data_frame(self):
        print("First 5 rows of the DataFrame: " + "\n" + str(self.df.head()))
        print("Last 5 rows of the DataFrame: " + "\n" + str(self.df.tail(5)))
        # print("\nList of new cases: " + "\n" + str(self.df['new_cases']))
        # print("\nList of new deaths: " + "\n" + str(self.df['new_deaths']))
        # print("Specific value at row 246, column 'new_cases': " + str(self.df.at[246, 'new_cases']))
        print("Retrieving a range of rows of data from the data frame: " + "\n" + str(self.df[240:250]))
        print("Retrieving a row of data from the data frame: " + "\n" + str(self.df.loc[243]))

    def analyzing_data(self):
        print("Computing the sum of values in a column or series: " + "\n" + str(self.df['new_cases'].sum()))
        print("Computing the mean of values in a column or series: " + "\n" + str(self.df['new_cases'].mean()))
        print("Querying a subset of rows satisfying the chosen criteria using boolean expressions: " + "\n" + str(self.df[self.df.new_cases > 1000]))
        print("Querying a subset of rows satisfying the chosen criteria using boolean expressions: " + "\n" + str(self.df[(self.df.new_cases > 1000) & (self.df.new_deaths > 100)]))
        print("Agregating data using the groupby method: " + "\n" + str(self.df.groupby('date').sum()))
        print("Agregating data using the groupby method: " + "\n" + str(self.df.groupby('date')[['new_cases', 'new_deaths']].sum()))

if __name__ == "__main__":
    # Instantiate the class with the URL of the CSV file
    data_manipulator = CSVDataManipulator("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv")
    
    # Call the method to import and manipulate the data
    data_manipulator.import_and_read_csv_file()
    data_manipulator.describe_csv_file()
    data_manipulator.retrieve_data_from_data_frame()
    data_manipulator.analyzing_data()
