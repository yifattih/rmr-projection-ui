"""
Equations Coefficients Module
----------
Coefficients for the equations defined below.

MIFFLINSTJEOR
----------
For the Mifflin-St. Jeor equations:
        For male:
                SI units system:
                        BMR = 10*weight + 6.25*height - 5*age + 5

                        weight in kilograms | height in meters | age in years

                Imperial units system:
                        BMR = 4.536*weight + 15.875*height − 5*age + 5

                        weight in pounds | height in inches | age in years

        For female:
                SI units system:
                        BMR = 10*weight + 6.25*height - 5*age - 161

                        weight in kilograms | height in meters | age in years


                Imperial units system:
                        BMR = 4.536*weight + 15.875*height − 5*age − 161

                        weight in pounds | height in inches | age in years

Returns:
----------
MIFFLINSTJEOR : dict
        Dictionary containing equations constants by sex and system of units.
"""

MIFFLINSTJEOR = {
    "male": {
        "imperial": {"weight": 4.536, "height": 15.875, "age": -5, "bias": 5},
        "si": {"weight": 10.0, "height": 6.25, "age": -5, "bias": 5.0},
    },
    "female": {
        "imperial": {
            "weight": 4.536,
            "height": 15.875,
            "age": -5,
            "bias": -161,
        },
        "si": {"weight": 10, "height": 6.25, "age": -5, "bias": -161},
    },
}
