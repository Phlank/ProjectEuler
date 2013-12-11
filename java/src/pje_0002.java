public class pje_0002 {
	public static void main(String[] args) {
		long a = 1, b = 2, c = 3, sum = 2;
		while (c < 4000000l) {
			a = b;
			b = c;
			c = a+b;
			if (c%2 == 0)
				sum += c;
		}
		System.out.println(sum);
	}
}