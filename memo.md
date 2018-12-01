
## 打ってみる
```
python

type(1)
type('1')
type([1, 2, 3])
type({'first': 1, 'second':2})
3 + 2
3 - 2
3 * 2
3 / 2
3 // 2
3 ** 2
5 % 3
3 ** 2
3 ** 3
'hello world'
'hello world
'hello world         '.split()
'          hello world         '.split()
'hello world'.split('o')
'hello world'.split('l')
'{0}, {1}'.format('hello', 'world')
'{0} and {1}'.format('Tom', 'Jerry')
‘{word1} and {word2}’.format(word1=‘Hello’,word2=‘world’)

[1, 2, 3]
[1, 2, 3] + [4, 5, 6]
1 in [1, 2, 3]
5 in [1, 2, 3]
nums = [1, 2, 3]
nums
nums.remove(1)
nums.remove(1)
nums

fruits = {
  'apple': 100,
  'orange': 50,
}
fruits
fruits['apple']
fruits['orange']
fruits['grape']
fruits['apple'] * 2
name = 'apple'
fruits[name] * 2
count = 2
fruits[name] * count
name = 'orange'
count = 3
fruits[name] * count
def calc_fruit_amount(name, count):
  return fruits[name] * count
calc_fruit_amount('orange', 2)
def decide_amount(name, count, threshold=1000):
    amount = calc_fruit_amount(name, count)
    if amount > threshold:
        print('高い')
    elif amount == threshold:
        print('普通')
    else:  # < threshold
        print('安い')
for name in ['apple', 'orange']:
    print('{} {} 円'.format(name, fruits[name]))

fruits = {
    'apple': 100,
    'orange': 50,
}

def calc_fruit_amount(name, count):
    try:
        return fruits[name] * count
    except:
        print('{}は存在しません'.format(name))

```