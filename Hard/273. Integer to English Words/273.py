class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }

        if num == 0:
            return d[0]
    
        res = ""
        group = 1
        while num > 0:
            num, remain = num // 1000, num % 1000
            hundred = remain // 100
            group_str = ""
            if hundred > 0:
                group_str = d[hundred] + " " + d[100] + " "
        
            tens = remain % 100
            if tens == 0:
                group_str += ""
            elif tens < 20 or tens % 10 == 0:
                group_str = group_str + d[tens] + " "
            else:
                tens, unit = tens // 10, tens % 10
                group_str = group_str + d[tens * 10] + " " + d[unit] + " "

            if group == 1:
                res = res + group_str
            elif remain == 0:
                res += ""
            else:
                res = group_str + d[group] + " " + res
            group = group * 1000
        return res.strip()