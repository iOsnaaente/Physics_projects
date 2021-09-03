# Posição-do-sol
Classe que efetua o rastreamento do sol dadas as coordenadas de Posição geográfica, Data  e Hora. Efetua os cálculos de rastreio do sol de forma simplificada, sendo adaptada para seu uso com um DS3231 sob um Raspberry Pi Pico em sistemas de geração solar com rastreamento inteligente do sol. 

- class Position 
- class Time 
- class Location 
- class Solar 


As três primeiras classes acima são usadas como parâmetros para a class Solar, que é a responsável pelo calculo da posição do sol. 

- Solar.__init__( location : Location, time : Time, position : Position, flags** ) 
- Solar.compute ( time : Time ) 
- Solar.get_azimute()
- Solar.get_altitude()
