//Java program to find sum of digits of digits of a number until sum becomes single digit.
import java.util.*;
public class SUM
{
  int sum=0;
  //Loop to do sum while 
  //sum is not less than
  //or else to 9
  while (n > 0 || sum >9)
  {
    if (n == 0)
    {
      n = sum;
      sum = 0;
    }
    sum  + =n%10;
    n /=10;
  }
  return sum;
}
//Driver code 
public static void main (string args[])
{
  int n=1234;
  system.out.println(digSum(n));
}
}
