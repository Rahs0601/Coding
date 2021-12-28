import java.util.Scanner;

public class calc {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		System.out.print("Enter first number");
		int X = input.nextInt();
		System.out.print("Enter 2nd number");
		int Y = input.nextInt();
		System.out.println(X+"+"+Y +"=" +(X+Y));
		System.out.println(X+"-"+Y + "="+(X-Y));
		System.out.println(X+"*"+Y +"=" +(X*Y));
		System.out.println(X+"/"+Y +"="+(X/Y));
		System.out.println(X+"%"+Y +"="+(X%Y));
	}

}
