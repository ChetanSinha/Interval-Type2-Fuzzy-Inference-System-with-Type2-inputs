import T2_T2_func as t2t2
import numpy as np

'''
input format:
x -- the starting value of the range.
y -- the upper bound of the range
z -- the incrementation value (the difference two values of the range)
'''
x, y, z = [float(x) for x in input("Enter the range of weight:").split(' ')]
x_weight = np.arange(x, y, z)

x, y, z = [float(x) for x in input("Enter the range of height:").split(' ')]
x_height = np.arange(x, y, z)

x, y, z = [float(x) for x in input("Enter the range of fitnes level:").split(' ')]
x_fitnessLevel = np.arange(x, y, z)


'''
w -- 2D tuple containing seperate UMF and LMF of weight(here).
w_types -- list containg the linguistic terms for weight(here).
'''
w_types = input(f'Enter the fuzzy inputs for weight :').split(' ') 
w = t2t2.fuzz_IT2_Inputs(x_weight, w_types)

h_types = input(f'Enter the fuzzy inputs for height :').split(' ') 
h = t2t2.fuzz_IT2_Inputs(x_height, h_types)


f_types = input(f'Enter the fuzzy inputs for fitness Level :').split(' ') 
f = t2t2.fuzz_IT2_Inputs(x_fitnessLevel, f_types)


'''
Ploting the membership values for each of antecedent and consequent
'''
t2t2.fuzz_IT2_plot_mf(x_weight, w, w_types, 'Weight')
t2t2.fuzz_IT2_plot_mf(x_height, h, h_types, 'Height')
t2t2.fuzz_IT2_plot_mf(x_fitnessLevel, f, f_types, 'Fitness Level')


'''
Displays the list of linguistic terms of the consequent, corresponding to a value.
'''
for i in range(len(f_types)):
    print(f'{i+1}) {f_types[i]}')


'''
rule_lst -- list of rules decided
'''
rule_lst = t2t2.fuzz_make_rules(w_types, h_types)


'''
Taking Type 2 Fuzzy Inputs.
'''
weight = t2t2.fuzz_IT2_Inputs(x_weight, ['weight'])
height = t2t2.fuzz_IT2_Inputs(x_height, ['height'])

t2t2.fuzz_IT2_plot_mf(x_weight, weight, ['w1'], 'Weight Input')
t2t2.fuzz_IT2_plot_mf(x_height, height, ['h1'], 'Height Input')



'''
x_memvalue -- membership value at a particular single value for the antecedent x(weight and height here).
'''
w_memvalue = t2t2.fuzz_IT2_Interplot_mem(w, weight)
h_memvalue = t2t2.fuzz_IT2_Interplot_mem(h, height)



'''
rule -- 2D tuple of maped rule for upper and lower membership values.
fitness_used -- list of fitness values decided based the rule_lst(to be used for ploting)
'''
rule, fitness_used = t2t2.fuzz_mapRule(w_memvalue, h_memvalue, f, rule_lst)


t2t2.fuzz_plot_outputMf(x_fitnessLevel, rule, fitness_used)


'''
R_combined -- 2D tuple containing aggregated rule for upper and lower membership values.
'''
R_combined = t2t2.fuzz_IT2_aggregation(rule)


'''
fitnessLevel -- output value(centroid value)
fitness_activation -- corresponding membership value of output
'''
fitnessLevel, fitness_activation = t2t2.fuzz_IT2_defuzz(x_fitnessLevel, R_combined)


t2t2.fuzz_IT2_output(x_fitnessLevel, f, fitnessLevel, fitness_activation, R_combined)

