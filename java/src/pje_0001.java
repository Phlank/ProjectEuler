public class pje_0001 {
	public static void main(String[] args) {
		int output = 0;
		for (int i = 3; i < 1000; i++) {
			if (i%3 == 0 || i%5 == 0)
				output += i;
		}
		System.out.println(output);
	}
}