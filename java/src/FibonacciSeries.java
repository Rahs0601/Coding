import java.util.*;
public class FibonacciSeries {

	public static int fibo(int n) {
		if(n==1) 
			return 0;
		else if(n==2||n==3)
			return 1;
		else
			return fibo(n-1)+fibo(n-2);
	}
	public static void main(String[] args) {
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		System.out.print("Enter number");
		int n= input.nextInt(); 
		for(int i =1;i<=n;i++)
			System.out.println(fibo(i));
		
	}

}
