import pandas as pd 

RAW_PATH = "data/Concrete_Data.xls"
CLEAN_PATH = "data/concrete.csv"

COLUMNS = ["cement", "slag", "fly_ash", "water", "superplasticizer","coarse_agg","fine_agg", "age", "strength" ]

def load_raw(): 
    df = pd.read_excel(RAW_PATH)
    print ("Tên cột gốc: ")
    for c in df.columns:
        print(" -", c)
    return df

# doi ten cot
def rename_columns(df):
    assert df.shape[1] == 9, f"Cần 9 cột, hiện có {df.shape[1]}"
    df = df.copy()
    df.columns = COLUMNS
    return df

def main():
    df = load_raw()
    df = rename_columns(df)
    df.to_csv(CLEAN_PATH, index=False)
    print("\nKích thước:", df.shape)
    print(df.head())
    print("\nKhoảng giá trị mỗi cột:")
    print(df.describe().T[["min", "max"]])


if __name__ == "__main__":
    main()