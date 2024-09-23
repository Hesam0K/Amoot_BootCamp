import datetime
from operator import itemgetter

# expense1 = [datetime.datetime(2024, 9, 15), 'apple', 2500]
# expense2 = [datetime.datetime(2022, 8, 10), 'banana', 3000]
# expense3 = [datetime.datetime(2025, 4, 3), 'cherry', 250]
# expense_list = [expense1, expense2, expense3]

# ['date', 'category', 'amount', 'notice']

expense_list = [
                ['2024_9_15', 'apple', '2500', 'foo'],
                ['2022_8_10', 'banana', '3000', 'bar'],
                ['2025_4_3', 'cherry', '250', 'ger']]
expense_list = sorted(expense_list, key=itemgetter(0), reverse=False)
print(expense_list)


# year = expense_list[1][0].split('_')[0]
# print(year)
