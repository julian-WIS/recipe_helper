import pandas as pd

def main():
    df = pd.read_csv("data/recipes.csv", index_col=0)

    print("First 5 records:", df.columns())


if __name__ == "__main__":
    main()
