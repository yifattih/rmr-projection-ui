def test_mifflinstjeor_rmr_valid(equations, valid_input_data) -> None:
    """
    Test mifflinstjeor_rmr with valid input data.
    """

    sex = valid_input_data["sex"]
    units = valid_input_data["units"]
    age = valid_input_data["age"]
    weight = valid_input_data["weight"]
    height = valid_input_data["height"]
    weight_loss_rate = valid_input_data["weight_loss_rate"]
    duration = valid_input_data["duration"]

    time_projection = [i for i in range(0, duration + 1)]
    rmr = equations.mifflinstjeor_rmr(
        sex, units, age, weight, height, weight_loss_rate, time_projection
    )

    assert rmr is not None
    assert isinstance(rmr, dict)
