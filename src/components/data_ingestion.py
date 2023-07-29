import os 
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## intialize the data ingestion configuration
@dataclass()
class DataIngestionConfig:
    train_data_path = os.path.join('artifact','train.csv')
    test_data_path = os.path.join('artifact','test.csv')
    raw_data_path = os.path.join('artifact','raw.csv')

## create a data ingestion class


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')
        try:
            df= pd.read_csv(os.path.join('notebook/data','dataset_es_train'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            
            train_data,test_data = train_test_split(df,test_size=0.3,random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            logging.info('Data Ingestion is Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )

        except Exception as e:
            logging.info('Error Ocured in Data Ingestion Config')
