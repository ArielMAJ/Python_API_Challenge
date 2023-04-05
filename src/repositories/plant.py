""" Defines the Plant repository """

from models import Plant


class PlantRepository:
    """The repository for the plant model"""

    @staticmethod
    def get(plant_id):
        """Query a plant by plant_id"""
        plant = Plant.query.filter_by(plant_id=plant_id).first()
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
        plant = self.get(plant_id)

        if not isinstance(plant, Plant):
            return plant
        if name != plant.name and Plant.query.filter_by(name=name).first() is not None:
            return "Plant name already exists."

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
        if Plant.query.filter_by(name=name).first() is not None:
            return "Plant name already exists."
        plant = Plant(
            name=name,
            cep=cep,
            longitude=longitude,
            latitude=latitude,
            max_capacity_gw=max_capacity_gw,
        )

        return plant.save()

    @staticmethod
    def delete(plant_id):
        """Delete a plant"""
        plant = PlantRepository.get(plant_id)
        if isinstance(plant, Plant):
            return plant.delete()
        return plant
