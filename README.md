# Fitness analysis

## Pre-requisites

- Python 3
- Garmin Connect account

## Getting started

- Install the required packages: `pip install -r requirements.txt`
- Create a `.env` file by copying the `.env.example` file and filling in the required values :
  - `GARMIN_LOGIN`: your Garmin Connect email address
  - `GARMIN_PASSWORD`: your Garmin Connect password
- In file `download.py`, change the `start_date` and `end_date` variables to the desired date range
- Run the script: `python download.py` to download heart rate data from Garmin Connect. Then data will be saved in the `heart_rate.csv` file.
- Open `analysis.ipynb` in Jupyter Notebook :
  - Change `sleep_start` and `sleep_end` variables to the desired sleep time range
  - Change `max_hr` variable to your maximum heart rate
  - Run the notebook to generate the analysis
