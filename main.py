import time
import pandas as pd 

from string_search.string_match import string_match

def job():
    input = pd.read_csv('string_search/test_files/3q_semrush.csv')
    match = pd.read_csv('string_search/test_files/3q_test_bigrams.csv')

    # list comprehension on string_match() to check for matches in input dataframe vs each row in match dataframe
    matching_phases = [string_match(input, 'Keyword', i) for i in match['match']]

    all_data = pd.concat(matching_phases)

    # print where matches are found
    match_exist = all_data[all_data['match_exist'] == True]
    
    return match_exist, all_data


if __name__ == '__main__':
    start_time = time.time()
    match_exist, all_data = job()
    end_time = time.time()
    print("Time elapsed: {} seconds".format(round(end_time - start_time),2))
    print("match_exist.shape: {}".format(match_exist.shape))
    print("all_data.shape: {}".format(all_data.shape))
    print("match_exist[['Keyword', 'match_phrase']]: \n{}".format(match_exist[['Keyword', 'match_phrase']].head(5)))
