vada_pav = int(input("enter number of vada pav"))
samosa = int(input("enter number of samosa"))
if vada_pav and samosa > 0:
    cost_vp = 12*vada_pav
    cost_s = 15*samosa
    print("cost of samosa:-",cost_s)
    print("cost of vada pav:-",cost_vp)
    print("----------------")
    print("Total price:-",cost_vp+cost_s)