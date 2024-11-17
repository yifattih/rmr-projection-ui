import unittest
from bs4 import BeautifulSoup


def load_html() -> str:
    """Fixture to load the index.html content."""
    with open("app/src/templates/index.html", "r") as file:
        return file.read()


class TestFormStructure(unittest.TestCase):
    def setUp(self) -> None:
        self.file = load_html()
        self.soup = BeautifulSoup(self.file, "html.parser")
        self.form = self.soup.find("form")

    def test_form_exist(self) -> None:
        """Check if file has a form"""
        self.assertIsNotNone(self.form)

    def test_form_fields(self) -> None:
        """Check if form has all required input fields"""
        fields = {
            "age": {"type": "number"},
            "weight": {"type": "number"},
            "height": {"type": "number"},
            "time": {"type": "number"},
            "rate": {"type": "number"},
            "energy": {"type": "number"},
        }

        for field_name, attribures in fields.items():
            field = self.form.find("input", {"name": field_name})
            self.assertIsNotNone(field)

            for attr, value in attribures.items():
                field_value = field.get(attr)
                self.assertEqual(field_value, value)

    def test_form_has_submit_button(self) -> None:
        submit_button = self.form.find("button", {"type": "submit"})
        self.assertIsNotNone(submit_button)

    def test_form_has_clear_button(self) -> None:
        clear_button = self.form.find("button", {"class": "clear"})
        self.assertIsNotNone(clear_button)
