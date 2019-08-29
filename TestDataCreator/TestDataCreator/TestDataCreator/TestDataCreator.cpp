//=======================================================
// This program generates three data files for testing
//  the statistical analyzer project.
// Author: Dr. Rick Coleman
// Date: January, 2009
//======================================================
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int main(void)
{
	fstream freqDataFile;
	fstream ordDataFile;
	fstream intDataFile;

	int expF, actF;
	int ans1, ans2, ans3, ans4, ans5;
	int preT, postT;
	double pcVal;
	time_t tSec;
	char line[128];

	// Create a frequency data test file
	//  Seven factors each with an expected frequency and actual frequency
	freqDataFile.open("FrequencyDataTest.csv", ios::out);
	if(!freqDataFile.is_open())
	{
		cout << "Failed to open frequency data output file.\n";
		cout << "Application terminating.\n";
		return 0;
	}
	time(&tSec);
	srand((unsigned int)tSec);
	strcpy(line, "Sample #, Expected Freq., Actual Freq.\n");
	freqDataFile.write(line, (long)strlen(line));
	for(int fVals = 0; fVals < 7; fVals++)
	{
		expF = rand() % 500;
		if((rand() % 2) == 0)
			actF = expF + (expF / ((rand() % 10) + 1)) ; // Add 1 to 10%
		else
			actF = expF - (expF / ((rand() % 10) + 1)); // Subtract 1 to 10%
		// Write a line to the file
		sprintf(line, "Sample %d, %d, %d\n", (fVals + 1), expF, actF);
		freqDataFile.write(line, (long)strlen(line));
	}
	freqDataFile.close();


	// Create an ordinal data test file
	//  50 questions each with answers
	//     1=Strongly disagree   (0 to 15%)
	//     2=Disagree            (10% to 35%)
	//     3=Neutral             (All others)
	//     4=Agree               (10% to 35%)
	//     5=Strongly agree      (0 to 15%)
	// Sample gives number of responses from 100 responders
	ordDataFile.open("OrginalDataTest.csv", ios::out);
	if(!ordDataFile.is_open())
	{
		cout << "Failed to open ordinal data output file.\n";
		cout << "Application terminating.\n";
		return 0;
	}
	time(&tSec);
	srand((unsigned int)tSec);
	strcpy(line, "Question #, SD, D, N, A, SA\n");
	ordDataFile.write(line, (long)strlen(line));
	for(int oVals = 0; oVals < 50; oVals++)
	{
		ans1 = rand() % 15;
		ans2 = rand() % 35;
		ans4 = rand() % 35;
		ans5 = rand() % 15;
		ans3 = 100 - (ans1 + ans2 + ans4 + ans5); 
		// Write a line to the file
		sprintf(line, "Question %d, %d, %d, %d, %d, %d\n", 
			(oVals+1), ans1, ans2, ans3, ans4, ans5);
		ordDataFile.write(line, (long)strlen(line));
	}
	ordDataFile.close();

	// Create an interval data test file
	intDataFile.open("IntervalDataTest.csv", ios::out);
	if(!intDataFile.is_open())
	{
		cout << "Failed to open interval data output file.\n";
		cout << "Application terminating.\n";
		return 0;
	}
	strcpy(line, "Subject ID, Pretest, Posttest\n");
	intDataFile.write(line, (long)strlen(line));
	for(int iVals = 0; iVals < 100; iVals++)
	{
		preT = rand() % 100;
		pcVal = (((rand() % 10) + 1.0)) / 100.0;
		postT = preT + (int)((double)preT * pcVal) ; // Add 1 to 10%
		if(postT < 50)
		{
			preT += 50;
			postT += 50;
		}
		if(postT > 100)
		{
			preT -= 25;
			postT -= 25;
		}
		// Write a line to the file
		sprintf(line, "Subject%03d, %d, %d\n", iVals, preT, postT);
		intDataFile.write(line, (long)strlen(line));
	}
	intDataFile.close();

	return 0;
}