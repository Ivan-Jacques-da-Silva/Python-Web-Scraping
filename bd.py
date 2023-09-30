win_Sg = 0
loss = 0
brancos = 0
win_g1 = 0
win_g2 = 0
total_win = 0
porcentagem = 0

b = win_Sg + brancos + win_g1 + win_g2
b = win_Sg + brancos + win_g1 + win_g2
if (win_Sg + brancos + win_g1 + win_g2 + loss) !=0:
    a = 100/(win_Sg + brancos + win_g1 + win_g2 + loss) * b
else:
    a = 0
porcentagem = (f'{a:,.2f}%')

analisar = 0
gale_atual = 0
analisar_open = 0
resultsDouble = []


# NOVAS VARIABLES
direction_color = 'NULL'
estrategy_name = 'TRUE'

finalnum = []
finalcor = []