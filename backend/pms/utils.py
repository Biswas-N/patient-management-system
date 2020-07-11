from dotenv import load_dotenv
import os


def get_database_path() -> str:
    """
    get_database_path method creates a SQLAlchemy specific database path based
    on key-value pairs present in .env file
    """
    load_dotenv()

    if os.getenv("mode") == "Development":
        database_filename = os.getenv("sqlite_filename")
        project_dir = os.path.dirname(os.path.abspath(__file__))
        database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
        return database_path
    else:
        # TODO: Logic for PostgreSQL connection
        pass
