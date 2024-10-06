def num_occ_lista(list, numb):
    for numbToVerify in list:
        reachNumber = False
        while reachNumber is False:
            if isinstance(list[numbToVerify], list):
                numbToVerify += [numbToVerify]