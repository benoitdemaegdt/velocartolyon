import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import random
from faker import Faker

def get_random_personne():
    fake_names = Faker('fr_FR')

    # civilité
    gender = random.choice(['Male', 'Female'])

    # prénom et noms aléatoires
    if gender == 'Male':
        civilité = 'Monsieur'
        prénom = fake_names.first_name_male()
        nom = fake_names.last_name()
    else:
        civilité = 'Madame'
        prénom = fake_names.first_name_female()
        nom = fake_names.last_name()

    return civilité, prénom, nom.upper()


def geo_df_signalements(nb_points):

    ts_box = (1679125015, 1679992616)
    nw_corner = (4.801246, 45.779813)
    se_corner = (4.883468, 45.716576)
    liste_types_signalements = [
        'Chaussée ou trottoir détérioré', "Pont, passerelle, trémie détérioré", "Marquage au sol effacé ou illisible",
        "Plaque au sol descellée, manquante...", "Armoire ouverte ou détériorée", "Mobilier urbain détérioré ou non remplacé",
        "Nuisances liées à des chantiers de travaux publics", "Panneau de signalisation détérioré ou non remplacé",
        "Feu tricolore ou sonore en panne ou détérioré", "Véhicule épave/abandonné", "Stationnement abusif et/ou gênant"
                            ]

    # id du signalement
    id_signalement = list(range(1, nb_points+1))

    # timestamp
    ts = [random.uniform(ts_box[0], ts_box[1]) for i in range(nb_points)]

    # geometry
    lon_list = [random.uniform(se_corner[0], nw_corner[0]) for i in range(nb_points)]
    lat_list = [random.uniform(nw_corner[1], se_corner[1]) for i in range(nb_points)]
    geometry = [Point(lon, lat) for lon, lat in zip(lon_list, lat_list)]

    # type du signalement
    type_signalement = [random.choice(liste_types_signalements) for i in range(nb_points)]

    # description
    description = ["J'ai constaté : " + signal.lower() + " !" for signal in type_signalement]

    # identité aléatoire
    personnes = [get_random_personne() for i in range(nb_points)]
    civilité = [personne[0] for personne in personnes]
    prénom = [personne[1] for personne in personnes]
    nom = [personne[2] for personne in personnes]

    # id utilisateur
    id_utilisateur = list(range(1, nb_points+1))

    cols = [
        'id_signalement',
        'ts',
        'geometry',
        'type_signalement',
        'description',
        'civilité',
        'prénom',
        'nom',
        'id_utilisateur',
        ]


    values_list = [
        id_signalement,
        ts,
        geometry,
        type_signalement,
        description,
        civilité,
        prénom,
        nom,
        id_utilisateur,
    ]

    # Creation du geoDataFrame
    geo_df_signalements = gpd.GeoDataFrame({key: value_list for key, value_list in zip(cols, values_list)}, crs='EPSG:4326')

    return geo_df_signalements


def convert_and_save(geo_df_signalements, title='sample_points_geojson'):
    geo_df_signalements.to_file(f'../client/assets/{title}.geojson', driver="GeoJSON")
    pass

if __name__ == "__main__":
    nb_points = 100
    geo_df_signalements = geo_df_signalements(nb_points)
    convert_and_save(geo_df_signalements, title=f'sample_{nb_points}_points')
    pass
