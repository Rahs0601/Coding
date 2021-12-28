import java.util.*;
public class DistanceBetweentwoPointsOnSurafceOfEarth {

	public static void main(String[] args) {
		final double radius = 6371.01;
		Scanner input = new Scanner(System.in);
		System.out.println("Input the latitude of coordinate 1");
		double x1 = input.nextDouble();
		x1 = Math.toRadians(x1);
		System.out.println("Input the longitude of coordinate 1");
		double y1 = input.nextDouble();
		y1 = Math.toRadians(y1);
		System.out.println("Input the latitude of coordinate 2");
		double x2 = input.nextDouble();
		x2 = Math.toRadians(x2);
		System.out.println("Input the longitude of coordinate 2");
		double y2 = input.nextDouble();
		y2 = Math.toRadians(y2);
		double distance = radius * Math.acos(Math.sin(x1) * Math.sin(x2) + Math.cos(x1) * Math.cos(x2) * Math.cos(y1 - y2));
		System.out.println(distance);
	}

}
