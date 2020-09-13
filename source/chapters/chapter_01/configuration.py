"""
configuration.py

Constants defined for data retrieval and preprocessing.
"""

# GitHub data directory URL.
DATA_DIRECTORY = (
    "https://raw.githubusercontent.com/mdcollab/covidclinicaldata/master/data/"
)

# Pattern for composing CSV file URLS to read.
CSV_FILE_PATTERN = "{week_id}_carbonhealth_and_braidhealth.csv"
CSV_URL_PATTERN = f"{DATA_DIRECTORY}/{CSV_FILE_PATTERN}"

# *week_id*s used to format CSV_FILE_PATTERN with.
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

# Values replacement dictionary by column name.
REPLACE_DICT = {"covid19_test_results": {"Positive": True, "Negative": False}}

# Name of the column containing the COVID-19 test results.
TARGET_COLUMN_NAME = "covid19_test_results"

# Fractional threshold of missing values in a feature.
NAN_FRACTION_THRESHOLD = 0.5

# Prefix used in columns containing X-ray data results.
X_RAY_COLUMN_PREFIX = "cxr_"