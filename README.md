# Medical Data Visualizer

## Overview
Medical Data Visualizer is a Python project that analyzes and visualizes medical examination data using pandas, matplotlib, and seaborn. It provides insights into patient health metrics through categorical plots and correlation heatmaps.

## Project Structure
```
medical-data-visualizer
├── src
│   ├── medical_data_visualizer.py
│   └── main.py
├── tests
│   └── test_module.py
├── data
│   └── medical_examination.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## File Descriptions
- **src/medical_data_visualizer.py**: Core logic for importing, processing, and visualizing the medical data. Includes functions for BMI calculation, data normalization, categorical plotting, and heatmap generation.
- **src/main.py**: Entry point for running the application. Imports and executes the main analysis and visualization functions.
- **tests/test_module.py**: Unit tests for the main data processing and visualization functions.
- **data/medical_examination.csv**: The dataset containing patient information such as age, height, weight, blood pressure, cholesterol, glucose, smoking, alcohol intake, physical activity, and cardiovascular disease.
- **requirements.txt**: Lists all Python dependencies.
- **.gitignore**: Specifies files and folders to be ignored by git.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd medical-data-visualizer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application and generate the visualizations:

```bash
python [main.py](http://_vscodecontentref_/2)
```

This will create `catplot.png` and `heatmap.png` in your project directory.

## Running Tests

To run the unit tests:

```bash
python -m unittest tests/test_module.py
```

## Dataset Information

The `medical_examination.csv` file contains the following columns:

- `age`: Age in years
- `height`: Height in cm
- `weight`: Weight in kg
- `ap_hi`: Systolic blood pressure
- `ap_lo`: Diastolic blood pressure
- `cholesterol`: 1 (normal), 2 (above normal), 3 (well above normal)
- `gluc`: 1 (normal), 2 (above normal), 3 (well above normal)
- `smoke`: 0 (no), 1 (yes)
- `alco`: 0 (no), 1 (yes)
- `active`: 0 (no), 1 (yes)
- `cardio`: 0 (no cardiovascular disease), 1 (cardiovascular disease)

## Visualizations

- **catplot.png:** Shows the counts of good and bad outcomes for cholesterol, glucose, alcohol, physical activity, smoking, and overweight status, split by presence or absence of cardiovascular disease.
- **heatmap.png:** Displays the correlation matrix for all numerical features, helping to identify relationships between health indicators.

## License

This project is for educational purposes and does not include a formal license.

