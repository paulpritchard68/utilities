/* Interactive REXX using the INTERPRET interuction */
Input = "SAY 'Enter a REXX instruction or type EXIT to exit'"
DO FOREVER
    INTERPRET Input
    Pull Input
    IF INPUT = "EXIT" then EXIT 0
    END
