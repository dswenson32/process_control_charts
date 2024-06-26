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
# UNLESS the rest of the dataset has 3 points >= 2*stdev (account for sales spikes)
def rule_2(datapoints, mean, stdev):
    count = 0
    two_plus_stdev_count = 0

    for point in datapoints[:9]:
        if point < mean:
            count += 1
            if count >= 9:
                for point2 in datapoints[9:]:
                    if point2 >= (mean + stdev * 2):
                        two_plus_stdev_count +=1
                if two_plus_stdev_count < 3:
                    print(RULE_2_TEXT)
                    return True
        else:
            count = 0
    return False


# 6 points in a row are decreasing
def rule_3(datapoints, mean, stdev):
    count = 0

    for i in range(1, 7):
        if datapoints[i - 1] < datapoints[i]:
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
    # datapoints = [0.776153, 0.957195, 0.959669, 0.947853, 0.947547, 0.971207, 0.967644, 0.962814, 0.951724, 0.949707, 0.964559, 0.965517, 0.973974, 0.962889, 0.958539, 0.700258, 0.966086, 0.947459, 0.948259, 0.948643, 0.976055, 0.970492, 0.966140, 0.976035, 0.961271, 0.930857, 0.965169, 0.965708, 0.980723, 0.970766]

    mean = sum(datapoints) / len(datapoints)
    stdev = np.std(datapoints)
    cov = round((stdev/mean) * 100)

    # print("--generate_reference_values--")
    # print("mean: " + str(mean))
    # print("stdev: " + str(stdev))
    # print(datapoints)

    rules_triggered = []if cov < 35:
        if rule_1(datapoints, mean, stdev): rules_triggered.append(RULE_1_TEXT)
        if rule_2(datapoints, mean, stdev): rules_triggered.append(RULE_2_TEXT)
        if rule_3(datapoints, mean, stdev): rules_triggered.append(RULE_3_TEXT)
        if rule_4(datapoints, mean, stdev): rules_triggered.append(RULE_4_TEXT)
        if rule_5(datapoints, mean, stdev): rules_triggered.append(RULE_5_TEXT)
        if rule_6(datapoints, mean, stdev): rules_triggered.append(RULE_6_TEXT)
    else :
        print("Coeffiecent of Variance is too high for reasonable alerting: " + str(cov))

    # if rule_2([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,11,11,11], 10, 5): rules_triggered.append("7")
    # if rule_8(datapoints, mean, stdev): rules_triggered.append("8")

    print(str(rules_triggered)[1:-1])
