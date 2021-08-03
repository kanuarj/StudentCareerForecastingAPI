import pandas as pd

def location_based_colleges(dataset_location, location_data):
    df = pd.read_csv(dataset_location)
    if location_data == 'Kurla':
        location_data = 'Dadar'
    elif location_data == 'Virar':
        location_data = 'Borivali'
    location_occurances = df.loc[df['Location'] == location_data]
    return location_occurances

def marks_based_colleges(dataset_location, marks_data):
    df = pd.read_csv(dataset_location)
    mark_occurances = df.loc[df['CS-CAP1'] <= marks_data]
    return mark_occurances
