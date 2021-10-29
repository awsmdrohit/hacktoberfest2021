#include <iostream>
using namespace std;
int main()
{
 float income,tax,Age;
 char gender;
 cout<<"Enter Income of person : ";
 cin>>income;
 cout<<"Enter the age of the person:";
 cin>>Age;
 //Reading gender from user
    cout<<"Enter gender (M/m or F/f): ";
    cin>>gender;

//first condn
if(income<=250000.00)
{
 cout<<"tax=0";   
}
//second condn
else if  (250000<income<=500000.00)
       {
           tax=(income-50000.00)*10/100;
            cout<<tax;
        }
 //third condition       
else if  (500000<income<=1000000.00){
     tax=(income-1000000.00)*20/100;
            cout<<tax;
}


 
 //fourth condition
 else if (income>1000000){
     switch(gender)
    {
        case 'M':
        case 'm':
            cout<<"Male";
            tax=(income-1000000.00)*35/100;
            cout<<tax;

            break;
        case 'F':
        case 'f':
             cout<<"Female";
             tax=(income-1000000.00)*33/100;
            cout<<tax;
            break;
        default:
             cout<<"Unspecified Gender"<<endl;
    }   
   
    
 

}