class String:
    is_empty = False

#А, затем, создаются два его экземпляра:

s1 = String()
s2 = String()

#После этого выполняется команда:

s2.is_empty = True
print(s2.is_empty)
print(s1.is_empty)
print(String.is_empty)
