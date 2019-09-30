import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades,
                   'classroom': np.random.choice(['A', 'B'], len(students))})
sns.relplot(data = df, x = 'math', y = 'english')

df['passing_math'] = df.math.apply(lambda n: 'passing' if n >= 70 else 'failing')


sns.relplot(data=df, x = 'math', y = 'english', col = 'classroom')

sns.relplot(data = df, x = 'math', y = 'english', hue = 'passing_math', style = 'classroom')


sns.distplot(df.math)

sns.boxplot(data = df, x = 'math')
sns.boxplot(data = df, y = 'math')

sns.boxplot(data = df, y = 'math', x = 'classroom')

sns.boxplot(data = df, y = 'math', x = 'classroom', hue = 'passing_math')
#overall math grade median
plt.hlines(df.math.median(), -1, 2, ls = ':', color = 'white')
plt.text(.5, df.math.median(), '{}'.format(df.math.median()),color = 'black')

from pydataset import data
tips = sns.load_dataset('tips')

sns.boxplot(data = tips, y = 'total_bill', x = 'size')
# add median.
plt.hlines(tips.total_bill.median(), -1, 6, ls = ':', color = "white")

sns.boxplot(data = tips, y = 'total_bill', x = 'size', hue = 'smoker')
# add a line at the overall median.
plt.hlines(tips.total_bill.median(), -1, 6, ls = ':', color = "white")

plt.figure(figsize = (10,7))
sns.heatmap(df.corr(), annot = True, cmap = 'Blues')

help(sns.heatmap)

pd.crosstab(tips['size'],tips.smoker)
tips.pivot_table('total_bill', 'size',['time','smoker'], aggfunc = 'max')
tips
sns.heatmap(pd.crosstab(tips['size'], tips.smoker))

sns.jointplot(data = df, x = 'reading', y = 'english')

# Good for explorations!!!
sns.pairplot(data = df)