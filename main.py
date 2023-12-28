# This is a sample Python script.
from __future__ import print_function
import numpy as np

datapoints = [1521, 1563, 1734, 1720, 1632, 1436, 1545, 1306, 1597, 1583, 1524, 1642, 1504, 1794, 1762, 1662,  2174, 1764, 1261, 1272, 1411,      1685,  1394,  1883, 1774, 1562, 1499, 1742, 1542, 1839]
mean = 0
stdev = 0


def generate_reference_values(dataset):
    mean = round(sum(dataset) / len(dataset))
    stdev = round(np.std(dataset))

    print("--generate_reference_values--")
    print("mean: " + str(mean))
    print("stdev: " + str(stdev))


# Check if any data point is < -3 STDEV
def rule_1():
    rule_triggered = False
    # Getting length of list
    i = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if datapoints[i] < (mean + -3 * stdev):
            print("Rule 1 triggered - " + str(datapoints[i]) + " falls below -3 standard deviations from the mean")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 1 not triggered")
        return False


# Nine or more data points in a row below the mean
def rule_2():
    rule_triggered = False
    # Getting length of list
    i = 0
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if datapoints[i] < mean and count < 9:
            count += 1
        else:
            count = 0
        if count == 9:
            print("Rule 2 triggered - 9 or more points in a row below the mean")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 2 not triggered")
        return False


# 6 points in a row are decreasing
def rule_3():
    rule_triggered = False
    # Getting length of list
    i = 1
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if datapoints[i] < datapoints[i - 1] and count < 6:
            count += 1
        else:
            count = 0
        if count == 6:
            print("Rule 3 triggered - six points in a row are decreasing")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 3 not triggered")
        return False


# 14 points in a row are alternating, increase then decrease
def rule_4():
    rule_triggered = False
    # Getting length of list
    i = 1
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if datapoints[i] < datapoints[i - 1] and count < 6:
            count += 1
        else:
            count = 0
        if count == 6:
            print("Rule 3 was triggered")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 3 not triggered")
        return False


# 2/3 points in a row are < -2 stdev from mean
def rule_5():
    rule_triggered = False
    # Getting length of list
    i = 2
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
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
    if not rule_triggered:
        print("Rule 5 not triggered")
        return False


# 4/5 points in a row are < -1 stdev from mean
def rule_6():
    rule_triggered = False
    # Getting length of list
    i = 4
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
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
    if not rule_triggered:
        print("Rule 6 not triggered")
        return False


# 15 points in a row are within 1 stdev from mean, + or -
def rule_7():
    rule_triggered = False
    # Getting length of list
    i = 0
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if (stdev + mean) > datapoints[i] > (-1 * stdev + mean) and count < 15:
            count += 1
        else:
            count = 0
        if count == 15:
            print("Rule 7 triggered - 15 points in a row are within +/- 1 standard deviation from the mean")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 7 not triggered")
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mean = round(sum(datapoints) / len(datapoints))
    stdev = round(np.std(datapoints))
    rules_triggered = []

    print("--generate_reference_values--")
    print("mean: " + str(mean))
    print("stdev: " + str(stdev))

    if rule_1(): rules_triggered.append("1")
    if rule_2(): rules_triggered.append("2")
    if rule_3(): rules_triggered.append("3")
    if rule_5(): rules_triggered.append("5")
    if rule_6(): rules_triggered.append("6")
    if rule_7(): rules_triggered.append("7")

    print(str(rules_triggered)[1:-1])
