# Exercise 5
# Recursive Subset finder
def recursive_subsets_finder(mySet):  # does only the calculation
    if mySet == []:
        return [[]]
    x = recursive_subsets_finder(mySet[1:])
    return x + [[mySet[0]] + y for y in x]

# =============================================================================
callCount = 1
def recursive_subsets_finder_Steps(mySet):  # calculates and demonstrates how it works with steps!
    global callCount
    print("-----------------I'm going in! --------------------------------")
    print(f'function is called for the {callCount}th time.')
    callCount += 1
    print(f'Input set is: {mySet}')
    if mySet == []:
        print('+++++++++++++++++ coming back +++++++++++++++++++++++++++++')
        callCount -= 1
        print(f'return in {callCount}th function is: [[]]')
        print('+++++++++++++++++ coming back +++++++++++++++++++++++++++++')
        return [[]]
    x = recursive_subsets_finder_Steps(mySet[1:])
    callCount -= 1
    print(f'x in {callCount}th function is : ', x)
    print(f'[new member "{mySet[0]}" added to each member of recent x] in {callCount}th function is: {[[mySet[0]] + y for y in x]}')
    print('now appending x to new set made by recent new member')
    print(f'return in {callCount}th function is: ', x + [[mySet[0]] + y for y in x])
    print('+++++++++++++++++ coming back +++++++++++++++++++++++++++++')
    return x + [[mySet[0]] + y for y in x]
# =========================================================================================
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

theSet = [1, 2, 3]
print(f'\nsubsets of {theSet} is: {recursive_subsets_finder(theSet)}')
print('\n========================================================\n')
print(f'now calculating subsets of {theSet} with steps:\n')
print(recursive_subsets_finder_Steps(theSet))
print('\n========================================================\n')
n = int(input("enter n to calculate it's fibonacci result: "))
print(f'{n}th number of fibonacci sequence is {fib(n)}')