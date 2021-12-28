import java.util.*;
public class AreaOfAPolygon {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the number of sides of the polygon");
		int n = input.nextInt();
		System.out.println("Enter the length of the side");
		double s = input.nextDouble();
		double area = (n*s*s)/(4*Math.tan(Math.PI/n));
		System.out.print("area :"+area);
	}

}
