# Meditation App A/B Testing

This project implements A/B testing of a mobile app that offers meditation services for a paid subscription as well as one-off in-app purchases. 

## 1. Introduction
The app is growing quickly and motivation is to maintain a strong free-trial to paying user conversion rate. Additionally, we want to maintain strength in a variety of other business areas as we will see. While this is a very specific example, we can imagine interchanging users, meditation-app, and purchases with other nouns and KPIs, and the same mathematical techniques would still apply.

## 2. Datasets
There are two data-sets related to app. 

### I. User demographics
First is a set of user demographics, tied to a unique user id number.
```
uid	        reg_date	          device  gender  country  age
54030035.0	2017-06-29T00:00:00Z  and	  M	      USA	   19
72574201.0	2018-03-05T00:00:00Z  iOS	  F	      TUR	   22
64187558.0	2016-02-07T00:00:00Z  iOS	  M	      USA	   16
```
### II. User actions
The second data contains the date the trial period ended, the date of purchase if they purchased, and the price they paid upon subscribing (in cents).
```
date        uid       sku            price
2017-07-10  41195147  sku_three_499  499
2017-07-15  41195147  sku_three_499  499
2017-11-12  41195147  sku_four_599   599
```

## 3. KPI: Conversion Rate
One question in defining our KPI is over what interval should we consider the conversion rate? The conversion immediately after lapse? one week after? One month? One way to decide this is to see the generalizability of these statistics across different demographic groups. Stability in this way is desired so we don't need custom KPIs for each breakdown. A second is to see if one is more correlated with important factors like retention or spending than the others.
