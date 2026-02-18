import phonenumbers
from phonenumbers import geocoder,carrier
from target import phone_number
import folium
from opencage.geocoder import OpenCageGeocode


#step1. this part of the code gets number and loaction.
check_number=phonenumbers.parse(phone_number,"IN")
number_location=geocoder.description_for_number(check_number,"en")
print(number_location)

#this will not show the current service provider it will show the first service provider.
service_provider=phonenumbers.parse(phone_number,"IN")
print(carrier.name_for_number(service_provider,"en"))


#get latitude / longitude
key="c00fca7144e34193ba4dbcbaef75229f"
geocoder_api=OpenCageGeocode(key)
query=str(number_location)
results=geocoder_api.geocode(query)
lat=results[0]["geometry"]["lat"]
lng=results[0]["geometry"]["lng"]
print(lat,lng)

#3. Generate map
my_map=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(my_map)
my_map.save("mylocation.html")