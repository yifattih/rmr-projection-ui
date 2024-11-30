"""
Equations Coefficients Module

Returns:
----------
MIFFLINSTJEOR : dict
        Dictionary containing equations constants by sex and system of units.
"""

MIFFLINSTJEOR = {"male": {"imperial": {"weight": 4.536, 
                                       "height": 15.875,
                                       "age": -5,
                                       "bias": 5.0},
                          "si": {"weight": 10.0,
                                     "height": 6.25,
                                     "age": -5,
                                     "bias": 5.0}}, 
                "female": {"imperial": {"weight": 4.536,
                                        "height": 15.875,
                                        "age": -5,
                                        "bias": -161},
                           "si": {"weight": 10,
                                  "height": 6.25,
                                  "age": -5,
                                  "bias": -161}
                           }
                }
                