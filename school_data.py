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
    #print(s_y_g_arr) #Testing array 
    # Prompt for user input
    userInput = input("Please enter the school id or school name for desired report: ")
    used_ID = True 
    if userInput.isdigit() and int(userInput) in school_ids:
        print('ID')
    elif userInput in school_names:
        used_ID = False 
        print('NAME')
    else:
        raise ValueError 
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
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
    print(f'{school_ID}: {school_name}')
    #Mean enrollment for Grade 10 
    print(s_y_g_arr[school_index,:,0].mean(dtype=np.integer))
    #Mean enrollment for Grade 11 
    print(s_y_g_arr[school_index,:,1].mean(dtype=np.integer))
    #Mean enrollment for Grade 12 
    print(s_y_g_arr[school_index,:,2].mean(dtype=np.integer))
    #Highest enrollment for a single grade with the entire 10 year period 
    print(int(s_y_g_arr[school_index,:,:].max()))
    #Highest enrollemnt for a single grade within the entire 10 year time period 
    print(int(s_y_g_arr[school_index,:,:].min()))
    #Total enrollment for each year from 2013 to 2022 
    for i in range(10):
        print(int(s_y_g_arr[school_index,i,:].sum()))
    #Total ten year enrollment 
    print(int(s_y_g_arr[school_index,:,:].sum()))
    #Mean total enrollment over 10 years 
    print(int(s_y_g_arr[school_index,:,:].sum()/s_y_g_arr[school_index,:,0].size))
    #ANY enrollment over 500, print the median value of those enrollments, else No enrollments over 500 
    print(s_y_g_arr[school_index,:,:])
    print(s_y_g_arr[school_index,s_y_g_arr[school_index,:,:] > 500])
    print(np.median(s_y_g_arr[school_index,s_y_g_arr[school_index,:,:] > 500]))




    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    sub_2013 = s_y_g_arr[:,0,:]
    sub_2022 = s_y_g_arr[:,-1,:]
    sub_2022 = sub_2022[~np.isnan(sub_2022)]
    grad = s_y_g_arr[:,9,2]
    grad = grad[~np.isnan(grad)]
    filtered = s_y_g_arr[~np.isnan(s_y_g_arr)]
    print(sub_2013.mean(dtype=np.integer))
    print(sub_2022.mean(dtype=np.integer))
    print(grad.sum())
    print(filtered.max())
    print(filtered.min())

if __name__ == '__main__':
    main()

