#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <Windows.h>

#include "Fall.h"

using std::endl;

int main(){
	//Variable declarations
	const int MAX_SIZE = 100;
	int board_size;
	std::string convText; //Text used to convert string into int
	std::stringstream stream; //String stream used to convert string into int

	//Opening the input file
	std::ifstream fileIn;
	fileIn.open("Input.txt");
	if (!(fileIn)){
		std::cout << "Fileure" << endl;
		return -1;
	}

	
	//Taking input from file and converting it into int
	std::getline(fileIn, convText);
	stream << convText;
	if (!(stream >> board_size)){
		std::cout << "Failure" << endl;
		return -1;
	}
	
	//Creating the board
	std::string board[MAX_SIZE];
	//Inputting the board
	for (int i = 0; i < board_size; i++){
		std::getline(fileIn, board[i]);
	}

	//Main solving and displaying loop
	while (solveForNext(board, board_size)){
		Sleep(250);
		system("cls");
		printBoard(board, board_size);

	}
	
	

	system("pause");

	return 0;
}