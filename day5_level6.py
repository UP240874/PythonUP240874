
# 1. Declare an empty list
my_list = []

# 2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6]

# 3. Find the length of your list
len(my_list)

# 4. Get first, middle, and last item
my_list[0]
my_list[len(my_list)//2]
my_list[-1]

# 5. Declare mixed_data_types list
mixed_data_types = ['Caro', 25, 1.75, 'Soltero', 'TuDirección']

# 6. Declare it_companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list
print(it_companies)

# 8. Print number of companies
len(it_companies)

# 9. Print first, middle, and last company
it_companies[0]
it_companies[len(it_companies)//2]
it_companies[-1]

# 10. Modify one company
it_companies[0] = 'Meta'

# 11. Add an IT company
it_companies.append('Tesla')

# 12. Insert in the middle
it_companies.insert(len(it_companies)//2, 'Intel')

# 13. Change name to uppercase (not IBM)
it_companies[1] = it_companies[1].upper()

# 14. Join with '#; '
'#; '.join(it_companies)

# 15. Check if company exists
'Google' in it_companies

# 16. Sort list
it_companies.sort()

# 17. Reverse list
it_companies.reverse()

# 18. Slice first 3
it_companies[:3]

# 19. Slice last 3
it_companies[-3:]

# 20. Slice middle
mid = len(it_companies)//2
it_companies[mid] if len(it_companies) % 2 != 0 else it_companies[mid-1:mid+1]

# 21. Remove first company
it_companies.pop(0)

# 22. Remove middle
mid = len(it_companies)//2
it_companies.pop(mid)

# 23. Remove last
it_companies.pop()

# 24. Remove all
it_companies.clear()

# 25. Destroy list
del it_companies

# 26. Join front_end and back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# 27. Insert Python and SQL after Redux
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
