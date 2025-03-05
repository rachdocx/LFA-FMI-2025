#include <iostream>
#include <fstream>
#include <limits>
using namespace std;
ofstream g("fisier1.in");
const int MAX_SIZE = numeric_limits<int>::max();
int* v = new int[MAX_SIZE];
int i, j, k,nr1, nr2,n;
// incerc sa generez cat mai multe numere din sirul Kolakoski, folosindu ma de un array simplu, am maximum nr de elemente pe care le poate retine un array
int main(){
    nr1=0;
    nr2=0;
    v[0]=1;
    v[1]=2;
    i=2;
    j=0;
    k=1;
    while(i<=MAX_SIZE)
    {
        for(int l=0;l<v[j];l++)
        {
            v[i]=v[k];
            i++;
        }
        j++;
        cout<<v[j]<<" "<<i;
        k=1-k;
    }
    for(int i=0;i<=MAX_SIZE;i++)
    {
        if(v[i]==1)
        {
            nr1++;
        }
        else
        {
            nr2++;
        }
        cout<<v[i]<<" ";
    }
    g<<endl<<nr1<<" "<<nr2;
    return 0;

}