import folium
import pandas
import json


def get_elevation_color(e):
    if e < 1500:
        return "lightblue"
    elif 1500 <= e < 2500:
        return "darkgreen"
    else:
        return "darkred"


map = folium.Map(location=(38.58, -99.09), zoom_start =6, tiles = "Stamen Terrain")
html = """<h4>Volcano Information: </h4><br>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s<br>
"""

coordinates = pandas.read_csv("C:\\mycode\\python\\Web Mapping Project 1\\Volcanoes.txt")
x, y, name, elev = coordinates["LAT"], coordinates["LON"], coordinates["NAME"], coordinates["ELEV"]

fg_tutorial = folium.FeatureGroup(name="First FeatureGroup")
for values in (range(38,42)):
    fg_tutorial.add_child(folium.Marker(location=(values, values-137), popup = "Hi, I'm a marker!", icon=folium.Icon(color="orange")))

fg_volcanoes = folium.FeatureGroup(name="Some American Volcanoes")
for i,j, n, e in zip(x,y, name, elev):
    iframe = folium.IFrame(html = html % (n, n, e), width=200, height=100)
    colour = get_elevation_color(e)

    fg_volcanoes.add_child(folium.CircleMarker(location=(i,j), radius = 10, popup = folium.Popup(iframe),
        fill_color=colour, color = "grey", fill_opacity = 0.7))

with open("C:\\mycode\\python\\Web Mapping Project 1\\world.json", "r", encoding="utf-8-sig") as readfile:
    reader = json.loads(readfile.read())

fg_population = folium.FeatureGroup(name="Population")
fg_population.add_child(folium.GeoJson(data=reader, style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10**6 \
        else "orange" if 10**6<= x["properties"]["POP2005"] < 20**6 else "red"}))

map.add_child(fg_population)
map.add_child(fg_volcanoes)
map.add_child(fg_tutorial)
map.add_child(folium.LayerControl())

map.save("C:\\mycode\\python\\Web Mapping Project 1\\Map1.html")
