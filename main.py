# This is a sample Python script.
from __future__ import print_function
import numpy as np


# Check if any data point is < -3 STDEV
def rule_1(datapoints, mean, stdev):
    recent_data = datapoints[0:1]

    if recent_data[0] < (mean + -3 * stdev):
        print("Rule 1 triggered - " + str(datapoints[i]) + " falls below -3 standard deviations from the mean")
        return True

# Nine or more data points in a row below the mean
def rule_2(datapoints, mean, stdev):
    i = 1
    count = 0
    recent_data = datapoints[0:9]

    while i < len(recent_data):
        if recent_data[i] < mean and count < 9:
            count += 1
        else:
            count = 0
        if count == 9:
            print("Rule 2 triggered - 9 or more points in a row below the mean")
            return True
        i += 1
    # print("Rule 2 not triggered")


# 6 points in a row are decreasing
def rule_3(datapoints, mean, stdev):
    i = 1
    count = 0
    recent_data = datapoints[0:6]

    while i < len(recent_data):
        if recent_data[i] < recent_data[i - 1] and count < 6:
            count += 1
        else:
            count = 0
        if count == 6:
            print("Rule 3 triggered - six points in a row are decreasing")
            return True
        i += 1
    # print("Rule 3 not triggered")


# 14 points in a row are alternating, increase then decrease
def rule_4(datapoints, mean, stdev):
    i = 1
    count = 0
    recent_data = datapoints[0:14]

    # Iterating using while loop
    while i < len(recent_data) - 1:
        if (recent_data[i - 1] < recent_data[i] > recent_data[i + 1]) or (recent_data[i - 1] > recent_data[i] < recent_data[i + 1]):
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
    recent_data = datapoints[0:3]

    # Iterating using while loop
    while i < len(recent_data):
        j = i - 2
        while j <= i:
            if recent_data[j] < mean + -2 * stdev:
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
    recent_data = datapoints[0:5]

    while i < len(recent_data):
        j = i - 4
        while j <= i:
            if recent_data[j] < mean + -1 * stdev:
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
    recent_data = datapoints[0:15]

    while i < len(recent_data):
        if (stdev + mean) > recent_data[i] > (-1 * stdev + mean) and count < 15:
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
    recent_data = datapoints[0:8]

    while i < len(recent_data) - 1:
        if (recent_data[i - 1] < recent_data[i] > recent_data[i + 1]) or (recent_data[i - 1] > recent_data[i] < recent_data[i + 1]) and ((stdev + mean) < recent_data[i] or (mean - stdev) > recent_data[i]):
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
