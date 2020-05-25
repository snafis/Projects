import pandas as pd
import plotly.graph_objs as go
from collections import OrderedDict, defaultdict
import requests

#World Bank indicators of interest for pulling
indicators_default = ['NY.GDP.MKTP.KD.ZG', 'NV.IND.TOTL.KD.ZG', 'FP.CPI.TOTL.ZG', 'PX.REX.REER', 'NE.IMP.GNFS.KD.ZG']

#list of countries of interest
country_default = OrderedDict([('Ukraine', 'UA'), ('Poland', 'PL'), ('Russia', 'RU'), ('Germany', 'DE'), ('United States', 'US')])
payload = {'format': 'json', 'per_page': 500, 'date': '2010:2019'}


def pull_data(countries=country_default, indicators=indicators_default):
    ''' Pulls data from the World Bank API
    Input:
        country_default (dict): list of countries for viz
        indicators (list): list of indicators for viz
    Output:
        list (dict): list containing the pulled data
    '''
    #prepare country data for World Bank API
    #the API uses ISO-2 country codes separated by ;
    country_filter = list(countries.values())
    country_filter = [x.lower() for x in country_filter]
    country_filter = ';'.join(country_filter)

    data_frames = [] #stores the data frames with the indicator data of interest

    #pull data from World Bank API
    # store results in data_frames
    for indicator in indicators:
        url = 'http://api.worldbank.org/v2/countries/' + country_filter +\
            '/indicators/' + indicator
    
        try:
            r = requests.get(url, params=payload)
        except:
            print('could not load data', indicator)

        data = r.json()[1]

        for value in data:
            value['indicator'] = value['indicator']['value']
            value['country'] = value['country']['value']

        data_frames.append(data)

        return data_frames

def return_figures():
    ''' Creates plotly viz using World Bank API
    Input:
        none
    Output:
        list (dict): list containing the plotly viz
    '''
    data_frames = pull_data()

    #first graph GDP in 2017 in selected countries as a bar chart
    graph_one = []
    df_one = pd.DataFrame(data_frames[0])    

    #country list of unique values to ensure legend have the same order and color
    #TODO: rewrite as ordered object in pandas
    #countrylist = df_one.country.unique().tolist()

    #filter values for the viz
    #TODO: make it dynamic - e.g. insert year now or previous year
    df_one = df_one[df_one['date'] == '2017']
    df_one.sort_values('value', ascending=False, inplace=True)

    graph_one.append(
        go.Bar(
            x = df_one.country.tolist(),
            y = df_one.value.tolist()
            )
        )

    layout_one = dict(
        title = "GDP growth in 2017, annual %",
        xaxis = dict(title = 'Country'),
        yaxis = dict(title = 'annual %')
    ) 

    #append all charts
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))

    return figures 

return_figures()