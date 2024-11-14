def get_weight() -> float:
    """
    Prompt the user for their weight and return it as a float.
    """
    weight_str = input("What is your weight in pounds? ")
    return float(weight_str)


def get_height() -> float:
    """
    Prompt the user for their height and return it as a float.
    """
    height_str = input("What is your height in inches? ")
    return float(height_str)


def get_age() -> int:
    """
    Prompt the user for their age and return it as an int.
    """
    age_str = input("What is your age in years? ")
    return int(age_str)


def get_time():
    """
    Prompt the user for the amount of time and return it as an int.
    """
    time_str = input("How many weeks you want to calculate? ")
    return int(time_str)
