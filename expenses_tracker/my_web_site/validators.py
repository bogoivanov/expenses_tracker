def validate_only_letters(value):
    if not value.isalpha():
        raise ValueError("Ensure this value contains only letters.")

# def validate_budget_is_not_below_zero(value):
#     pass