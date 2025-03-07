import random
from tabulate import tabulate  

def fitness(chromosome):
    return chromosome.count('1')

# دالة الاختيار بطريقة عجلة الروليت
def roulette_wheel_selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        return population

    probabilities = [f / total_fitness for f in fitness_scores]
    cumulative_probs = []
    cumulative_sum = 0
    for prob in probabilities:
        cumulative_sum += prob
        cumulative_probs.append(cumulative_sum)

    new_population = []
    for _ in range(len(population)):
        rand = random.random()
        for i, cum_prob in enumerate(cumulative_probs):
            if rand <= cum_prob:
                new_population.append(population[i])
                break

    return new_population

# دالة الكروس أوفر (One-Point Crossover)
def one_point_crossover(parent1, parent2, pCross=0.6):
    if random.random() > pCross:
        return parent1, parent2

    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    return offspring1, offspring2

# دالة الطفرة (Mutation)
def bit_flip_mutation(chromosome, pMut=0.05):
    return ''.join(
        bit if random.random() > pMut else ('0' if bit == '1' else '1') for bit in chromosome
    )

def genetic_algorithm(pop_size=20, num_generations=10, chrom_length=5, pCross=0.6, pMut=0.05):
    population = [''.join(random.choice('01') for _ in range(chrom_length)) for _ in range(pop_size)]
    
    best_hist = []  
    avg_hist = []   

    for generation in range(num_generations):
        fitness_scores = [fitness(chrom) for chrom in population]
        
        best_hist.append(max(fitness_scores))
        avg_hist.append(sum(fitness_scores) / pop_size)

        # **طباعة الجدول لكل جيل**
        table_data = [[i + 1, population[i], fitness_scores[i]] for i in range(pop_size)]
        print(f"\n=== Generation {generation + 1} ===")
        print(tabulate(table_data, headers=["Chromosome #", "Chromosome", "Fitness"], tablefmt="grid"))
        print(f"Best Fitness: {best_hist[-1]}, Average Fitness: {avg_hist[-1]}\n")

        # **Elitism**: الاحتفاظ بأفضل 2 كروموسوم
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        new_population = sorted_population[:2]

        # اختيار باقي الأفراد
        selected_population = roulette_wheel_selection(population, fitness_scores)

        # الكروس أوفر
        offspring_population = []
        for i in range(2, pop_size, 2):
            if i + 1 < pop_size:
                offspring1, offspring2 = one_point_crossover(selected_population[i], selected_population[i+1], pCross)
                offspring_population.extend([offspring1, offspring2])
            else:
                offspring_population.append(selected_population[i])

        # الطفرة
        new_population.extend([bit_flip_mutation(chrom, pMut) for chrom in offspring_population])

        # تحديث الجيل
        population = new_population

    return population, best_hist, avg_hist

# تشغيل الألجورزم 10 مرات
for run in range(10):
    random.seed(run)
    final_population, best_hist, avg_hist = genetic_algorithm()
    
    print(f"\n=== Run {run + 1} Finished ===")
    print(f"Final Best Fitness: {best_hist[-1]}, Final Average Fitness: {avg_hist[-1]}")
