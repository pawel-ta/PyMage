
from PyMage import *
from SampleClasses import A, B

# Become Python Mage
PyMage.become_mage(globals())

# Examples

## Enchant objects with other objects
print("\nEnchanting objects with other objects\n")

some_object = A() << enchanted_with >> B()

print(some_object.field, some_object.field_2, sep='\n')
some_object.method()
some_object.method_2()

## Summon objects
print("\nSummon and unsummon objects\n")

summon >> A() >> "tss"
summon >> B() >> "bss"
summon >> A() >> "css"
summon >> B() >> "dss"
tss.method()
bss.method()
css.method()
dss.method()

unsummon >> "tss"

try:
    tss.method()
except NameError as err:
    print("Nie ma tss")

unsummon >> all_summons

try:
    print(dss, sep=" ")
except NameError as err:
    print("Nie ma dss")
