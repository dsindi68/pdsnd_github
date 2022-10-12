import pandas as pd

import time
import pandas as pd
import numpy as np
day=0
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
 print('What city you want to load chicago,new york city,washington or all')
 city = input("Enter your value: ")
 print(city) 
 while (city.lower() not in  ['chicago','new york city','washington'] or city is None):
     print('Please select one of the city  or all ')
     city = input("Enter your value: ")
     print(city) 
 print('What month january, february, march, april, may, june or all')
 month = input("Enter your value: ")           
 print(month) 
 while (month.lower() not in  ['january', 'february', 'march', 'april', 'may', 'june'] or month is None):
    print('Please select one of the month january, february, march, april, may, june or all ')
    month = input("Enter your value: ")
    print(month) 
 print('What day please in integer')
 global day
 day=0
 day= input("Enter your value: ")     
 print(day)
 while (not (str(day).isdigit()) or (int(day)<1 or int(day)>7) ):
    print('Please select day from 1 to 7 ')
    day = input("Enter your value: ")
    print(day) 
   
 return (city.lower(),month.lower(),day) 

def load_data(city, month, day):
 df_temp= list()
 for key in CITY_DATA:
     if(key==city):
         df=pd.read_csv(CITY_DATA[key]) 
 if city =='all':
     cities= ['chicago','new york city','washington']
     for key in CITY_DATA:
            data_temp = pd.read_csv(CITY_DATA[key])
            df_temp.append(data_temp)
     df = pd.concat(df_temp, ignore_index=True , sort=True) 

 df['month'] = pd.DatetimeIndex(df['Start Time']).month 
    # TO DO: get user input for month (all, january, february, ... , june)
 months = ['january', 'february', 'march', 'april', 'may', 'june']
 df['Start Time'] = pd.to_datetime(df['Start Time'])
 for x in months:
   if (x == month):
        df = df[df['month'] ==  months.index(x)+1]
 
 WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.day_name() 

 for index in range(len(WEEKDAYS)):
    if int(index+1)== int(day):
          df =df[df['day_of_week'] ==  WEEKDAYS[index]]
            
 return df

def time_stats(df):
  # "Displays statistics on the most frequent times of travel."
 #print('\nCalculating The Most Frequent Times of Travel...\n')
   # start_time = time.time()

    # TO DO: display the most common month
  start_time = time.time()
  print('-------Selected Month--------')
  popular_month=df['month'].mode()[0]
  print(popular_month)
   # TO DO: display the most common day of week
  df['week'] = df['Start Time'].dt.week
  print('-------WEEK--------') 
  popular_week = df['week'].mode()[0]
  print(popular_week)
    # TO DO: display the most common start hour
  print('-------HOUR--------')
  df['hour'] = df['Start Time'].dt.time
   
# find the most popular hour
  popular_hour = df['hour'].mode()[0]
  print(popular_hour)
  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)
  return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('-------start_station--------')
    print(popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('-------end_station--------')
    print(popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].describe()[:1])

    # TO DO: display mean travel time
    print(df['Trip Duration'].describe()[:2])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n user type...\n')
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
       print('\n Gender...\n')
       print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birthno
    if 'Birth Year' in df.columns:
     print('\n most common year...\n')
     print(df['Birth Year'].mode())
     print('\n most recent year...\n')
     print(df['Birth Year'].max())
     print('\n earliest year...\n')
     print(df['Birth Year'].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
 start_loc = 0
 view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
 while view_data.lower()=='yes':
   print(df.iloc[start_loc:start_loc+5])
   start_loc += 5
   view_data = input("Do you wish to continue?: ").lower()    
 return  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

