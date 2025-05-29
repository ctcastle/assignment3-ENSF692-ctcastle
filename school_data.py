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
def gen_school_dict(enrollment_data):
    return 0 

def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    total_arr = np.array([year_2013,year_2014,year_2015,year_2016,
                 year_2017,year_2018,year_2019,year_2020,
                 year_2021,year_2022]) 
    y_s_g_arr = total_arr.reshape((10,20,3))
    s_y_g_arr = np.swapaxes(y_s_g_arr,0,1) 
    print("array number of dimensions: ", s_y_g_arr.ndim)
    print("array shape: ", s_y_g_arr.shape)
    print("array size: ", s_y_g_arr.size)
    print(s_y_g_arr)
    # Prompt for user input

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

