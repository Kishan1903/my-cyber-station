import os

def run_diagnostic():
    filename = "rockyou.txt"
    
    print("--- [ SYSTEM CHECK ] ---")
    
    # 1. Check if file exists
    if os.path.exists(filename):
        print(f" [+] SUCCESS: '{filename}' found.")
        
        # 2. Check File Size
        file_size_bytes = os.path.getsize(filename)
        file_size_mb = file_size_bytes / (1024 * 1024)
        print(f" [+] FILE SIZE: {file_size_mb:.2f} MB")
        
        if file_size_mb < 50:
            print(" [!] WARNING: Your rockyou.txt seems small. Did it download fully?")
        
        # 3. Test Reading (First 3 lines)
        try:
            with open(filename, "r", encoding="latin-1") as f:
                head = [next(f).strip() for _ in range(3)]
                print(f" [+] PREVIEW: First 3 passwords: {head}")
            print("--- [ STATUS: READY TO CRACK ] ---")
        except Exception as e:
            print(f" [-] READ ERROR: Could not read the file. {e}")
            
    else:
        print(f" [-] ERROR: '{filename}' NOT FOUND!")
        print(f" Make sure it is in: {os.getcwd()}")
        print("--- [ STATUS: SYSTEM FAILURE ] ---")

if __name__ == "__main__":
    run_diagnostic()