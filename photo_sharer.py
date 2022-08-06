from filestack import Client


class PhotoSharer:

    def __init__(self, filepath, api="AZYGHLUOHTlOp7mj4S19Fz"):
        self.filepath = filepath
        self.api = api

    def share(self):
        client = Client(self.api)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url