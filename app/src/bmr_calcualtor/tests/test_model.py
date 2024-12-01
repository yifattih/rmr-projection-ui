def test_valid_input(bmr_model, valid_input_data) -> None:
    """
    Test the model with valid input data.
    """
    result = bmr_model.process(valid_input_data)
    assert result["exit_code"] == 0
    assert "rmr" in result["output"]


def test_invalid_age(bmr_model, invalid_age_data) -> None:
    """
    Test the model with an invalid age (out of range).
    """
    result = bmr_model.process(invalid_age_data)
    assert result["exit_code"] == 1
    assert "Invalid age" in result["error"]


def test_negative_duration(bmr_model, valid_input_data) -> None:
    """
    Test the model with a negative duration.
    """
    valid_input_data["duration"] = -1  # Invalid duration
    result = bmr_model.process(valid_input_data)
    assert result["exit_code"] == 1
    assert "Invalid duration" in result["error"]
