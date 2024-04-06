class URLManager:
    def __init__(self, urls_file):
        self.urls_file = urls_file

    def get_urls(self):
        with open(self.urls_file, 'r') as file:
            return [line.strip() for line in file]
