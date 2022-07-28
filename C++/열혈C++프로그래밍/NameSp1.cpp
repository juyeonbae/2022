#include<iostream>

namespace BestComImpl{
	void SimpleFunc(void){
		std::cout<<"BestCom이 정의한 함수"<<std::endl;
	}
} 

namespace ProgComImpl{
	void SimpleFunc(void){
		std::cout<<"ProgCom이 정의한 함수"<<std::endl;
	}
}
int main(void){
	BestComImpl::SimpleFunc(); 	//BestComImpl 내에 저장된 함수 호출 문장  
	ProgComImpl::SimpleFunc();	//ProgComImpl 내에 저장된 함수 호출 문장  
	return 0;
}

//연산자 :: = 범위지정 연산자(Scope Resolution Operator)
//이름공간을 지정할 때 사용하는 연산자  
