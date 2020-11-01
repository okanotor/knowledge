# python

## main

```python
def main():
    # any program

if __name__ == '__main__':
    main()
```

## CSV 読み込み

```python
import csv

with open('/path/to/file.csv', encoding='utf-8') as ins:
    reader = csv.reader(ins)
    for row in reader:
        # any program with row
```
