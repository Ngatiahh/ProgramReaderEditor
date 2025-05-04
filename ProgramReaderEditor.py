def process_file():
    print("File Processing Program")
    print("-----------------------")
    
    # Getting input filename from user:
    input_filename = input("Enter the name of the file to process: ")
    output_filename = "output_" + input_filename
    
    try:
        # Reading input file with error handling:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Processing the content (converting to uppercase):
        processed_content = content.upper()
        
        # Writting to output file:
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(processed_content)
            
            # Displaying the success message with statistics:
            word_count = len(content.split())
            line_count = len(content.splitlines())
            
            print("\nFile processed successfully!")
            print(f"Input file: {input_filename}")
            print(f"Output file: {output_filename}")
            print(f"Lines processed: {line_count}")
            print(f"Words processed: {word_count}")
            print(f"Characters processed: {len(content)}")
        
        except PermissionError:
            print(f"Error: Cannot write to {output_filename} (permission denied)")
        except Exception as e:
            print(f"Error writing to file: {str(e)}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Cannot read '{input_filename}' (permission denied).")
    except UnicodeDecodeError:
        print(f"Error: Cannot read '{input_filename}' (not a text file).")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Running the program:
if __name__ == "__main__":
    process_file()
