# Programming Assignment Two

### Students

Hugo Liu - 46439406
Ethan Krol - 33541943

### Instructions to Run

Navigate to **comparison.py**. You may manually set the input_file, and output_file string variables to files with the appropriate format (see: **I/O Format**).

- If these are left blank, you will be prompted to type in these file locations on the command line.

### I/O Format

The input file must follow the following format:

```
k m
r1 r2 r3 ... rm
```

Where:

```
( k ) = cache capacity ( ( k >= 1 ) )

( m ) = number of requests

( r_1, .., r_m ) = sequence of integer IDs
```

The output file can be any plaintext writable file type (.txt, .out, etc), and will be overwritten with:

```
FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
```

### Extra Files

**writtencomponent.pdf** contains the written portion of the assignment.

**questionone.py** contains some helper code used to solve question 1, and can be disregarded.
