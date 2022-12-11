
from math import sqrt
import sys
from typing import List

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
    part = sys.argv[2]

    class Monkey:
        def __init__(self, op, div, if_true, if_false, items: List[int]):
            self._items = items
            self._operation = op
            self._divider = div
            self._monkey_if_true = if_true
            self._monkey_if_false = if_false
            self._items_inspected = 0

        def throw_item(self):
            item_to_throw = self._items.pop(0)
            return (item_to_throw, self._monkey_if_true) if item_to_throw % self._divider == 0 else (item_to_throw, self._monkey_if_false)

        def inspect_item(self):
            if len(self._items) > 0:
                inspected_item = self._items[0]
                self._items_inspected += 1
                self._items[0] = self._op(inspected_item)

        def get_bored_part_a(self):
            if self._items[0]:
                self._items[0] = int(self._items[0] / 3)

        def get_bored_part_b(self):
            if self._items[0]:
                self._items[0] = self._items[0] % super_divider

        def amount_of_items(self):
            return len(self._items)

        def catch_item(self, x):
            self._items.append(int(x))

        def items_inspected(self):
            return self._items_inspected
        
        def _op(self, x):
            return self._operation(x)

    monkeys: List[Monkey] = []
    monkeys_items = []
    super_divider = 1
    with open(file) as f:
        for line in f:
            line = line.lstrip().rstrip()
            if line.startswith('Monkey '):
                monkey_id = int(line.split(' ')[1].rstrip(':'))
            elif line.startswith('Starting items'):
                items = [int(x) for x in line.split(': ')[1].split(', ')]
            elif line.startswith('Test'):
                test = int(line.split(' ')[-1])
                super_divider *= test
            elif line.startswith('If true'):
                if_true = int(line.split(' ')[-1])
            elif line.startswith('If false'):
                if_false = int(line.split(' ')[-1])
            elif line == '':
                monkeys.append(Monkey(ops[monkey_id], test, if_true, if_false, items))
        else:
            monkeys.append(Monkey(ops[monkey_id], test, if_true, if_false, items))

    rounds = 20 if part == 'a' else 10000
    for _ in range(rounds):
        for monkey in monkeys:
            items_to_throw = monkey.amount_of_items()
            for j in range(items_to_throw):
                monkey.inspect_item()
                if part == 'a':
                    monkey.get_bored_part_a()
                else:
                    monkey.get_bored_part_b()
                item_to_throw, monkey_to_throw_to = monkey.throw_item()
                monkeys[monkey_to_throw_to].catch_item(item_to_throw)

    items_inspected_by_monkeys = []
    for monkey in monkeys:
        items_inspected_by_monkeys.append(monkey.items_inspected())

    max_inspected_items = max(items_inspected_by_monkeys)
    items_inspected_by_monkeys.remove(max_inspected_items)
    second_max_items = max(items_inspected_by_monkeys)

    print(max_inspected_items * second_max_items)