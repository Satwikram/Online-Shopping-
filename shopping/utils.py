import random
import string

from django.utils.text import slugify

"""
@Author: Satwik Ram K
version: 1.0.0
method: generates random strings for slug
"""
def random_string_generator(size = 10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


"""
@Author: Satwik Ram K
version: 1.0.0
method: generates random integers for slug
"""
def random_integer_generator():
    random_num = random.randint(1, 100000000000000)
    #print("Random Number Generated for slugs:", random_num)
    #my_num = 247902799
    return random_num


"""
@Author: Satwik Ram K
version: 1.1.0
method: to maintain uniqueness for each slug
"""
def unique_slug_generator(instance, new_slug = None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        print("Yes Slug exist in the database")
        new_slug = "{slug}-{rand}".format(
            slug = slug,
            rand = random_integer_generator() #Calling the function, call string if u want string.
        )
        new_slug_exist = Klass.objects.filter(slug = new_slug).exists()
        if new_slug_exist:
            print("Yes new slug also exists in database")
            new_slug1 = "{slug}-{rand}".format(
                slug = slug,
                rand = random_string_generator(size = 5) # Calling string generator if random fails!
            )
            new_slug = new_slug1

            new_slug_exist =  Klass.objects.filter(slug = new_slug).exists()
            if new_slug_exist:
                unique_slug_generator(instance, new_slug = new_slug)

        return unique_slug_generator(instance, new_slug = new_slug) #Calling Reccursion if all condition fails!
    return slug