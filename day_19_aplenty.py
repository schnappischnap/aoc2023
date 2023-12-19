from collections import defaultdict
import itertools
import operator as op
import re


def part_1(data):
    a, b = data.split("\n\n")
    workflows = defaultdict(list)
    for line in a.splitlines():
        name, *rules = re.findall(r"\w+|<|>", line)
        for rule in itertools.batched(rules, 4):
            if len(rule) == 4:
                variable, operator, value, result = rule
                workflows[name].append((variable, op.gt if operator == ">" else op.lt, int(value), result))
        workflows[name].append(rules[-1])
    
    def r(part, workflow="in"):
        ratings = {category: rating for category, rating in zip("xmas", map(int, re.findall(r"\d+", part)))}
        result = None
        for rule in workflows[workflow]:
            if len(rule) == 4:
                variable, operator, value, result = rule
                if operator(ratings[variable], value):
                    break
        else:
            result = workflows[workflow][-1]
        return sum(ratings.values()) if result == "A" else 0 if result == "R" else r(part, result)

    return sum(r(part) for part in b.splitlines())


def part_2(data):
    workflows = defaultdict(list)
    for line in data.split("\n\n")[0].splitlines():
        name, *rules = re.findall(r"\w+|<|>", line)
        for rule in itertools.batched(rules, 4):
            if len(rule) == 4:
                variable, operator, value, result = rule
                workflows[name].append((variable, op.gt if operator == ">" else op.lt, int(value), result))
        workflows[name].append(rules[-1])

    accepting_conditions = []
    def r(workflow="in", conditions=[]):
        for rule in workflows[workflow]:
            if len(rule) == 4:
                variable, operator, value, result = rule
                if result == "A":
                    accepting_conditions.append(conditions + [(variable, operator, value)])
                    conditions.append((variable, op.ge if operator == op.lt else op.le, value))
                elif result == "R":
                    conditions.append((variable, op.ge if operator == op.lt else op.le, value))
                else:
                    r(result, conditions + [(variable, operator, value)])
                    conditions.append((variable, op.ge if operator == op.lt else op.le, value))
        else:
            result = workflows[workflow][-1]
            if result == "A":
                accepting_conditions.append(conditions)
            elif result == "R":
                pass
            else:
                r(result, conditions)

    r()
    answer = 0
    for accepting_condition in accepting_conditions:
        combinations = 1
        for variable in "xmas":
            values = list(range(1, 4001))
            for condition in accepting_condition:
                if condition[0] == variable:
                    values = [v for v in values if condition[1](v, condition[2])]
            combinations *= len(values)
        answer += combinations
    return answer


if __name__ == "__main__":
    with open("day_19_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
