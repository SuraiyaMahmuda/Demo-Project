class CalculateSubstraction:
    """
    A class to represent basic mathematical operations.

    Attributes
    ----------
    num1 : float or int
        The first number
    num2 : float or int
        The second number

    Methods
    -------
    subtract():
        Subtracts num2 from num1 and returns the result.
    """
    
    def __init__(self, num1, num2):
        """
        Constructs all the necessary attributes for the Math object.

        Parameters
        ----------
        num1 : float or int
            The first number
        num2 : float or int
            The second number
        """
        self.num1 = num1
        self.num2 = num2
    
    def subtract(self):
        """
        Subtracts the second number (num2) from the first number (num1).

        Returns
        -------
        float or int
            The result of the subtraction (num1 - num2).
        """
        return self.num1 - self.num2

# Example usage:
math_obj = CalculateSubstraction(10, 5)
result = math_obj.subtract()
print(f"Subtraction result: {result}")
