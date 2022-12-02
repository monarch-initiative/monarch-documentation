import logging, sys

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance"""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("| %(levelname)-8s | %(name)-8s | %(message)s |")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger