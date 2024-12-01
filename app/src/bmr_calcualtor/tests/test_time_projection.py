def test_generate_time_projection_valid(time_projection) -> None:
    """
    Test generate_time_projection with valid input.
    """

    duration = 10
    result = time_projection.calculate(duration)
    assert result["result"].tolist() == list(range(0, duration + 1))


def test_generate_time_projection_negative(time_projection) -> None:
    """
    Test generate_time_projection with negative input.
    """

    duration = -5
    result = time_projection.calculate(end=duration)
    assert "error" in result
