

# ing for one cake
eggs = 2
flour_ounces = 4
sugar_ounces = 4
butter_ounces = 4
bpow_tsp = 1

def scale_sponge (num_of_cakes):
    eggs = 2 * num_of_cakes
    flour_ounces = 4 * num_of_cakes
    sugar_ounces = 4 * num_of_cakes
    butter_ounces = 4 * num_of_cakes
    bpow_tsp = 1 * num_of_cakes


    recipe = f'{num_of_cakes} Cake: {eggs} eggs, {flour_ounces} ounces of flour, {sugar_ounces} ounces of sugar, {bpow_tsp} teaspoons of baking powder'
    print(recipe)





scale_sponge(400)