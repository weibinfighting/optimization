
#include<iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <ctime>
#include <fstream>
using namespace std;

#define N 30  // number of cities
#define M 1000 //number of iterative
int x[N];
double coord[N][2];
clock_t  Begin, End;
double duration;

double randomnum()
{
	return (double)rand() / RAND_MAX;
}

void randomlize(int *a, int n)
{

	int i = 0, j = 0, k = 0;
	for (i = 0; i < n; i++)
	{
		j = rand() % (n - i) + i;
		k = a[i];
		a[i] = a[j];
		a[j] = k;
	}
}

double distance(double *x,double *y)
{
	double d = 0;
	for (int i = 0; i < 2; i++)
		d = d + pow((x[i] - y[i]),2);
	d = sqrt(d);
	return d;
}

double obf(int a[N])
{
	double D = 0,coord_x[2],coord_y[2];
	for (int i = 0; i < N-1; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			coord_x[j] = coord[a[i]][j];
			coord_y[j] = coord[a[i + 1]][j];
		}
		D = D + distance(coord_x, coord_y);
	}
	return D;
}

int *nerighbor_city(int x[N])
{
	int a, b;
	static int X[N];
	for (int i = 0; i < N; i++)
		X[i] = x[i];
	a = floor(randomnum()*N);
	do
	{
		b = floor(randomnum()*N);
	} while (a==b);
	X[a] = x[b];
	X[b] = x[a];
	return X;
}

void iterative_inner(double t_0, int iter_num)
{
	double f_i, f_j, delta_f, A_ij;
	int *x_1;
	for (int i = 0; i < iter_num; i++)
	{
		f_i = obf(x);
		x_1 = nerighbor_city(x);
		f_j = obf(x_1);
		delta_f = (f_j - f_i)/200;
		//cout << "x_0:" << '\t';
		//for (int i = 0; i < N; i++)
		//	cout << x[i] << "->";
		//cout << '\n'<<"x_1:"<<'\t';
		//for (int i = 0; i < N; i++)
		//	cout << x_1[i] << "->";
		//cout << endl;
		if (delta_f<=0)
		{
			A_ij = 1;
		}
		else
		{
			A_ij = exp(-delta_f / t_0);
		}
		if (A_ij>randomnum())
		{
			for (int i = 0; i < N; i++)
			{
				x[i] = x_1[i];
			}
		}
		else
		{
			continue;
		}
	}
}

double initT(int K)
{
	int n = 500,a[N];
	double f_1=0,f_2 = 0,detal_0;
	double f[500];
	for (int i = 0; i < n; i++)
	{
		for (int i = 0; i < N; i++)
			a[i] = i;
		randomlize(a,N);
		f[i] = obf(a);
		f_1 = f_1 + f[i];
	}
	double average_f;
	average_f = f_1 / n;
	for (int i = 0; i < n; i++)
		f_2 = f_2 + pow((f[i] - average_f), 2);
	f_2 = f_2 / (n - 1);
	detal_0 = 6 * sqrt(f_2);
	return detal_0*K;
}

int main(){
	Begin = clock();
	srand((unsigned)time(NULL));
	double P;
	int i;
	float read1, read2;
	ifstream fp("DATA30.dat");

	fp.open("DATA30.dat", ios::in);
    while(!fp.eof()){
        char read[10];
	    fp.getline(read,10);
		coord[i][0] = read1; coord[i][1] = read2;
	}
	fp.close();

	for (int i = 0; i < N; i++)
		x[i] = i;
	randomlize(x, N);
	double T[M];
	T[0] = initT(5);
	cout << "the begin T is:\t" << initT(5) << endl;
	for (int i = 1; i < M; i++)
	{
		T[i] = T[i - 1] * 0.98;
		iterative_inner(T[i], 100);
		//cout << "The T is:" << T[i] << endl;
		//cout << "this result is:" << '\t' << obf(x) << endl;
	}
	cout << '\n' << "the last result is:" << '\t' << obf(x) << endl;
	for (int i = 0; i < N; i++)
	{
		cout << x[i] << "->";
	}
	End = clock();
	duration = double(End - Begin);
	system("pause");
	return 0;
}