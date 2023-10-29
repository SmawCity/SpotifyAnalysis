import numpy as np
import pandas as pd

def clean_data(dataset, column):
    dataset.sort_values([column], axis=0,ascending=[False], inplace=True)
    dataset['streams'] = pd.to_numeric(dataset['streams'], errors='coerce')
    dataset.dropna(subset=column)

def main():
    df = pd.read_csv('spotify-2023.csv', encoding='latin-1')
    pd.options.display.float_format = '{:.2f}'.format
    df.drop(['in_deezer_playlists', 'in_deezer_charts','danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'], axis = 1, inplace=True)

    df['released_date'] = pd.to_datetime(df['released_year'].astype(str) + '-' + df['released_month'].astype(str) + '-' + df['released_day'].astype(str), format = '%Y-%m-%d')
    df.drop(['released_year', 'released_month', 'released_day'], axis = 1, inplace=True)

    bpm_chart = df
    key_chart = df
    mode_chart = df

    clean_data(bpm_chart, "bpm")
    clean_data(key_chart, "key")
    clean_data(mode_chart, "mode")

    # Gets the average streams for the fastest and slowest songs respectively
    print('\033[1mSorted by BPM:\033[0m')
    avg_streams = bpm_chart.head(50)['streams'].astype(float).mean()
    print(f"Average streams(Top 50 Fastest Songs): {avg_streams}")
    avg_streams = bpm_chart.tail(50)['streams'].astype(float).mean()
    print(f"Average streams(Top 50 Slowest Songs): {avg_streams}")

    # Groups songs together by key and calculates the average number of streams per key
    print('\033[1m\nSorted by Key:\033[0m')
    key_groups = key_chart.groupby('key')
    avg_key_streams = key_groups['streams'].mean()

    # Prevents the name of the pandas series from displaying
    avg_key_streams.name = None
    print(avg_key_streams)

    # Groups songs together by mode and calculates the average number of streams in each mode
    print('\033[1m\nSorted by Mode:\033[0m')
    mode_groups = mode_chart.groupby('mode')
    avg_mode_streams = mode_groups['streams'].mean()

    avg_mode_streams.name = None
    print(avg_mode_streams)

if __name__ == "__main__":
    main()