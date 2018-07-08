import pandas as pd
ad_clicks = pd.read_csv("ad_clicks.csv")

#Inspect first few rows of the csv file.
#print (ad_clicks.head(5))


#Finding which source gets more views.
most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(most_views)
most_views.to_csv("Most_views.csv")


#Check if the link is clicked or not.
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
#print (ad_clicks.head(10))
ad_clicks.to_csv("Clicked_or_not.csv")


#Percentage of people clicking the ad from various sources.
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
#print (clicks_by_source)
clicks_by_source.to_csv("No_of_clicks_by_source.csv")

clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()
#print(clicks_pivot)
clicks_pivot.to_csv("No_of_clicks_pivot_table.csv")

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)
clicks_pivot.to_csv("Percentage_of_user_clicks.csv")


#Total number of people in each experimental group.
people_shown_ads = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(people_shown_ads)
people_shown_ads.to_csv("No_of people_in_each_group.csv")


#Finding out which group had greater click percentage.
more_ad_clicks = ad_clicks.groupby(['is_click','experimental_group']).user_id.count().reset_index()
#print(more_ad_clicks)
more_ad_clicks_pivot = more_ad_clicks.pivot(columns = 'is_click',index = 'experimental_group', values = 'user_id').reset_index()
#print(more_ad_clicks_pivot)
more_ad_clicks_pivot["percent_clicked"] = more_ad_clicks_pivot[True] / (more_ad_clicks_pivot[True] + more_ad_clicks_pivot[False])
#print(more_ad_clicks_pivot)
more_ad_clicks_pivot.to_csv("The_better_group.csv")


#Checking the number of clicks in experimental group per day.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
#print(a_clicks)
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#print(b_clicks)

a_clicks_by_day = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
a_clicks_by_day_pivot = a_clicks_by_day.pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()
a_clicks_by_day_pivot["percent_clicked"] = a_clicks_by_day_pivot[True] / (a_clicks_by_day_pivot[True]+a_clicks_by_day_pivot[False]) * 100
#print(a_clicks_by_day_pivot)
a_clicks_by_day_pivot.to_csv("Percentage_of_A_clicks_by_day.csv")

b_clicks_by_day = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_clicks_by_day_pivot = b_clicks_by_day.pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()
b_clicks_by_day_pivot["percent_clicked"] = b_clicks_by_day_pivot[True] / (b_clicks_by_day_pivot[True]+b_clicks_by_day_pivot[False]) * 100
#print(b_clicks_by_day_pivot)
b_clicks_by_day_pivot.to_csv("Percentage_of_B_clicks_by_day.csv")