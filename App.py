from logger import Logger

logger = Logger().get_logger()

def main():
    logger.info("Application started.")

    try:
        # Your application logic here
        logger.debug("Performing calculations...")
        # Simulate a calculation
        result = 10 / 2  # Example calculation
        logger.info(f"Calculation result: {result}")

        # Simulate additional operations
        logger.debug("Performing more operations...")
        result = 10 / 5  # Another example calculation
        logger.info(f"Another calculation result: {result}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

    logger.info("Application finished.")

if __name__ == "__main__":
    main()
    