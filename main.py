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

# Check if any data point is < -3 STDEV
def rule_1(datapoints, mean, stdev):
    i = 0

    while i < len(datapoints):
        if datapoints[i] < (mean + -3 * stdev):
            print("Rule 1 triggered - " + str(datapoints[i]) + " falls below -3 standard deviations from the mean")
            return True
        i += 1
    return False


# Nine or more data points in a row below the mean
def rule_2(datapoints, mean, stdev):
    count = 0

    for point in datapoints[:9]:
        if point < mean:
            count += 1
            if count >= 9:
                print("Rule 2 triggered - 9 or more points in a row below the mean")
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
                print("Rule 3 triggered - six points in a row are decreasing")
                return True
        else:
            count = 0
    return False


# 14 points in a row are alternating, increase then decrease
def rule_4(datapoints, mean, stdev):
    i = 1
    count = 0

    # Iterating using while loop
    while i < len(datapoints) - 1:
        if (datapoints[i - 1] < datapoints[i] > datapoints[i + 1]) or (datapoints[i - 1] > datapoints[i] < datapoints[i + 1]):
            count += 1
        else:
            count = 0
        if count == 13:
            print("Rule 4 triggered - 14 consecutive points are alternating, increasing then decreasing")
            return True
        i += 1
    # print("Rule 4 not triggered")


# 2/3 points in a row are < -2 stdev from mean
def rule_5(datapoints, mean, stdev):
    i = 2
    count = 0

    # Iterating using while loop
    while i < len(datapoints):
        j = i - 2
        while j <= i:
            if datapoints[j] < mean + -2 * stdev:
                count += 1
            j += 1
        if count >= 2:
            print("Rule 5 triggered - 2 of last 3 points are more than -2 standard deviations below the mean")
            return True
        else:
            count = 0
        i += 1
    # print("Rule 5 not triggered")


# 4/5 points in a row are < -1 stdev from mean
def rule_6(datapoints, mean, stdev):
    i = 4
    count = 0

    while i < len(datapoints):
        j = i - 4
        while j <= i:
            if datapoints[j] < mean + -1 * stdev:
                count += 1
            j += 1
        if count >= 4:
            print("Rule 6 triggered - 4 of last 5 points are more than -1 standard deviations below the mean")
            return True
        else:
            count = 0
        i += 1
    # print("Rule 6 not triggered")


# 15 points in a row are within 1 stdev from mean, + or -
def rule_7(datapoints, mean, stdev):
    i = 0
    count = 0

    while i < len(datapoints):
        if (stdev + mean) > datapoints[i] > (-1 * stdev + mean) and count < 15:
            count += 1
        else:
            count = 0
        if count == 15:
            print("Rule 7 triggered - 15 points in a row are within +/- 1 standard deviation from the mean")
            return True
        i += 1
    # print("Rule 7 not triggered")

# 8 points in a row are above or below 1 standard deviation, alternating up and down
def rule_8(datapoints, mean, stdev):
    i = 1
    count = 0

    while i < len(datapoints) - 1:
        if (datapoints[i - 1] < datapoints[i] > datapoints[i + 1]) or (datapoints[i - 1] > datapoints[i] < datapoints[i + 1]) and ((stdev + mean) < datapoints[i] or (mean - stdev) > datapoints[i]):
            count += 1
        else:
            count = 0
        if count == 7:
            print("Rule 8 triggered - 8 points in a row are above or below 1 standard deviation, alternating up and down")
            return True
        i += 1
    #print("Rule 8 not triggered")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Add your datapoints in the array below, ordered by most recent datapoints to oldest datapoints
    datapoints = [145, 118, 118, 113, 136, 125, 136, 141, 155, 134, 137, 175, 182, 149, 136, 197, 155, 150, 157, 139, 139, 144, 147, 157, 200, 169, 155, 130, 172, 152]

    mean = round(sum(datapoints) / len(datapoints))
    stdev = round(np.std(datapoints))
    rules_triggered = []

    print("--generate_reference_values--")
    print("mean: " + str(mean))
    print("stdev: " + str(stdev))
    print(datapoints)

    if rule_1(datapoints, mean, stdev): rules_triggered.append("1")
    if rule_2(datapoints, mean, stdev): rules_triggered.append("2")
    if rule_3(datapoints, mean, stdev): rules_triggered.append("3")
    if rule_4(datapoints, mean, stdev): rules_triggered.append("4")
    if rule_5(datapoints, mean, stdev): rules_triggered.append("5")
    if rule_6(datapoints, mean, stdev): rules_triggered.append("6")
    if rule_7(datapoints, mean, stdev): rules_triggered.append("7")
    if rule_8(datapoints, mean, stdev): rules_triggered.append("8")

    print(str(rules_triggered)[1:-1])
