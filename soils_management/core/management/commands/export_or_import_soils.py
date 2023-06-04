import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Polygon

from django.http import JsonResponse
from django.forms.models import model_to_dict
from core.models import Soil, SoilArea

def export_soil_areas(file_path):
    data = []
    soils = Soil.objects.all()

    for soil in soils:
        soil_data = model_to_dict(soil)
        soil_areas = SoilArea.objects.filter(soil=soil)
        area_list = []
        if soil_areas:
            for area in soil_areas:
                area_list.append({"polygon":str(area.polygon.coords)})

            soil_data['areas'] = area_list
        data.append(soil_data)
    # convertir le dic en objet JSON
    json_data = json.dumps(list(data), indent=4, ensure_ascii=False)
    
    # ouvrir le fichier JSON et y placer les données
    with open(file_path, 'w') as file:
        file.write(json_data)
        
def json_file_to_list(file_path):
    # Lire le fichier JSON
    with open(file_path, 'r') as file:
        json_str = file.read()

    # Charger la chaîne JSON en une liste de dictionnaires Python
    data_list = json.loads(json_str)

    return data_list

class Command(BaseCommand):
    help = 'commande permettant d\'importer la liste des sols ou de les exporter depuis votre BD'

    def add_arguments(self, parser):
        parser.add_argument('choice', type=str, help='choisir export pour exporter sous fichier json ou import pour importer via le json file')

    def handle(self, *args, **options):
        choice = options['choice']
        if choice == "export":
            print()
            export_soil_areas('soils.json')
            self.stdout.write(self.style.SUCCESS('données exportés avec succès'))
            print()
        elif choice == "import":
            print()
            data = json_file_to_list("soils.json")
            for soil_data in data:
                if not Soil.objects.filter(type= soil_data["type"]):
                    soil = Soil.objects.create(type = soil_data["type"], description = soil_data["description"], composition = soil_data["composition"])
                    for item in soil_data["areas"]:
                        area = SoilArea.objects.create(soil = soil, polygon = Polygon(eval(item['polygon'])[0]))
                    print()
                    self.stdout.write(self.style.SUCCESS(f'votre sol de type {soil.type} et ses zones géografiques ont bien été enregistrés'))
                    print()
                else:
                    print()
                    self.stdout.write(self.style.ERROR_OUTPUT("A soil with this datas already exists"))
                    print()
            print()
        else:
            print()
            self.stdout.write(self.style.ERROR_OUTPUT('votre choix n\'est pas pris en charge'))
            print()