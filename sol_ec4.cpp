#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <cmath>
using namespace std;



int main(){
    ofstream outfile;
    int nX=1,nTim=15;
    float fX=1.0,fTim=6.0;
    int num_x=101,num_tim=120;
    float dX=fX/(num_x-1),dTim=fTim/num_tim,rho=1e-2,ten=4*1e-4;
    float c=sqrt(ten/rho);
    float c1=dX/dTim,radio=c*c/(c1*c1);
    
    /*
    condiciones iniciales
    */
    double cuerr[3][nX*num_x];
    for(int i=0;i<nX*num_x;i++){
        cuerr[0][i]=-(i/(nX*100.0)*2-1)*(i/(nX*100.0)*2-1)+1;
    }

    cuerr[1][0]=0;
    cuerr[1][-1]=0;

    for(int i=1;i<nX*(num_x-1);i++){
        cuerr[1][i]=cuerr[0][i]+radio/2*(cuerr[0][i+1]+cuerr[0][i-1]-2*cuerr[0][i]);
    }

    /*
    solucion
    */
   outfile.open("dat_ec4.dat");
    for (int j=0;j<nTim*20;j++){
        for(int i=1;i<nX*(num_x-1);i++){
            cuerr[2][i]=2*cuerr[1][i]-cuerr[0][i]+radio*(cuerr[1][i+1]+cuerr[1][i-1]-2*cuerr[1][i]);
        }

        /*
        imprime linea j, t=j*dTim
        */
        for(int i=0;i<nX*num_x;i++){
        outfile << cuerr[0][i] << " ";
        }
        outfile << "\n";

        for(int i=1;i<nX*(num_x-1);i++){
            cuerr[0][i]=cuerr[1][i];
            cuerr[1][i]=cuerr[2][i];
        }
        
    }

    return 0;
}

