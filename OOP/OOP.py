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
    t = BlackTea('good', 'red')
    t.info() # Smell:good, Color:red called by BlackTea
    
    