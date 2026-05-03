from extract import fetch_weather
from transform import transform_data
from load import load_to_db
from utils.logger import setup_logger
import logging

def run_pipeline():
    setup_logger()

    try:
        logging.info("Pipeline started")

        raw_data = fetch_weather()
        df = transform_data(raw_data)
        load_to_db(df)

        logging.info("Pipeline finished successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()