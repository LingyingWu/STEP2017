import java.io.FileNotFoundException;
import java.util.Scanner;

public class HazWordz {

	public static void main(String[] args) throws FileNotFoundException {

		// receive input
		Scanner sc = new Scanner(System.in);
		DictionaryNaive dict = new DictionaryNaive();

		while (true) {
			System.out.print("Please input the characters: ");
			String input = sc.next().toLowerCase();
			if (input.equals("quit"))
				break;

			String[] candidate = dict.searchDict(input).split(" ");

			System.out.println("Best result: " + findBest(candidate));
			System.out.println("Enter quit to exit the program.");
			System.out.println();
		}

		sc.close();
	}

	// find the word with the highest score in the candidate list
	public static String findBest(String[] list) {
		String best = "";
		int max = 0;
		for (int i = 0; i < list.length; i++) {
			int x = computeScore(list[i]);
			if (x > max) {
				best = list[i];
				max = x;
			}
		}
		return best;
	}

	// compute the final score
	public static int computeScore(String str) {
		int score = 0;
		char[] chars = str.toCharArray();
		for (int i = 0; i < chars.length; i++) {
			switch (chars[i]) {
			case 'a':
			case 'b':
			case 'd':
			case 'e':
			case 'g':
			case 'i':
			case 'n':
			case 'o':
			case 'r':
			case 's':
			case 't':
			case 'u':
				score += 1;
				break;
			case 'c':
			case 'f':
			case 'h':
			case 'l':
			case 'm':
			case 'p':
			case 'v':
			case 'w':
			case 'y':
				score += 2;
				break;
			case 'j':
			case 'k':
			case 'q':
			case 'x':
			case 'z':
				score += 3;
				break;
			}
		}

		return score;
	}
}
