import numpy as np
import pandas as pd
from sklearn.metrics import jaccard_similarity_score

# This code calculate two people's similarity base on only their intersets
# by using jaccard similarity to predict the matching result
# If the jaccard similarity > 0.5, we assume it is a match
# After calculating the prdict model, it will compare to the real matching result
# to check how accurate the model is

def main():
    fields = ['iid','wave', 'round', 'pid', 'match']
    interest = ['sports', 'tvsports', 'exercise', 'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing',
                'reading', 'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga']
    pairs = ['iid', 'pid']

    data = pd.read_csv("data/Speed-Dating-Data.csv", encoding="windows-1252", skipinitialspace=True, usecols=fields)
    interest_data = pd.read_csv("data/Speed-Dating-Data.csv", encoding="windows-1252", skipinitialspace=True, usecols=interest)
    pairs_data = pd.read_csv("data/Speed-Dating-Data.csv", encoding="windows-1252", skipinitialspace=True, usecols=pairs)

    data_value = data.values
    interest_value = interest_data.values
    pairs_value = pairs_data.values
    match_values = data['match'].values

    total_data_amount = len(data_value)
    # print(data)

    # build a interest data matrix by person
    person_interest = np.zeros(shape=(552, 17))

    cur = 0
    for i, d in enumerate(data_value):
        if d[0] != cur:
            person_interest[cur] = interest_value[i]
            cur += 1
        else:
            continue
    # print(person_interest)

    # calculate the jaccard sim scores by pairs
    J_sim_scores = np.zeros(total_data_amount)
    # print(pairs_value[7431])
    # print(person_interest[509])
    # print(person_interest[552])

    for i, p in enumerate(pairs_value):
        # print(i)
        checking = np.isnan(pairs_value[i])
        if checking[0] and not checking[1]:
            first_interest = np.zeros(17)
            second_interest = person_interest[int(p[1])-1]
        elif checking[1] and not checking[0]:
            first_interest = person_interest[int(p[0])-1]
            second_interest = np.zeros(17)
        else:
            first_interest = person_interest[int(p[0])-1]
            second_interest = person_interest[int(p[1])-1]

        if np.any(np.isnan(first_interest)) or np.any(np.isnan(second_interest)):
            J_sim_scores[i] = 0

        else:
            J_sim_scores[i] = jaccard_similarity_score(first_interest, second_interest)

    # print(J_sim_scores)

    # build the prediction matches
    pred_matches = np.zeros(total_data_amount)

    for i, n in enumerate(J_sim_scores):
        if n > 0.5:
            pred_matches[i] = 1
        else:
            pred_matches[i] = 0

    # comparing the accuracy to the real matching result
    J_sim_matches = jaccard_similarity_score(pred_matches, match_values)
    # print(total_data_amount)
    print("The Jaccard Similarity model is", round(J_sim_matches * 100), "% accurate.")


if __name__ == "__main__":
    main()
