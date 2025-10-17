'''
https://chatgpt.com/share/68e93e8f-7568-8002-ac0c-c07c80340e7e

'''

# Importing Necessary Modules
import requests
import folium
import datetime
import time
import webbrowser
import os

# This method will return our actual coordinates using IP address
def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except Exception as e:
        print("Internet not available or error:", e)
        exit()
        return False
    


# This method will fetch coordinates and create an HTML file of the map
def gps_locator():
    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print("You are in {}, {}".format(city, state))
        print("Your latitude = {} and longitude = {}".format(lat, long))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        # Save map to a file
        folder = "C:/screengfg"
        os.makedirs(folder, exist_ok=True)  # Create folder if not exists
        fileName = os.path.join(folder, "Location_" + str(datetime.date.today()) + ".html")

        obj.save(fileName)

        return fileName

    except Exception as e:
        print("Error generating map:", e)
        return False


# Main method
if __name__ == "__main__":

    print("--------------- GPS Using Python ---------------\n")

    # Function calling
    page = gps_locator()
    if page:
        print("\nOpening map in browser...")
        webbrowser.open('file://' + os.path.realpath(page))
        time.sleep(2)
        print("\nMap opened successfully!")
    else:
        print("Could not generate or open the map.")




'''

Below codes are using selenium also but there are some errors in code so commented complete code:

# Importing Necessary Modules
import requests
from selenium import webdriver
import folium
import datetime
import time

# this method will return us our actual coordinates
# using our ip address

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io/')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
        # return lat, long
    except:
        # Displaying ther error message
        print(&quot;Internet Not avialable&quot;)
        # closing the program
        exit()
        return False


# this method will fetch our coordinates and create a html file
# of the map
def gps_locator():

    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print(&quot;You Are in {},{}&quot;.format(city, state))
        print(&quot;Your latitude = {} and longitude = {}&quot;.format(lat, long))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        fileName = &quot;C:/screengfg/Location&quot; + \
            str(datetime.date.today()) + &quot;.html&quot;

        obj.save(fileName)

        return fileName

    except:
        return False


# Main method
if __name__ == &quot;__main__&quot;:

    print(&quot;---------------GPS Using Python---------------\n&quot;)

    # function Calling
    page = gps_locator()
    print(&quot;\nOpening File.............&quot;)
    dr = webdriver.Chrome()
    dr.get(page)
    time.sleep(4)
    dr.quit()
    print(&quot;\nBrowser Closed..............&quot;)
'''
# added this comment after adding to github repo
