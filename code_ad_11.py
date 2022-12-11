

import sys

def monkey_0_op(x): return x * 11

def monkey_1_op(x): return x + 4

def monkey_2_op(x): return x * x

def monkey_3_op(x): return x + 2

def monkey_4_op(x): return x + 3

def monkey_5_op(x): return x + 1

def monkey_6_op(x): return x + 5

def monkey_7_op(x): return x * 19

ops = [monkey_0_op, monkey_1_op, monkey_2_op, monkey_3_op, monkey_4_op, monkey_5_op, monkey_6_op, monkey_7_op]

if __name__ == '__main__':
    file = sys.argv[1]

    class Monkey:
        def __init__(self, op, div, if_true, if_false):
            self.operation = op
            self.divider = div
            self.monkey_if_true = if_true
            self.monkey_if_false = if_false
        def throw(self, x):
            if x % self.divider == 0:
                return self.monkey_if_true
            else:
                return self.monkey_if_false
        
        def op(self, x):
            return self.operation(x)

    monkeys = []
    monkeys_items = []
    with open(file) as f:
        monkey_id = 0
        test = 0
        if_true = 0
        if_false = 0
        for line in f:
            line = line.lstrip().rstrip()
            if line.startswith('Monkey '):
                monkey_id = line.split(' ')[1]
            elif line.startswith('Starting items'):
                monkeys_items.append([int(x) for x in line.split(': ')[1].split(', ')])
            elif line.startswith('Test'):
                test = int(line.split(' ')[-1])
            elif line.startswith('If true'):
                if_true = int(line.split(' ')[-1])
            elif line.startswith('If false'):
                if_false = int(line.split(' ')[-1])
            elif line == '':
                monkeys.append(Monkey(ops[monkey_id], test, if_true, if_false))