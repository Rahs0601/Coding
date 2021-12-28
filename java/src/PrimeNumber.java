import java.util.*;
public class PrimeNumber {
	
	public static void prime(int n) {
		int key =0;
		for(int i=2; i<n;i++) {
			if (n%i==0) {
				System.out.println("Not Prime");
				key =1;
				break;
			}
		}
		if (key == 0)
			System.out.print("Prime");
		
	}

	public static void main(String[] args) {
		Scanner rahs = new Scanner(System.in);
		System.out.print("Input a number");
		int n = rahs.nextInt();
		
		prime(n);
	}

}

