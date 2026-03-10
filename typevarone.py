user_id="GuruRajesh" #global variable
def home():
    dep="computer science" #Local variable
    print("Welcome :", user_id) #global variable used here
    def profile():
        reg_num="13UCA068"
        print(f"Welcome to the home page :{dep} department") #enclose variable used here
        print(f"your register no :{reg_num} {dep} department and your name is {user_id} then your register number {len(reg_num)}") #builtin function used here
        print(__file__) # builtin varibles
    profile()
home()