import logging


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.debug("This is a debug message.")
logging.info("The program is running normally.")
logging.warning("Something unexpected happened.")
logging.error("An operation failed.")
logging.critical("A serious problem occurred.")
logging.exception("Example exception occurred")