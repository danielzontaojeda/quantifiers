import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from config import COUNTERS, N_ITERATIONS, ALPHA_VALUES, BATCH_SIZES, MEASURE


def apply_quantifier(quantifier, thr, measure, train_test, test_sample):
    print(
        f"quantifier = {quantifier}, thr = {thr}, measure = {measure}, train_test = {len(train_test)}, test_sample = {len(test_sample)}"
    )


def run_quantifiers(scores, classes):
    # Split the data into two equal halves
    X_train, X_test, y_train, y_test = train_test_split(
        scores, classes, test_size=0.5, stratify=classes
    )
    train_test = [X_train, X_test, y_train, y_test]

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

                # TODO: por que calcular isso, nao é sempre alpha?

                # Counting num of actual positives in test sample
                n_pos_sample_test = list(test_label).count(1)

                # actual pos class prevalence in generated sample
                calcultd_pos_prop = round(n_pos_sample_test / len(sample_test), 2)

                for quantifier in COUNTERS:
                    pred_pos_prop = apply_quantifier(
                        quantifier=quantifier,
                        thr=0.5,
                        measure=MEASURE,
                        train_test=train_test,
                        test_sample=test_sample,
                    )

                    # pred_pos_prop = round(
                    #     pred_pos_prop[1], 2
                    # )


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

    run_quantifiers(scores, classes)


if __name__ == "__main__":
    main()
