from kivy.properties import ObjectProperty 
from kivy.core.window import Window
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivymd.app import MDApp 

Builder.load_file( 'calc.kv' )
Window.size = ( 500, 700 )

class MyCalculator( Widget ):
    operations = [] 
    numbers_to_calc = []

    def button_press(self, button ):

        display = self.ids.calc_input.text
         # If display is equal to zero, the number has to be add lonely
        if display == '0':
            display = ''
        
        # Variable usedo to draw the rigth number in display 
        to_display = ''
    
        # Numbers keys 
        if button == 0:
            to_display = display + '0'
        elif button == 1:
            to_display = display + '1'
        elif button == 2:
            to_display = display + '2'
        elif button == 3:
            to_display = display + '3'
        elif button == 4:
            to_display = display + '4'
        elif button == 5:
            to_display = display + '5'
        elif button == 6:
            to_display = display + '6'
        elif button == 7:
            to_display = display + '7'
        elif button == 8:
            to_display = display + '8'
        elif button == 9:
            to_display = display + '9'

        # Add a dot 
        elif button == '.':
            if display == '':
                to_display = '0.'
            else: 
                if '.' not in display: 
                    to_display = display + '.'
                else: 
                    to_display = display


        # Clear one digit 
        elif button == '<=':
            if display == '':
                to_display = '0'
            else: 
                to_display = display[:-1]
                if to_display == '':
                    to_display = '0'

        # Return display to zero if is the case 
        if display == '':
            display = '0'

        # Operations 
        if button == '-':
            self.operations.append( '-' )
            self.numbers_to_calc.append( float(display) )
            to_display = '0'             
        elif button == '+':
            self.operations.append( '+' )
            self.numbers_to_calc.append( float(display) )
            to_display = '0'
        elif button == '/':
            self.operations.append( '/' )
            self.numbers_to_calc.append( float(display) )
            to_display = '0'
        elif button == 'x':
            self.operations.append( 'x' )
            self.numbers_to_calc.append( float(display) )
            to_display = '0'
        elif button == '%':
            self.operations.append( '%' )
            self.numbers_to_calc.append( float(display) )
            to_display = '0'
        
        # Clear Entry 
        elif   button == 'CE':
            to_display = '0'
        # Clear 
        elif button == 'C':
            self.operations = [] 
            self.numbers_to_calc = [] 
            to_display = '0'
        # Execute the calculation 
        elif button == '=':
            self.numbers_to_calc.append( float(display) if display != '' else 0 )
            to_display = self.calculate() 
            self.numbers_to_calc = [] 
            self.operations = []

        self.ids.calc_input.text = to_display

    def calculate(self):
        for operation in self.operations:
            num1 = self.numbers_to_calc.pop(0)
            if operation == '-':
                self.numbers_to_calc[0] = num1 - self.numbers_to_calc[0]
            elif operation == '+':
                self.numbers_to_calc[0] = num1 + self.numbers_to_calc[0]
            elif operation == '/':
                self.numbers_to_calc[0] = num1 / self.numbers_to_calc[0]
            elif operation == 'x':
                self.numbers_to_calc[0] = num1 * self.numbers_to_calc[0]
            elif operation == '%':
                self.numbers_to_calc[0] = num1 * ( self.numbers_to_calc[0] / 100 )
        
        calculated = str(self.numbers_to_calc[0]).split('.')
        if int(calculated[1]) == 0:
            return calculated[0]
        else:   
            return str(self.numbers_to_calc[0])


class MyApp( MDApp ):
    def build(self): 
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightBlue'
        return MyCalculator()


if __name__ == '__main__':
    MyApp().run()