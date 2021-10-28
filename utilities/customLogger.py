import inspect
import logging

class custom_Logger:
    def custstomLogger(logLevel=logging.INFO):
        logger_Name=inspect.stack()[1][3]
        logger=logging.getLogger(logger_Name)
        logger.setLevel(logLevel)
        destinationFile=logging.FileHandler(".\\eCommerceLogs\\eCommerceAppTest.log",)
        logFormat=logging.Formatter('%(asctime)s: %(levelname)s - %(message)s',
                                    datefmt='%d/%m/%Y %H:%M:%S %p')
        destinationFile.setFormatter(logFormat)
        logger.addHandler(destinationFile)
        return logger