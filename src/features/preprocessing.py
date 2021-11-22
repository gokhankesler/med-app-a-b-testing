import pandas as pd

def truncated_mean(data):
    """Compute the mean and excluding outliers.

    Args:
        data (DataFrame): Pandas dataframe.

    Returns:
        int: Mean of the column.
    """
    top_val = data.quantile(0.9)
    bot_val = data.quantile(0.1)
    trunc_val = data[(data <= top_val) & (data >= bot_val)]
    mean = trunc_val.mean()
    return (mean)
