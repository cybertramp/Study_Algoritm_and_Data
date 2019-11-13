/*
*
*	What is this program?
*
*	Snail array program
*
*/
#define SIZE 7
#include<stdio.h>

void snail(){
	int x=-1,y=0,r;
	int arr[SIZE][SIZE];		// 5x5
	int t=SIZE;
	int num=1;
	int delta=1;

	while(1){
		for(r=0;r<t;r++){
			x = x+delta;
			arr[y][x] = num;
			num++;
		}

		t--;

		if(t < 0)
			break;

		for(r=0;r<t;r++){
			y = y+delta;
			arr[y][x] = num;
			num++;
		}

		delta = delta*-1;
	
	}
	
	// print array
	for(y=0;y<SIZE;y++){
		for(x=0;x<SIZE;x++){
			printf("%d\t",arr[y][x]);
		}
		printf("\n");
	}

}

void main(){
	snail();
}
