import os
import pytest

from document_generator import CSVGenerator


@pytest.fixture
def csv_generator():
    return CSVGenerator()


def test_create_csv(csv_generator):
    csv_generator.create_csv("test.csv")
    assert csv_generator.csvfile is not None


def test_add_row(csv_generator):
    csv_generator.create_csv("test.csv")
    csv_generator.add_row(["Hello", "world"])
    csv_generator.save("test.csv")
    with open("test.csv", "r") as f:
        content = f.read()
    assert "Hello,world" in content
    os.remove("test.csv")


def test_save_csv(csv_generator):
    csv_generator.create_csv("test.csv")
    csv_generator.add_row(["Hello", "world"])
    csv_generator.save("test.csv")
    assert os.path.exists("test.csv")
    os.remove("test.csv")
