""""
track when the patterns in the values repeat and corrilate that with the current page

track the current page 
check if it mactches the page queried 
count the number of items on the page 

"""

# def page_item_count(collection,items_per_page,page_indexed):
#     page = 0
#     total = 0
#     answer = tuple(len(collection[i:i + items_per_page]) for i in range(0, len(collection), items_per_page))
#     for index,item in enumerate(collection):
#         if (index % items_per_page) == 0:
#             page += 1
#         if page == page_indexed:
#             total += 1
#     print(answer[page_indexed])        
# page_item_count(['a','b','c','d','e','f','g'], 2,3)        

def from_roman(roman_num):
        values = {'I':1,'IV':4,"V":5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        keys = ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
        answer = 0
        counter = 0
        for letter in roman_num:
            if len(roman_num) > 1:
                larger_letter = roman_num[(counter + 1)]
                normal_letter = roman_num[]                                                                                                            
                if values[letter] < values[larger_letter]:
                    answer += values[larger_letter] - values[letter]
                else:
                    answer += values[letter]
            else:
                answer = values[roman_num]

from_roman("MMVIII")     