import os
import json

from app.schemas.configure import Configure


class ConfigService:
    def __init__(self, configure=Configure):
        self.configrue = configure
        self.config_directory = "app/static/configure"

    async def last_modify(self):
        files = [
            os.path.join(self.config_directory, f)
            for f in os.listdir(self.config_directory)
            if os.path.isfile(os.path.join(self.config_directory, f))
        ]
        latest_file = max(files, key=os.path.getmtime)
        return latest_file

    async def count_files(self) -> int:
        files = [
            os.path.join(self.config_directory, f)
            for f in os.listdir(self.config_directory)
        ]
        return len(files)

    async def current_config(self):
        print("current_config")
        path = await self.last_modify()
        config = Configure()
        json = config.from_json(path)
        print(json)
        return json

    async def create_config_file(self, data):
        length: int = await self.count_files()
        file_name = self.config_directory + "/" + f"config{length + 1}.json"
        try:
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)
            return "created"
        except Exception as e:
            return f"Error: {e}"
