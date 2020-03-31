# つくば市のゴミ収集カレンダー

> つくば市西地区のごみ収集カレンダーをインターネット上からスクレイピングして取得し，iCal形式で出力するスクリプト

## Prerequisites

- Python 3.8
- Poetry

## Setup

```bash
poetry install
```

## Lint

```bash
flake8 --show-source .
```

## Format

```bash
autopep8 -ivr .
```

## Usage

```bash
poetry shell # enter virtual env
python main.py # execute script
```
