"""
The MIT License (MIT)

Copyright 2024-present 0x747

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the “Software”), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE.

"""

class Country:
    def __init__(self, id: int, 
                 name: str, 
                 iso3: str, 
                 iso2: str, 
                 phonecode: int, 
                 capital: str, 
                 currency: str,    
                 native: str,    
                 emoji: str,  
                 numeric_code: int = None,
                 currency_name: str = None,
                 currency_symbol: str = None,
                 tld: str = None,
                 region: str = None,
                 region_id: int = None,
                 subregion: str = None, 
                 subregion_id: int = None, 
                 nationality: str = None, 
                 timezones: str = None, 
                 translations: str = None, 
                 latitude: str = None, 
                 longitude: str = None,
                 emojiU: str = None,
                 **kwargs) -> None:
        
        self.id = id
        self.name = name
        self.iso3 = iso3
        self.numeric_code = numeric_code
        self.iso2 = iso2
        self.phonecode = phonecode
        self.capital = capital
        self.currency = currency
        self.currency_name = currency_name
        self.currency_symbol = currency_symbol
        self.tld = tld
        self.native = native
        self.region = region
        self.region_id = region_id
        self.subregion = subregion
        self.subregion_id = subregion_id
        self.nationality = nationality
        self.timezones = timezones
        self.translations = translations
        self.latitude = latitude
        self.longitude = longitude
        self.emoji = emoji
        self.emoji_u = emojiU
        self.__dict__.update(kwargs)

