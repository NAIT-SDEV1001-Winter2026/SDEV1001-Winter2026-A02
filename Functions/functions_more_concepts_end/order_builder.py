
import pizza

if __name__ == "__main__":
    ordering_pizza = True
    while ordering_pizza:
        # see if the user is done ordering pizzas
        ordering = input("Are you done ordering pizzas? (y/n): ")
        if ordering == "n":
            ordering_pizza = False
            continue
        # get the size and crust
        size = int(input("What size pizza would you like? (12, 16, 18): "))
        crust = input("What type of crust would you like? (thin, medium, thick): ")
        # get the toppings
        toppings = []
        topping = input("What topping would you like? (enter 'done' when finished): ")
        while topping != "done":
            toppings.append(topping)
            topping = input("What topping would you like? (enter 'done' when finished): ")
        
        # get the special requests.
        special_requests = {}
        special_request_topping = input("What modification to toppings? (enter 'done' when finished): ")
        while special_request_topping != "done":
            special_request_amount = input("How much? (light, extra, double): ")
            special_requests[special_request_topping] = special_request_amount
            special_request_topping = input("What modification to toppings? (enter 'done' when finished): ")

        # use our function to make the pizza.
        pizza.make_pizza(*toppings, size=size, crust=crust, **special_requests)