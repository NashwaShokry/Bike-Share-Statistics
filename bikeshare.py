import time
import pandas as pd
import numpy as np

# Define global variables

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = [ 'all', 'monday', 'tuesday', 'wednesday', 
            'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in CITY_DATA:
        city = input("Please select a city from the following:\n     {}\n".format(list(CITY_DATA.keys())))
    city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month.lower() not in MONTHS:
        month = input("Which month do you want? Select from the following:\n     {}\n".format(MONTHS))
    month = month.lower()
 
     # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.lower() not in DAYS:
        day = input("Which day of week do you want? Select from the following:\n    {}\n".format(DAYS))
    day = day.lower()

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
    # Print selected data
    print('Analyzing data for '+ city.title())
    if month != 'all':
        print ('Month: {}'.format(month.title()))
    if day != 'all':
        print ('Day: {}'.format(day.title()))
    print('-'*40)
    # Load data for the selected city
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the MONTHS list to get the corresponding int
        month = MONTHS.index(month)
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    if day != 'all':
        # use the index of the DAYS list to get the corresponding int
        day = DAYS.index(day)-1 #subtract one as Monday has a value 0
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]    

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month (only if there no filter for months)
    if month == 'all':
        print("The most popular month is: {}\n".format(MONTHS[df['month'].mode()[0]].title()))

    # display the most common day of week (only if there is no filter for days)
    if day == 'all':
        print("The most frequent day is: {}\n".format(DAYS[df['day_of_week'].mode()[0]+1].title()))

    # display the most common start hour
    print("And the most common start hour is: {}".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: {}\n".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("And the most commonly used end station is: {}\n".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    favourite_trip = df.groupby(['Start Station','End Station']).size().idxmax()
    print("While the most common trip is from {} to {}".format(favourite_trip[0], favourite_trip[1] ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    start_time = time.time()
    print('\nCalculating Trip Duration...\n')
    
    # display total travel time
    print( "Total travel time is: {}\n".format(
        pd.Timedelta(seconds=df['Trip Duration'].sum())))

    # display mean travel time
    print( "Average trip duration is: {}".format(
        pd.Timedelta(seconds=df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Number of trips by user types:\n')
    print(df.groupby(['User Type']).size())

    # Display counts of each gender if the gender column exists
    if 'Gender' in df.columns:
        print('\nNumber of trips by user gender:\n')
        print(df.groupby(['Gender']).size())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nStatistics by user's birth year:\n")
        print("Earliest year is: {},\n most recent year is: {}\n and most common year: {}".format(
            int(df['Birth Year'].min()), int(df['Birth Year'].max())
            , int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        #Show a sample of data
        while True:
            if input('\nWould you like to view a sample of data? Enter yes or no.\n') == 'yes':
                print("Showing sample of 5 data rows:")
                print(df.drop(['month','day_of_week','hour'], axis=1).sample(5))
            else:
                break
        
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
