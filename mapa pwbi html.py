import folium
import json

# Caminho para o seu arquivo GeoJSON do Espírito Santo
geojson_path = "ES_UF_2022.json"  # certifique-se de que está no mesmo diretório do script

# Coordenadas centrais aproximadas do ES
center_coords = [-19.5, -40.5]
zoom_level = 8

# Lista de hospitais com coordenadas
hospitais = [
    {"nome": "Hospital Antônio Bezerra de Farias", "lat": -20.334106, "lon": -40.284944},
    {"nome": "Hospital Estadual Central", "lat": -20.3189, "lon": -40.3400},
    {"nome": "Hospital Doutor Dório Silva", "lat": -20.1917, "lon": -40.2333},
    {"nome": "Hospital Maternidade Silvio Avidos", "lat": -19.53649, "lon": -40.63173},
    {"nome": "Centro de Reabilitação Física do Espírito Santo (CREFES)", "lat": -20.3290, "lon": -40.2920},
    {"nome": "Hospital Estadual de Atenção Clínica", "lat": -20.3144062, "lon": -40.3814337},
]

# URL da logo personalizada
logo_url = "logo.png"  # troque pela sua se quiser

# Criação do mapa com fundo branco (sem tiles)
mapa = folium.Map(location=center_coords, zoom_start=zoom_level, tiles=None)

# Adiciona contorno do ES
with open(geojson_path, "r", encoding="utf-8") as f:
    es_geojson = json.load(f)

folium.GeoJson(es_geojson, name="ES", style_function=lambda x: {
    "fillColor": "#e0f3f8",
    "color": "#2b8cbe",
    "weight": 2,
    "fillOpacity": 0.5
}).add_to(mapa)

# Adiciona os hospitais com ícones personalizados
for hospital in hospitais:
    icon = folium.CustomIcon(logo_url, icon_size=(40, 40))
    folium.Marker(
        location=[hospital["lat"], hospital["lon"]],
        popup=hospital["nome"],
        icon=icon
    ).add_to(mapa)

# Salva o mapa
mapa.save("mapa_hospitais_sem_fundo.html")
