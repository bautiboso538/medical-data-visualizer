import unittest
import pandas as pd
from src.medical_data_visualizer import add_overweight_column, normalize_data, draw_categorical_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):

    def setUp(self):
        # Crea un DataFrame de ejemplo para los tests
        self.df = pd.DataFrame({
            'height': [170, 160],
            'weight': [70, 80],
            'cholesterol': [1, 2],
            'gluc': [1, 3],
            'smoke': [0, 1],
            'alco': [0, 1],
            'active': [1, 0],
            'ap_hi': [120, 140],
            'ap_lo': [80, 90],
            'cardio': [0, 1]
        })

    def test_add_overweight_column(self):
        df = add_overweight_column(self.df.copy())
        # BMI: 70/(1.7^2)=24.22 (not overweight), 80/(1.6^2)=31.25 (overweight)
        self.assertEqual(df['overweight'].tolist(), [0, 1])

    def test_normalize_data(self):
        df = normalize_data(self.df.copy())
        # cholesterol: [1,2] -> [0,1], gluc: [1,3] -> [0,1]
        self.assertEqual(df['cholesterol'].tolist(), [0, 1])
        self.assertEqual(df['gluc'].tolist(), [0, 1])

    def test_draw_categorical_plot(self):
        df = add_overweight_column(self.df.copy())
        df = normalize_data(df)
        fig = draw_categorical_plot(df)
        self.assertIsNotNone(fig)

    def test_draw_heat_map(self):
        df = add_overweight_column(self.df.copy())
        df = normalize_data(df)
        fig = draw_heat_map(df)
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()