from pathlib import Path


class ThemeManager:

    def __init__(self, theme_path):
        self.path = Path(theme_path)
        self.id = self.path.name

    @property
    def display_name(self):
        names = {
            "studio45": "Olivetti Studio 45",
        }
        return names.get(self.id, self.id)
