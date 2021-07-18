from DataSource import DataSource

def main():
    source = DataSource()
    source.to_csv("data", "rent.csv")

if __name__ == "__main__":
    main()