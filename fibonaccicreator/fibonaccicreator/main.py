"""Perform an experiment to study efficiency of Fibonacci algorithms."""

from pyinstrument import Profiler  # type: ignore

import typer

from rich.console import Console

import os
import psutil  # type: ignore
import time

# TODO: Note that certain versions of Windows may not be able to
# correctly use these modules in the resource package. If you are
# running Windows and cannot get this to work, please talk with the
# course instructor about an alternative arrangement. With that said,
# this import and the use of its modules in this program should normally
# work correctly on both the MacOS and Linux operating systems.
if os.name != "nt":
    from resource import getrusage, RUSAGE_SELF

from fibonaccicreator import fibonacci

FIBONACCI_FUNCTION_BASE = "fibonacci"
UNDERSCORE = "_"


# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a Profiler object to support timing program code segments
profiler = Profiler()

def format_bytes(size_of_memory_used) -> str:
    """Formats the size_of_memory_used into a string representing the value in bytes in a human-readable fashion."""
    # TODO: Certain versions of MacOS do not support the calculation
    # of human-readable memory in bytes in a standard fashion. As such,
    # you may need to uncomment one or more lines of source code in this
    # function if you notice that the program is reporting that it is
    # using either kilo-bytes (KB) or giga-bytes (GB) of memory. In
    # particular, using only a few KB of memory would probably be too little
    # and using many GB of memory would probably be too much!
    # Reference:
    # https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778
    power = 2 ** 10
    n = 0
    # power_labels = {0: "", 1: "", 2: "kilo", 3: "mega", 4: "giga"}
    # power_labels = {0: "kilo", 1: "mega", 2: "giga", 3: "tera", 4: "peta"}
    power_labels = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}
    while size_of_memory_used > power:
        size_of_memory_used /= power
        n += 1
    return str(size_of_memory_used) + " " + power_labels[n] + "bytes"


@cli.command()
def fibonaccicreator(
    approach: str = typer.Option(...),
    number: int = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
    pyinstrument: bool = typer.Option(False, "--pyinstrument"),
):
    """Create the list of Fibonacci values in a specified approach."""
    # TODO: make sure that you understand all the steps in this function
    # create a console for rich text output
    console = Console()
    # display the debugging output for the program's command-line arguments
    console.print("")
    console.print(f":luggage: Awesome, the chosen type of approach is the {approach}!")
    console.print("")
    console.print(
        f":abacus: The program will compute up to the {number}th Fibonacci number!"
    )
    console.print("")
    # construct the full name of the function to call
    function = FIBONACCI_FUNCTION_BASE + UNDERSCORE + approach
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = getattr(fibonacci, function)
    # call the constructed function and capture the result
    profiler.start()
    start = time.time()
    fibonacci_result = function_to_call(number)
    end = time.time()
    profiler.stop()
    # display debugging information with the function's output
    if display:
        console.print(f":sparkles: This is the output from the {approach} function:")
        console.print()
        # display the output from the computation
        console.print(str(fibonacci_result))
        console.print()
    # display a final message and some extra spacing, asking a question
    # about the efficiency of the approach to computing the number sequence
    console.print(
        "🤷 So, was this an efficient approach for storing the Fibonacci sequence?"
    )
    console.print("")
    process = psutil.Process(os.getpid())
    # display the estimated overall memory use as reported by the operating system
    # Reference:
    # https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    console.print("Estimated overall memory according to the operating system:")
    console.print("   " + format_bytes(process.memory_info().vms))
    console.print("")
    # display the estimated peak memory use as reported by the operating system
    # Reference:
    # https://pythonspeed.com/articles/estimating-memory-usage/
    console.print("Estimated peak memory according to the operating system:")
    # TODO: you may need to adjust this function call in the print
    # statement depending on your operating system. This should produce
    # the correct output value for Linux. However, you may need to
    # adjust the value of 1024 to be larger or smaller, depending on
    # your operating system and the way in which it reports memory use.
    # https://pythonspeed.com/articles/estimating-memory-usage/
    # https://stackoverflow.com/questions/12050913/whats-the-unit-of-ru-maxrss-on-linux
    if os.name != "nt":
        console.print("   " + format_bytes(getrusage(RUSAGE_SELF).ru_maxrss * 1024))
    else:
        console.print("   " + format_bytes(psutil.Process().memory_info().peak_wset))
    console.print()
    # display a simplified execution time
    # Reference:
    # https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
    console.print("Estimated execution time according to the simple timer:")
    console.print(f"    {(end - start):.5f} seconds")
    # display the execution time recorded by the pyinstrument package
    # Reference:
    # https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-a-specific-chunk-of-code
    if pyinstrument:
        console.print()
        console.print(
            ":bookmark: Estimated execution time according to pyinstrument displayed in your browser!"
        )
        profiler.open_in_browser()
