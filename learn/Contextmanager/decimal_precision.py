from decimal import Decimal, getcontext, setcontext, localcontext, Context


# Temporarily change Decimal Precision

# Bad
old_context = getcontext().copy()
getcontext().prec = 40
print(Decimal(22) / Decimal(7))
setcontext(old_context)

# Good
with localcontext(Context(prec=50)):
    print(Decimal(22) / Decimal(7))

print(Decimal(22) / Decimal(7))
