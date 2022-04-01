# 1.  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# Տրված է ամբողջ թվերի զանգված/լիստ և նպատակային արժեք (target)։ Վերադարձնել լիստի միջի այն երկու թվերի ինդեքսները
# որոնց գումարը հավասար է նպատակին։
# Կարող ենք համարել, որ լուծում միշտ գոյություն ունի և միայն մի հատ է։

import time


def two_sum(lst_attr, target_attr):
    lst_result = []
    key_i = 0
    for i in lst_attr:
        key_j = 0
        for j in lst_attr[key_i + 1]:
            if i + j == 17:
                print(i, j)
                lst_result.append(key_i)
                lst_result.append(key_j + index)
                break
        if not lst_result:
            key_j += 1
        else:
            break

    return lst_result


start = time.time()
lst = [12, 6, 12, 14, 5]
target = 17
result = two_sum(lst, target)
# print(result)
end = time.time()
# print(end - start)


# 2․ You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Տրված է տարբեր օրերին որոշակի ապրանքի արժեքները պարունակող լիստ։ Համարել, որ ինդեքսները օրերն են։ Ընտրելով մեկ
# օր և գնելով ապրանքը ապա վաճառելով մեկ այլ օր՝ մենք ենք ուզում ստանալ առավելագույն շահույթ։
# Եթե շահույթ ստանալ հնարավոր չէ, վերադարձնել 0։

def profit(prices_attr):
    min_buy_val = prices_attr[0]
    max_sell_val = prices_attr[1]
    future_min_buy_val = max_sell_val
    max_income = max_sell_val - min_buy_val
    for next_val in prices_attr[2:]:
        if next_val > max_sell_val:
            max_sell_val = next_val
            if future_min_buy_val < min_buy_val:
                max_income = max_sell_val - future_min_buy_val
            else:
                max_income = max_sell_val - min_buy_val
        elif next_val < min_buy_val:
            future_min_buy_val = next_val
        else:
            if next_val - future_min_buy_val > max_income:
                max_income = next_val - future_min_buy_val
                min_buy_val = future_min_buy_val
            future_min_buy_val = next_val
    return max_income


prices = [200, 250, 300, 270, 380, 190, 375, 100]
# prices = [240, 220, 225, 280, 195, 320]
k = profit(prices)
print(k)

# 3. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Տրված է ամբողջ թվերի զանգված/լիստ։ Վերադարձնել նոր answer լիստ, որտեղ answer[i]-ն հավասար կլինի օրիգինալ լիստի
# բոլոր տարրերի արտադրյալին բացի i-րդ տարրից։
# Գրել կոդ, որը կաշխատի O(n) ժամանակային բարդությամբ։

# Օրինակ՝
# Input: [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
