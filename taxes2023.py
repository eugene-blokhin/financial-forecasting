def calculate_zvw(box_1_income):
    # See https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/zorgverzekeringswet/veranderingen-bijdrage-zvw/
    return min(66956, box_1_income) * 0.0543

def calculate_arbeidskorting(income_from_work):
    # See https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/heffingskortingen/arbeidskorting/tabel-arbeidskorting-2023
    # Arbeidsinkomen 	Arbeidskorting    
    # tot € 10.741 	8,231% x arbeidsinkomen
    if income_from_work <= 10741: 
        arbeidskorting = 0.08231 * income_from_work
        
    # vanaf € 10.741 tot € 23.201 	€ 884 + 29,861% x (arbeidsinkomen - € 10.740)
    elif income_from_work <= 23201:
        arbeidskorting = 884 + 0.29861 * (income_from_work - 10740)
        
    # vanaf € 23.201 tot € 37.691 	€ 4.605 + 3,085% x (arbeidsinkomen - € 23.201)
    elif income_from_work <= 37691:
        arbeidskorting = 4605 + 0.03085 * (income_from_work - 23201)
        
    # vanaf € 37.691 tot € 115.295 	€ 5.052 - 6,510% x (arbeidsinkomen - € 37.691)
    elif income_from_work <= 115295:
        arbeidskorting = 5052 - 0.06510 * (income_from_work - 37691)
        
    # vanaf € 115.295 	€ 0
    else:
        arbeidskorting = 0
        
    return arbeidskorting

def calculate_algemene_heffingskorting(taxable_amount):
    # See https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/heffingskortingen/algemene_heffingskorting/tabel-algemene-heffingskorting-2023
    if taxable_amount <= 22661: 
        algemene_heffingskorting = 3070
    elif taxable_amount <= 73031: 
        algemene_heffingskorting = 3070 - 0.06095 * (taxable_amount - 22660)
    else:
        algemene_heffingskorting = 0
        
    return algemene_heffingskorting

def calculate_tax(taxable_amount):
    # See https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/hoeveel-inkomstenbelasting-betalen
    BRACKET_THRESHOLD = 73031
    BRACKET_1_TAX_RATE = 36.93 / 100
    BRACKET_2_TAX_RATE = 49.50 / 100
    
    bracket_1_amount = min(taxable_amount, BRACKET_THRESHOLD)
    bracket_2_amount = max(0, taxable_amount - BRACKET_THRESHOLD)
    
    bracket_1_tax = bracket_1_amount * BRACKET_1_TAX_RATE
    bracket_2_tax = bracket_2_amount * BRACKET_2_TAX_RATE
    
    return bracket_1_tax + bracket_2_tax

# See https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2023/ondernemersaftrek-2023/zelfstandigenaftrek-2023
def calculate_zelfstandigenaftrek(revenue, apply_startersaftrek):
    zelfstandigenaftrek = 5030
    startersaftrek = 2123
    
    amount = zelfstandigenaftrek
    if apply_startersaftrek:
        amount += startersaftrek
    
    return min(revenue, amount)

# See https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling
def calculate_mkb_winstvrijstelling(revenue_after_zelfstandigenaftrek):
    return revenue_after_zelfstandigenaftrek * 0.14

# See https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/afbouw-tarief-aftrekposten-bij-hoog-inkomen
def calculate_tariefsaanpassing_box_1(income, adjustable_deductions):
    return max(0, min(adjustable_deductions, income - 73031) * 0.1257)