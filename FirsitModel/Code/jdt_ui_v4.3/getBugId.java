package test;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class getBugId 
{
	public static void main(String[] args) throws FileNotFoundException 
	{
		java.io.File infile = new java.io.File("input");
		Scanner input = new Scanner(infile);
		
		java.io.File outfile = new java.io.File("output");
		java.io.PrintWriter output = new java.io.PrintWriter(outfile);

		
		while (input.hasNext())
		{
			
			String line = input.nextLine().trim();
			if (line.indexOf("</bug_id>")>-1)
			{
				line = line.replaceAll("<bug_id>", "");
				line = line.replaceAll("</bug_id>", "");
				output.println(line);
			}
			
		}

		input.close();
		output.close();
		System.out.print("finished");
		
	}
}
