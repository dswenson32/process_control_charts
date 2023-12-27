# This is a sample Python script.
from __future__ import print_function
import numpy as np

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

datapoints = [1521, 1563, 1734, 1839, 1632, 1436, 1261, 1272, 1411, 1662, 2174, 1764, 1524, 1642, 1306, 1685, 1545,
              1720, 1597, 1583, 1394, 1504, 1794, 1762, 1883, 5, 1562, 1499, 1742, 1542]
mean = 0
stdev = 0
global rule_triggered


def generate_reference_values(dataset):
    mean = round(sum(dataset) / len(dataset))
    stdev = round(np.std(dataset))

    print("--generate_reference_values--")
    print("mean: " + str(mean))
    print("stdev: " + str(stdev))


# Check if any data point is < -3 STDEV
def rule_1():
    # Getting length of list
    i = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if datapoints[i] < (mean + -3 * stdev):
            print("Rule 1 triggered: " + str(datapoints[i]) + " falls below -3 stdev")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 1 not triggered")
        return False


# Nine or more data points in a row below the mean
def rule_2():
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
            print("Rule 2 was triggered")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 2 not triggered")
        return False


# 6 points in a row are decreasing
def rule_3():
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


# 14 points in a row are alternating, increase then decrease
def rule_4():
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
            print("Rule 5 was triggered")
            return True
        else:
            count = 0
        i += 1
    if not rule_triggered:
        print("Rule 5 not triggered")
        return False


# 4/5 points in a row are < -1 stdev from mean
def rule_6():
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
            print("Rule 6 was triggered")
            return True
        else:
            count = 0
        i += 1
    if not rule_triggered:
        print("Rule 6 not triggered")
        return False


# 15 points in a row are within 1 stdev from mean, + or -
def rule_7():
    # Getting length of list
    i = 0
    count = 0

    # Iterating using while loop
    while i < len(datapoints) and not rule_triggered:
        if stdev > datapoints[i] > -1 * stdev and count < 15:
            count += 1
        else:
            count = 0
        if count == 15:
            print("Rule 7 was triggered")
            return True
        i += 1
    if not rule_triggered:
        print("Rule 7 not triggered")
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mean = round(sum(datapoints) / len(datapoints))
    stdev = round(np.std(datapoints))
    rule_triggered = False

    print("--generate_reference_values--")
    print("mean: " + str(mean))
    print("stdev: " + str(stdev))

    # Check dataset against rules
    while True:
        if rule_1(): break
        if rule_2(): break
        if rule_3(): break
        if rule_5(): break
        if rule_6(): break
        if rule_7(): break
        print("passed all checks")
        rule_triggered = False
        break

    print(rule_triggered)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
