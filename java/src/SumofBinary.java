
public class SumofBinary {


	public static void main(String[] args) {
		int x = 10 , y = 01 , r = 0 ,i = 0;
		int[] sum = {} ;
		while(x!=0 || y!=0) {
			sum[i++]= ((x%10 + y%10+ r)%2);
			r = ((x%10 +y%10+r)/2);
			x = x/10;
			y = y/10;
		}
		if (r !=0) {
			sum[i++]= r;
		}
		--i;
		System.out.print("Sum of two binary numbers:");
		while(i>=0) {
			System.out.print(sum[i--]);
		}
		System.out.print("\n");
	}

}
