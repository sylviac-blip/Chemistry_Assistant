from drafter import *
from bakery import assert_equal
from dataclasses import dataclass

set_website_title("Chemistry Assistant")
set_site_information(
    author="Sylvia Capri",
    description="Finds theoretical yield, limiting reactant, percent yield, heat per mole of product, and identifies whether reaction is exothermic or endothermicfrom a balanced chemical equation and starting masses.",
    sources="",
    planning=["plan.pdf", "design.pdf"],
    links=[]
)
hide_debug_information()
    
MOLAR_MASSES_DICTIONARY = {

    "H": 1.008,
    "He": 4.003,
    "Li": 6.94,
    "Be": 9.012,
    "B": 10.81,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.38,
    "Br": 79.904,
    "Ag": 107.868,
    "I": 126.904,
    "Ba": 137.327,
    "Hg": 200.592,
    "Pb": 207.2,

    "H2": 2.016,
    "N2": 28.014,
    "O2": 31.998,
    "F2": 37.996,
    "Cl2": 70.90,
    "Br2": 159.808,
    "I2": 253.808,
    "H2O": 18.015,
    "H2O2": 34.014,
    "NH3": 17.031,
    "CH4": 16.043,
    "C2H6": 30.070,
    "C3H8": 44.097,
    "C4H10": 58.124,
    "CO": 28.010,
    "CO2": 44.009,
    "NO": 30.006,
    "NO2": 46.005,
    "N2O": 44.013,
    "N2O4": 92.010,
    "SO2": 64.06,
    "SO3": 80.06,
    "H2S": 34.076,
    "HCl": 36.458,
    "HF": 20.006,
    "HBr": 80.912,
    "HI": 127.912,

    "HNO3": 63.012,
    "HNO2": 47.013,
    "H2SO4": 98.072,
    "H2SO3": 82.072,
    "H3PO4": 97.994,
    "H2CO3": 62.024,
    "HC2H3O2": 60.052,
    "CH3COOH": 60.052,

    "NaOH": 39.997,
    "KOH": 56.105,
    "Ca(OH)2": 74.092,
    "Mg(OH)2": 58.319,
    "Al(OH)3": 78.003,
    "NH4OH": 35.046,

    "NaCl": 58.44,
    "KCl": 74.551,
    "LiCl": 42.39,
    "CaCl2": 110.98,
    "MgCl2": 95.211,
    "AlCl3": 133.34,
    "FeCl2": 126.75,
    "FeCl3": 162.20,
    "CuCl2": 134.45,
    "NaF": 41.988,
    "CaF2": 78.075,
    "NaBr": 102.89,
    "KBr": 119.00,
    "NaI": 149.89,
    "KI": 166.00,
    "AgNO3": 169.87,
    "NaNO3": 84.995,
    "KNO3": 101.103,
    "NH4NO3": 80.043,
    "Mg(NO3)2": 148.313,
    "Ca(NO3)2": 164.086,
    "Cu(NO3)2": 187.554,
    "Na2SO4": 142.04,
    "K2SO4": 174.26,
    "MgSO4": 120.366,
    "CaSO4": 136.14,
    "CuSO4": 159.609,
    "BaSO4": 233.39,
    "(NH4)2SO4": 132.14,
    "Na2CO3": 105.988,
    "NaHCO3": 84.007,
    "CaCO3": 100.086,
    "MgCO3": 84.313,
    "K2CO3": 138.205,
    "Na3PO4": 163.94,
    "Ca3(PO4)2": 310.174,
    "NH4Cl": 53.491,
    "Na2S": 78.045,
    "ZnS": 97.44,
    "FeS": 87.91,
    "ZnO": 81.38,
    "MgO": 40.304,
    "CaO": 56.077,
    "Al2O3": 101.96,
    "Fe2O3": 159.69,
    "Fe3O4": 231.53,
    "CuO": 79.545,
    "Cu2O": 143.09,
    "MnO2": 86.936,
    "P4O10": 283.89,

    "C6H12O6": 180.156,
    "C12H22O11": 342.297,
    "C2H5OH": 46.069,
    "C2H6O": 46.069,
    "C3H6O": 58.080,
    "C2H4": 28.054,
    "C2H2": 26.038,
    "C6H6": 78.114,
    "C7H8": 92.141,
    "C8H18": 114.232,
    "CS2": 76.14,
    "SiO2": 60.084,
    "KClO3": 122.55,
    "KClO4": 138.55,
    "NaClO": 74.44,
    "NaClO3": 106.44,
    "KMnO4": 158.034,
    "K2Cr2O7": 294.18,
    "H2O2": 34.014
}


@dataclass
class Chemical:
    formula:str
    coefficient:int
    molar_mass:float
    starting_mass:float
    chemical_type:str
    final_mass:float

@dataclass
class State:
    reaction_equation:str
    chemicals:list[Chemical] 
    product_actual_mass:float
    delta_h:float
    limiting_reactant:list[str]
    theoretical_yield:float
    percent_yield:float
    heat_per_mole:float
    reaction_type:str
    product:Chemical
#-----------------------------------------------------#


def get_reactants(reaction_equation:str)->list[Chemical]:
    """Takes the balanced chemical equation and returns a list of reactants
        Args:
        reaction_equation (str): balanced chemical equation
        Returns:
        list[Chemical]: list of reactants
    """
    if not reaction_equation:
        return []
    reactants=[]
    reactant_side=reaction_equation.split("->")[0]
    chemicals=reactant_side.split("+")
    for chemical in chemicals:
        parts=chemical.strip().split()
        
        if len(parts)==2:
            coefficient=int(parts[0])
            formula=parts[1]
        else:
            coefficient=1
            formula=parts[0]
        reactants.append(Chemical(formula,coefficient,0.0,0.0,"reactant",0.0))
    return reactants

assert_equal(get_reactants("2 H2 + O2 -> 2 H2O"),
    [Chemical("H2",2,0.0,0.0,"reactant",0.0),
    Chemical("O2",1,0.0,0.0,"reactant",0.0)])

assert_equal(get_reactants("H2 + O2 -> H2O"),
    [Chemical("H2",1,0.0,0.0,"reactant",0.0),
     Chemical("O2",1,0.0,0.0,"reactant",0.0)])


assert_equal(get_reactants("CH4 + 2 O2 -> CO2 + 2 H2O"),
    [Chemical("CH4",1,0.0,0.0,"reactant",0.0),
    Chemical("O2",2,0.0,0.0,"reactant",0.0)])

assert_equal(get_reactants(""),[])

def get_molar_mass(formula:str)->float:
    """Takes in a compound/element and finds the molar mass from the molar mass dictionary
    Args:
    formula(str): formula/element
    Returns:
    float: molar mass of compound/element
    """
    if not formula:
        return 0.0
    return MOLAR_MASSES_DICTIONARY[formula]

assert_equal(get_molar_mass("O"), 15.999)
assert_equal(get_molar_mass("H2O"), 18.015)
assert_equal(get_molar_mass(""), 0.0)



def get_first_product(reaction_equation:str)->Chemical:
    """Takes the reaction equation and updates the Chemical dataclass for the first product
        Args:
        reaction_equation(str): the balanced chemical equation
        Returns:
        Chemical: dataclass for the first product in the equation."""
    
    if not reaction_equation:
        return Chemical("",1,0.0,0.0,"product",0.0)
    
    product_side=reaction_equation.split("->")[1]
    first_product=product_side.split("+")[0].strip().split()
    
    if len(first_product)==2:
        coefficient=int(first_product[0])
        formula=first_product[1]
    else:
        coefficient=1
        formula=first_product[0]
    
    molar_mass=get_molar_mass(formula)
    
    return Chemical(formula,coefficient,molar_mass,0.0,"product",0.0)

assert_equal(get_first_product("2 H2 + O2 -> 2 H2O"),Chemical("H2O",2,18.015,0.0,"product",0.0))
assert_equal(get_first_product("H2 + O2 -> H2O"),Chemical("H2O",1,18.015,0.0,"product",0.0))
assert_equal(get_first_product("CH4 + 2 O2 -> CO2 + 2 H2O"),Chemical("CO2",1,44.009,0.0,"product",0.0))
assert_equal(get_first_product(""),Chemical("",1,0.0,0.0,"product",0.0))


def find_limiting_reactant(chemicals:list[Chemical])->list[str]:
    """Takes a list of Chemical dataclasses and finds which one has the smallest amount of moles,
        making it the limiting reactant. Then it updates its formula to a list of strings. If both
        reactants have the same amount of moles, they are both added to the list of strings
        Args:
        chemicals(list[Chemical]):list of chemicals in the reactants.
        Returns:
        list[str]: a list of the formulas of the limiting reactant(s)
        """
    smallest_amount=1000000
    limiting_reactants= []
    if not chemicals:
        return []
    for chemical in chemicals:
        moles=chemical.starting_mass/chemical.molar_mass
        reaction_amount=moles/chemical.coefficient
        
        if reaction_amount< smallest_amount:
            smallest_amount=reaction_amount
            limiting_reactants=[]
            limiting_reactants.append(chemical.formula)
            
        elif reaction_amount == smallest_amount:
            limiting_reactants.append(chemical.formula)
            
    return limiting_reactants

test_chemicals= [
    Chemical("CH4",1,16.04,16.04,"reactant",0.0),
    Chemical("O2",2,32.00,32.00,"reactant",9.9)
    ]
assert_equal(find_limiting_reactant(test_chemicals),["O2"])

test_chemicals2 = [
    Chemical("H2", 2, 2.016, 4.032, "reactant", 0.0),
    Chemical("O2", 1, 32.00, 32.00, "reactant", 0.0)]
assert_equal(find_limiting_reactant(test_chemicals2), ["H2", "O2"])
assert_equal(find_limiting_reactant([]), [])

def find_theoretical_yield(chemicals:list[Chemical], product:Chemical)->float:
    """ Calculates the theoretical yield by finding the limiting reactant and finding how much product
        is produced
        Args:
        chemicals(list[Chemical]: list of reactants and their dataclass information
        product(Chemical): dataclass of all of the information about the product
        Returns:
        float: value of the theoretical yield
        """
    if not chemicals:
        return 0.0
    reaction_amounts=[]

    for chemical in chemicals:
        moles=chemical.starting_mass/chemical.molar_mass
        reaction_amount=moles/chemical.coefficient
        reaction_amounts.append(reaction_amount)

    smallest_amount=reaction_amounts[0]

    for amount in reaction_amounts:
        if amount<smallest_amount:
            smallest_amount=amount

    product_moles=smallest_amount*product.coefficient
    theoretical_yield=product_moles*product.molar_mass

    return theoretical_yield

test_product = Chemical("H2O", 2, 18.015, 0.0, "product", 0.0)
assert_equal(find_theoretical_yield([], test_product), 0.0)
test_chemicals1 = [Chemical("H2", 2, 2.016, 2.016, "reactant", 0.0),Chemical("O2", 1, 32.00, 32.00, "reactant", 0.0)]
assert_equal(find_theoretical_yield(test_chemicals1, test_product), 18.015)

def find_percent_yield(actual_yield:float,theoretical_yield:float)->float:
    """determines the percent yield by dividing the actual yield given by the theoretical yield
        Args:
        actual_yield(float):the actual yield provided by the user
        theoretical_yield(float): the calculated theoretical yield
        Returns:
        float: the percent yield for the first product in the equation
        """
    if not theoretical_yield:
        return 0.0
    percent_yield=(actual_yield/theoretical_yield)*100
    return percent_yield

assert_equal(find_percent_yield(50.0, 50.0), 100.0)
assert_equal(find_percent_yield(40.0, 50.0), 80.0)
assert_equal(find_percent_yield(60.0, 50.0), 120.0)
assert_equal(find_percent_yield(0.0, 50.0), 0.0)
assert_equal(find_percent_yield(50.0, 0.0), 0.0)

def find_leftover_mass(chemicals:list[Chemical])->list[float]:
    """Finds the leftover masses of each reactant by find the amount of moles of each reactant,
        detemining the limiting reactant, and subtracting the mass used by the beginning mass
        Args:
        chemicals(list[Chemical]): list of reactants and their dataclasses
        Returns:
        list[float]: list of leftover masses of each reactant
        """
    if not chemicals:
        return []
    leftover_masses=[]
    reaction_amounts=[]
    
    for chemical in chemicals:
        moles=chemical.starting_mass/chemical.molar_mass
        reaction_amount=moles/chemical.coefficient
        reaction_amounts.append(reaction_amount)
    smallest_amount=reaction_amounts[0]    
    for amount in reaction_amounts:
        if amount<smallest_amount:
            smallest_amount=amount
    for chemical in chemicals:
        moles_used=smallest_amount*chemical.coefficient
        mass_used=moles_used*chemical.molar_mass
        leftover_mass=chemical.starting_mass-mass_used
        leftover_masses.append(leftover_mass)
    return leftover_masses

test_chemicals5 = [
    Chemical("H2", 2, 2.0, 10.0, "reactant", 0.0),
    Chemical("O2", 1, 32.0, 32.0, "reactant", 0.0)
]
assert_equal(find_leftover_mass(test_chemicals5), [6.0, 0.0])
assert_equal(find_leftover_mass([]), [])


def find_reaction_type(delta_h:float)->str:
    """Looks at the delta_h value provided by the user and checks if the value is less
        than 0 or greater than 0. Greater than 0 is endothermic, less than 0 is exothermic, and 0 is neutral
        Args:
        delta_h(float): value of the change in enthalpy of the reaction
        Returns:
        str: returns whether reaction is endothermic, exothermic, or neutral
        """
    
    if delta_h<0:
        return "Exothermic"
    elif delta_h>0:
        return "Endothermic"
    else:
        return "neutral"

assert_equal(find_reaction_type(-100), "Exothermic")
assert_equal(find_reaction_type(-25.5), "Exothermic")
assert_equal(find_reaction_type(100), "Endothermic")
assert_equal(find_reaction_type(25.5), "Endothermic")
assert_equal(find_reaction_type(0), "neutral")

def heat_per_mole_calculation(delta_h:float,product_moles:float)->float:
    """Finds the heat per mole of the product using the delta_h value put in by the user
        Args:        
        delta_h(float):value of the change in enthalpy of the reaction
        product_moles(float):moles of product in the reaction
        Returns:
        float: heat per mole of the reaction
        """
    if not product_moles:
        return 0.0
    return delta_h/product_moles
  
assert_equal(heat_per_mole_calculation(-100, 2), -50.0)
assert_equal(heat_per_mole_calculation(100, 2), 50.0)
assert_equal(heat_per_mole_calculation(-500, 5), -100.0)
assert_equal(heat_per_mole_calculation(250, 10), 25.0)
assert_equal(heat_per_mole_calculation(0, 5), 0.0)

@route
def index(state:State)->Page:
    """Shows the homepage of the Chemistry Assistant.
    Args:
        state(State): the current state of the Chemistry Assistant
    Returns:
        Page: the homepage with an introduction and a start button
    """
    return Page(state,[
        Header("Hello! I am your Chemistry Assistant."),
        Text("I can help you calculate limiting reactants, theoretical yield, percent yield, and reaction heat."),
        LineBreak(),
        Button("Start Calculation","reaction_page")
                ])
test_state1 = State("", [], 0.0, 0.0, [], 0.0, 0.0, 0.0, "", Chemical("", 1, 0.0, 0.0, "product", 0.0))

assert_equal(index(test_state1).state, test_state1)


@route
def reaction_page(state:State)->Page:
    """Opens the page where the user enters a balanced chemical equation.
    Args:
        state(State): the current state of the Chemistry Assistant
    Returns:
        Page: a page with instructions, an example, and a textbox
        to enter the reaction
    """
    return Page(state,[
        Header("Please enter your balanced chemical equation:"),
        LineBreak(),
        Text("Note: Make sure to put a space between each coefficient and the element or compound"),
        Text("Example: 2 H2 + O2 -> 2 H2O"),
        LineBreak(),
        Text("If your reaction has multiple products, place the product you want to calculate the yield for first"),
        TextBox("reaction_equation"),
        LineBreak(),
        Button("Continue","add_chemical")
                    ])
test_state = State("", [], 0.0, 0.0, [], 0.0, 0.0, 0.0, "", Chemical("", 1, 0.0, 0.0, "product", 0.0))

assert_equal(reaction_page(test_state).state, test_state)

@route
def add_chemical(state:State,reaction_equation:str)->Page:
     """This route starts to process the equation entered by the user and makes the user
        put in the starting masses for all reactants
        Args:
        state(State): current state of Chemistry Assistant
        reaction_equation(str): the balanced chemical equation entered by the user
        Returns:
        Page: a text displaying the reaction that was inputted as well as textboxes to enter the starting masses
        of reactants
    """
     state.reaction_equation=reaction_equation
     state.chemicals= get_reactants(reaction_equation)
     state.product=get_first_product(reaction_equation)
     for chemical in state.chemicals:
         chemical.molar_mass= get_molar_mass(chemical.formula)
     
     return Page(state,[
         Header("Reactant Information"),
         Text("Your Reaction:" + state.reaction_equation),
         LineBreak(),
         Text("Enter the starting mass of your first reactant in grams:"),
         TextBox("mass1"),
         LineBreak(),
         Text("Enter the starting mass of your second reactant in grams:"),
         TextBox("mass2"),
         LineBreak(),
         Button("Continue","product_info")
         ])
test_state7 = State("", [], 0.0, 0.0, [], 0.0, 0.0, 0.0, "", Chemical("", 1, 0.0, 0.0, "product", 0.0))

result = add_chemical(test_state7, "2 H2 + O2 -> 2 H2O")
assert_equal(test_state7.reaction_equation, "2 H2 + O2 -> 2 H2O")


@route
def product_info(state:State,mass1:float,mass2:float)->Page:
    """Saves the starting masses of both reactants and shows the
    page where the user enters product information.
    Args:
        state(State): the current state of Chemistry Assistant
        mass1(float): starting mass of the first reactant
        mass2(float): starting mass of the second reactant
    Returns:
        Page: the product information page
    """
    state.chemicals[0].starting_mass=mass1
    
    state.chemicals[1].starting_mass=mass2
    
    return Page(state,[
        Header("Product Information"),
        Text("Enter the actual mass of the product collected in grams:"),
        TextBox("product_actual_mass"),
        LineBreak(),
        Text("Enter the heat of the reaction (Delta H) in kJ:"),
        TextBox("delta_h"),
        LineBreak(),
        Button ("Continue","calculating_results")
        ])
test_state9 = State("2 H2 + O2 -> 2 H2O",
    [Chemical("H2", 2, 2.0, 0.0, "reactant", 0.0),Chemical("O2", 1, 32.0, 0.0, "reactant", 0.0)],
    0.0, 0.0, [], 0.0, 0.0, 0.0, "",
    Chemical("H2O", 2, 18.015, 0.0, "product", 0.0))
product_info(test_state9, 10.0, 32.0)

assert_equal(test_state9.chemicals[0].starting_mass, 10.0)
assert_equal(test_state9.chemicals[1].starting_mass, 32.0)


@route
def calculating_results(state:State,product_actual_mass:float,delta_h:float)->Page:
    """Calculates the  results and saves them in the state dataclass.
    Args:
        state(State): the current state of the Chemistry Assistant
        product_actual_mass(float): the actual mass of product collected
        delta_h(float): the change of enthalpy of the reaction in kJ
    Returns:
        Page: the results page showing the final chemistry calculations
"""
    state.product_actual_mass=product_actual_mass
    state.delta_h=delta_h
    
    state.limiting_reactant=find_limiting_reactant(state.chemicals)
    state.theoretical_yield=find_theoretical_yield(state.chemicals,state.product)
    state.percent_yield=find_percent_yield(state.product_actual_mass,state.theoretical_yield)
    state.reaction_type=find_reaction_type(state.delta_h)
    state.heat_per_mole=heat_per_mole_calculation(state.delta_h,(state.theoretical_yield/state.product.molar_mass))
    
    return results_page(state)
#tests written below

@route
def results_page(state:State)->Page:
    """Shows the final  results to the user.
    Args:
        state(State): the current state of Chemistry Assistant
    Returns:
        Page: a page showig the limiting reactant, theoretical yield,
        percent yield, leftover masses, reaction type, and heat per mole
    """
    leftover_masses=find_leftover_mass(state.chemicals)
    return Page(state,[
        Header("Your Results"),
        Text("Limiting Reactant: " + state.limiting_reactant[0]),
        LineBreak(),
        Text("Theoretical Yield: " + str(state.theoretical_yield)+" g"),
        LineBreak(),
        Text("Percent Yield: " +str(state.percent_yield) + "%"),
        LineBreak(),
        Text("Leftover Reactant Masses:"),
        Text(state.chemicals[0].formula + ": " + str(leftover_masses[0]) + "g"),
        Text(state.chemicals[1].formula + ": " + str(leftover_masses[1]) + "g"),
        LineBreak(),
        Text("Reaction Type: " + state.reaction_type),
        LineBreak(),
        Text("Heat per Mole of Product: " + str(state.heat_per_mole)+ "kJ/mol"),
        Button("Start New Calculation","reset")
             ])
#tests written below

@route
def reset(state:State)->Page:
    """Resets back to the index/home page and resets all of the information in the state
    Args:
    state(State): the current state of the Chemistry Assistant
    Returns:
        Page: the homepage with a new state thats empty
    """
    state.reaction_equation=""
    state.chemicals=[]
    state.product_actual_mass=0.0
    state.delta_h=0.0
    state.limiting_reactant=[]
    state.theoretical_yield=0.0
    state.percent_yield=0.0
    state.heat_per_mole=0.0
    state.reaction_type=""
    state.product=Chemical("",1,0.0,0.0,"product",0.0)

    return index(state)
#tests written below

test_state10 = State("2 H2 + O2 -> 2 H2O",
    [Chemical("H2", 2, 2.0, 10.0, "reactant", 0.0),Chemical("O2", 1, 32.0, 32.0, "reactant", 0.0)],
    0.0, 0.0, [], 0.0, 0.0, 0.0, "",
    Chemical("H2O", 2, 18.015, 0.0, "product", 0.0))

calculating_results(test_state10, 30.0, -500.0)

assert_equal(test_state10.product_actual_mass, 30.0)
assert_equal(test_state10.delta_h,-500.0)


test_state11 = State("2 H2 + O2 -> 2 H2O",
    [Chemical("H2", 2, 2.0, 10.0, "reactant", 0.0),Chemical("O2", 1, 32.0, 32.0, "reactant", 0.0)],
    30.0, -500.0, ["O2"], 36.03, 83.26394671107356,
    -250.0, "Exothermic",Chemical("H2O", 2, 18.015, 0.0, "product", 0.0))

results_page(test_state11)
assert_equal(test_state11.limiting_reactant, ["O2"])
assert_equal(test_state11.theoretical_yield, 36.03)

test_state12 = State("2 H2 + O2 -> 2 H2O",
    [Chemical("H2", 2, 2.0, 10.0, "reactant", 0.0),Chemical("O2", 1, 32.0, 32.0, "reactant", 0.0)],
    30.0, -500.0, ["O2"], 36.03, 83.26,-250.0, "Exothermic",
    Chemical("H2O", 2, 18.015, 0.0, "product", 0.0))

reset(test_state12)
assert_equal(test_state12.reaction_equation, "")
assert_equal(test_state12.chemicals, [])
assert_equal(test_state12.product_actual_mass, 0.0)

start_server(State("",[],0.0,0.0,[],0.0,0.0,0.0,"",Chemical("",1,0.0,0.0,"product",0.0)))
    
    
    
