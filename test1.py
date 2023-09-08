import requests

api_url = "https://bookmyotservice.pythonanywhere.com/GetSpecialityList"

try:
    response = requests.get(api_url)

    if response.status_code == 200:

        data = response.json()
        if isinstance(data.get("ResultData"), list):
            result_date = data["ResultData"]

            for specialty in result_date:
                code = specialty.get('code')
                description = specialty.get("description")
                name = specialty.get("name")
                specialitylistid = specialty.get("specialitylistid")


                print(f"specialty code : {code}")
                print(f"specialty description : {description}")
                print(f"specialty name : {name}")
                print(f"specialitylistid : {specialitylistid}")

            else:
                print("thae data was fetched thie is api data formate in api response..")
        else:
            print(f"Request failed with status code {response.status_code}")
except Exception as e:
    print(f"Response error as : {e}")
