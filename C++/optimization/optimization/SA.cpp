

#include "stdafx.h"
#include<iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
using namespace std;

#define N 30  // number of cities
#define M 1500 //number of iterative
int x[N];
double coord[N][2];

double random()
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
	a = floor(random()*N);
	do
	{
		b = floor(random()*N);
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
		delta_f = (f_j - f_i)/20;
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
		if (A_ij>random())
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

double initT(int K,int *x)
{
	int n = 500;
	double f_1=0,f_2 = 0,detal_0;
	double f[500];
	for (int i = 0; i < n; i++)
	{
		f[i] = obf(x);
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

void main()
{
	srand((unsigned)time(NULL));
	double P;
	int i;
	float read1, read2;
	FILE *fp;

	fopen_s(&fp, "DATA30.dat", "r");
	for (i = 0; i <= N; i++) {
		fscanf_s(fp, "%f %f", &read1, &read2);
		coord[i][0] = read1; coord[i][1] = read2;
	}
	fclose(fp);

	for (int i = 0; i < N; i++)
		x[i] = i;
	randomlize(x, N);
	double T[M];
	T[0] = initT(5, x);
	for (int i = 1; i < M; i++)
	{
		T[i] = T[i - 1] * 0.95;
		iterative_inner(T[i], 150);
		//cout << "The T is:" << T[i] << endl;
		//cout << "this result is:" << '\t' << obf(x) << endl;
	}
	cout << '\n' << "the last result is:" << '\t' << obf(x) << endl;
	system("pause");
}