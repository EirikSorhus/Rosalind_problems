"""Function to calculate the chance of a child to have a dominant trait (at least one dominant allel),
#given a number of possible parents with homozygote dominant, hetrozygote and homozygote recesive.

# First calculate the chance of "drawing" each of the possibilities
# determen outcome of the combinations
# add the probebilities together


This is not the best way to do it, but it works
"""
def mendelian_inheritance(k, m, n):
    Sum = k + m + n

    chance_k = k/Sum
    chance_m = m/Sum
    chance_n = n/Sum
    chance_k2 = k/(Sum-1)
    chance_k2_k_drawn = (k-1)/(Sum-1)
    chance_m2 = m/(Sum-1)
    chance_m2_m_drawn = (m-1)/(Sum-1)
    chance_n2 = n/(Sum-1)
    chance_n2_n_drawn =(n-1)/(Sum-1)

    P_DD_1 = (chance_k + chance_m*chance_k2 + chance_n*chance_k2) * 1.00
    P_Dr_075 = (chance_m*chance_m2_m_drawn) * 0.75
    P_rr_050 = (chance_m*chance_n2 + chance_n*chance_m2) * 0.50
    #P_rr_0 = (chance_n*chance_n2_n_drawn) * 0

    P = P_DD_1 + P_Dr_075 + P_rr_050
    return P
print(mendelian_inheritance(2,2,2))