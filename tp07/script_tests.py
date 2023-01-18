import fraction_Quentin


maFraction = fraction_Quentin.Fraction(5, 0)  # devrait retourner une erreur de divison par 0
maFraction2 = fraction_Quentin.Fraction(1, 8)

print(maFraction2)  # devrait retourner 0.13
print(maFraction2.as_mixed_number())  # devrait retourner la fraction + un entier
print(maFraction2+3)  # devrait retourner 3.125
print(maFraction2-3)  # devrait retourner -2.875
print(maFraction2*3)  # devrait retourner 0.375
print(maFraction2/3)  # devrait retourner 0.041666666666666664
print(maFraction2**2)  # devrait retourner 0.015625
print(maFraction2 == 3)  # devrait retourner False
print(float(maFraction2))  # devrait retourner 0.125
print(maFraction2.is_zero())  # devrait retourner False
print(maFraction2.is_integer())  # devrait retourner False
print(maFraction2.is_proper())  # devrait retourner True
print(maFraction2.is_unit())  # devrait retourner True
(maFraction2.is_adjacent_to(1/16))  # devrait retourner True
