import pandas as pd
def process_weather_data(raw_data):
    if 'error' in raw_data:
        return raw_data
    
    processesd_data = {
        'City':raw_data['name'],
        'Temperature':raw_data['main']['temp'],
        'Humidity':raw_data['main']['humidity'],
        'Weather':raw_data['weather'][0]['description']
    }
    
    df = pd.DataFrame([processesd_data])
    df.fillna('Unknowm',inplace = True)
    return df