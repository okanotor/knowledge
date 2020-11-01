# ruby

## main

```ruby
def main
  # any program
end

if __FILE__ == $0
  main
end
```

## CSV 読み込み

```ruby
require 'csv'

CSV.foreach('/path/to/file.csv', encoding: 'UTF-8') do |row|
  # any program with row
end
```
