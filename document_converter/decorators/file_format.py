import os


def validate_file_type(valid_extensions):
    def decorator(func):
        def wrapper(file_path: str, *args, **kwargs):
            if not any(file_path.lower().endswith(ext) for ext in valid_extensions):
                raise ValueError(f"Invalid file type. Only {', '.join(valid_extensions)} files are allowed.")

            if not os.path.exists(file_path):
                raise FileNotFoundError("File {} not found".format(file_path))

            return func(file_path, *args, **kwargs)

        return wrapper

    return decorator
