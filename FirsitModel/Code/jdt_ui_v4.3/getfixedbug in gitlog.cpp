#include <iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
	ifstream infile1("bugid");
	
	
	ofstream outfile("output");
	string id;
	string line;
	while (getline(infile1, id))
	{
		ifstream infile2("gitlog");
		while (getline(infile2, line))
		{
			bool find = false;
			if (line.find(id) != string::npos)
			{
				find = true;
				outfile << id << endl;
				while (getline(infile2, line))
				{
					if (line.find(".java") != string::npos)
						outfile << line << endl;
					else if (line.find("commit") != string::npos)
					{
						outfile << endl;
						break;
					}
						
				}
			}
			if (find)
				break;
		}
		infile2.close();

	}
	infile1.close();
	outfile.close();
}