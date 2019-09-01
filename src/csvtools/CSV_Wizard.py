import pandas as pd 
import numpy as np
import sys

# https://stackoverflow.com/a/52485322/5763413
# Allows me to catch ParserError
from pandas.io.parsers import ParserError

def openFile(fn, sep=",", header=0):
    '''
    Opens the requested file, if available. 

    Parameters:
        fn: a string holding a relative or absolute file path
        sep: optional, specifies separator 
            Default: comma
        header: optional, specifies which row contains headers. Default: 0
            Set  to None if no headers
    Returns:
        Tuple of DF and Error string
        If no errors: 
            (Dataframe, None) << Error string is empty
        If IO Error, File not found, or Parser error: 
            (None, ERR_STRING) << df set to None

    '''
    df = None 
    try:
        f = open(fn)
    except IOError:
        err_string = "IO Error occured\n"
        if __debug__:
            sys.stderr.write(err_string)
        return df, err_string

    except FileNotFoundError:
        err_string = "File Not Found\n"
        if __debug__:
            sys.stderr.write(err_string)
        return df, err_string

    else:
        with f:
            try:
                df = pd.read_csv(f)
            except ParserError:
                err_string = "Error in Parsing Data\n"
                if __debug__:
                    sys.stderr.write(err_string)
                df = None
                return df, err_string
            except(...):
                err_string = "Unknown Error Occured\n"
                if __debug__:
                    sys.stderr.write(err_string)
                df = None
            return df, None


