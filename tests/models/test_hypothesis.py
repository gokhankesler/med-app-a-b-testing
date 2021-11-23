from models import *

class TestGetSampleSize(object):
    def test_case_one(data):
        expected = 101
        assert expected == get_sample_size(0.8, 0.3, 1.1 ,0.90)

    def test_case_two(data):
        expected = "Increase Max N Value"
        assert expected == get_sample_size(0.95, 0.03, 0.03, 0.90)

# # class TestGetPower(object):
# #     def test_on_type_first_arg(df):
# #         test_argument = pd.DataFrame({'test': [0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]})
# #         expected = 0.55
# #         assert 1 == 1

# # class TestGetPvalue(object):
# #     def test_on_type_first_arg(df):
# #         test_argument = pd.DataFrame({'test': [0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]})
# #         expected = 0.55
# #         assert 1 == 1
