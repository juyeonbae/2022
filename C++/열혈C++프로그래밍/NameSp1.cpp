#include<iostream>

namespace BestComImpl{
	void SimpleFunc(void){
		std::cout<<"BestCom�� ������ �Լ�"<<std::endl;
	}
} 

namespace ProgComImpl{
	void SimpleFunc(void){
		std::cout<<"ProgCom�� ������ �Լ�"<<std::endl;
	}
}
int main(void){
	BestComImpl::SimpleFunc(); 	//BestComImpl ���� ����� �Լ� ȣ�� ����  
	ProgComImpl::SimpleFunc();	//ProgComImpl ���� ����� �Լ� ȣ�� ����  
	return 0;
}

//������ :: = �������� ������(Scope Resolution Operator)
//�̸������� ������ �� ����ϴ� ������  
