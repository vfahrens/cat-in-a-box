import numpy as np # contains arrays
from astropy.time import Time
# from math import * # contains functions like sqrt etc.
# from scipy.constants import * # contains values for G, c, pi etc. (CODATA2014)

from import_catalog import *
from Keplerian_velocities_maxmin import *


# #### calculation of dates:
# # calculate the observation dates from start/end dates and desired number of grid points
# def calc_observations_date(julian_start, julian_end, n_grid):
#     print("Hi to you all! I will start calculating a date now...")
#     duration = julian_end - julian_start
#     julian_dates_list = []
#     for i_date in range(n_grid):
#         julian_dates_list.append(julian_start + ( i_date * duration) / n_grid)
#         # julian_date = julian_start + ( i_date * duration) / n_grid
#         # yield julian_date

#     julian_dates = np.array(julian_dates_list)
#     print("The dates were calculated. Have fun!")
#     return julian_dates





## conversion from TDB-2400000.5 to JD, UTC
T0_dates = Time(T0, format='mjd', scale='tdb')
# T0_UTC = T0_dates.utc
T0_UTC_JD = T0_dates.utc.jd
# print(T0_dates)
# print(T0_UTC_JD)


## start with a chosen date
t_start = Time('2018-05-03 00:00:00', format='iso', scale='utc')
t_start_UTC_JD = t_start.jd
print(t_start_UTC_JD)


T_begin_date = T0_UTC_JD
# print(T_begin_date)
for i in range(number_systems):
    ## add as much periods as necessary to reach the given date
    # T_begin_date = T0_UTC_JD[i]

    while T_begin_date[i] < t_start_UTC_JD:
        T_begin_date[i] += P[i]
        # print(T_begin_date[i])

    print(T_begin_date[i])

    if T_begin_date[i] >= t_start_UTC_JD:
        T_begin_date[i] -= P[i]
        # print(T_begin_date[i])

    print(T_begin_date[i])




## first maximum of measured Keplerian RV after T_begin_date
max_T_beg = []
for i in range(number_systems):
    print(phase_extrema[i,0]*P[i])
    max_T_beg.append(T_begin_date[i] + phase_extrema[i,0]*P[i])
    
print(max_T_beg)

## interesting interval for observation: +-5% of period from max of measured Keplerian RV
interval_max_start = []
for i in range(number_systems):
    interval_max_start.append(max_T_beg[i] - 0.05*P[i])
# print(interval_max_start)

interval_max_end = []
for i in range(number_systems):
    interval_max_end.append(max_T_beg[i] + 0.05*P[i])
# print(interval_max_end)



## first minimum of measured Keplerian RV after T0
min_T_beg = []
for i in range(number_systems):
    min_T_beg.append(T_begin_date[i] + phase_extrema[i,1]*P[i])
    
print(min_T_beg)

## interesting interval for observation: +-5% of period from max of measured Keplerian RV
interval_min_start = []
for i in range(number_systems):
    interval_min_start.append(min_T_beg[i] - 0.05*P[i])
# print(interval_min_start)

interval_min_end = []
for i in range(number_systems):
    interval_min_end.append(min_T_beg[i] + 0.05*P[i])
# print(interval_min_end)



# ## start with a chosen date
# t_start = Time('2018-05-03 00:00:00', format='iso', scale='utc')
# t_start_UTC_JD = t_start.jd
# print(t_start_UTC_JD)



# ## add as much periods as necessary to reach the given date
# blubb = T0_UTC_JD[0]

# while blubb < t_start_UTC_JD:
#     blubb += P[0]

# print(blubb)

# if blubb >= t_start_UTC_JD:
#     blubb -= P[0]

# print(blubb)
