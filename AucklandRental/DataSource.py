import html2text
import requests
import pandas as pd
import os
from Property import Property

class DataSource:
    def __init__(self, region='Auckland', district='Auckland-City', suburb='Parnell'):
        self.region = region.lower()
        self.district = district.lower()
        self.suburb = suburb.lower()
        self.Property = Property()

    # Public method to request page content and convert plain text
    def page2text(self, page_num = 1):
        """
        Convert html to text
        """
        base_url = 'https://www.trademe.co.nz/a/property/residential/rent'
        url = base_url + '/' + self.region + '/' + self.district + '/' + self.suburb
        res = requests.get(url)
        res.encoding = 'utf-8'
        content = html2text.html2text(res.text)
        return content

    # Public method to convert plain text to pandas dataframe
    def text2df(self, content):
        apts_map = self.text2apts_map(content)
        df = pd.DataFrame(apts_map)
        return df

    def text2apts_map(self, content):
        listings = content.split("![Loading Image 1 of")
        houses_map = {key:[] for key in self.Property.keys}
        for j in range(1, len(listings)):
            listing = listings[j]
            single_map = self.Property.get_map(listing)
            for key in self.Property.keys:
                houses_map[key].append(single_map[key])
        return houses_map

    #########
    # Save the data source to csv file
    # parameter - path : file path (not including file name)
    # parameter - file_name : file name
    #########
    def to_csv(self, path, file_name):
        if not os.path.exists(path):
            os.makedirs(path)
        page_text = self.page2text()
        dataframe = self.text2df(page_text)
        dataframe['Suburb'] = self.suburb
        dataframe.to_csv(os.path.join(path, file_name), index = False)