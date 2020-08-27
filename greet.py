import requests

def fetch_ip_address():
    """Return a string of my IP Address"""
    response = requests.get('https://api.ipify.org')
    return response.text

def locate_ip_address(ip_address):
    """Return lat & lon based data for a given IP address"""
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    keys = ('lat','lon','city','region','country')
    return {key : data[key] for key in keys}

def get_temp(lat,lon):
    """Return current temperature for a location given the latitude & longitude."""

    url_base = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    response = requests.get(url_base,params={'lat': lat, 'lon': lon})
    data =response.json()
    temperature = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
    
    return temperature 

def locate_ip_address_cplx(ip_address):
    """Return lat & lon based data for a given IP address"""
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    return response.json()

def conver_to_fahr(temp):
    return 9/5*temp+32

def greet(ip_address):
    # ip_address  = fetch_ip_address()
    geo_data = locate_ip_address(ip_address)
    temp_C = get_temp(geo_data['lat'],geo_data['lon'])
    temp_F = conver_to_fahr(temp_C)
    return f"It's {temp_F} deg F in {geo_data['city']},{geo_data['region']}, {geo_data['country']}"

if __name__ == "__main__":
    import sys

    print(greet(sys.argv[1]))