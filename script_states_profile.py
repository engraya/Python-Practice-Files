def full_state_profile(state_name, capital_name, region_name='' ):
    """"generate a clear profile for nigerian states"""
    if region_name:
         complete_state_profile = f"{state_name} {capital_name} {region_name}"
    else:
        complete_state_profile = f"{state_name} {capital_name}"
    return complete_state_profile.upper()
    