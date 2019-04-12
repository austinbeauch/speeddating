import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model

# This code is calculating the matching rate base on how much do the participant rate for specific interest
# It can be rate from 1 to 10; 1 is less interest and 10 is most interest
# There are 17 interests can be rated; therefore, there are 17 graphs output
# All the output graphs have been saved in the folder "interest_matching_rate_output"

def main():
    # You can switch "gaming" to any other interest to calculate the matching rate
    # for specific interest
    # ['sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing',
    #  'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga']
    # 17 interests
    fields = ['wave', 'iid', 'pid', 'match', 'gaming', 'round']
    data = pd.read_csv("data/Speed-Dating-Data.csv", encoding="windows-1252", skipinitialspace=True, usecols=fields)

    data_value = data.values
    # print(data)

    # store amount of people for each waves
    wave_ppl = np.zeros(21)
    cur_wave = 1
    for d in data_value:
        if int(d[1]) != cur_wave:
            cur_wave = int(d[1])
        else:
            wave_ppl[cur_wave - 1] = int(d[2])

    # print("wave_ppl :")
    # print(wave_ppl)
    # print("==========")

    # calculate the match rate
    # count how many matches for one peron in each waves
    match_rate = []
    total_count = np.zeros(552)
    for i, d in enumerate(data_value):
        if d[4] == 1:
            cur_num = int(d[0] - 1)
            total_count[cur_num] += 1

    # print("total_count: ")
    # print(total_count)

    # store all the waves total people for each person
    round_number = np.zeros(552)
    for d in data_value:
        cur = int(d[0]) - 1
        round_number[cur] = int(d[2])

    # ignore all the nan value -- no data
    np.seterr(divide='ignore', invalid='ignore')

    # calculate the average match rate for all the participant
    match_rate = np.divide(total_count, round_number)
    # print("match_rate: ")
    # print(match_rate)

    # count for total people in any level of interest
    interest = np.zeros(552)
    for d in data_value:
        if str(d[5]) != 'nan':
            cur = int(d[0]) - 1
            interest[cur] = int(d[5])
        else:
            cur = int(d[0]) - 1
            interest[cur] = 0
    # print(interest)

    # store the result into a dictionary base on the level of the interest
    # it calculate the average when making the dictionary
    relationship_interest = dict(zip(interest, match_rate))
    # print(len(relationship_interest))

    # build the matching rate array base on the dictionary data
    match_result = np.zeros(10)
    for key, value in relationship_interest.items():
        if int(key) < 10:
            cur_exercise = int(key) - 1
            match_result[cur_exercise] = value

    match_result = np.dot(match_result, 100)
    # print(match_result)
    print("The graph have been created.")

    # draw the ouput (diagram)
    rating = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plt.bar(rating, match_result)
    plt.title('gaming')
    plt.xticks(np.arange(0, 11, 1))
    plt.axis([0, 10, 0, 100])
    plt.xlabel('interest of gaming (rate from 1-10)')
    plt.ylabel('matching rate (%)')
    plt.show()

    # output the png file
    # plt.savefig("gaming.png")


if __name__ == "__main__":
    main()
