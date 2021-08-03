import pandas as pd

def analysis(dataset_path, data_json):
    df = pd.read_csv(dataset_path)
    position = data_json['position']
    location = data_json['location']
    cgpa = data_json['CGPA']
    dotnet = data_json['.NET']
    c = data_json['C']
    cpp = data_json['Cpp']
    python = data_json['Python']
    java = data_json['Java']
    sql = data_json['SQL']
    js = data_json['Javascript']
    html = data_json['HTML']
    android = data_json['Android']
    ds = data_json['Data Science']
    php = data_json['PHP']
    position_and_location = df.loc[(df['Position'] == position) & (df['Location'] == location)]
    cgpa_basis = df.loc[df['CGPA'] <= cgpa]
    skills = df.loc[(df['.NET'] == dotnet) & (df['C'] == c) & (df['C++'] == cpp) & (df['Python'] == python) \
        & (df['Java'] == java) & (df['SQL'] == sql) & (df['Data Science'] == ds) & (df['Javascript'] == js) \
        & (df['PHP'] == php) & (df['Android'] == android) & (df['HTML'] == html)]
        
    return position_and_location, cgpa_basis, skills

def value_evaluator(data_json):
    position = data_json['position']
    if position == 'Software Developer':
        droid, dsci, nwengg, sqldev, webdev = 0, 0, 0, 0, 0
        sde = 1
    elif position == 'Network Engineer':
        droid, dsci, sde, sqldev, webdev = 0, 0, 0, 0, 0
        nwengg = 1
    elif position == 'Web Developer':
        droid, dsci, nwengg, sqldev, sde = 0, 0, 0, 0, 0
        webdev = 1
    elif position == 'Android Developer':
        sde, dsci, nwengg, sqldev, webdev = 0, 0, 0, 0, 0
        droid = 1
    elif position == 'SQL Developer':
        droid, dsci, nwengg, sde, webdev = 0, 0, 0, 0, 0
        sqldev = 1
    elif position == 'Data Scientist':
        droid, sde, nwengg, sqldev, webdev = 0, 0, 0, 0, 0
        dsci = 1

    location = data_json['location']
    if location == 'Mumbai':
        bang, chennai, delhi, hyd = 0, 0, 0, 0
        mum = 1
    elif location == 'Bengaluru':
        mum, chennai, delhi, hyd = 0, 0, 0, 0
        bang = 1
    elif location == 'Hyderabad':
        mum, chennai, delhi, bang = 0, 0, 0, 0
        hyd = 1
    elif location == 'Chennai':
        mum, bang, delhi, hyd = 0, 0, 0, 0
        chennai = 1
    elif location == 'Delhi':
        mum, chennai, bang, hyd = 0, 0, 0, 0
        delhi = 1

    dotnet = data_json['.NET']
    c = data_json['C']
    cpp = data_json['Cpp']
    python = data_json['Python']
    java = data_json['Java']
    sql = data_json['SQL']
    js = data_json['Javascript']
    html = data_json['HTML']
    android = data_json['Android']
    ds = data_json['Data Science']
    php = data_json['PHP']
    
    ctc = data_json['CTC']
    backlogs = data_json['backlogs']
    cgpa = data_json['CGPA']

    array = [dotnet, c, cpp, python, java, sql, html, php, js, ds, android, \
        cgpa, ctc, backlogs, droid, dsci, nwengg, sqldev, sde, webdev, \
            bang, chennai, delhi, hyd, mum]

    return array

