# Q1: Frequency of elements using a dictionary

numbers = [4, 7, 2, 7, 9, 4, 7, 2, 9, 9]

def count_frequency(lst):
    f = {}
    for num in lst:
        if num in f:
            f[num] += 1
        else:
            f[num] = 1
    return f

print(count_frequency(numbers))

# Q2: Find the second largest unique number.
      
numbers = [12, 5, 8, 21, 3, 16, 21, 7]

def second_largest(lst):
    max_num=0
    s_max=float('-inf')
    for num in lst:
        if (num > max_num):
            s_max = max_num
            max_num = num
        elif (num > s_max) and (num != max_num):
            s_max = num
    return s_max

print(second_largest(numbers))

#Q3:Create a new list with duplicates removed, while keeping the original order.

numbers = [4, 7, 2, 7, 9, 4, 2, 8, 9, 10]

def remove_duplicates(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(remove_duplicates(numbers))

#Q4:Find the first character that appears only once.
    
text = "aabbcdde"

def first_unique_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(first_unique_char(text))

#Q5:Create a new list containing the common elements.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

def common_elements(lst1, lst2):
    lst3 = []
    for n in lst1:
        for m in lst2:
            if n == m:
                lst3.append(n)
    return lst3

print(common_elements(list1, list2))

#Q6:You are given numbers from 1 to n, but exactly one number is missing.
 
numbers = [1, 2, 3, 5, 6, 7, 8]

def missing_num(lst):
    n=len(lst)+1
    total_sum = n * (n + 1) // 2
    sum=0
    for num in lst:
        sum+=num
    
    return total_sum - sum

print(missing_num(numbers))

#Q7: longest word

sentence = "Python is extremely useful for machine learning"

def longest_word(sen):
    words = sen.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(sentence))

#Q8:Anagram check

#It should return True if two strings contain the same characters with the same frequencies, otherwise False.
#are_anagrams("listen", "silent")
# True

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True

print(are_anagrams("listen", "silent"))

#Q9: Create the analyze_numbers() function we practiced earlier.

numbers = [12, 5, 8, 21, 3, 16, 7]
#the function should return a dictionary with the following keys and their corresponding values:
{
    "even_count": 3,
    "odd_count": 4,
    "largest": 21,
    "smallest": 3
}

def analyze_numbers(lst):   
    even_count = 0
    odd_count = 0
    largest = float('-inf')
    smallest = float('inf')
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        if num > largest:
            largest = num
        
        if num < smallest:
            smallest = num
    
    return {
        "even_count": even_count,
        "odd_count": odd_count,
        "largest": largest,
        "smallest": smallest
    }

print(analyze_numbers(numbers))
