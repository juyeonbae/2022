#include<iostream>

int main(void){
	int x; //x=판매 금액, 기본 급여:50만원
	
	while(1){
		std::cout<<"판매 금액을 만원 단위로 입력(-1 to end):";
		std::cin>>x;
		if(x==-1){
			std::cout<<"프로그램을 종료합니다.";
			break;
		}
		else{
			std::cout<<"이번 달 급여: "<<50+x*0.12<<"만원"<<std::endl ;
		}
	} 
}
