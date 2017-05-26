from django.apps import AppConfig


class AssetManagerConfig(AppConfig):
    name = 'asset_manager'

    def ready(self):
        import asset_manager.signals
