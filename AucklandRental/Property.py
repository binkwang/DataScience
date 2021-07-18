import pandas as pd
import numpy as np
import re

class Property:

  def __init__(self):
    self.keys = ['Id', 'Bedrooms', 'Bathrooms', 'Address', 'Rent', 'RentPerRoom', 'ListedDate']

  def get_map(self, single_property):
    """
    Get the Single Property map from the single_property (string) 
    """
    singleProperty = {key:'' for key in self.keys}

    # Id
    tmp_id = re.findall('listing/([\d]+)', single_property)
    singleProperty['Id'] = tmp_id[0] if len(tmp_id) > 0 else np.nan

    # Bedrooms
    tmp_nBedroom = re.findall('Bedrooms ([\d+\.?]+)', single_property)
    singleProperty['Bedrooms'] = float(tmp_nBedroom[0].replace("+", "")) if len(tmp_nBedroom) > 0 else np.nan

    # Bathrooms
    tmp_nBathroom = re.findall('Bathrooms ([\d+\.?]+)', single_property)
    singleProperty['Bathrooms'] = float(tmp_nBathroom[0].replace("+", "")) if len(tmp_nBathroom) > 0 else np.nan

    # Address
    tmp_address = re.findall('(.*?)Available:', single_property, re.M)
    singleProperty['Address'] = tmp_address[0] if len(tmp_address) > 0 else np.nan

    # Rent
    tmp_rent = re.findall('\$([\d,+\.?]+)', single_property, re.M)
    singleProperty['Rent'] = float(tmp_rent[0].replace(",", "")) if len(tmp_rent) > 0 else np.nan

    # RentPerRoom
    singleProperty['RentPerRoom'] = singleProperty['Rent'] / singleProperty['Bedrooms'] if singleProperty['Bedrooms'] != 0 else np.nan

    # ListedDate
    tmp_listedDate = re.findall('(?<=Listed  ).*$', single_property, re.M)
    singleProperty['ListedDate'] = tmp_listedDate[0] if len(tmp_listedDate) > 0 else np.nan

    return singleProperty