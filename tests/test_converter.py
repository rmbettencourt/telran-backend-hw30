# ./tests/test_converter.py
from unittest import TestCase, main
from pandas import DataFrame

from src.converter import enumerator, columns_mapper, convert_x


class TestConverter(TestCase):

    def setUp(self):
        self.df = DataFrame({
            "Company": ['Toyota', 'Toyota', 'Hundai', 'Hundai', 'Hundai'],
            "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']
        })
        self.mapper = columns_mapper(["Company", "Model"], self.df)

    def test_enumerator(self):
        expected = {
            'Toyota': 0,
            'Hundai': 1
        }
        values = self.df['Company'].unique().tolist()
        actual = enumerator(values)
        self.assertEqual(expected, actual)

    def test_columns_mapper(self):
        actual = columns_mapper(["Company"], self.df)
        expected = {
            "Company": {"Toyota": 0, "Hundai": 1}
        }
        self.assertEqual(expected, actual)

    def test_convert_x(self):
        df_converted = convert_x(self.df, self.mapper)
        actual = df_converted.to_dict(orient="list")
        expected = {
            "Company": [0, 0, 1, 1, 1],
            "Model": [0, 1, 2, 3, 4]
        }
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
