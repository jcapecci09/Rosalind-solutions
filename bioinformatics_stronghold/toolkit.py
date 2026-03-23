"""A toolkit containing fuctions that reoccur throughout each script

Author: Jimmy Capecci
"""

def output(out, arguments):
    """If output file is specefied writes to the file. If not 
    the function will  print to terminal

    :param out: What to write or print
    :param arguments: input arguments to check if  output file exists
    """

    # Write to output file 
    if arguments.output:
        with open(arguments.output, 'w') as f:
            f.write(out)
    
    # If it doesnt exist print to terminal
    else:
        print(out)