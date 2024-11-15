# Country State City API Wrapper

A simple Python API wrapper for the [Country State City API](https://countrystatecity.in/) 

## Usage

```py
import country_state_city as csc

client = csc.Client(api_key='api-key')

# Countries
client.get_countries() # Get all countries
client.get_countries(['US', 'DE', 'AU']) # Get specific countries
client.get_country('US') # Get a single country

# States
client.get_states() # Get all states
client.get_states('US') # Get all states from a country
client.get_state('US', 'CA') # Get a state from a country

# Cities
client.get_cities('US') # Get all cities from a country
client.get_cities('US', 'CA') # Get all cities from a state
```

## Future Updates

- Add documentation
- Add async support
- Add caching
- Account for rate limit