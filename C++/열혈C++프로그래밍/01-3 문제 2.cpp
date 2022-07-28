//문제 01-3 [매개변수의 디폴트 값] 
//Q. 다음과 같은 형태로의 함수 오버로딩은 문제가 있다. 어떠한 문제가 있는지 설명해보자.  

#include<iostream>
using namespace std;

int SimpleFunc(int a=10){
	return a+1;
}

int SimpleFunc(void){
	return 10;
}

//A. 함수 오버로딩의 조건을 만족해서 컴파일은 된다.
// 그러나 인자를 전달하지 않으면서 함수를 호출하는 경우,
//두 함수 모두 호출조건을 만족하기 때문에 컴파일 에러가 발생한다. 
//ex) SimpleFunc() 경우 컴파일 에러 발생 	
