Doctor Droid platform enables you to peek inside your code and get deep insights into the building blocks of your product.

* Look into arguments, responses and performance of your internal functions and any I/O in and out of your services.  <br>
* Get pre-created graphs with ability to slice data using in-context filters.  <br>
* Get alerted in real-time for anomalies in data returned from your downstream API calls or internal functions.  <br>

## Install and setup
```
# Install through pip 
pip install pycodemarker

# Setup DoctorDroid Keys in your configuration
DOCTOR_DROID_KEY = <drdroid_key>
```

## Instrumentations
1. Requests module
```
from pycodemarker import codemarker
codemarker.DroidInstrumentor().instrument_request(requests)
```

2. Instrument your functions
```
@codemarker.droid_peek
def function_call(argument1, argument2):
    return return_value
```

## Examples
### Downstream API calls
Once your request module is instrumented, you can see what data if flowing through your API calls:

1. Request & Response Headers, Body
2. Endpoint & its query parameters
3. Response Time

You can search this data with any attribute associated with these values with insights as deep as first level keys in your Request and Response bodies.

See this code snippet:
```
c_type = 'Flat'
city = 'BLR'
url = 'https://<hostname>/api/coupons'

query_params = {'city': city, 'c_type': c_type}
response = requests.get(url, params=query_params)
	
coupons_data = response.json()['coupons']
```

What you see in your Doctor Droid dashboard:

1. Length of the json array of first level ‘coupons’ key in the api response. This, when seen in context of ‘city’ query parameter and put under the metrics bucket of user conversion, can reliably tell the root cause for conversion dropping for a certain city due to coupons not being returned for it. 
![](https://drdroid-public-content.s3.us-west-2.amazonaws.com/charts/Screenshot+2022-11-14+at+8.31.36+PM.png) <br>
2. Response time aggregation basis contextual parameters / filters. 
![](https://drdroid-public-content.s3.us-west-2.amazonaws.com/charts/Screenshot+2022-11-14+at+8.31.43+PM.png) <br>
3. Coupons data returned for a certain user filtered by their ID (If this code snippet was within an authenticated API call from the user’s mobile app where she is logged in).

### Function calls
Once your function call is instrumented, you can see:

1. Arguments passed in it
2. Data being returned from it
3. Time taken by function
4. Where the function was called from

For the following code snippet:
```
@codemarker.droid_peek
def allocateDriverToRide(city, drivers):
    allowedDistance = getAllocationDistance(city)
    if len(drivers) > 0:
        closeDrivers = list(filter(lambda x: x['distance'] < allowedDistance, drivers))
        if len(closeDrivers) > 0:
            closeDrivers = sorted(closeDrivers, key=lambda x: x['distance'])
                return closeDrivers[0]
    return None
```

What you see in your Doctor Droid dashboard:

1. Time this function call is taking. This can create help you benchmarks for performance at function level.
![](https://drdroid-public-content.s3.us-west-2.amazonaws.com/charts/Screenshot+2022-11-14+at+11.35.00+PM.png) <br>
2. Allocation success rate by putting together total function call count vs when it returns an allocated driver.
![](https://drdroid-public-content.s3.us-west-2.amazonaws.com/charts/Screenshot+2022-11-14+at+11.21.27+PM.png) <br>
3. Allocation success count at city level. It can help you identify if some issue is happening at a city level even though overall it looks fine. 
![](https://drdroid-public-content.s3.us-west-2.amazonaws.com/charts/Screenshot+2022-11-14+at+11.20.07+PM.png) <br>

For getting early access and live demo, leave a message at [here](https://drdroid.io/#section-cta) or reach us at [dipesh@drdroid.io](mailto:dipesh@drdroid.io).
