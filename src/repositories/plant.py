""" Defines the Plant repository """

import requests

import util
from models import Plant


class PlantRepository:
    """The repository for the plant model"""

    @staticmethod
    def get(plant_id):
        """Query a plant by plant_id"""
        plant = PlantRepository.get_by(plant_id=plant_id)
        if plant is None:
            return "Plant not found."
        return plant

    @staticmethod
    def get_all():
        """Query all plants"""
        return Plant.query.all()

    @staticmethod
    def get_top_capacity_plants(top):
        """Query the top capacity (max_capacity_gw) plants"""
        return Plant.query.order_by(Plant.max_capacity_gw.desc()).limit(top)

    def update(
        self,
        plant_id,
        name,
        cep,
        longitude,
        latitude,
        max_capacity_gw,
        updated_at,
    ):
        """Update a plant's data"""
        cep = util.cep.process(cep)
        plant = self.get(plant_id)
        if not isinstance(plant, Plant):
            return plant

        if error := PlantRepository.check_plant_is_valid_when_updating(
            plant, name, cep
        ):
            return error

        plant.name = name
        plant.cep = cep
        plant.longitude = longitude
        plant.latitude = latitude
        plant.max_capacity_gw = max_capacity_gw
        plant.updated_at = updated_at

        return plant.save()

    @staticmethod
    def create(name, cep, longitude, latitude, max_capacity_gw):
        """Create a new plant"""
        cep = util.cep.process(cep)

        plant = Plant(
            name=name,
            cep=cep,
            longitude=longitude,
            latitude=latitude,
            max_capacity_gw=max_capacity_gw,
        )

        if errors := PlantRepository.check_plant_is_valid_when_creating(plant):
            return errors

        return plant.save()

    @staticmethod
    def delete(plant_id):
        """Delete a plant"""
        plant = PlantRepository.get(plant_id)
        if isinstance(plant, Plant):
            return plant.delete()
        return plant

    @staticmethod
    def get_by(**kwargs):
        """Query a plant by any of its attributes"""
        if len(kwargs) == 0:
            return "No get/filter parameter provided."
        if len(kwargs) > 1:
            return "Too many get/filter parameters provided."
        return Plant.query.filter_by(**kwargs).first()

    @staticmethod
    def check_plant_name_is_valid(name):
        """Check if a name is valid"""
        if len(name) < 3:
            return "Name is too short. "
        return ""

    @staticmethod
    def check_plant_cep(cep):
        """Check if the plant cep is valid"""
        if len(cep) != 8:
            return "Invalid amount of digits in CEP. "
        if not cep.isnumeric():
            return "Invalid type of digits in CEP. "

        resp = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)

        if resp.status_code != 200 or "erro" in resp.json():
            return "Invalid CEP. "

        return ""

    @staticmethod
    def check_plant_is_Plant(plant):
        """Check if a plant is an instance of Plant"""
        if not isinstance(plant, Plant):
            return plant + " "
        return ""

    @staticmethod
    def check_name_exists(name):
        """Check if a name already exists"""
        if PlantRepository.get_by(name=name) is not None:
            return "Plant name already exists. "
        return ""

    @staticmethod
    def check_plant_is_valid_when_updating(plant, name, cep):
        """Check if the plant is valid when updating"""
        errors = ""
        errors += PlantRepository.check_plant_is_Plant(plant)
        if plant.cep != cep:
            errors += PlantRepository.check_plant_cep(cep)
        if plant.name != name:
            errors += PlantRepository.check_plant_name_is_valid(name)
            errors += PlantRepository.check_name_exists(name)
        return errors.rstrip()

    @staticmethod
    def check_plant_is_valid_when_creating(plant):
        """Check if the plant is valid when creating"""
        errors = ""
        errors += PlantRepository.check_plant_name_is_valid(plant.name)
        errors += PlantRepository.check_name_exists(plant.name)
        errors += PlantRepository.check_plant_cep(plant.cep)
        return errors.rstrip()
