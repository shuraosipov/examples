import math
import sys

BASE = 4

def round_up_to_nearest_4KB_read(average_item_size) -> float:
    """
    Round up the item size to the nearest 4 KB.
    """
    round_up_value = BASE * math.ceil(average_item_size / BASE)
    return round_up_value

def round_up_to_nearest_1KB_write(average_item_size) -> float:
    """
    Round up the item size to the nearest 1 KB.
    """

    round_up_value = math.ceil(average_item_size)
    return round_up_value


def calcuate_rcu_strongly_consistent(average_item_size, item_read_per_second) -> int:

    item_size = round_up_to_nearest_4KB_read(average_item_size)
    number_of_strongly_consistent_read_units = item_size / BASE
    rcu = number_of_strongly_consistent_read_units * item_read_per_second
    return int(rcu)

def calcuate_rcu_eventually_consistent(average_item_size, item_read_per_second) -> int:

    item_size = round_up_to_nearest_4KB_read(average_item_size)
    number_of_eventually_consistent_read_units = item_size / BASE / 2
    rcu = number_of_eventually_consistent_read_units * item_read_per_second
    return int(rcu)

def calcuate_rcu_transactional(average_item_size, item_read_per_second) -> int:

    item_size = round_up_to_nearest_4KB_read(average_item_size)
    number_of_eventually_consistent_read_units = item_size / BASE
    rcu = number_of_eventually_consistent_read_units * item_read_per_second * 2
    return int(rcu)


def calculate_wcu_standart(average_item_size, item_write_per_second) -> int:
    item_size = round_up_to_nearest_1KB_write(average_item_size)
    wcu = item_size * item_write_per_second
    return int(wcu)

def calculate_wcu_transactional(average_item_size, item_write_per_second) -> int:
    item_size = round_up_to_nearest_1KB_write(average_item_size)
    wcu = item_size * item_write_per_second * 2
    return int(wcu)


if __name__ == "__main__":
    average_item_size = int(sys.argv[1])
    item_read_per_second = int(sys.argv[2])
    item_write_per_second = int(sys.argv[3])
    
    print(f"Calculating RCU and WCU for an item size of {average_item_size} KB and {item_read_per_second} Item read/second and {item_write_per_second} Item write/second ")
    print("")

    print("Read capacity units (Strongly Consistent) :", + calcuate_rcu_strongly_consistent(average_item_size, item_read_per_second))
    print("Read capacity units (Eventually Consistent) :", + calcuate_rcu_eventually_consistent(average_item_size, item_read_per_second))
    print("Read capacity units (Transactional) :", + calcuate_rcu_transactional(average_item_size, item_read_per_second))
    print("Write capacity units (Standard) :", + calculate_wcu_standart(average_item_size, item_write_per_second))
    print("Write capacity units (Transactional) :", + calculate_wcu_transactional(average_item_size, item_write_per_second))