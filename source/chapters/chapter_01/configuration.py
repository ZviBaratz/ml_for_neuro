"""
configuration.py

Constants defined for data retrieval and preprocessing.
"""

DATA_DIRECTORY = (
    "https://raw.githubusercontent.com/mdcollab/covidclinicaldata/master/data/"
)
CSV_FILE_PATTERN = "{week_id}_carbonhealth_and_braidhealth.csv"
CSV_URL_PATTERN = f"{DATA_DIRECTORY}/{CSV_FILE_PATTERN}"
WEEK_IDS = (
    "04-07",
    "04-14",
    "04-21",
    "04-28",
    "05-05",
    "05-12",
    "05-19",
    "05-26",
    "06-02",
    "06-09",
    "06-16",
)
REPLACE_DICT = {"covid19_test_results": {"Positive": True, "Negative": False}}
TARGET_COLUMN_NAME = "covid19_test_results"
NAN_FRACTION_THRESHOLD = 0.1
