#-----------Christian Flores----08/02/2021
#lugares a visitar:
#Canadá, Findalndia, París, Escocia, Nueva York
places = ["canada", "finalndia", "paris", "escocia", "nueva york"]
print(f"La lista original es: {places}")
print("")
print(f"La lista ordenada SIN modificar es: {sorted(places)}" )
print("")
print(f"La lista original nuevamente es: {places}")
print("")
places.reverse()
print(f"La lista en orden invertido es: {places}")
print("")
places.reverse()
print(f"La lista ha vuelto a su orden original: {places}")
print("")
places.sort()
print(f"La lista en orden alfabetico es: {places}")
print("")
places.sort(reverse=True)
print(f"La lista en orden alfabetico invertido es: {places}")
print("")
print(f"La longitud de la lista es: {len(places)}")
