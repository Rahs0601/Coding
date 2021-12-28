import java.util.Scanner;
public class AverageOf3Numbers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		System.out.print("Enter 3 numbers");
		int x= input.nextInt();
		int y =input.nextInt();
		int z = input.nextInt();
		int Average = (x+y+z)/3;
		System.out.print("Average:"+Average);
		input.close();

	}

}
