import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
#lcd.color = [100, 0 , 0]
lcd.message = "   Hello!" 
time.sleep (1)
lcd.clear()
scroll_msg = " Sunseeker "
lcd.message = scroll_msg
print('Scrolling msg...'+scroll_msg)
for i in range (len(scroll_msg)):
        time.sleep(0.5)
        lcd.move_left()
        print(scroll_msg[i], end ="")        
lcd.clear()
print('\nEnd!')
time.sleep(1)


