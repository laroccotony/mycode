import requests
from crayons import cyan



def main():
    url = "http://api.open-notify.org/iss-now.json"
    iss_req = requests.get(url)
    iss_json = iss_req.json()
    timestamp = iss_json['timestamp']
    lat = iss_json['iss_position']['latitude']
    long = iss_json['iss_position']['longitude']
    print(f"The ISS time is {cyan(timestamp)}, the Latitude is {cyan(lat)} and the Longitude is {cyan(long)} ")

if __name__ == "__main__":
    main()