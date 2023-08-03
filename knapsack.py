import random

# アイテムの重さと価値
weights = [10, 20, 30, 20, 30, 50]
values = [60, 100, 120, 40, 45, 150]
WEIGHT_LIMIT = 100

# 集団のサイズ、個体の長さ、世代数
POPULATION_SIZE = 10
INDIVIDUAL_LENGTH = len(weights)
GENERATIONS = 100

# 集団の初期化
population = [[random.randint(0, 3) for _ in range(INDIVIDUAL_LENGTH)] for _ in range(POPULATION_SIZE)]

# 適応度関数
def fitness(individual):
    weight = sum(individual[i]*weights[i] for i in range(INDIVIDUAL_LENGTH))
    value = sum(individual[i]*values[i] for i in range(INDIVIDUAL_LENGTH))
    if weight > WEIGHT_LIMIT:
        return 0  # 重量制限を超える場合は適応度を0とする
    else:
        return value

# 選択（トーナメント選択）
def selection(population):
    return random.choice(sorted(random.sample(population, 3), key=fitness, reverse=True))

# 交叉（一点交叉）
def crossover(parent1, parent2):
    crossover_point = random.randint(1, INDIVIDUAL_LENGTH-1)
    return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]

# 突然変異（ビット反転）
def mutation(individual):
    mutation_point = random.randint(0, INDIVIDUAL_LENGTH-1)
    individual[mutation_point] = 1 - individual[mutation_point]
    return individual

# 遺伝的アルゴリズムの実行
for generation in range(GENERATIONS):
    print(f"Generation {generation}: Max fitness = {max(map(fitness, population))}")
    #print(f"Population : {max(population)} ")
    new_population = []
    for _ in range(POPULATION_SIZE//2):
        parent1 = selection(population)
        parent2 = selection(population)
        offspring1, offspring2 = crossover(parent1, parent2)
        new_population.append(mutation(offspring1))
        new_population.append(mutation(offspring2))
    population = new_population
