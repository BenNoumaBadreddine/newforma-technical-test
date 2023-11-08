from config import StateValues


# Define a function to check if the state is in the valid states list
def is_valid_state(row):
    return row['state'] in StateValues.valid_states
