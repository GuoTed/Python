# Encapsulation
# Inheritance
# Polymorphism

# pythno class using Encapsulation
class Tea:
    def __init__(self):
        self.smell = 'none'
        self.color = 'transparent'

    def info(self):
        print('Smell:{}, Color:{} called by Tea'.format(self.smell, self.color))
 
# using Inheritance 
class BlackTea(Tea):
    # class attribute: same value for all instances
    name = 'BlackTea' 
    # instance attribute
    def __init__(self, smell, color):
        super().__init__()
        print('Inherit from Tea ->')
        super().info() # Smell:none, Color:transparent called by Tea
        print('Init from params ->')
        self.init_params(smell, color)
        super().info() # Smell:good, Color:red called by Tea

    def init_params(self, smell, color):
        self.smell = smell
        self.color = color

    # using Polymorphism
    def info(self):
        print('Smell:{}, Color:{} called by BlackTea'.format(self.smell, self.color))

if __name__ == '__main__':
    t1 = BlackTea('good', 'red')
    t1.info() # Smell:good, Color:red called by BlackTea

    # check if instance will be the same
    t2 = BlackTea('good', 'red')
    print('t1 & t2 are differnt !!') if t1 != t2 else print('t1 & t2 are the same !!')
    
    # change class atrribute
    t1.name = 'BlackTea-old'
    print(t1.name)
    print(t2.name)

# To-Do-List
# 1. super() usage
# 2. Dsign Pattern