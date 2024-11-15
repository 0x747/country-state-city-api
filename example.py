import country_state_city as csc

KEY = 'your-api-key'

client = csc.Client(api_key=KEY)

# Get all countries
countries = client.get_countries()

for country in countries:
    print(country.name, country.capital)

# Get specific countries/country in a list
spec_countries = client.get_countries(['US', 'DE', 'AU'])
# Returns United States, Germany, and Australia in a list of Country objects

# Get a single country
country = client.get_country("US") # United States

# Get all states
states = client.get_states()

# Get states from a country
country_states = client.get_states("US")

# Get a specific state from a country
state = client.get_state("US", "NY") # New York

# Get all cities from a country
cities = client.get_cities("US") # Returns all cities in the US

# Get cities from a state
state_cities = client.get_cities("US", "CA") # Get cities from California
