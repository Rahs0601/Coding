
public class Divby35andBoth {

	public static void main(String[] args) {
		int n=1;
		while(n<100) {
			if(n%3 == 0) 
				System.out.println("div by 3 "+n);
			if (n%5 == 0)
				System.out.println("div by 5 "+n);
			if(n%3 == 0 && n%5==0)
				System.out.println("div by both "+n);
			n++;
	}
		System.out.println("\nDivided by 3: ");		
		for (int i=1; i<100; i++) {
			if (i%3==0) 
			System.out.print(i +", ");			
		}			
				
		System.out.println("\n\nDivided by 5: ");
		for (int i=1; i<100; i++) {
			if (i%5==0) System.out.print(i +", ");			
		}
				
		System.out.println("\n\nDivided by 3 & 5: ");			
		for (int i=1; i<100; i++) {
			if (i%3==0 && i%5==0) System.out.print(i +", ");			
		}
		System.out.println("\n");

}
}