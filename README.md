This Jupyter notebook can help you forecast your yearly budget as a ZZP in the Netherlands.

## Output examples
```
Gross income: 120000 
	(avg. per month: 10000)
Effective tax rate: 0.328664
----
Net income: 68560.3 
	(avg. per month: 5713.36)
Disposable income: 56560.3 
	(avg. per month: 4713.36)
----
Savings: 12000
Pension contributions: 12000
```

![image](https://github.com/eugene-blokhin/financial-forecasting/assets/873290/61a2e8b4-89d6-49d7-9070-d1bb22849989)

## Running it locally

1. Execute:
```
git clone git@github.com:eugene-blokhin/financial-forecasting.git
cd financial-forecasting
docker-compose up -d
```

2. Once the container has spun up, navigate to http://localhost:8888/lab/tree/CalculateTax.ipynb?token=easy and follow the instructions in the notebook.
