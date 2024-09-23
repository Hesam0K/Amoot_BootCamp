# Expense manager program
import csv
import os
import datetime
from operator import itemgetter  # to sort a list of lists by a specific index of the inner lists
# in this project : sorting list of expenses by their date


class Expense:
    # ====================== constructor ======================
    def __init__(self, date, category='miscellaneous', amount=0, notice='Empty'):

        # obj gets the datas
        self.__date = date
        self.__category = category
        self.__amount = amount
        self.__notice = notice

    # ====================== getter functions ======================
    @property
    def date(self):
        return self.__date

    @property
    def category(self):
        return self.__category

    @property
    def amount(self):
        return self.__amount

    @property
    def notice(self):
        return self.__notice

    # ====================== setter functions ======================
    @date.setter  # date has to be str in form of '0000_00_00'
    def date(self, new_date):
        try:
            user_date = new_date.split('_')
            self.__date = datetime.datetime(int(user_date[0]), int(user_date[1]), int(user_date[2]))
        except Exception as e:
            print('Invalid date format!')
            print('Error occurred:', e)

    @category.setter  # category has to be string
    def category(self, new_category):
        if type(new_category) is not str:
            raise TypeError('Only strings are allowed!')
        else:
            self.__category = new_category

    @amount.setter  # amount has to be positive integer
    def amount(self, new_amount):
        if type(new_amount) is not int:
            raise TypeError('Only integers are allowed!')
        elif new_amount < 0:
            raise Exception('Negative amount is not allowed!')
        else:
            self.__amount = new_amount

    @notice.setter  # notice has to be string
    def notice(self, new_notice):
        if type(new_notice) is not str:
            raise TypeError('Only strings are allowed!')
        else:
            self.__notice = new_notice

    # ====================== add_expense method ======================
    def add_expense(self):  # writes the expense obj in the csv data file
        if not os.path.exists('expenses.csv'):  # writes field names if file does not exist
            field_names = ['date', 'category', 'amount', 'notice']
            with open('expenses.csv', 'w') as csvfile:  # creating the data file to write
                csvwriter = csv.writer(csvfile)  # building the writer iterator obj
                csvwriter.writerow(field_names)  # writing field names (first row)
        # building a string line of data
        expense_data = map(str, [f'{self.__date.year}_{self.__date.month}_{self.__date.day}',
                                 self.__category, self.__amount, self.__notice])
        with open('expenses.csv', 'a') as csvfile:  # appending the new data line to cvs data file
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(expense_data)

    # ====================== delete_expense method ======================
    def delete_expense(self, *search_stuff):  # gets some strings to search and deletes the first match
        if not os.path.exists('expenses.cvs'):  # checks whether data file exists
            raise Exception('There is no data to delete!')
        data_list = []  # transports datas from file to a list
        with open('expenses.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # passes the field row
            for row in reader:
                data_list.append(row)
        # now the search begins
        index_of_matched_line = -1
        found = False
        for i in range(len(data_list)):  # moves through rows of old data by index
            for column in data_list[i]:  # moves through items of every line of data
                if column in search_stuff:  # finds a match in the line
                    index_of_matched_line = i
                    found = True
                    break
            if found:
                break
        if index_of_matched_line == -1:
            print('no match found')
            return
        print(f"expense: {', '.join(data for data in data_list[index_of_matched_line])}"
              f" on line {index_of_matched_line} is deleted.")
        data_list.pop(index_of_matched_line)  # removing the flagged line from the list
        with open('expenses.csv', 'w') as csvfile:  # now writes the new data into file
            writer = csv.writer(csvfile)
            writer.writerow(['date', 'category', 'amount', 'notice'])  # writing field names (first row)
            writer.writerows(data_list)  # writing all data rows at once

    # ====================== total_expense method ======================

    def total_expense(self, category):
        if type(category) is not str:
            raise TypeError('category must be a string')
        if not os.path.exists('expenses.cvs'):
            raise Exception('there is no data to survey through!')
        data_list = []  # transports datas from file to a list
        with open('expenses.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # passes the field row
            for row in reader:
                data_list.append(row)
        total_amount = 0  # sum of expenses
        for row in data_list:
            if row[1] == category:  # finds lines of data with the same category
                total_amount += float(row[2])  # adds amount of the expense to the total_amount
        return total_amount

    # ====================== list_expenses_by_date module ======================

    def list_expenses_by_date(self, date):
        if not os.path.exists('expenses.cvs'):
            raise Exception('there is no data to survey through!')
        try:
            date_str = f'{date.year}_{date.month}_{date.day}'
            data_list = []  # transports datas from file to a list
            data_output = []  # saves data lines with the same date as inputted
            with open('expenses.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # passes the field row
                for row in reader:
                    data_list.append(row)
            for row in data_list:
                if row[0] == date_str:  # adds to data_output if it has the same date
                    data_output.append(row)
            print(f'Expenses by date {date_str} :')
            print('date  _  category  _  amount  _  notice')  # printing field row
            for row in data_output:  # now prints data_output line by line
                print(' _ '.join(data for data in row))
        except Exception as e:
            print('error occurred: ', e)

    # ====================== generate_report module ======================

    def generate_report(self):
        if not os.path.exists('expenses.cvs'):
            raise Exception('there is no data to generate report!')
        try:
            data_list = []  # transports datas from file to a list
            with open('expenses.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # passes the field row
                for row in reader:
                    data_list.append(row)
            data_list = sorted(data_list, key=itemgetter(0))  # sorts data_list by date from past to moment
            # printing the expenses sorted by year and month with category boxes
            year = data_list[0][0].split('_')[0]  # year of the first expense
            month = data_list[0][0].split('_')[1]  # month of the first expense
            month_category_dict = {data_list[0][1]: [data_list[0]]}
            # saving expenses by category.
            # category as key
            # list of expenses with the same category as value
            print(f'========== Year {year} ==========')
            print(f'---------- month {month} ----------')
            for row in data_list[1:]:
                if row[0].split('_')[0] == year and row[0].split('_')[1] == month:
                    # surveying through expenses in the same month and year
                    if row[1] not in month_category_dict:
                        # if new category found, add it to month_category_dict
                        month_category_dict[row[1]] = row
                    else:
                        # else append it to list of expenses with the same category
                        month_category_dict[row[1]].append(row)
                elif row[0].split('_')[0] == year:
                    # a month has passed, so we print all expenses seperated by category
                    for category in month_category_dict:
                        print(f'***** category: {category} *****')
                        for ex in category:
                            print(ex)
                    month = row[0].split('_')[1]  # month of the new expense which is the next month
                    month_category_dict.clear()
                    month_category_dict = {row[1]: [row]}




        except Exception as e:
            print('error occurred: ', e)
