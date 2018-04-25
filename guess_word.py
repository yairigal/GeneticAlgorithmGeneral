import random
import string


def gen_pop(N):
    pop = []
    for _ in range(N):
        element = ""
        for _ in range(len(target)):
            letter = random.choice(scope)
            element += letter
        pop.append(element)
    return pop


def calc_fitness(pop, target):
    fit = 0
    for element in pop:
        fit += calc_single_element_fitness(element, target)
    return fit / len(pop)


def calc_single_element_fitness(element, target):
    local_fitness = 0
    for i in range(len(element)):
        if element[i] == target[i]:
            local_fitness += 1
    return local_fitness


def eliminate(pop, target):
    N = len(pop)
    pop = sorted(pop, key=lambda x: calc_single_element_fitness(x, target))
    return pop[int(N * (1 / 3)):]


def is_mutation(mutations_rate):
    mutations_rate = mutations_rate * 100
    items = list(range(1, 101))
    choice = random.choice(items)
    if choice <= mutations_rate - 1:
        return True
    return False


def merge(first, second, mutations_rate):
    child = ""
    for i in range(len(first)):
        mutate = is_mutation(mutations_rate)
        if mutate:
            child += random.choice(scope)
        else:
            choice = random.randint(0, 1)
            if choice == 0:
                child += first[i]
            else:
                child += second[i]
    return child


def reprodouce(pop, mutations_rate):
    new_pop = []
    while pop:
        first = random.choice(pop)
        pop.remove(first)
        second = random.choice(pop)
        pop.remove(second)
        new_pop.append(first)
        new_pop.append(second)
        child = merge(first, second, mutations_rate)
        new_pop.append(child)
    return new_pop


def is_done(pop, target):
    if target in pop:
        return True
    return False


def fittest_word(pop, target):
    return sorted(pop, key=lambda x: calc_single_element_fitness(x, target))[-1]


target = 'Hello, my Name is Yair.'
scope = string.ascii_lowercase + string.ascii_uppercase + " .,"
N = 999
mutation_rate = 0.05


def main():
    pop = gen_pop(N)
    i = 0
    while not is_done(pop, target):
        i += 1
        print("gen {}: {}".format(i, fittest_word(pop, target)), end='\r')
        pop = eliminate(pop, target)
        pop = reprodouce(pop, mutation_rate)
    print("gen {}: {}".format(i + 1, fittest_word(pop, target)), end='\r')


if __name__ == '__main__':
    main()
