import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.sun.xml.internal.ws.addressing.v200408.ProblemAction;

public class link {
	public static void main(String[] args)
	{
		File bugFile = new java.io.File("bugfile");
		Scanner inputBugFile = null;
		try {
			inputBugFile = new Scanner(bugFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		HashSet<String> bugFileNameHashSet = new HashSet<String>();
		
		while(inputBugFile.hasNext()){
			String temp = inputBugFile.nextLine();
			bugFileNameHashSet.add(temp);
			//System.out.println(temp);
		}
		inputBugFile.close();
		
		//System.out.println(bugFileNameHashSet.contains("AdvancedQuickAssistProcessor.java"));
		
		File dataFile = new java.io.File("NoTag");
		Scanner inputData = null;
		try {
			inputData = new Scanner(dataFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		File outFile = new File("ProcessedData.csv");
		PrintWriter output = null;
		try {
			output = new PrintWriter(outFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}		
		
		Pattern pattern = Pattern.compile("(.*?).java");
		Matcher m = null; 
		
		int count = 0;
		
		while(inputData.hasNext()){
			String temp = inputData.nextLine();
			m = pattern.matcher(temp);
			
			if(m.find()){
				//
				if(bugFileNameHashSet.contains(m.group(1)+".java")){
					//System.out.println(m.group(1)+".java");
					temp = temp + ",true";
					//count ++;
					//System.out.println(count + temp);
				}
				else {
					temp = temp + ",false";
				}
			}
			output.println(temp);
		}
		output.close();
	}
}
