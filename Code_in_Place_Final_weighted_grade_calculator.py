def get_components_details():
    weight = [] 
    components = int(input("How many weighted compenents do you have for your grade? "))
    #getting all weighted percentages
    for i in range (0, components):
        name_component = input(f"What is the name of component {i+1} " )
        input_val = float(input(f"What is the weight of the {name_component} (in decimals): "))
        weight.append((name_component, input_val))

    #making sure all weighted components add up to 100% of the grade 
    #print(weight)
    sum_of_weight=0
    for i in range (0, components):
        sum_of_weight+=weight[i][1]
#     sum_of_weight = sum(weight[1])
    if sum_of_weight != 1:
        print ("Sorry, your weighted components do not add up to 100% of your grade")
        exit (0)
    return weight

def get_grades (component_count, weight):
    grades=[]

    for i in range(0,component_count):
        name_subcomponent = weight[i][0]
        number_of_subcomponent = int(input(f"How many {name_subcomponent} do you have? "))
        grade_subcomponents = []
        for i in range (0,number_of_subcomponent):
            grade_for_each_subcomponent = float(input(f"What is the percent of the grade for {name_subcomponent} {i+1} (in decimals) "))
            grade_subcomponents.append(grade_for_each_subcomponent)
        grades.append((name_subcomponent, grade_subcomponents))
    return(grades)

    


name = input("Hello what is your name?" )
weight_1=get_components_details()

# weight_1=[('test', 0.7), ('hw', 0.3)]
component_count = len(weight_1)

grades=get_grades(component_count,weight_1)
#grades = [('test', [0.2, 0.1, 0.35]), ('hw', [0.3, 0.5])]

tot_grade=0
for i in range (0, len(grades)):   

    total_grade= sum(grades[i][1])
    avg_grade = total_grade / len(grades[i][1])
    weight_grade = weight_1[i][1] * avg_grade
    tot_grade+=weight_grade
    print("----------------------")
    
grade_necessary = (0.90 - (tot_grade))/ weight_1[0][1]

print (f"You will need a {round(grade_necessary,2)*100}% on your next test to get an A in your class")
#0.92 + 0.7 * x = 0.90

