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


## ODBC接続文字列作成

- cf. https://docs.microsoft.com/en-us/sql/relational-databases/native-client/applications/using-connection-string-keywords-with-sql-server-native-client?view=sql-server-ver15

```python
info = {
    'Driver': '{Some Driver}',
    'Server': 'some_server',
    'UID': 'userid',
    'PWD': 'password',
    'Database': 'some_database'
}

def create_connstring(info):
    return ';'.join(map(lambda x: '='.join(x), info.items()))
```


# sqlite3

```python
import sqlite3

with sqlite3.connect('./test.db') as conn:
    cursor = conn.cursor()
```