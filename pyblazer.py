import os

class color():
    fg = "\33[38;5;"
    bg = "\33[48;5;"
    OkB = '\33[94m'
    OkG = '\33[1;92m'
    Fail = '\33[91m'
    End = '\33[0m'
    Blk = '\33[0;30m'
    Blk2 = '\33[1;30m'
    BlkB = '\33[40m'
    BlkU = '\33[4;30m'
    Blue = '\33[0;34m'
    Blue2 = '\33[2;34m'
    BlueB = '\33[44m'
    BlueU = '\33[4;34m'
    Cyan = '\33[0;96m'
    Cyan2 = '\33[1;96m'
    CyanI = '\33[3;96m'
    CyanB = '\33[46m'
    CyanU = '\33[4;96m'
    Grn = '\33[0;32m'
    Grn2 = '\33[1;32m'
    GrnB = '\33[42m'
    GrnU = '\33[4;32m'
    Purp = (fg + '55m')   # deep indigo
    Purp2 = (fg + '93m')  # medium purple
    PurpB = (fg + '129m') # magenta-purple
    PurpU = '\33[4;35m'
    Pink = '\33[0;95m'
    Pink2 = '\33[1;95m'
    PinkB = '\33[45m'
    PinkU = '\33[4;95m'
    Red = '\33[0;31m'
    Red2 = '\33[1;31m'
    RedB = '\33[41m'
    RedU = '\33[4;31m'
    Wht = '\33[0;37m'
    Wht2 = '\33[1;37m'
    WhtB = '\33[47m'
    WhtU = '\33[4;37m'
    Ylw = (fg + '3m')
    Aqua = (fg + '79m')
    Rose = (fg + '161m')
    
def obfuscate_file(input_file, output_file):
    """Obfuscate a Python file"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()

        obfuscated_chars = []
        fill_char = input("Enter obb character or string: ")  # e.g. '+'
        if not fill_char or len(fill_char) == 0:
            fill_char = "ۣ"
        for char in source_code:
            ascii_value = ord(char)
            obfuscated_chars.append(f"'{fill_char * ascii_value}'")
        # Create the obfuscated code template
        obfuscated_code = f'''# Python code obfuscated with PyBlazer by @BlazeK1ng420
BlazeWuzHere = [
    {',\n    '.join(obfuscated_chars)}
]
skrt = [chr(len(s)) for s in BlazeWuzHere]
exec(''.join(skrt))
'''
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        print(f"Obfuscated {input_file} -> {output_file}")
        print(f"Output file size: {os.path.getsize(output_file)} bytes")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
    except Exception as e:
        print(f"Error: {e}")

def deobfuscate_only(obfuscated_file):
    """Just show what's hidden without executing"""
    try:
        with open(obfuscated_file, 'r', encoding='utf-8') as f:
            content = f.read()
        # Find the BlazeWuzHere array
        if 'BlazeWuzHere = [' in content:
            # Extract the array content
            start_idx = content.find('BlazeWuzHere = [') + 5
            end_idx = content.find(']', start_idx)
            array_content = content[start_idx:end_idx]

            # Split into individual string elements
            elements = array_content.split(',')

            # Clean up each element
            elements = [elem.strip().strip("'") for elem in elements if elem.strip()]
            
            # Decode the characters
            decoded_chars = [chr(len(s)) for s in elements]
            decoded_code = ''.join(decoded_chars)

            print("Deobfuscated code preview (first 500 chars):")
            print("-" * 50)
            print(decoded_code[:500])
            if len(decoded_code) > 500:
                print("... (truncated)")
            print("-" * 50)
        else:
            print("Not an obfuscated file")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print(color.Grn + "=" * 50)
    print(color.Purp2 + "  PyBlazer   ||  Python Script Obfuscator  ||   by: @BlazeK1ng420")
    print(color.Grn + "=" * 50 + color.End)
    while True:
        print(color.Cyan)
        print("\nOptions:")
        print("1. Obfuscate a Python file")
        print("2. Preview obfuscated code")
        print("3. Exit")

        choice = input("\nSelect: ").strip()
        if choice == '1':
            input_file = input("Input Python file path: ").strip()
            if not input_file:
                print("No file specified.")
                continue
            if not os.path.exists(input_file):
                print(f"File '{input_file}' does not exist.")
                continue
            output_file = input("Output file path (Enter for blazed_input_file): ").strip()
            if not output_file:
                output_file = f"blazed_{input_file}"
            obfuscate_file(input_file, output_file)

        elif choice == '2':
            obfuscated_file = input("Enter obfuscated file path: ").strip()
            if not obfuscated_file:
                print("No file specified.")
                continue
            if not os.path.exists(obfuscated_file):
                print(f"File '{obfuscated_file}' does not exist.")
                continue
            deobfuscate_only(obfuscated_file)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
