#!/usr/bin/env python
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


def calculate_conversion_rate(df, days):
    """ Return conversion rate

    Args:
        df ([DataFrame]): [description]
        days ([int]): Number of last days

    Returns:
        [int]: Conversion rate
    """
    current_date = df.reg_date.max()
    lapse_date = pd.to_timedelta(days, 'd')
    max_lapse_date = current_date - lapse_date
    conv_sub_data = df[df.reg_date < max_lapse_date]
    total_users_count = conv_sub_data.price.count()
    max_sub_date = conv_sub_data.reg_date + lapse_date
    total_subs = conv_sub_data[(conv_sub_data.price > 0) & (
        conv_sub_data.date < max_sub_date)]
    total_subs_count = total_subs.price.count()
    conversion_rate = total_subs_count / total_users_count

    return conversion_rate


def gc7(sub_date):
    total = sub_date.count()
    sub = sum(sub_date < 7)
    return (sub / total)
