#include<iostream>
using namespace std;

inline int SQUARE(int x){
	return x*x;
}

//매크로 함수는 정의하기가 복잡하니, 일반 함수처럼 정의가 가능하면 좋겠다!
// >> C++에서 만족 
 
int main(void){
	cout<<SQUARE(5)<<endl;
	cout<<SQUARE(12)<<endl;
	return 0;
}

//매크로를 이용한 함수의 인라인화는 전처리기에 의해서 처리
//키워드 inline을 이용한 함수의 인라인화는 컴파일러에 의해서 처리
//따라서 컴파일러는 함수의 인라인화가 오히려 성능에 해가 된다고 판단할 경우, 키워드를 무시하기도 한다. 
//또한 컴파일러는 필요한 경우, 일부 함수를 임의로 인라인 처리하기도 한다.  

//매크로 함수가 정의되면, 함수호출 문장은 자료형에 의존적이지 않다.
// ex) #define SQIARE(x) ((x)*(x))
// 	   std::cout<<SQUARE(12); std::cout<<SQUARE(3.15) double형 함수 호출 

//인라인 함수로 정의하면, 자료형에 의해 데이터 손실이 발생할 수 있음.
// ex) inline int SQUARE(int x) {return x*x;} \n std::cout<<SQUARE(3.15); 0.15 손실

//C++의 템플릿을 이용하여 매크로 함수와 마찬가지로 자료형에 의존적이지 않은 함수를 완성할 수 있음.
 
