from building_toolbox.preprocesing import *

def test_importer():
    """
    Test the importer function
    """
    # Test the importer function
    path = 'tests/test_data/'
    file_name = 'test_data.csv'
    data = importer(path, file_name)
    assert data.shape == (3, 3)

def test_duplicate_count():
    """
    Test the duplicate_count function
    """
    # Test the duplicate_count function
    path = 'tests/test_data/'
    file_name = 'test_data.csv'
    data = importer(path, file_name)
    count = duplicate_count(data)
    assert count == 2

    def test_drop_duplicates():
        """
        Test the drop_duplicates function
        """
        # Test the drop_duplicates function
        path = 'tests/test_data/'
        file_name = 'test_data.csv'
        data = importer(path, file_name)
        data = drop_duplicates(data)
        assert data.shape == (2, 3)
