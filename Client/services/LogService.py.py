"""
DEBUG	Detailed information, typically of interest only when diagnosing problems.
INFO	Confirmation that things are working as expected.
WARNING	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR	Due to a more serious problem, the software has not been able to perform some function.
CRITICAL	A serious error, indicating that the program itself may be unable to continue running.


"""
import logging
import ReadLogFile as htmlgenerator

def log(message, level):
    logger = logging.getLogger(__name__)
    logger.propagate = False
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('log31121.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if level == 0:
        logger.setLevel(logging.DEBUG)
        logger.debug(message)
    elif level == 1:
        logger.setLevel(logging.INFO)
        logger.info(message)
    elif level == 2:
        logger.setLevel(logging.WARNING)
        logger.warning(message)
    elif level == 3:
        logger.setLevel(logging.ERROR)
        logger.error(message)
    elif level == 4:
        logger.setLevel(logging.CRITICAL)
        logger.critical(message)
    logger.removeHandler(file_handler)
    htmlgenerator.generateHtmlLog()


log('error',0 )
log('not allowed to access',1 )
log('not allowed to access server',2 )
log('not allowed to access fatal error',3 )
log('not allowed to access system crash',4 ) 
