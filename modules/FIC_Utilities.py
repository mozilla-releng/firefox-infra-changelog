from datetime import datetime, timedelta


def return_time(time_format=None, operation=None, operation_days=None):
    """
    Utility function that returns the DateTime object taking into account certain passed arguments.
    :param time_format: Takes a string to be used with .strftime("")
    :param operation: Accepts a string containing "add" or "sub" which tells timedelta if we
    need to add or subtract days from the current time.
    :param operation_days: Number of days to add or subtract.
    :return: Object of DateTime
    """
    strformat = None if time_format is None else str(time_format)

    # Check that operation_days is an int or not.
    if operation_days is None:
        pass
    else:
        try:
            int(operation_days)
        except (ValueError, TypeError):
            print("operation_days needs to be an int or float!")
            exit(-1)

    # Simple return.
    if (operation is None) and (operation_days is None):
        if strformat is None:
            return datetime.utcnow()
        else:
            return datetime.now().strftime(strformat)

    # Check if we need to do any addition or subtraction
    elif (operation is not None) and operation_days:
        # Add N days to datetime based on operation_days
        if operation == "add":
            if strformat is None:
                return datetime.now() + timedelta(days=operation_days)
            else:
                time_str = datetime.strftime(datetime.now() + timedelta(days=operation_days), strformat)
                return datetime.strptime(time_str, strformat)

        # Subtract N days from datetime based on operation_days
        elif operation == "sub":
            if strformat is None:
                return datetime.now() - timedelta(days=operation_days)
            else:
                time_str = datetime.now() - timedelta(days=operation_days)
                return datetime.strftime(time_str, strformat)
        else:
            print("Operation {} not supported!".format(operation))
            exit(-1)

    elif ((operation is not None) or (operation_days is not None)) and \
         ((operation is None) or (operation_days is None)):
        print("Both operation and operation_days need to be provided!")
        exit(-1)
