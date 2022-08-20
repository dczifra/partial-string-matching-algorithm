import pandas as pd
import time

def string_match(full_vals, full_vals_col_name , matching_phase):
    """string_match

    Args:
        full_vals (DataFrame): Input dataframe with all values.
        full_vals_col_name (Str):  Name of the column with items to check for matching.
        matching_phase (Str): Phrase to check against the full_vals column.

    Returns:
        DataFrame: Dataframe with two new columns:
            - 'match_exist': Boolean value indicating if the matching_phase was found in the full_vals column.
            - 'match_phrase': String value with the matching_phase if it was found.
    """
    full_vals = full_vals.copy() # copy full_val to avoid mutating it
    full_vals[full_vals_col_name] = full_vals[full_vals_col_name].str.lower() # lowercase all phrases
    matching_phase = matching_phase.lower() # lowercase all phrases 
    full_vals['match_exist'] = full_vals[full_vals_col_name].str.contains(matching_phase) # check if phrase is in the string
    full_vals['match_phrase'] = matching_phase # add matching phrase to the dataframe
    
    return full_vals
    

# input = pd.read_csv('test_files/3q_semrush.csv')
# match = pd.read_csv('test_files/3q_test_bigrams.csv')


# # start timer
# start_time = time.time()

# # list comprehension on string_match() to check for matches in input dataframe vs each row in match dataframe
# matching_phases = [string_match(input, 'Keyword', i) for i in match['match']]

# df = pd.concat(matching_phases)

# # print where matches are found
# match_exist = df[df['match_exist'] == True]
# print(match_exist[['Keyword', 'match_phrase']])

# end_time = time.time()
# print("Time elapsed: {} seconds".format(end_time - start_time))