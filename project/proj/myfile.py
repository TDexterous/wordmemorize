import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

''' 
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''

format_dict = {
    'Bold' : "\x1b[1m",
    'Dim' : "\x1b[2m",
    'Italic' : "\x1b[3m",
    'Underlined' : "\x1b[4m",
    'Blink' : "\x1b[5m",
    'Reverse' : "\x1b[7m",
    'Hidden' : "\x1b[8m",
    # Reset part
    'Reset' : "\x1b[0m",
    'Reset_Bold' : "\x1b[21m",
    'Reset_Dim' : "\x1b[22m",
    'Reset_Italic' : "\x1b[23m",
    'Reset_Underlined' : "\x1b[24",
    'Reset_Blink' : "\x1b[25m",
    'Reset_Reverse' : "\x1b[27m",
    'Reset_Hidden' : "\x1b[28m"
}

color_dict = {
    # Foreground
    'F_Default' : "\x1b[39m",
    'F_Black' : "\x1b[30m",
    'F_Red' : "\x1b[31m",
    'F_Green ': "\x1b[32m",
    'F_Yellow' : "\x1b[33m",
    'F_Blue' : "\x1b[34m",
    'F_Magenta' : "\x1b[35m",
    'F_Cyan' : "\x1b[36m",
    'F_LightGray' : "\x1b[37m",
    'F_DarkGray' : "\x1b[90m",
    'F_LightRed' : "\x1b[91m",
    'F_LightGreen' : "\x1b[92m",
    'F_LightYellow' : "\x1b[93m",
    'F_LightBlue' : "\x1b[94m",
    'F_LightMagenta' : "\x1b[95m",
    'F_LightCyan' : "\x1b[96m",
    'F_White' : "\x1b[97m",
    # Background
    'B_Default' : "\x1b[49m",
    'B_Black' : "\x1b[40m",
    'B_Red' : "\x1b[41m",
    'B_LightRed' : "\x1b[101m",
    'B_Green' : "\x1b[42m",  
    'B_LightGreen' : "\x1b[102m", 
    'B_DarkGray' : "\x1b[100m",
    'B_LightGray' : "\x1b[47m",   
    'B_Yellow' : "\x1b[43m",
    'B_LightYellow' : "\x1b[103m",
    'B_Blue' : "\x1b[44m",
    'B_LightBlue' : "\x1b[104m",
    'B_Magenta' : "\x1b[45m",
    'B_LightMagenta' : "\x1b[105m",
    'B_Cyan' : "\x1b[46m",
    'B_LightCyan' : "\x1b[106m",
    'B_White' : "\x1b[107m",
}

for col in color_dict:
    if col[0] == 'B':
        # print('Background Colors:')
        print(Fore.BLACK + color_dict[col] + format_dict['Italic'] + f'This is {col} Background')
    else:
        # print('Foreground Colors:')
        print(color_dict[col] + f'This is {col} Foreground')
