from Jumpscale import j


class Car(j.baseclasses.object_config):
    """
    one car instance
    """

    _SCHEMATEXT = """
        @url = jumpscale.example.car.1
        name** = ""
        city = ""
        mother_id** = 0
        
        """

    def _init(self, **kwargs):
        pass


class Cars(j.baseclasses.object_config_collection):
    """
    collection of cars no test tools
    """

    _CHILDCLASS = Car


class Ship(j.baseclasses.object_config):
    """
    one ship instance
    """

    _SCHEMATEXT = """
        @url = jumpscale.example.ship.1
        name** = ""
        location = ""
        onsea = true (b)
        """

    def _init(self, **kwargs):
        self.a = "some"
        pass


class Ships(j.baseclasses.object_config_collection):
    """
    ...
    """

    _CHILDCLASS = Ship

    def _init(self, **kwargs):
        self.a = "a"

    def test(self):
        pass


class World(j.baseclasses.factory):
    """
    generic usable factory
    """

    _CHILDCLASSES = [Cars, Ships]


class World2(j.baseclasses.factory_data):

    _CHILDCLASSES = [Cars, Ships]
    _SCHEMATEXT = """
        @url = jumpscale.example.world2
        name** = ""
        color = "red,blue" (E)
        """


class BaseClasses_Object_Structure(j.baseclasses.testtools, j.baseclasses.object):

    __jslocation__ = "j.tutorials.world"

    def test(self):
        """
        to run:

        kosmos -p 'j.tutorials.world.test()'
        """
        ships = Ships()
        ship1 = ships.get(name="ibizaboat")
        ships.reset()

        # test that all ids, indexes, ... are empty
        assert len(ships._model._list_ids()) == 0
        assert ships._model.count() == 0
        assert len(ships.find()) == 0
        assert len(ships._model.find()) == 0
        assert len(ships._model.find(name="ibizaboat")) == 0  # also need to check that find on name is 0

        ship1 = ships.get(name="ibizaboat")

        assert ship1.name == "ibizaboat"
        # the data should be saved automatically (means there will be an id)
        assert isinstance(ship1._id, int)
        assert ship1._id > 0

        assert len(ships._model._list_ids()) == 1
        assert len(ships.find()) == 1
        assert len(ships._model.find()) == 1

        assert len(ship1._dataprops_names_get()) == 3

        w = World()
        w.reset()

        assert len(w._children_recursive_get()) == 2
        # indeed correct children are cars & ships which are empty though

        assert len(w._dataprops_names_get()) == 0  # there are no dataproperties on the world object itself
        assert len(w._children_names_get()) == 2  # there are 2 subobjects so there should be 2 names

        # here we check they are empty
        assert len(w.cars.find()) == 0
        assert len(w.cars._model.find()) == 0
        assert len(w.ships.find()) == 0
        assert len(w.ships._model.find()) == 0
        assert len(ships._model.find(name="ibizaboat")) == 0  # also need to check that find on name is 0

        assert w.cars._children._data == {}  # no children in memory, so got cleared

        # twcie same search
        assert w.cars._findData(name="rabbit") == []
        assert w.cars._model.find(name="rabbit") == []

        car = w.cars.get("rabbit")
        car2 = w.cars.get("bobby")

        assert car2._mother_id_get() == None  # because the cars & world obj have no id

        assert car.name == "rabbit"
        assert car2.name == "bobby"
        assert car._id > 0
        assert car2._id > 0

        assert len(w.cars.find()) == 2
        assert len(w.cars._model._list_ids()) == 2

        assert len(w.cars._model.find()) == 2  # is autosave

        assert len(w.cars.find(name="rabbit")) == 1

        allchildren = w._children_recursive_get()
        assert len(allchildren) == 4

        w.save()
        assert len(w.cars._model.find()) == 2  # now should be saved

        w.cars._children = j.baseclasses.dict()

        assert len(w.cars.find()) == 2
        # proves that the data has been saved in the DB

        assert len(w.cars.find()) == 2
        w2 = World2(name="world2")
        w3 = World2(name="world3")
        assert isinstance(w2, j.baseclasses.object)
        assert isinstance(w2, j.baseclasses.object_config)

        # needs to be 0 because is a new obj with other children

        assert len(w3.cars.find()) == 0

        assert len(w2.cars.find()) == 0
        car3 = w2.cars.get("rabbit3")
        car3.save()
        assert car3._id  # cannot be empty

        assert len(w2.cars.find()) == 1  # then we know that world 2 only has 1 car

        car4 = w3.cars.get("rabbit4")
        car5 = w3.cars.get("rabbit5")
        car6 = w3.cars.get("rabbit6")

        assert len(w3.cars.find()) == 3
        assert len(w2.cars.find()) == 1

        assert len(w.cars.find()) == 6

        print("TEST OK")
