import pytest
import pandas as pd
from src.covid_data_manipulator import CovidDataManipulator

@pytest.fixture
def data_manipulator():
    return CovidDataManipulator(
        "https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv",
        "https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv"
    )

def test_import_and_read_csv_file(data_manipulator):
    data_manipulator.import_and_read_csv_file()
    
    # Add assertions to check if the CSV file is imported and read correctly
    assert data_manipulator.covid_df is not None, "CSV file was not imported correctly"
    assert isinstance(data_manipulator.covid_df, pd.DataFrame), "Data is not stored as a DataFrame"
    assert len(data_manipulator.covid_df) > 0, "No data was read from the CSV file"

def test_describe_covid_data(data_manipulator):
    data_manipulator.import_and_read_csv_file()
    data_manipulator.describe_covid_data()
    
    # Add assertions to check if the COVID data is described correctly
    assert "max" in str(data_manipulator.covid_df.describe()), "COVID data description is incorrect"
    assert "mean" in str(data_manipulator.covid_df.describe()), "COVID data description is incorrect"
    assert "std" in str(data_manipulator.covid_df.describe()), "COVID data description is incorrect"
    assert "min" in str(data_manipulator.covid_df.describe()), "COVID data description is incorrect"
    assert "max" in str(data_manipulator.covid_df.describe()), "COVID data description is incorrect"


# def test_retrieve_covid_data_from_data_frame(data_manipulator):
#     data_manipulator.retrieve_covid_data_from_data_frame()
#     # Add assertions to check if the COVID data is retrieved correctly from the data frame

# def test_retrieve_location_data_from_data_frame(data_manipulator):
#     data_manipulator.retrieve_location_data_from_data_frame()
#     # Add assertions to check if the location data is retrieved correctly from the data frame

# def test_analyzing_covid_data(data_manipulator):
#     data_manipulator.analyzing_covid_data()
#     # Add assertions to check if the COVID data is analyzed correctly

# def test_save_data_to_csv(data_manipulator):
#     data_manipulator.save_data_to_csv()
#     # Add assertions to check if the data is saved to CSV correctly
