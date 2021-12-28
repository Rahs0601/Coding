import java.util.*;
public class Factorial {
	
	public static long fact(int n) {
		if (n==0 || n== 1)
			return 1;
		else 
			return fact(n-1)*n;		
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter number which you want to find factorial of:");
		int n = input.nextInt();
		System.out.print(fact(n));

	}

}
