# Debug: Detailed information,typiclly of interest only when diagnosing problem
# info: Conformation that things are working as expected
#warning: an indicaton that something unexpected,or indicative of some problem in near future e.g:'disk space low' the software is still working as expectedd 
# Error: Due to a more serious problem,that software has not been able to performed some function.
#Critical:A serious error,indicating that the program itself may be unable to continue running.

import logging

# Configure logging to save messages to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    x = int(input("Enter a number: "))
    logging.debug("User entered value: %s", x)  # DEBUG level logging
    result = 10 / x  # This might cause a division by zero error
    logging.info("Calculation completed successfully.")  # INFO level logging
    print(f"Result: {result}")
except ZeroDivisionError as e:
    logging.error("Division by zero error: %s", e)  # ERROR level logging
    print("Error: Cannot divide by zero")
except ValueError as e:
    logging.error("Invalid input: %s", e)  # ERROR level logging
    print("Error: Please enter a valid number")
