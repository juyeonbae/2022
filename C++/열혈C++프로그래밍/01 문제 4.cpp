#include<iostream>

int main(void){
	int x; //x=�Ǹ� �ݾ�, �⺻ �޿�:50����
	
	while(1){
		std::cout<<"�Ǹ� �ݾ��� ���� ������ �Է�(-1 to end):";
		std::cin>>x;
		if(x==-1){
			std::cout<<"���α׷��� �����մϴ�.";
			break;
		}
		else{
			std::cout<<"�̹� �� �޿�: "<<50+x*0.12<<"����"<<std::endl ;
		}
	} 
}
