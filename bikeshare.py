import time
import pandas as pd
import numpy as np
import statistics

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    city = input('Choose a number')

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please, choose a city (chicago, new york city or washington):_')
    city=city.lower()
    while city not in ['chicago','new york city','washington']:
        print('That is not one of our options today. Please, try again')
        city=input('Please, choose a city between chicago, new york city and washington:_')
  
    filt = input('Would you like to filter the data by month, day, both or none? Please type 1 for month, 2 for day, 3 for both, 4 for none:_')
    while filt not in ['1','2','3', '4']:
        print('Please type 1, 2, 3 or 4:_')
        filt=input('Would you like to filter the data by month, day, both or none? Please type 1 for month, 2 for day, 3 for both, 4 for none:_')
    # TO DO: get user input for month (all, january, february, ... , june)
    day= 'all'
    month = 'all'
    if (filt == '1' or filt == '3'):
        month = input('Please type a month from January to June:_')
        month = month.lower()
        while month not in ['january', 'february','march','april','may','june']:
            month= input('please type a month from january to june:_')
    if (filt == '2' or filt == '3'):
        day = input('Please type a number from 1 to 7 to indicate a day of the week:_')
        while day not in ['1','2','3','4','5', '6','7']:
            day = input('Please type a number from 1 to 7 to indicate a day of the week:_')

    
           

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city=city.replace(" ","_")
    df=pd.read_csv("{}.csv".format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    if day != 'all':
        # filter by day of week to create the new dataframe
        #weekdays =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        #weekdayx =weekdays.index(day)
        df = df[df['day_of_week']== int(day)-1]
        
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        monthx = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==monthx]

    # filter by day of week if applicable
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=statistics.mode(df['month'])
    print('Most Frequent month: ',popular_month)


    # TO DO: display the most common day of week
    popular_day=statistics.mode(df['day_of_week'])
    print('Most Frequent day: ',int(popular_day)+1)

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = statistics.mode(df['hour'])
    
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = statistics.mode(df['Start Station'])
    print('Most Frequent Start Station:', popular_start_station)
    


    # TO DO: display most commonly used end station
    popular_end_station = statistics.mode(df['End Station'])
    print('Most Frequent End Station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['start_to_end']=df['Start Station']+' '+df['End Station']
    popular_start_end = statistics.mode(df['start_to_end'])
    print('Most Frequent Start-End trip:', popular_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=sum(df['Trip Duration'])
    print('Total travel time: ',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time=statistics.mean(df['Trip Duration'])
    print('Mean travel time: ',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    


    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print(gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    common_year=statistics.mode(df['Birth Year'])
    earliest = min(df['Birth Year'])
    recent = max(df['Birth Year'])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def main():
    df0=pd.read_csv('chicago.csv')
    print(df0.info())
    df1=df0[df0['Start Station']==df0['End Station']]
    print(df1.info())
    while True:
        city, month, day = get_filters()
   
        df = load_data(city, month, day)
        
        i=0
        head = input('Would you like to see a sample of the data? Enter Yes or No.')
        head = head.lower()
        while head =="yes":
            print(df.iloc[i:].head())
            i+=5
            head = input('Would you like to see another sample of the data? Enter Yes or No.')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city in ['new york city','chicago']:
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
