from buliding_toolbok.preprocessing import importing_data, duplicate_count, drop_duplicates
import pandas as pd

def test_duplicate_count():
    """
    Test the duplicate_count function.
    """
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    assert duplicate_count(data) == 0
