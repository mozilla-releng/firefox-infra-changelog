from datetime import datetime, timedelta


def return_time(input_time=None, input_time_format=None, input_time_unix=False,
                output_time_format=None, operation=None, operation_days=None):
    """
    Utility function that returns the DateTime object taking into account certain passed arguments.
    :param output_time_format: Takes a string to be used with .strftime("")
    :param operation: Accepts a string containing "add" or "sub" which tells timedelta if we
    need to add or subtract days from the current time.
    :param operation_days: Number of days to add or subtract.
    :return: Object of DateTime
    """
    input_strformat = None if input_time_format is None else str(input_time_format)
    output_strformat = None if output_time_format is None else str(output_time_format)

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
        # Return Date + Time in UTC format
        if (output_strformat is None) and not input_time:
            return datetime.utcnow()
        # Return Date + Time in Provided format
        if output_strformat and not input_time:
            return datetime.utcnow().strftime(output_strformat)
        # Return Input time in UTC format.
        elif input_time_unix and not output_strformat:
            return datetime.utcfromtimestamp(int(input_time))
        # Return Time in a specific format, not interpreted from Unix time.
        elif output_strformat and not (input_time_unix or input_time):
            return datetime.now()
        # Return Time in a specific format, from an provided Unix time.
        elif output_strformat and input_time_unix:
            return datetime.utcfromtimestamp(int(input_time)).strftime(output_strformat)
        # Return Time interpreted from a string.
        elif input_time and input_strformat and not (input_time_unix or output_strformat):
            return datetime.strptime(input_time, input_time_format)
        # Return Time in a specific format interpreted from a string.
        elif input_time and input_time_format and output_time_format and not input_time_unix:
            return datetime.strptime(input_time, input_time_format).strftime(output_strformat)
        else:
            exit(13)

    # Check if we need to do any addition or subtraction
    elif (operation is not None) and operation_days:
        # Add N days to datetime based on operation_days
        if operation == "add":
            if output_strformat is None and not input_time:
                return datetime.now() + timedelta(days=operation_days)

            elif output_strformat and not input_time:
                time_str = datetime.strftime(datetime.now() + timedelta(days=operation_days), output_strformat)
                return datetime.strptime(time_str, output_strformat)

            elif input_time_unix and not output_strformat:
                return datetime.utcfromtimestamp(int(input_time)) + timedelta(days=operation_days)

            elif input_time and input_time_unix and output_strformat:

                return datetime.strftime(datetime.utcfromtimestamp(int(input_time)) + timedelta(days=operation_days), output_strformat)

            elif input_time and not (input_time_unix or output_time_format):
                return datetime.strptime(input_time, input_time_format) + timedelta(operation_days)

            elif input_time and output_time_format and not input_time_unix:
                return datetime.strftime(datetime.strptime(input_time, input_time_format) + timedelta(operation_days), output_time_format)
            else:
                exit(13)

        # Subtract N days from datetime based on operation_days
        elif operation == "sub":
            if output_strformat is None and not input_time:
                return datetime.now() - timedelta(days=operation_days)

            elif output_strformat and not input_time:
                time_str = datetime.strftime(datetime.now() - timedelta(days=operation_days), output_strformat)
                return datetime.strptime(time_str, output_strformat)

            elif input_time_unix and not output_strformat:
                return datetime.utcfromtimestamp(int(input_time)) - timedelta(days=operation_days)

            elif input_time and input_time_unix and output_strformat:
                return datetime.strftime(datetime.utcfromtimestamp(int(input_time)) - timedelta(days=operation_days), output_strformat)

            elif input_time and not (input_time_unix or output_time_format):
                return datetime.strptime(input_time, input_time_format) - timedelta(operation_days)

            elif input_time and output_time_format and not input_time_unix:
                return datetime.strftime(datetime.strptime(input_time, input_time_format) - timedelta(operation_days), output_time_format)
            else:
                exit(13)

    elif ((operation is not None) or (operation_days is not None)) and \
         ((operation is None) or (operation_days is None)):
        print("Both operation and operation_days need to be provided!")
        exit(-1)
