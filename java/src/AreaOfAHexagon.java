import java.util.Scanner;
public class AreaOfAHexagon {

	public static void main(String[] args) {
		Scanner side  = new Scanner(System.in); 
		System.out.print("Enter the vaule of a side" );
		double s = side.nextDouble();
		double Area = (6*s*s)/(4*Math.tan(Math.PI/6));
		System.out.print(Area);
		
	}

}
