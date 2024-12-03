import re

with open("input.txt", "r") as f:
    file_content = f.readlines()

reports = [re.findall(r"\d+", line) for line in file_content]
reports = [[int(i) for i in report] for report in reports]

nb_safe_reports = 0

for report in reports:
    upward = False
    downward = False
    for i in range(len(report)):
        temp_report = report.copy()
        del temp_report[i]
        for i in range(len(temp_report)):
            if i == len(temp_report) - 1:
                break
            if (temp_report[i] < temp_report[i+1]) and ((temp_report[i+1] - temp_report[i]) <= 3):
                upward = True
            else:
                upward = False
                break
        if upward:
            break
        for i in range(len(temp_report)):
            if i == len(temp_report) - 1:
                break
            if (temp_report[i] > temp_report[i+1]) and ((temp_report[i] - temp_report[i+1]) <= 3):
                downward = True
            else:
                downward = False
                break
        if downward:
            break
    if upward or downward:
        nb_safe_reports += 1

print(nb_safe_reports)