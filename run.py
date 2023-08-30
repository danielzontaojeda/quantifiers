import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from config import COUNTERS, N_ITERATIONS, ALPHA_VALUES, BATCH_SIZES, MEASURE
from quantifiers.quantifier_factory import QuantifierFactory
from tqdm import tqdm


def apply_quantifier(quantifier_name, thr, measure, train_test, test_sample):
    factory = QuantifierFactory()
    quantifier = factory.create_quantifier(quantifier_name)
    if quantifier:
        if quantifier_name.lower() in quantifier.needs_dist_matching:
            quantifier.set_scores(train_test)
        quantifier.setTprFpr(train_test["X_train"], train_test["y_train"])
        return quantifier.predict(test_sample, thr, measure=measure)


def run_quantifiers(scores, classes):
    # Split the data into two equal halves
    X_train, X_test, y_train, y_test = train_test_split(
        scores, classes, test_size=0.5, stratify=classes
    )

    train_test = {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
    }

    columns = [
        "sample",
        "Test_size",
        "alpha",
        "actual_prop",
        "pred_prop",
        "abs_error",
        "quantifier",
    ]
    table = pd.DataFrame(columns=columns)

    # seperating positive and negative test examples
    df_test = pd.concat([X_test, y_test], axis="columns")
    df_test_pos = df_test.query("`class` == 1")
    df_test_neg = df_test.query("`class` == 0")

    total_iterations = len(BATCH_SIZES) * len(ALPHA_VALUES) * N_ITERATIONS
    overall_bar = tqdm(total=total_iterations, desc="Progress")

    # Sampling the dataset to run tests
    for sample_size in BATCH_SIZES:
        for alpha in ALPHA_VALUES:
            for iteration in range(N_ITERATIONS):
                # Number of positive and negative instances in sample
                pos_size = int(sample_size * alpha)
                neg_size = sample_size - pos_size

                # Creating sample
                if pos_size != sample_size:
                    sample_test_pos = df_test_pos.sample(pos_size, replace=False)
                else:
                    sample_test_pos = df_test_pos.sample(frac=1, replace=False)
                sample_test_neg = df_test_neg.sample(neg_size, replace=False)
                sample_test = pd.concat([sample_test_pos, sample_test_neg])
                test_label = sample_test["class"]
                test_sample = sample_test.drop(["class"], axis=1)
                test_sample = test_sample["score"].astype(float)

                # TODO: por que calcular isso, nao é sempre alpha?

                # Counting num of actual positives in test sample
                n_pos_sample_test = list(test_label).count(1)

                # actual pos class prevalence in generated sample
                calcultd_pos_prop = round(n_pos_sample_test / len(sample_test), 2)

                for quantifier in COUNTERS:
                    pred_pos_prop = apply_quantifier(
                        quantifier_name=quantifier,
                        thr=0.5,
                        measure=MEASURE,
                        train_test=train_test,
                        test_sample=test_sample,
                    )
                    if pred_pos_prop:
                        # Getting only the positive proportion
                        pred_pos_prop = round(pred_pos_prop, 2)

                        # ---------------RESULTS---------------
                        abs_error = round(abs(calcultd_pos_prop - pred_pos_prop), 2)
                        result = {
                            "sample": iteration + 1,
                            "Test_size": sample_size,
                            "alpha": alpha,
                            "actual_prop": calcultd_pos_prop,
                            "pred_prop": pred_pos_prop,
                            "abs_error": abs_error,
                            "quantifier": quantifier,
                        }
                        result = pd.DataFrame([result])

                        table = pd.concat([table, result], ignore_index=True)
            overall_bar.update(1)
    overall_bar.close()
    return table


def main():
    # Check if filename was passed as argument
    if len(sys.argv) < 2:
        print("ERROR! Dataset name should be passed as an argument:")
        print(r"python run.py {dataset_name}.csv")
        exit(1)

    dataset_name = sys.argv[1]
    df = pd.read_csv(dataset_name)
    scores = df["score"]
    classes = df["class"]

    table = run_quantifiers(scores, classes)
    print(table)
    table.to_csv("output.csv", index=False)
    print("Data saved successfully")
    average_abs_error = table.groupby('quantifier')['abs_error'].mean()
    average_abs_error = average_abs_error.sort_values()
    print("Average error:")
    print(average_abs_error)

if __name__ == "__main__":
    main()
