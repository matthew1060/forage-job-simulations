import pandas as pd

data = pd.read_csv('final_data.csv')
summary = pd.read_csv('summary_final_data.csv')

def simple_chatbot(user_query, company_entered, selected_year):
   company_entered = company_entered.capitalize()
   if user_query == "What is the total revenue?":
       revenue = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Total Revenue'].values[0]
       return f"The total revenue (in millions) for {company_entered} for the year {selected_year} is ${revenue}."
   elif user_query == "What are the total operating expenses?":
       operating_expenses = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Total Operating Expenses'].values[0]
       return f"The total operating expenses (in millions) for {company_entered} for the year {selected_year} is ${operating_expenses}"
   elif user_query == "What is the net income?":
       net_income = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Net Income'].values[0]
       return f"The net income (in millions) for {company_entered} for the year {selected_year} is ${net_income}"
   elif user_query == "What is the value of the total assets?":
       total_assets = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Total Assets'].values[0]
       return f"The value of the total assets (in millions) for {company_entered} for the year {selected_year} is ${total_assets}"
   elif user_query == "What is the value of the total liabilities?":
       total_liabilities = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Total Liabilities'].values[0]
       return f"The value of the total liabilities (in millions) for {company_entered} for the year {selected_year} is ${total_liabilities}"
   elif user_query == "What is the cash from operating activities?":
       cash_operating_activities = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Cash From Operating Activities'].values[0]
       return f"The cash from operating activities (in millions) for {company_entered} for the year {selected_year} is ${cash_operating_activities}"
   elif user_query == "What is the total revenue growth?":
       revenue_growth = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Revenue Growth (%)'].values[0].round(3)
       return f"The revenue growth (%) for {company_entered} for the year {selected_year} is {revenue_growth}"
   elif user_query == "What is the total operating expenses growth?":
       operating_expenses_growth = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Operating Expenses Growth (%)'].values[0].round(3)
       return f"The operating expenses growth (%) for {company_entered} for the year {selected_year} is {operating_expenses_growth}"
   elif user_query == "What is the total net income growth?":
       net_income_growth = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Net Income Growth (%)'].values[0].round(3)
       return f"The net income growth (%) for {company_entered} for the year {selected_year} is {net_income_growth}"
   elif user_query == "What is the total assets growth?":
       assets_growth = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Total Assets Growth (%)'].values[0].round(3)
       return f"The total assets growth (%) for {company_entered} for the year {selected_year} is {assets_growth}"
   elif user_query == "What is the total liabilities growth?":
       liabilities_growth = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Total Liabilities Growth (%)'].values[0].round(3)
       return f"The total liabilities growth (%) for {company_entered} for the year {selected_year} is {liabilities_growth}"
   elif user_query == "What is the total cash from operating activities growth?":
       cash_operating_activities_growth = data[(data['Year'] == selected_year) & (data['Company'] == company_entered)]['Operating Activities Cash Growth (%)'].values[0].round(3)
       return f"The total cash from operating activities growth (%) for {company_entered} for the year {selected_year} is {cash_operating_activities_growth}"
   else:
       return "Sorry, I can only provide information on predefined queries."
   



while(True):
    user_input = input("\nEnter 'start' to start the chatbot, 'exit' to quit : ")
    if user_input.lower() == 'exit':
        print("You are exiting the chatbot! Hope you had a pleasent experience.")
        break
    elif user_input.lower() == 'start':
        print("\nWelcome, This is the financial Chatbot")
        print("\nWhich company do you want to look at? ")
        print("Your options are: \n1. Apple \n2. Tesla \n3. Microsoft")
        company_entered = input("\nEnter a company name from the options above: ").lower()
        if(company_entered not in ["apple", "tesla", "microsoft"]):
            print("Invalid company name! please start again.")
            print("-------------------------------------------------------")
            continue
        else:
            print("\nChoose data from the following financial years: \n1. 2021 \n2. 2022 \n3. 2023")
            selected_year = int(input("Enter the financial year: "))
            if(selected_year not in [2021, 2022, 2023]):
                print("Enter a valid year! and start again.")
                print("-------------------------------------------------------")
                continue
            else:
                print("\n")
                user_query = input("Enter your query here: ")
                chatbot = simple_chatbot(user_query, company_entered, selected_year)
                print(chatbot)
                print("-------------------------------------------------------")
                continue
    else:
        print("\nEnter a valid input!")
        print("-------------------------------------------------------")
        continue
    