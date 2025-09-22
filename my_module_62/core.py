# Example: re-define built-ins with Georgian names

def ბეჭდე(*args, **kwargs):  # print
    return print(*args, **kwargs)

def სია(*args, **kwargs):  # list
    return list(*args, **kwargs)

def ლექსიკონი(*args, **kwargs):  # dict
    return dict(*args, **kwargs)

def სიგრძე(obj):  # len
    return len(obj)

def მთელი(x=0):  # int
    return int(x)

def წილადი(x=0):  # float
    return float(x)

def სტრიქონი(x=""):  # str
    return str(x)

def სახელი(obj):  # type
    return type(obj)

def დამრგვალე(x, n=0):  # round
    return round(x, n)

def შეკრიბე(iterable, start=0):  # sum
    return sum(iterable, start)

def მინიმუმი(*args, **kwargs):  # min
    return min(*args, **kwargs)

def მაქსიმუმი(*args, **kwargs):  # max
    return max(*args, **kwargs)

def ყველა(iterable):  # all
    return all(iterable)

def რომელიმე(iterable):  # any
    return any(iterable)

def დიაპაზონი(*args):  # range
    return range(*args)

def დაალაგე(iterable, **kwargs):  # sorted
    return sorted(iterable, **kwargs)

def შედარება(a, b):  # cmp (removed in py3, but emulate)
    return (a > b) - (a < b)

def ფაილი(*args, **kwargs):  # open
    return open(*args, **kwargs)

def შეავსე(თანმიმდევრობა):  # enumerate
    return enumerate(თანმიმდევრობა)

def დააწყვილე(*iterables):  # zip
    return zip(*iterables)
def აბს(x):  # abs
    return abs(x)

async def აითერი(aiterable):  # aiter (async iterator)
    return aiter(aiterable)

async def ანექსტი(iterator):  # anext
    return await anext(iterator)

def ასკი(obj):  # ascii
    return ascii(obj)

def ბინ(x):  # bin
    return bin(x)

def ბული(x=False):  # bool
    return bool(x)

def გაჩერება(*args, **kwargs):  # breakpoint
    return breakpoint(*args, **kwargs)

def ბაიტმასივი(*args, **kwargs):  # bytearray
    return bytearray(*args, **kwargs)

def ბაიტები(*args, **kwargs):  # bytes
    return bytes(*args, **kwargs)

def დარეკვადი(obj):  # callable
    return callable(obj)

def სიმბოლო(n):  # chr
    return chr(n)

def საკლასომეთოდი(func):  # classmethod
    return classmethod(func)

def კომპილაცია(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):  # compile
    return compile(source, filename, mode, flags, dont_inherit, optimize)

def კომპლექსი(*args):  # complex
    return complex(*args)

def წაშალატრ(obj, name):  # delattr
    return delattr(obj, name)

def დირექტორია(obj=None):  # dir
    return dir(obj)

def დივმოდი(a, b):  # divmod
    return divmod(a, b)

def გაფილტრე(func, iterable):  # filter
    return filter(func, iterable)

def ფორმატი(value, spec=""):  # format
    return format(value, spec)

def გაყინულინაბორი(*args):  # frozenset
    return frozenset(*args)

def მიიღე(obj, name, default=None):  # getattr
    return getattr(obj, name, default)

def გლობალები():  # globals
    return globals()

def გაქვს(obj, name):  # hasattr
    return hasattr(obj, name)

def ჰეში(obj):  # hash
    return hash(obj)

def დახმარება(obj=None):  # help
    return help(obj)

def ჰექს(x):  # hex
    return hex(x)

def აიდი(obj):  # id
    return id(obj)

def შემოტანი(prompt=""):  # input
    return input(prompt)

def არისინსტანცია(obj, cls):  # isinstance
    return isinstance(obj, cls)

def არისქვეკლასი(cls, class_or_tuple):  # issubclass
    return issubclass(cls, class_or_tuple)

def იტერაცია(obj):  # iter
    return iter(obj)

def ლოკალები():  # locals
    return locals()

def რუკა(func, *iterables):  # map
    return map(func, *iterables)

def მეხსიერებაშეხედვა(obj):  # memoryview
    return memoryview(obj)

def შემდეგი(iterator, default=None):  # next
    return next(iterator, default)

def ობიექტი():  # object
    return object()

def ოკტ(x):  # oct
    return oct(x)

def ორდ(ch):  # ord
    return ord(ch)

def სიმძლავრე(a, b, mod=None):  # pow
    return pow(a, b, mod) if mod else pow(a, b)

def საკუთრება(fget=None, fset=None, fdel=None, doc=None):  # property
    return property(fget, fset, fdel, doc)

def რეპრ(obj):  # repr
    return repr(obj)

def უკუღმა(seq):  # reversed
    return reversed(seq)

def ნაკვეთი(start, stop=None, step=None):  # slice
    return slice(start, stop, step)

def სტატიკურიმეთოდი(func):  # staticmethod
    return staticmethod(func)

def სუპერ(cls=None, obj=None):  # super
    return super(cls, obj) if cls else super()

def ტუპლი(*args):  # tuple
    return tuple(*args)

def ცვლადები(obj=None):  # vars
    return vars(obj) if obj else vars()

def იმპორტი(name, globals=None, locals=None, fromlist=(), level=0):  # __import__
    return __import__(name, globals, locals, fromlist, level)
