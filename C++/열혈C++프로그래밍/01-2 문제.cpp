#include<iostream>
using namespace std;

void swap(int *num1, int *num2){
	int temp;
	temp = *num1; 		//temp에 &num1 주소값을 가리키는 *num1 포인터 값 임시 저장 
	*num1 = *num2;		//*num2 포인터가 가리키는 주소값을 *num1 포인터가 가리키는 주소에 값 저장  
	*num2 = temp;		//포인터 개념 공부 필요  
} 
void swap(char *ch1, char *ch2){
	char temp;
	temp = *ch1;
	*ch1 = *ch2;
	*ch2 = temp;
}
void swap(double *dbl1, double *dbl2){
	double temp;
	temp = *dbl1;
	*dbl1 = *dbl2;
	*dbl2 = temp;
}

int main(void){
	int num1 = 20, num2 = 30;
	swap(&num1,&num2);
	cout<<num1<<' '<<num2<<endl;
	
	char ch1='A', ch2='Z';
	swap(&ch1,&ch2);
	cout<<ch1<<' '<<ch2<<endl;
	
	double dbl1=1.111, dbl2=5.555;
	swap(&dbl1,&dbl2);
	cout<<dbl1<<' '<<dbl2<<endl;
	
	return 0;
}
