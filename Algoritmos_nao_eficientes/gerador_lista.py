import random

def generate_ordered_sequence(size):
    return list(range(1, size + 1))

def generate_reverse_ordered_sequence(size):
    return list(range(size, 0, -1))

def generate_almost_ordered_sequence(size, swap_prob):
    sequence = generate_ordered_sequence(size)
    for i in range(size):
        if random.random() < swap_prob:
            j = random.randint(0, size - 1)
            sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence

def generate_random_sequence(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]