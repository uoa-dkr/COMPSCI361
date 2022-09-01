import numpy as np
import pandas as pd

## one-dimensional series
a = [n for n in range(1, 6)]
x = pd.Series(a)
print(x)
print(f'{x[2]}')  # third element of the series
print(x.values)
print(np.exp(x))
print()

x = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])  # change the varb name
print(x)
print(f'{x[["c"]]}')
print(x.index)
print()

a = {'a': '1', 'b': '2', 'c': 3}  # user-defined varb name
x = pd.Series(a)
print(f'{x}')
print()

a = {'x': True, 'y': True, "z": False}
x = pd.Series(a, index=['a', 'z', 'x'])  # pick some varb, it doesn't exist then the value is NaN
print(f'{x}\n')

print(x.name, x.index.name)
x.name = 'T-F';
x.index.name = 'letter'
print(x, x.name, x.index.name)
print()
x = x.drop('a')  # have to assign to a new varb
print(x)
print()
print()

## two-dimensional series (dataframe)
a = [n for n in range(1, 6)]
x = pd.DataFrame(a)
print(x)  # special df

a = {'cars': ["BMW", "Volvo", "Ford"],
     'pass': [3, 7, 2],
     'import': [True, False, False]}
x = pd.DataFrame(a)
y = pd.DataFrame(a, columns=['import', 'cars', 'pass'])  # adjust the position of col
print(f'\n\n{x}\n')
print(y)
print()
y.index = ['one', 'two', 'three']
y = y.drop('one')
print(y)
print()
print()

pop = {'Nevada': {2001: 2.4, 2002: 2.9},  # nested dic
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
df = pd.DataFrame(pop)  # inner key as row indices, outer key as col indices
print(df)
print(df.T)
df.index.name = 'year';
df.columns.name = 'city'
print(df)
print()
print()

# work on col
print(f"{x['cars']}\n")  # first column(series)
print(f"{x[['cars']]}\n")  # first column(itself) pretty close
print(x.loc[:, "cars"])  # loc allows both int and varb name
print(f'\n{x.iloc[:, [0]]}\n')  # iloc only allows int
print(x[['cars', 'pass']])  # choose multiple cols
print(f'\n{x.iloc[:, 0:2]}\n\n')  # choose multiple cols  ... etc

# work on row
print(f'{x[1:2]}\n')  # 2sr row(itself)
print(x.iloc[1])  # 2st row(series)
print(f'\n{x.iloc[[1]]}\n')  # 2st row(itself)
print(x.loc[1])  # 2st row(series)
print(f'\n{x.iloc[[1, 2, 0]]}\n')  # multiple rows

# filter (care for series or itself)
print(f'\n{x.loc[1, "cars"]}\n')  # row 2 col 1
print(f'{x.iloc[[0, 2], 1]}\n')  # row 1,3 col 2
print(f'{x.iloc[0:2, [-1]]}\n\n')  # row 1,2,3 col 3

print(x[x['pass'] > 2.5])  # pass > 2.5
print(f'\n{x.loc[x["pass"] > 2.5, ["pass", "import"]]}\n')  # pass > 2.5 and only pass and import
print(x[(x['pass'] > 2.5) & (x['import'] == True)])  # pass > 2.5 and import == T
print(f'\n{x[x["pass"].between(2, 7)]}')
print()
print()

# Arithmetic and statistical
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('bdca'))
df2 = pd.DataFrame(np.arange(20., 40.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'c'] = np.nan
print(df1 - df2)
print(df1.add(df2, fill_value=0))
print(df1.reindex(columns=df2.columns, fill_value=0))
print()
print()

print(s1.rank())
print(df1.rank(axis=1))
print(s1.sort_values(ascending=False))
print(df1.sort_values(by=['c', 'b']))  # sort by multiple columns
print(df1.sort_index(axis=1))
print(df2.mean(skipna=False))
print(df2.describe())
print()
print()


# function application
f = lambda x: x.max() - x.min()
print(df2, df2.apply(f, axis=1))
print()

def func(x):
    return x.max() - x.min()
print(df2.apply(func, axis=1))
print()


####################################################################################################
# read files

df = pd.read_csv('data/practice.csv')
print(f'\n{df}')
print()

df = pd.read_csv('data/practice.csv', header=None)  # remove header
print(df)
print()

df = pd.read_csv('data/practice.csv', names=['a', 'b', 'c', 'd'])  # modify the header
print(df)
print()

print(pd.read_csv('data/practice.csv', skiprows=[0, 1]))  # skip 1st and 2nd rows
print(pd.read_csv('data/practice.csv', nrows=5))  # only read 1st 5 rows
print()

df = pd.read_csv('data/practice.csv', na_values=[1.599])  # treat all 1.599 as NA
print(df)
print(df.describe())
print()

# first_5 = df.head(5)
# print(f'\n{first_5}')

