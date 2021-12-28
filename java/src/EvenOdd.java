import java.util.*;
public class EvenOdd {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Input a number");
		int num = input.nextInt();
		if(num %2 ==0) {
			System.out.print("1");
		}
		else {
			System.out.print("0");
		}
		
	}

}
