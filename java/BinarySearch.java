import java.util.*;
public class BinarySearch {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the length of array");
		int n = input.nextInt();
		int[] list = new int[n];
		System.out.println("Enter the array");
		for(int i = 0 ; i<n;i++)
			list[i] = input.nextInt();
		System.out.println("Enter the key");
		//int key= input.nextInt() ;
		int low  = 0 , up = list.length-1;
		input.close();
		while(low <= up) {
			int key= input.nextInt() ;
			int mid = (low+up)/2;
			if (list[mid] == key) {
				int pos = mid;
				System.out.println("Found at"+ (pos+1));
				
			}
			else {
				if( list[mid]<=key)
					low  = mid +1;
				else 
					up = mid -1;
			}
			
		}
		if(low >up) {
			System.out.print("not found");
		}
			
		
		

	}

}
