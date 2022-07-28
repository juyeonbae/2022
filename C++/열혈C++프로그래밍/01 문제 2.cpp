#include<iostream>

int main(void){
	char name[100];
	char Pnum[100];
	
	std::cout<<"Your name:";
	std::cin>>name;
	std::cout<<"Your Phone Number:";
	std::cin>>Pnum;
	
	std::cout<<"My name is "<<name<<".\n";
	std::cout<<"My phone number is "<<Pnum<<"."; 
}
