# The purpose of this script is to organize Pentesting scans in a new Case directory and organizing scan results
# Get IP address / IP range from the users for scanning
# Create a folder to save scan results for the given IP
# Save the scanresults in a Case_directory/toolname.txt : ----> <ScanningToolName + IP_address>/toolname.txt
# Easy Case Builder Script v1.0 by Serkan
import os

print()
print("\t\tEasy Case Builder Tool v1.0")
print("* "*30)
# Get IP address/IP range to scan from the user input.
ip_address = input("Which IP address would you like to scan: ")

# Selecting the scanning tool to initialize;

def main():
    print() #print a blank line at start
    print("\t\tScanning Tool Selection")
    print("-"*60)
    print("\t1. Whois Scan\t\t2. Nmap Scan\n\t3. Nikto Scan\t\t4. SSLscan")
    print("-"*60)
  # Get the users tool selection   
    tool_selection = input("Select the tool you want use: ")
    if tool_selection == "1":
        whois()
    elif tool_selection == "2":
        nmap()
    elif tool_selection == "3":
        nikto()
    elif tool_selection == "4":
        sslscan()
    else:
        print("! @ "*17)
        print("Nice Try...!!! but the only available tool selections are 1-2-3-4")

# Check If the Case Directory Exists, If Not, Create It;
def case():
    case_dir = (f"Case_{ip_address}")
    check_dir = os.path.isdir(case_dir)
    if not check_dir:
        os.mkdir(f"Case_{ip_address}")
    else:
        pass

# whois scan        
def whois():
    print(f"initializing whois scan for {ip_address}")
    print()
    os.system(f"whois {ip_address} > Case_{ip_address}/whois.txt")
    print(f"whois scan result for {ip_address} is succesfully saved as whois.txt file.")
# nmap scan
def nmap():
    print(f"initializing nmap scan for {ip_address}")
    os.system(f"nmap -sV -sC -A {ip_address} -oN Case_{ip_address}/nmapscan.txt")
    print(f"nmap scan result for {ip_address} is succesfully saved as nmapscan.txt file.")
# nikto scan
def nikto():
    print(f"initializing nikto scan for {ip_address}")
    print()
    os.system(f"nikto -h {ip_address} > Case_{ip_address}/niktoscan.txt")
    print(f"nikto scan result for {ip_address} is succesfully saved as niktoscan.txt")
# ssl scan
def sslscan():
    print(f"initializing sslscan for {ip_address}")
    os.system(f"sslscan {ip_address} > Case_{ip_address}/sslscan.txt")
    print(f"sslscan result for {ip_address} is succesfully saved as sslscan.txt")

# Best practice python naming convention
if __name__ == "__main__":
    case()
    main()
