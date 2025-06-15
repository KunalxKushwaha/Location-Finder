import phonenumbers
from phonenumbers import geocoder, carrier , timezone

nmuber = input("Enter the phone number with country code: ")

phoneNumber = phonenumbers.parse(nmuber)

timeZone = timezone.time_zones_for_number(phoneNumber)
print("Timezone: ", str(timeZone))

geolocation = geocoder.description_for_number(phoneNumber, "en")
print("Geolocation: ", geolocation)

service = carrier.name_for_number(phoneNumber, "en")
print("Service Provider: ", service)