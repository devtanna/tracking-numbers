from tracking_numbers import get_tracking_number


def test_usps_not_confused_for_dhl():
    """Tests that a USPS number is not mistakenly considered to be DHL. This occurs
    if we don't do a full match on the regex, since DHL numbers are syntactically
    short USPS numbers (for the most part).
    """
    tracking_number = get_tracking_number("9405511108078863434863")

    assert tracking_number is not None
    assert tracking_number.courier.code == "usps"

def test_text_extraction():
    """ Tests that a tracking number can be extracted from a string of text.
        Taking into consideration word boundaries.
    """

    tracking_number = get_tracking_number("This is a test! 9405511108078863434863 TrackingCode")

    assert tracking_number is not None
    assert tracking_number.courier.code == "usps"
    assert tracking_number.number == "9405511108078863434863"
