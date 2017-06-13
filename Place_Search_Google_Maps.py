import webbrowser
print("Enter a Valid Place to Find it on Google Maps")
Place=input()
Url="https://www.google.com/maps/place/"+Place
webbrowser.open(Url)
