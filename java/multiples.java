import java.util.Scanner;

public class multiples {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		System.out.print("Enter your number");
		int N= input.nextInt();
		int i= 1; 
		while(i<=10) {
			System.out.println(N*i);
			i++;
			input.close();
		}
		
		
	}

}
