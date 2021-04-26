# Challenge 5 

I'm not quite sure how to approch it but i think @classmethod decorator will be helpful.
I'd store class name into a dictionary of class mapings. Then, inside EventTuple constructor
i'd get correct class name provided by user and call 'create' class method with specified 
arguments, and finally return the instance.
