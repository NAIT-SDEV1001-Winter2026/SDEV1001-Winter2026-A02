def make_pizza(*args, size=None, crust=None, **kwargs):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with " +
          crust + " crust.")

    print("Toppings added are:")
    # note here that args is a tuple that you can loop through
    # you can also insert a breakpoint here to see exactly what it is.
    for topping in args:
        print("- " + topping)
    
    # note you can see here that kwargs is a dictionary
    # you can also insert a breakpoint here to see exactly what it is.
    if kwargs:
        print("Special instructions for the pizza are:")
        for key, value in kwargs.items():
            print(F"- {key}: {value}")
