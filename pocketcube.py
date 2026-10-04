"""
PocketCube Class
Partially implemented virtual 2x2 Rubik's Cube (Pocket Cube) in Python.

To use this class:

    from pocketcube import PocketCube

    twobytwo = PocketCube()     # Declare an instance with default solved state
    twobytwo.print_cube()       # Print visual grid layout of the cube
    twobytwo.make_move('U')     # Perform a U move
    twobytwo.make_move('S')     # Perform an R' move
    twobytwo.make_move('r')     # Perform an R' move
    twobytwo.print_cube()       # Print the updated visual grid
    twobytwo.print_state()      # Print the raw cube state tuple

print_cube(), print_state(), and make_move(move) are the primary public methods.
Individual face turns are handled by internal methods.

Supported move arguments for make_move():

    Arg        Result
    -------------------------------------------
    'U'        U clockwise
    'u' / 'V'  U counterclockwise (U prime)
    'R'        R clockwise
    'r' / 'S'  R counterclockwise (R prime)
    'F'        F clockwise
    'f' / 'G'  F counterclockwise (F prime)

Moves such as D, D', L, L', U2, D2, R2, L2, F2, B2, x, y, and z are not implemented.

The cube state is represented as a 24-element tuple of integers (0 through 5):
    0 = White  (Up)
    1 = Green  (Left)
    2 = Red    (Front)
    3 = Blue   (Right)
    4 = Orange (Back)
    5 = Yellow (Down)

Layout and tuple subscripts:

            Sticker Numbers                         Tuple Subscripts

            0   0                                   00  01
             Up                                       Up
            0   0                                   02  03

    1   1   2   2   3   3   4   4           04  05  06  07  08  09  10  11
    Left    Front   Right   Back             Left   Front   Right    Back
    1   1   2   2   3   3   4   4           12  13  14  15  16  17  18  19

            5   5                                   20  21
            Down                                     Down
            5   5                                   22  23

Based on the original C++ implementation by tim@tim.id.au
http://tim.id.au/limejuice/generating-the-full-list-of-valid-states-of-a-2x2-rubiks-cube/
"""

COLOR_MAP = {0: "W", 1: "G", 2: "R", 3: "B", 4: "O", 5: "Y"}


class PocketCube:
    DEFAULT_STATE = (
        0, 0, 0, 0,  # Up (W)
        1, 1, 2, 2, 3, 3, 4, 4,  # Upper ring (G, R, B, O)
        1, 1, 2, 2, 3, 3, 4, 4,  # Lower ring (G, R, B, O)
        5, 5, 5, 5,  # Down (Y)
    )

    def __init__(self, initial_state: tuple[int, ...] = DEFAULT_STATE):
        self.state: tuple[int, ...] = initial_state

    def make_move(self, move: str) -> bool:
        """Performs a quarter turn based on input character.
        Returns True if the move is valid, False otherwise.
        """
        match move:
            case "U":
                self._turn_U()
                return True
            case "V" | "u":
                self._turn_Uprime()
                return True
            case "R":
                self._turn_R()
                return True
            case "S" | "r":
                self._turn_Rprime()
                return True
            case "F":
                self._turn_F()
                return True
            case "G" | "f":
                self._turn_Fprime()
                return True
            case _:
                return False

    def print_cube(self) -> None:
        """Prints out the cube's state in a visual grid format using color characters."""
        s = [COLOR_MAP[val] for val in self.state]
        print(f"Current cube state: {''.join(s)}")
        print(f"       {s[0]} {s[1]}")
        print(f"       {s[2]} {s[3]}")
        print(
            f"  {s[4]} {s[5]}  {s[6]} {s[7]}  {s[8]} {s[9]}  {s[10]} {s[11]}"
        )
        print(
            f"  {s[12]} {s[13]}  {s[14]} {s[15]}  {s[16]} {s[17]}  {s[18]} {s[19]}"
        )
        print(f"       {s[20]} {s[21]}")
        print(f"       {s[22]} {s[23]}")

    def print_state(self) -> None:
        """Prints out the raw cube state tuple of numbers."""
        print(self.state)

    # --- Private Helper Turn Methods ---

    def _turn_U(self) -> None:
        s = list(self.state)
        s[1], s[3], s[2], s[0] = self.state[0], self.state[1], self.state[3], self.state[2]
        s[9], s[8], s[7], s[6] = self.state[11], self.state[10], self.state[9], self.state[8]
        s[5], s[4], s[11], s[10] = self.state[7], self.state[6], self.state[5], self.state[4]
        self.state = tuple(s)

    def _turn_Uprime(self) -> None:
        s = list(self.state)
        s[0], s[1], s[3], s[2] = self.state[1], self.state[3], self.state[2], self.state[0]
        s[11], s[10], s[9], s[8] = self.state[9], self.state[8], self.state[7], self.state[6]
        s[7], s[6], s[5], s[4] = self.state[5], self.state[4], self.state[11], self.state[10]
        self.state = tuple(s)

    def _turn_R(self) -> None:
        s = list(self.state)
        s[9], s[17], s[16], s[8] = self.state[8], self.state[9], self.state[17], self.state[16]
        s[10], s[18], s[23], s[21] = self.state[3], self.state[1], self.state[10], self.state[18]
        s[15], s[7], s[3], s[1] = self.state[23], self.state[21], self.state[15], self.state[7]
        self.state = tuple(s)

    def _turn_Rprime(self) -> None:
        s = list(self.state)
        s[8], s[9], s[17], s[16] = self.state[9], self.state[17], self.state[16], self.state[8]
        s[3], s[1], s[10], s[18] = self.state[10], self.state[18], self.state[23], self.state[21]
        s[23], s[21], s[15], s[7] = self.state[15], self.state[7], self.state[3], self.state[1]
        self.state = tuple(s)

    def _turn_F(self) -> None:
        s = list(self.state)
        s[7], s[15], s[14], s[6] = self.state[6], self.state[7], self.state[15], self.state[14]
        s[8], s[16], s[21], s[20] = self.state[2], self.state[3], self.state[8], self.state[16]
        s[13], s[5], s[2], s[3] = self.state[21], self.state[20], self.state[13], self.state[5]
        self.state = tuple(s)

    def _turn_Fprime(self) -> None:
        s = list(self.state)
        s[6], s[7], s[15], s[14] = self.state[7], self.state[15], self.state[14], self.state[6]
        s[2], s[3], s[8], s[16] = self.state[8], self.state[16], self.state[21], self.state[20]
        s[21], s[20], s[13], s[5] = self.state[13], self.state[5], self.state[2], self.state[3]
        self.state = tuple(s)


if __name__ == "__main__": # testing
    twobytwo = PocketCube()
    twobytwo.print_cube()
    twobytwo.make_move("U")
    twobytwo.make_move("S")
    twobytwo.make_move("r")
    twobytwo.print_cube()
    twobytwo.print_state()