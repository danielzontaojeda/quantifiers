Implementation of [quantifiers](https://www.researchgate.net/publication/242222834_Quantifying_Counts_Costs_and_Trends_Accurately_via_Machine_Learning) in python.

The dataset needs to have a `class` column with the instance label and a `score` column generated by some classificator.

|class|score      |
|-----|-----------|
|1    |0.940896749|
|1    |0.528437793|
|1    |0.644506037|
|1    |0.975728273|
|...  |...        |
|0    |0.223694086|
|0    |0.532646298|
|0    |0.452957034|
|0    |0.431746483|
|...  |...        |

## Installation

```
pip install venv
git clone https://github.com/danielzontaojeda/quantifiers
cd quantifiers
python -m venv .venv
source env/bin/activate # (UNIX) 
.\.venv\Scripts\activate # (Windows) 
pip install -r requirements.txt
python run.py dataset.csv
```

## Output
The result table will be saved in `output.csv` comparing the performance of different quantifiers. Multiple runs will be conducted for each combination of sample, size, and class distribution.

|sample|Test_size  |alpha|actual_prop|pred_prop|abs_error|accuracy|quantifier|
|------|-----------|-----|-----------|---------|---------|--------|----------|
|1     |10         |0    |0          |0.1      |0.1      |0.9     |CC        |
|1     |10         |0    |0          |0.23     |0.23     |0.7     |PCC       |
|1     |10         |0    |0          |0.09     |0.09     |0.9     |PACC      |
|1     |10         |0    |0          |0.05     |0.05     |1       |HDy       |
|1     |10         |0    |0          |0.03     |0.03     |1       |DyS       |
|1     |10         |0    |0          |0.13     |0.13     |0.8     |SMM       |
|2     |10         |0    |0          |0.1      |0.1      |0.9     |CC        |
|2     |10         |0    |0          |0.29     |0.29     |0.7     |PCC       |
|2     |10         |0    |0          |0.16     |0.16     |0.9     |PACC      |
|2     |10         |0    |0          |0.03     |0.03     |1       |MS        |
|2     |10         |0    |0          |0.05     |0.05     |1       |HDy       |
|2     |10         |0    |0          |0.03     |0.03     |1       |DyS       |


## Experiment settings
The settings can be configured in `config.py` to change the number of iterations, sample sizes or list of class distributions for the experiment.