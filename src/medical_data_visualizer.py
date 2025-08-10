import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
def import_data(file_path):
    return pd.read_csv(file_path)

# 2. Add overweight column
def add_overweight_column(df):
    bmi = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (bmi > 25).astype(int)
    return df

# 3. Normalize cholesterol and gluc
def normalize_data(df):
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
    return df

# 4-8. Draw categorical plot
def draw_categorical_plot(df):
    # 5. Melt DataFrame
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # 6. Group and reformat
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # 7. Draw catplot
    fig = sns.catplot(
        x='variable', y='total', hue='value', col='cardio',
        data=df_cat, kind='bar'
    ).fig
    # 8. Return fig
    return fig

# 9-17. Draw heat map
def draw_heat_map(df):
    # 10. Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    # 11. Correlation matrix
    corr = df_heat.corr()
    # 12. Mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # 13. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    # 14. Draw heatmap
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".1f", center=0, vmax=.3, vmin=-.1, square=True, linewidths=.5, cbar_kws={"shrink": .5}
    )
    # 15. Return fig
    return fig