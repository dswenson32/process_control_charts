# This is a sample Python script.
from __future__ import print_function
import numpy as np

RULE_1_TEXT = "Rule 1 triggered - A datapoint falls below -3 standard deviations from the mean"
RULE_2_TEXT = "Rule 2 triggered - 9 or more points in a row below the mean"
RULE_3_TEXT = "Rule 3 triggered - six points in a row are decreasing"
RULE_4_TEXT = "Rule 4 triggered - 14 consecutive points are alternating, increasing then decreasing"
RULE_5_TEXT = "Rule 5 triggered - 2 of last 3 points are more than -2 standard deviations below the mean"
RULE_6_TEXT = "Rule 6 triggered - 4 of last 5 points are more than -1 standard deviations below the mean"
RULE_7_TEXT = "Rule 7 triggered - 15 points in a row are within +/- 1 standard deviation from the mean"
RULE_8_TEXT = "Rule 8 triggered - 8 points in a row are above or below 1 standard deviation, alternating up and down"

# Check if last datapoint is < -3 STDEV
def rule_1(datapoints, mean, stdev):
    if datapoints[0] < (mean + -3 * stdev):
        print(RULE_1_TEXT)
        return True
    return False  


# Nine or more data points in a row below the mean
def rule_2(datapoints, mean, stdev):
    count = 0

    for point in datapoints[:9]:
        if point < mean:
            count += 1
            if count >= 9:
                print(RULE_2_TEXT)
                return True
        else:
            count = 0
    return False


# 6 points in a row are decreasing
def rule_3(datapoints, mean, stdev):
    count = 0

    for i in range(1, 7):
        if datapoints[i] < datapoints[i - 1]:
            count += 1
            if count == 6:
                print(RULE_3_TEXT)
                return True
        else:
            count = 0
    return False


# 14 points in a row are alternating, increase then decrease
def rule_4(datapoints, mean, stdev):
    count = 0

    # Iterating using loop
    for i in range(1, 15):
        if (datapoints[i - 1] < datapoints[i] > datapoints[i + 1]) or (datapoints[i - 1] > datapoints[i] < datapoints[i + 1]):
            count += 1
            if count == 14:
                print(RULE_4_TEXT)
                return True
        else:
            count = 0
    return False
    # print("Rule 4 not triggered")


# 2/3 points in a row are < -2 stdev from mean
def rule_5(datapoints, mean, stdev):
    threshold = mean - 2 * stdev
    count = sum(1 for point in datapoints[:3] if point < threshold)
    
    if count >= 2:
        print(RULE_5_TEXT)
        return True
    return False


# 4/5 points in a row are < -1 stdev from mean
def rule_6(datapoints, mean, stdev):
    threshold = mean - 1 * stdev
    count = sum(1 for point in datapoints[:5] if point < threshold)
    
    if count >= 4:
        print(RULE_6_TEXT)
        return True
    return False


# # 15 points in a row are within 1 stdev from mean, + or -
# def rule_7(datapoints, mean, stdev):
#     i = 0
#     count = 0

#     for i in range(0,14):
#         if (stdev + mean) > datapoints[i] > (-1 * stdev + mean):
#             count += 1
#         else:
#             count = 0
#         if count >= 15:
#             print("Rule 7 triggered - 15 points in a row are within +/- 1 standard deviation from the mean")
#             return True
#         i += 1
#     return False

# # 8 points in a row are above or below 1 standard deviation, alternating up and down
# def rule_8(datapoints, mean, stdev):
#     i = 1
#     count = 0

#     while i < len(datapoints) - 1:
#         if (datapoints[i - 1] < datapoints[i] > datapoints[i + 1]) or (datapoints[i - 1] > datapoints[i] < datapoints[i + 1]) and ((stdev + mean) < datapoints[i] or (mean - stdev) > datapoints[i]):
#             count += 1
#         else:
#             count = 0
#         if count == 7:
#             print("Rule 8 triggered - 8 points in a row are above or below 1 standard deviation, alternating up and down")
#             return True
#         i += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Add your datapoints in the array below, ordered by most recent datapoints to oldest datapoints
    # datapoints = [145, 118, 118, 113, 136, 125, 136, 141, 155, 134, 137, 175, 182, 149, 136, 197, 155, 150, 157, 139, 139, 144, 147, 157, 200, 169, 155, 130, 172, 152]

    # mean = round(sum(datapoints) / len(datapoints))
    # stdev = round(np.std(datapoints))

    # print("--generate_reference_values--")
    # print("mean: " + str(mean))
    # print("stdev: " + str(stdev))
    # print(datapoints)

    rules_triggered = []
    #if rule_1([50,51,52,20,53,52,51], 50, 5): rules_triggered.append("1")
    #if rule_2([1,2,3,4,5,6,7,8,9], 10, 1): rules_triggered.append("2")
    #if rule_3([6,5,4,3,2,1,0], 0, 0): rules_triggered.append("3")
    #if rule_4([6,5,6,5,6,5,6, 5,6,5,6,5,6,5,6,5], 0, 0): rules_triggered.append("4")

    #if rule_5([3,15,6,1,1,1,1,1], 10, 2): rules_triggered.append("5")
    #if rule_6([10,15,10,1,7,1,1,1], 10, 2): rules_triggered.append("6")
    #if rule_7([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10], 10, 5): rules_triggered.append("7")
    # if rule_8(datapoints, mean, stdev): rules_triggered.append("8")

    print(str(rules_triggered)[1:-1])
