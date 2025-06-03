# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
school_names = ['Centennial High School','Robert Thirsk School','Louise Dean School',
                'Queen Elizabeth High School','Forest Lawn High School','Crescent Heights High School',
                'Western Canada High School','Central Memorial High School','James Fowler High School',
                'Ernest Manning High School','William Aberhart High School','National Sport School',
                'Henry Wise Wood High School','Bowness High School','Lord Beaverbrook High School',
                'Jack James High School','Sir Winston Churchill High School','Dr. E. P. Scarlett High School',
                'John G Diefenbaker High School','Lester B. Pearson High School']
school_ids = [1224,1679,9626,9806,9813,9815,9816,9823,9825,9826,
              9829,9830,9836,9847,9850,9856,9857,9858,9860,9865]

# You may add your own additional classes, functions, variables, etc.
class SchoolStats:
    """Class for generating statistics around a given school's enrollment data.
    The class provides nan-safe functions, meaning all functions will ignore nan values entirely, 
    assuming that the data is not available for the given range, year, school, etc."""
    def __init__(self, name, id, arr):
        self.name = name 
        self.id = id 
        self.arr = arr 
    def grade_mean(self,grade):
        """
        Calculates the mean of a school's enrollment data for a given grade
        
        Args:
            grade (int): The desired grade to find the mean enrollment of 
        Returns:
            int: Nansafe mean of the school and grade's enrollment
            OR
            NAN: If incorrect input
        """
        match grade:
            case 10:
                return int(np.nanmean(self.arr[:,0])) 
            case 11: 
                return int(np.nanmean(self.arr[:,1])) 
            case 12: 
                return int(np.nanmean(self.arr[:,2])) 
            case _:
                return np.nan 
    def total_mean(self):
        """
        Calculates the mean for the school's entire range of input data
        
        Args: None 
        Returns:
            int: Total mean of the school's enrollment over entire range of data
        
        """
        return int(np.nansum(self.arr)/np.nansum(~np.isnan(self.arr[:,0])))
    def median_of_500_plus_enrollments(self):
        """
        Calculates the median value of all enrollments greater than 500
        
        Args: None
        Returns: 
            int: Median value of all enrollments over 500 
            OR 
            String: Info that no enrollments were over 500 for this school 
        """
        sub_arr = self.arr[self.arr > 500] 
        if sub_arr.size > 0:
            return int(np.nanmedian(sub_arr))
        else:
            return "No enrollments over 500"
    def max_enroll(self):
        """
        Outputs the nansafe max value of the school's entire enrollment data
        
        Args: None 
        Returns: 
            int: Nansafe max value of school's entire enrollment data 
        """
        return int(np.nanmax(self.arr))
    def min_enroll(self):
        """
        Outputs the nansafe min value of the school's entire enrollment data"""
        return int(np.nanmin(self.arr))
    def enroll_per_year(self,year):
        """
        Outputs the nansafe sum of the enrollment data of a school for a particular year
        
        Args: 
            year (int): Index of which specified year of which to find total enrollment [0-9: corresponding to 2013-2022]
        Returns: 
            int: The total enrollment for that school during that year, zero if all values are nan 
        """
        return int(np.nansum(self.arr[year,:]))
    def total_enroll(self):
        """
        Outputs the nansafe sum of the total enrollment data for a given school across all years of available data

        Args: None
        Returns: 
            int: Total enrollment for the school over the entire data range 
        """
        return int(np.nansum(self.arr))
    
def inputParser(userInput):
    """
    Processes user input and returns the school id, name, and associated data index of the school from which statistical information is desired.
    If the input field is invalid data, a ValueError is raised
    
    Args: 
        userInput (String): The name or school id of the school on which statistics are desired 
    Returns: 
        int: The 4 digit code of the school 
        String: The name of the school 
        int: The index of the desired school in the numpy array holding it's enrollment data 
    """
    used_ID = True 
    if userInput.isdigit() and int(userInput) in school_ids:
        print('ID')
    elif userInput in school_names:
        used_ID = False 
        print('NAME')
    else:
        raise ValueError 

    index = list(range(20))
    school_id_dict = dict(zip(school_ids,index))
    school_name_dict = dict(zip(school_names,index))
    #School name and code 
    if used_ID:
        school_ID = int(userInput)
        school_index = school_id_dict[school_ID]
        school_name = school_names[school_index]
    else: 
        school_name = userInput 
        school_index = school_name_dict[school_name]
        school_ID = school_ids[school_index]
    return school_ID, school_name, school_index 

def main():

    print("ENSF 692 School Enrollment Statistics")
    # Print Stage 1 requirements here
    total_arr = np.array([year_2013,year_2014,year_2015,year_2016,
                 year_2017,year_2018,year_2019,year_2020,
                 year_2021,year_2022]) # Aggregating data into one large numpy array 
    y_s_g_arr = total_arr.reshape((10,20,3)) # Reshaping data to usable form 
    s_y_g_arr = np.swapaxes(y_s_g_arr,0,1)  #Reshaping again for personal preference 
    print("Dimensions of full data array: ", s_y_g_arr.ndim)
    print("Shape of full data array: ", s_y_g_arr.shape)
    print("Total data array size: ", s_y_g_arr.size)

    # Prompt for user input
    userInput = input("Please enter the school id or school name for desired report: ")
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    # Attempting to parse user input, if invalid the program will let the user know and exit 
    try:
        school_ID, school_name, school_index = inputParser(userInput)
    except ValueError:
        print('You must enter a valid school id or name to continue')
        return
    
    # Creating the school object for the desired school to perform analysis on
    school = SchoolStats(school_name, school_ID, s_y_g_arr[school_index,:,:]) 
    print(f'School ID - {school.id}: Name - {school.name}')

    # Mean enrollment for Grade 10 
    print(f'Mean enrollment for Grade 10: {school.grade_mean(10)}')

    # Mean enrollment for Grade 11 
    print(f'Mean enrollment for Grade 11: {school.grade_mean(11)}')

    # Mean enrollment for Grade 12 
    print(f'Mean enrollment for Grade 12: {school.grade_mean(12)}')

    # Highest enrollment for a single grade with the entire 10 year period 
    print(f'Highest enrollment for a single grade: {school.max_enroll()}')

    # Lowest enrollment for a single grade within the entire 10 year time period 
    print(f'Lowest enrollment for a single grade: {school.min_enroll()}')
    
    # Total enrollment for each year from 2013 to 2022 
    for i in range(10):
        print(f'Total enrollment for {i+2013}: {school.enroll_per_year(i)}')
    # Total ten year enrollment 
    print(f'Total ten year enrollment: {school.total_enroll()}')
    # Mean total enrollment over 10 years 
    print(f'Mean total enrollment over 10 years: {school.total_mean()}')
    # ANY enrollment over 500, print the median value of those enrollments, else No enrollments over 500 
    print(f'Median value of enrollments over 500: {school.median_of_500_plus_enrollments()}')




    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    print(f'Mean enrollment in 2013: {int(np.nanmean(s_y_g_arr[:,0,:]))}')
    print(f'Mean enrollment in 2022: {int(np.nanmean(s_y_g_arr[:,-1,:]))}')
    print(f'Total graduating class of 2022: {int(np.nansum(s_y_g_arr[:,-1,2]))}')
    print(f'Highest enrollment for a single grade: {int(np.nanmax(s_y_g_arr))}')
    print(f'Lowest enrollment for a single grade: {int(np.nanmin(s_y_g_arr))}')

if __name__ == '__main__':
    main()

