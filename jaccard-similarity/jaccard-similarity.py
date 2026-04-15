def jaccard_similarity(set_a, set_b):
   set_a = set(set_a)
   set_b = set( set_b)
    
   if len(set(set_a)) == 0 and len(set(set_b))==0:
       return 0
   else:
       return  len(set(set_a & set_b)) / len(set(set_a | set_b))

    