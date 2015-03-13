package test;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class getfiles 
{
	public static void main(String[] args) throws FileNotFoundException 
	{
		java.io.File infile = new java.io.File("bugid_files");
		Scanner input = new Scanner(infile);
		
		java.io.File outfile = new java.io.File("files");
		java.io.PrintWriter output = new java.io.PrintWriter(outfile);

		
		while (input.hasNext())
		{
			String line = input.nextLine().trim();
			if (line.indexOf(".java")>-1)
			{
				int m = line.lastIndexOf("/");
				int n = line.lastIndexOf("|");
				if (n==-1)
					n = line.length();
				line = line.substring(m+1,n);
				output.println(line);
			}
			
		}
		
		
		
		
		
		
		input.close();
		output.close();
		System.out.print("finished");
		
	}

}
