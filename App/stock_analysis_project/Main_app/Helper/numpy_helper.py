import numpy


def split_array_numpy(size, companies_obj):
    """
        split queryset companies_obj to the size
    """
    
    return numpy.array_split(numpy.array(companies_obj),size)
    