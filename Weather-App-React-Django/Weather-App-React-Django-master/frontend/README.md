# WeatherFinder

A React web-app that display weather based on the city entered by the user.

## Features

##### Start typing a city name and autosuggestions will appear

## Technical Details

### APIs Used:

#### [Google Places Autocomplete API](https://developers.google.com/places/web-service/autocomplete)
- To show suggestions based on the city typed in input box
- <a href="https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Ahme&types=(cities)&key=yourAPIKey">Endpoint to Display list of cities based on initials of input</a>
    - Will return JSON object of list of cities that start with "Ahme"

- [React component to use Google places Autocomplete API](https://www.npmjs.com/package/react-google-places-autocomplete)

#### [OpenWeatherMap API](https://openweathermap.org/current)

- To display weather based on city, country, latitude, longitude, etc.

##### OpenWeatherMap API Endpoints
- [Display weather based on City and Country name](http://api.openweathermap.org/data/2.5/weather?appid=yourAPIKey&q=Ahmedabad,%20Gujarat,%20%C3%8Dndia)

- [Display weather based on City](http://api.openweathermap.org/data/2.5/weather?appid=yourAPIKey&q=Mumbai)

- [Display weather based on Latitude longitude](http://api.openweathermap.org/data/2.5/weather?appid=yourAPIKey&lat=23&lon=72)


##### Weather display data JSON details
- Type of weather
    - weather[0].description
- Weather type icon
    - weather[0].icon
- latitude, longitude
    - coord.lon, coord.lat
- temperature (given in K) = (K-273) celcius
    - main.temp
- Humidity in %
    - main.humidity
- Wind speed (given in m/s) = ms*3.6 kmph
    - wind.speed
