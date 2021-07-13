

# ing for one cake
eggs = 2
flour_ounces = 4 
sugar_ounces = 4
butter_ounces = 4
bpow_tsp = 1

def scale_sponge (num_of_cakes):
    new_eggs = eggs * num_of_cakes
    new_flour_ounces = flour_ounces * num_of_cakes
    new_sugar_ounces = sugar_ounces * num_of_cakes
    new_butter_ounces = butter_ounces * num_of_cakes
    new_bpow_tsp = bpow_tsp * num_of_cakes


    recipe = f'{num_of_cakes} Cake: {new_eggs} eggs, {new_flour_ounces} ounces of flour, {new_sugar_ounces} ounces of sugar, {new_bpow_tsp} teaspoons of baking powder'
    print(recipe)





scale_sponge(6)