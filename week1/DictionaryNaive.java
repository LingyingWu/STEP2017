import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

public class DictionaryNaive {

	private Map<String, String> dictionary = new TreeMap<String, String>();
	private Set<String> combination = new HashSet<String>();

	public DictionaryNaive() throws FileNotFoundException {
		createDict();
	}

	// create a dictionary
	// the keys are the sorted strings of each word
	// put the words with same anagram under the same key
	public void createDict() throws FileNotFoundException {
		File file = new File("dictionary.words.txt");
		Scanner sc = new Scanner(file);
		while (sc.hasNextLine()) {
			String word = sc.nextLine();
			String key = sortString(word);
			if (dictionary.containsKey(key))
				dictionary.put(key, dictionary.get(key) + " " + word);
			else
				dictionary.put(key, word);
		}
		sc.close();
	}

	// search for the words having the same anagram with the combinations of the
	// input characters in the dictionary
	public String searchDict(String input) {
		String result = "";
		generateCombination(sortString(input), new StringBuffer(), 0);
		for (String str : combination) {
			if (dictionary.containsKey(str))
				result += dictionary.get(str) + " ";
		}
		combination.clear();
		return result;
	}

	// generate all possible combinations of the input characters
	public void generateCombination(String str, StringBuffer output, int index) {
		for (int i = index; i < str.length(); i++) {
			output.append(str.charAt(i));
			combination.add(output.toString());
			generateCombination(str, output, i + 1);
			output.deleteCharAt(output.length() - 1);
		}
	}

	// sort the characters in a given string
	public static String sortString(String s) {
		char[] chars = s.toCharArray();
		Arrays.sort(chars);
		return new String(chars);
	}
}
