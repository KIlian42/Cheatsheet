import pandas as pd




def main():
    df = pd.read_csv("dataset.csv", delimiter=";")

    # => All column names
    columns = df.columns

    # => Iterate table
    for index, row in df.iterrows():
        column1_value = row["column1_name"]
        column2_value = row["column2_name"]
    
    # => Access row 3 and column 2 with iloc
    third_row_value = df.iloc[2, 1]

    # => Print datatypes of table columns
    print(df.dtypes)

    # Drop column
    df.drop('ColumnA', axis=1, inplace=True)

    # => Convert column to specific type
    df['column_name'] = df['column_name'].astype(str)

    # => Convert specific columns to list
    title = list(df['title'])
    description = list(df['notes'])

    # => Drop nans
    # Drop row if specific column is nan
    df.dropna(subset=['column_name'], inplace=True)
    # Drop row if all columns are nan except one
    mask = df.drop(columns=[exclude_column]).isna().all(axis=1)
    df_clean = df[~mask]
    # Drop row if all columns are nan
    df_clean = df.dropna(how='all')

    # => Write modified table to csv
    df.to_csv(file_path, sep=';', index=False)

if __name__ == "__main__":
    main()