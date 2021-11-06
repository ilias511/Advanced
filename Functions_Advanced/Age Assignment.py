def age_assignment(*args,**kwargs):
    final_dict ={

    }
    for name in args:
        for key,value in kwargs.items():
            if key in name:
                final_dict[name]=value

    return final_dict



print(age_assignment("Peter", "George", G=26, P=19))