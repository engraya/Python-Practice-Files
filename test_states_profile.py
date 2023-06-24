from script_states_profile import full_state_profile

print("You can enter 'end' to quit the program")
while True:
    state_name = input("\n Enter the name of the state here please:  ")
    if state_name == 'end':
        break
    capital_name = input("\n Enter teh capital name here please:   ")
    if capital_name == 'end':
        break
    
    complete_formatted_name = full_state_profile(state_name, capital_name)
    print(f"\t Complete state profile:............ {complete_formatted_name}........")
