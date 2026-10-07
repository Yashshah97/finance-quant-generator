# Finance Quant Synthetic Data Generator

This project provides a reliable and customizable tool for generating synthetic financial data, allowing developers to simulate real-world market scenarios without relying on actual market data. With its focus on statistical plausibility, this generator can be used to test trading strategies, risk models, and other quantitative finance applications with confidence. By leveraging pure Python implementation, it's easy to integrate into existing workflows.

## What makes it unique

Combines market time series and risk metrics with a statistically-plausible fake data generator for testing — a niche where few ready-made tools exist.

## Features

- **`finance_quant_generator/data_generator.py`** — The main entry point for the synthetic data generator.
- **`finance_quant_generator/utils.py`** — Utility functions used throughout the project.
- **`finance_quant_generator/market_models.py`** — Statistical models for generating market time series data.
- **`finance_quant_generator/risk_metrics.py`** — Functions to calculate statistically-plausible risk metrics.
- **`finance_quant_generator/config.py`** — Configuration and parameter management for the generator.
- **`finance_quant_generator/tests_test_data_generator.py`** — Tests for the synthetic data generator.

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/finance-quant-generator.git
cd finance-quant-generator

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
finance-quant-generator/
├── finance_quant_generator/
│   ├── data_generator.py
│   ├── utils.py
│   ├── market_models.py
│   ├── risk_metrics.py
│   ├── config.py
│   ├── tests_test_data_generator.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **finance-quant** · Archetype: **generator** ·
Built autonomously by JARVIS on 2026-10-06. MIT licensed.
