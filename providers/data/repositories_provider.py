class RepositoriesProvider:

    @staticmethod
    def existing_repository():
        return {
            "name": 'become-qa-auto',
            "total_count": 16,
            "items_count": 16
        }

    @staticmethod
    def non_existing_repository():
        return {
            "name": 'kajsbdhbjhasbdkjvhbajskdbv',
            "total_count": 0,
            "items_count": 0
        }
