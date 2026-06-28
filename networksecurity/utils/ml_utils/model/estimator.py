from networksecurity.constants.traning_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME



import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            logging.info(f"Entered the NetworkModel class constructor")
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise NetworkSecurityException(e,sys) 

    def predict(self, x):
        try:
            logging.info(f"Entered the predict method of NetworkModel class")
            x_transform=self.preprocessor.transform(x)
            y_hat=self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e

   