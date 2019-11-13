#include<stdio.h>

void gugudan(){
	int x=0,y=0;
	for(y=1;y<10;y++){
		for(x=1;x<10;x++)
			printf("%d x %d = %d\n",y,x,x*y);
	
		printf("============\n");
	}
}

void gugudanWhile(){
	int x=1,y=1;
	while(1){
		if(y>9){
			break;
		}

		printf("%d x %d = %d\n",y,x,x*y);
		x++;
		if(x>9){
			printf("============\n");
			x=1;
			y++;
		}
	}
}


void main(){

	gugudan();
	gugudanWhile();

}
