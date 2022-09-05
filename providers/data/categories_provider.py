class CategoriesProvider:

    @staticmethod
    def existing_category():
        return {
            "name": "Apps",
            "count": 69,
            "id": 577051039
        }

    @staticmethod
    def non_existing_category():
        return {
            "name": 'kajsbdhbjhasbdkjvhbajskdbv',
            "count": 0,
            "id": 0
        }
    @staticmethod
    def empty_category():
        return {
            "name": '',
            "count": '',
            "id": ''
        }