import pandas as pd
from features import truncated_mean

class TestTruncatedMean(object):
    def test_on_functionality_truncated_mean(data):
        test_argument = pd.DataFrame({'test': [0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]})
        expected = 0.55
        assert expected == truncated_mean(test_argument)[0]
