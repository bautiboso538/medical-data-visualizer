# main.py

from medical_data_visualizer import import_data, add_overweight_column, normalize_data, draw_categorical_plot, draw_heat_map

def main():
    # Import data
    df = import_data('data/medical_examination.csv')
    # Add overweight column
    df = add_overweight_column(df)
    # Normalize data
    df = normalize_data(df)
    # Draw categorical plot
    fig_cat = draw_categorical_plot(df)
    fig_cat.savefig('catplot.png')
    # Draw heat map
    fig_heat = draw_heat_map(df)
    fig_heat.savefig('heatmap.png')

if __name__ == "__main__":
    main()