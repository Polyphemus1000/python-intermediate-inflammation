from unittest.mock import Mock
import unittest
import numpy as np

def test_analyse_data_mock_source():
    from inflammation.compute_data import analyse_data
  

    mock_raw_data = [
        np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), # Patient 1 data
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Patient 2 data
        ]

    data_source = Mock()

    data_source.load_information_data.return_value = mock_raw_data

# 4. Mock the 'views.visualize' function
# We don't want to actually show a plot during the test.
# # We'll use a patch to temporarily replace views.visualize with a Mock.
   # with unittest.mock.patch('inflammation.views.visualize') as mock_visualize:
        # 5. Call the function under test with the mock DataSource
    analyse_data(data_source)

         # 6. Assertions:
        # Verify that load_information_data was called exactly once
    data_source.load_information_data.assert_called_once()

            # Verify that visualize was called (and inspect its arguments if needed)
    #mock_visualize.assert_called_once()

            # We can also check the data that was passed to visualize
            # Calculate the expected standard deviation manually
            # Based on mock_raw_data:
            # Patient 1: daily_mean = [0.33, 0.33, 0.33]
            # Patient 2: daily_mean = [0.33, 0.33, 0.33]
            # means_by_day_matrix (after np.stack and daily_mean application) would look like:
            # [[0.333..., 0.333..., 0.333...],
            #  [0.333..., 0.333..., 0.333...]]
            # The standard deviation across rows for each column will be 0.0
    expected_std_dev = np.array([0., 0., 0.])

            # Get the arguments passed to visualize
    #args, kwargs = mock_visualize.call_args
        #actual_graph_data = args[0] # The first argument is the dictionary

            # Assert that the 'standard deviation by day' data matches our expectation
        #np.testing.assert_array_almost_equal(
       # actual_graph_data['standard deviation by day'],
        #expected_std_dev )
  



