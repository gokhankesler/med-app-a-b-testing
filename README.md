# Medication App A/B Testing

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

## III. KPI: Conversion Rate
For now, let’s consider the KPI of conversion rate. We will consider a variety of others throughout the course. One question in defining our KPI is over what interval should we consider the conversion rate? The conversion immediately after lapse? one week after? One month? One way to decide this is to see the generalizability of these statistics across different demographic groups. Stability in this way is desired so we don't need custom KPIs for each breakdown. A second is to see if one is more correlated with important factors like retention or spending than the others.

6. Joining the demographic and subscription data
To begin answering these questions, we must match our demographics data to our subscription data so that we can explore specific relationships. We will do this with the pandas merge() method. This performs the equivalent of a SQL join on two dataFrames. There are two ways to call this method, either as a method of pandas or as a method of a dataFrame object. We will only consider the latter case here but they are equivalent.

7. Merging mechanics
As in SQL we have a left and right table. We call the merge method on one of our dataFrames, and this is considered the left dataFrame. In this case our demographics dataset. Next, we specify the right dataFrame as our first argument, in this case the subscription data. Then, we specify the `how` argument. This can be one of four values: inner, outer, left, or right, each analogous to a sql join. Understanding SQL is not important for this course, it suffices to say that these arguments specify the behavior of which rows are returned in the final output. For our purpose we will use an inner join which returns all rows that are matched between the two dataFrames. The next argument is the `on` argument. This is a list of fields, that appear in both dataFrames, which we want to match the rows on. There is a way to specify this argument when the columns differ in name, but we will not cover that here. We will match on the `uid`. As we can see in the output, the rows are associated with a corresponding row from the other dataFrame.

8. Next steps
Our next step is to aggregate our newly combined data set and to calculate the potential KPIs we are interested in.

9. Let's practice!
The exercises will allow you to practice the techniques covered here with another interesting aspect of our mediation app data. Good luck!