import yfinance as yf
import pandas as pd


def registration(email, password,filename = "users.csv"):
   
       with open(filename,mode="a") as file:
        file.write(f"{email},{password}\n")
        return "Registered."
  
        

def authenticate(email, password, filename="users.csv"):
    try:
        with open(filename, mode="r") as file:
            for line in file:
                if not line.strip():
                    continue
    
                parts = line.strip().split(",")
                if len(parts) != 2:
                    print(f"Skipping malformed line: {line.strip()}")  # Debugging message
                    continue
                
                stored_email, stored_password = parts
                if email == stored_email and password == stored_password:
                    return True
        return False  # No match found
    except FileNotFoundError:
        return "User database not found. Please register first."
    except Exception as e:
        return f"An error occurred during authentication: {e}"

    
def get_closing_prices(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data["Close"]

def analyze_closing_prices(data):
    avg_price = data.mean()
    pct_change = ((data[-1] - data[0]) / data[0]) * 100
    highest = data.max()
    lowest = data.min()
    return {
        "average_price": avg_price,
        "percentage_change": pct_change,
        "highest_price": highest,
        "lowest_price": lowest,
    }

def save_to_csv(data,filename="users.csv"):
    df=pd.DataFrame([data])
    try:
        with open(filename, mode="r"):
            df.to_csv(filename, mode="a",header=False, index=False)
    except FileNotFoundError:
        df.to_csv(filename, index=False)

def read_from_csv(filename="users.csv"):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError("Invalid")
    
def clean_csv(filename="users.csv"):
    cleaned_lines = []
    try:
        with open(filename, mode="r") as file:
            for line in file:
                parts = line.strip().split(",")
                # Keep only lines with exactly two values
                if len(parts) == 2:
                    cleaned_lines.append(line.strip())
        
        # Rewrite the cleaned lines back to the file
        with open(filename, mode="w") as file:
            for line in cleaned_lines:
                file.write(line + "\n")
        print("CSV file cleaned successfully.")
    except FileNotFoundError:
        print("CSV file not found.")

    
    