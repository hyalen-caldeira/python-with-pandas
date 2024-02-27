import pandas as pd
from urllib.request import urlretrieve

class CovidDataManipulator:
    def __init__(self, covid_data_csv_url, location_data_csv_url=None):
        self.covid_data_csv_url = covid_data_csv_url
        self.location_data_csv_url = location_data_csv_url

    def import_and_read_csv_file(self):
        # Download the CSV file and save it locally
        covid_data, _ = urlretrieve(self.covid_data_csv_url, "data.csv")
        location_data, _ = urlretrieve(self.location_data_csv_url, "location.csv")
        
        # Read the CSV file into a Pandas DataFrame
        self.covid_df = pd.read_csv(covid_data)
        self.location_df = pd.read_csv(location_data)

    def describe_covid_data(self):
        print("\nView basic infomation about rows, columns & data types: " + "\n" + str(self.covid_df.info()))
        print("\nView statistical information about numeric columns: " + "\n" + str(self.covid_df.describe()))
        print("\nGet the list of column names: " + "\n" + str(self.covid_df.columns))
        print("\nGet the number of rows & columns as a tuple: " + "\n" + str(self.covid_df.shape))

    def retrieve_covid_data_from_data_frame(self):
        print("COVID --> ")
        print("First 5 rows of the DataFrame: " + "\n" + str(self.covid_df.head()))
        print("Last 5 rows of the DataFrame: " + "\n" + str(self.covid_df.tail(5)))
        # print("\nList of new cases: " + "\n" + str(self.covid_df['new_cases']))
        # print("\nList of new deaths: " + "\n" + str(self.covid_df['new_deaths']))
        # print("Specific value at row 246, column 'new_cases': " + str(self.covid_df.at[246, 'new_cases']))
        print("Retrieving a range of rows of data from the data frame: " + "\n" + str(self.covid_df[240:250]))
        print("Retrieving a row of data from the data frame: " + "\n" + str(self.covid_df.loc[243]))

    def retrieve_location_data_from_data_frame(self):
        print("LOCATION --> ")
        print("First 5 rows of the DataFrame: " + "\n" + str(self.location_df.head()))
        print("Last 5 rows of the DataFrame: " + "\n" + str(self.location_df.tail(5)))

    def analyzing_covid_data(self):
        print("Computing the sum of values in a column or series: " + "\n" + str(self.covid_df['new_cases'].sum()))
        print("Computing the mean of values in a column or series: " + "\n" + str(self.covid_df['new_cases'].mean()))
        print("Querying a subset of rows satisfying the chosen criteria using boolean expressions: " + "\n" + str(self.covid_df[self.covid_df.new_cases > 1000]))
        print("Querying a subset of rows satisfying the chosen criteria using boolean expressions: " + "\n" + str(self.covid_df[(self.covid_df.new_cases > 1000) & (self.covid_df.new_deaths > 100)]))
        self.add_date_columns()
        self.group_and_aggregate_data()
        self.merge_data()

    def group_and_aggregate_data(self):
        self.covid_df['total_cases'] = self.covid_df.new_cases.cumsum()
        self.covid_df['total_deaths'] = self.covid_df.new_deaths.cumsum()
        self.covid_df['total_tests'] = self.covid_df.new_tests.cumsum()

        print("Agregating data using the groupby method: " + "\n" + str(self.covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()))
        print("Agregating data using the groupby method: " + "\n" + str(self.covid_df.groupby('month')[['new_cases', 'new_deaths']].sum()))

    def add_date_columns(self):
        self.covid_df['date'] = pd.to_datetime(self.covid_df.date)
        self.covid_df['year'] = pd.DatetimeIndex(self.covid_df.date).year
        self.covid_df['month'] = pd.DatetimeIndex(self.covid_df.date).month
        self.covid_df['day'] = pd.DatetimeIndex(self.covid_df.date).day
        self.covid_df['weekday'] = pd.DatetimeIndex(self.covid_df.date).weekday
        print(self.covid_df.head())

    def merge_data(self):
        # Add a column to the DataFrame with the location
        self.covid_df['location'] = "Italy"
        self.merged_df = self.covid_df.merge(self.location_df, on="location")
        self.merged_df['cases_per_million'] = self.merged_df.total_cases / self.merged_df.population

        # Merge the two DataFrames
        self.merged_df = self.covid_df.merge(self.location_df, on="location")
        self.merged_df['cases_per_million'] = self.merged_df.total_cases / self.merged_df.population
        self.merged_df['deaths_per_million'] = self.merged_df.total_deaths / self.merged_df.population
        self.merged_df['tests_per_million'] = self.merged_df.total_tests / self.merged_df.population
        print(self.merged_df.tail())

    def save_data_to_csv(self):
        self.merged_df.to_csv("covid_data_merged.csv", index=False)

if __name__ == "__main__":
    # Instantiate the class with the URL of the CSV file
    data_manipulator = CovidDataManipulator(
        "https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv",
        "https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv")  
    
    # Call the method to import and manipulate the data
    data_manipulator.import_and_read_csv_file()
    data_manipulator.describe_covid_data()
    data_manipulator.retrieve_covid_data_from_data_frame()
    data_manipulator.retrieve_location_data_from_data_frame()
    data_manipulator.analyzing_covid_data()
    data_manipulator.save_data_to_csv()
    
