class BaseDocument:
    def save(self, file_path):
        raise NotImplementedError("Subclasses should implement this method")
