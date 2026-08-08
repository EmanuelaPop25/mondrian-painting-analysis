import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    painting_info = pd.read_csv("data/mondrian-painting-info.csv")
    painting_features = pd.read_csv("data/mondrian-painting-features.csv")
    fp26_features = pd.read_csv("data/fp26-features.csv")
    return painting_info, painting_features, fp26_features

def calculate_complexity(painting_features):
    complexity = painting_features.groupby("painting_id").size()
    complexity = complexity.reset_index(name="complexity")
    return complexity

def merge_data(painting_info, complexity):
    painting_info = painting_info.merge(complexity,on="painting_id")
    return painting_info

def create_chart(painting_info):
    plt.figure(figsize=(10,6))
    plt.scatter(painting_info["year"], painting_info["complexity"])
    plt.title("Complejidad de las pinturas de Mondrian")
    plt.xlabel("Año")
    plt.ylabel("Complejidad")
    plt.show()

def main():
    painting_info, painting_features, fp26_features = load_data()

    complexity = calculate_complexity(painting_features)

    painting_info = merge_data(painting_info, complexity)

    create_chart(painting_info)

    print("Complejidad media:", painting_info["complexity"].mean())
    print("Complejidad mínima:", painting_info["complexity"].min())
    print("Complejidad máxima:", painting_info["complexity"].max())

    average_complexity = painting_info["complexity"].mean()

    fp26_complexity = len(fp26_features)

    print("Complejidad de fp26:", fp26_complexity)

    if fp26_complexity > average_complexity:
        print("La pintura fp26 tiene una complejidad superior a la media.")
    else:
        print("La pintura fp26 tiene una complejidad inferior o igual a la media.")


if __name__ == "__main__":
    main()