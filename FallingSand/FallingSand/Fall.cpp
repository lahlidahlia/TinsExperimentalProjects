#include <iostream>
#include <string>
#include "Fall.h"

void printBoard(std::string board[], int size){
	for (int i = 0; i < size; i++){
		std::cout << board[i] << std::endl;
	}
}
void fall(std::string board[], int x, int y){
	/*Makes the object at given position fall*/
	char object = board[y][x];
	char objectUnderneath = board[y + 1][x];
	
	board[y][x] = objectUnderneath; //Replaces the given object w/ the one underneath it
	board[y + 1][x] = object;
}
bool solveForNext(std::string board[], int size){
	/*Returns whether a move was made*/
	bool isMoveMade = false;
	for (int y = size - 1; y >= 0; y--){
		for (int x = 0; x < size; x++){
			if (board[y][x] == '.'){	//Checking for sand
				if (y == size - 1){ //If on last row
					continue;
				}

				char objectUnderneath = board[y + 1][x]; 
				if (objectUnderneath == ' '){ //If there is empty space underneath
					//Move sand down
					fall(board, x, y);
					isMoveMade = true;
					continue;
				}
				else if (objectUnderneath == '#'){ //If there is stone
					continue;
				}
			}
		}
	}
	return isMoveMade;
}