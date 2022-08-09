# Build a profile of yourself by calling build_profile(), using first & last names,
# And three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('steven', 'haynes',
                             location='pflugerville',
                             field='strength & conditioning',
                             dysfunction='bad back')
print(user_profile)
