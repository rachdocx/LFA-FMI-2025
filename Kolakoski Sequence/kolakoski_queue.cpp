#include <bits/stdc++.h>
#include <fstream>
#include <limits>
using namespace std;
ofstream g("fisier2.in");
int main(){
    const int MAX_SIZE = numeric_limits<int>::max();
    const int MAX_QUEUE_SIZE = 2147483647;
    cout<<MAX_SIZE<<endl;
    cout<<MAX_QUEUE_SIZE<<endl;
    int nr=1;
    queue<int> q;
    int n;
    int nr1=1;
    int nr2=0;
    q.push(1);
    cout<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    q.pop();
    q.push(2);
    nr++;
    nr2++;
    cout<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    q.push(2);
    nr++;
    nr2++;
    cout<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    q.pop();
    int k=1;
    while(q.size() < MAX_QUEUE_SIZE)
    {
        int current = q.front();
        for(int l=0;l<current;l++)
            q.push(k);
        nr++;
        if(q.front()==1)
            nr1++;
        else
            nr2++;   
        cout<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==1000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==2000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==3000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==4000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==6000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==9000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==12000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==15000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==20000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==30000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==50000000)
            g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(q.back()==1)
            k=2;
        else
            k=1;
            q.pop();
    }
    while(!q.empty())
    {
        nr++;
        if(q.front()==1)
            nr1++;
        else
            nr2++;
        cout<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        if(nr==1000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==2000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==3000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==4000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==6000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==9000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==12000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==15000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==20000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==30000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
    if(nr==50000000)
        g<<q.front()<<' '<<nr<<' '<<nr1<<' '<<nr2<<endl;
        q.pop();

    }
    cout<<nr;
    return 0;
}