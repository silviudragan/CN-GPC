#define _CRT_SECURE_NO_WARNINGS

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <float.h>

// #include "glut.h"
#include <GL/freeglut.h>

// dimensiunea ferestrei in pixeli
#define dim 300

// numarul maxim de iteratii pentru testarea apartenentei la mult.Julia-Fatou
#define NRITER_JF 5000
// modulul maxim pentru testarea apartenentei la mult.Julia-Fatou
#define MODMAX_JF 10000000
// ratii ptr. CJuliaFatou
#define RX_JF 0.01
#define RY_JF 0.01

unsigned char prevKey;
int nivel = 0;


class C2coord
{
public:
	C2coord()
	{
		m.x = m.y = 0;
	}

	C2coord(double x, double y)
	{
		m.x = x;
		m.y = y;
	}

	C2coord(const C2coord &p)
	{
		m.x = p.m.x;
		m.y = p.m.y;
	}

	C2coord &operator=(C2coord &p)
	{
		m.x = p.m.x;
		m.y = p.m.y;
		return *this;
	}

	int operator==(C2coord &p)
	{
		return ((m.x == p.m.x) && (m.y == p.m.y));
	}

protected:
	struct SDate
	{
		double x, y;
	} m;
};

class CPunct : public C2coord
{
public:
	CPunct() : C2coord(0.0, 0.0)
	{}

	CPunct(double x, double y) : C2coord(x, y)
	{}

	CPunct &operator=(const CPunct &p)
	{
		m.x = p.m.x;
		m.y = p.m.y;
		return *this;
	}

	void getxy(double &x, double &y)
	{
		x = m.x;
		y = m.y;
	}

	int operator==(CPunct &p)
	{
		return ((m.x == p.m.x) && (m.y == p.m.y));
	}

	void marcheaza()
	{
		glBegin(GL_POINTS);
		glVertex2d(m.x, m.y);
		glEnd();
	}

	void print(FILE *fis)
	{
		fprintf(fis, "(%+f,%+f)", m.x, m.y);
	}

};

class GrilaCarteziana {
	public:
		void grila(int nr_linii, int nr_coloane)
		{
			double width = glutGet(GLUT_WINDOW_WIDTH);
			double height = glutGet(GLUT_WINDOW_HEIGHT);
			double length, max = width;
			printf("%d %d\n",width,height );
			int i;
			if (width < height)
      			max = height;

			double latura = nr_linii;

			if (latura < nr_coloane)
				latura = nr_coloane;
			latura = 1.98 / latura;

			double pct_start = 0.99;
			double latura_scalata1, latura_scalata2;
			latura_scalata1 = latura * (width/max);
			latura_scalata2 = latura * (height/max);

			glColor3f(0, 0, 0); 
			glBegin(GL_LINES); 

			for (i = 0; i <= nr_linii; i++){
				glVertex2f(-0.99,pct_start);
				glVertex2f(-0.99 + (nr_coloane * latura_scalata2), pct_start);
				pct_start -= latura_scalata1;
			}

			glColor3f(0, 0, 0); 
			pct_start = -0.99;
			for (i = 0; i <= nr_coloane; i++){
				glVertex2f(pct_start, 0.99);
				glVertex2f(pct_start, 0.99 - (nr_linii * latura_scalata1));
				pct_start += latura_scalata2;
			}
			glEnd();

			writePixel(2,2,latura_scalata1,latura_scalata2);
			writePixel(3,3,latura_scalata1,latura_scalata2);
			writePixel(4,4,latura_scalata1,latura_scalata2);
			writePixel(5,5,latura_scalata1,latura_scalata2);
		}

		void writePixel(int index_linie, int index_coloana, double latura_scalata1, double latura_scalata2)
		{
			glColor3f(0, 0, 0); 
			double pi = 3.14;
			int i;
			glBegin(GL_POLYGON);
			double p1,p2;
			p1 = -0.99 + (index_linie*latura_scalata2);
			p2 = 0.99 - (index_coloana*latura_scalata1);
			for (i = 0; i <= 360; i++){
				glVertex2f(sin(i * pi / 180) * latura_scalata2/3 + p1,cos(i * pi / 180) * latura_scalata1/3 + p2);
			}
			glEnd();
		}
};

void Display2(){
	GrilaCarteziana grila;

	grila.grila(10,10);
}

void Init(void) {

	glClearColor(1.0, 1.0, 1.0, 1.0);

	glLineWidth(1);

	glPointSize(3);

	glPolygonMode(GL_FRONT, GL_LINE);
}

void Display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	switch(prevKey){
		case '1':
			Display2();
			break;
		default:
			break;
	}
	glFlush();
}

void Reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
}

void KeyboardFunc(unsigned char key, int x, int y)
{
	prevKey = key;
	if (key == 27) // escape
		exit(0);
	glutPostRedisplay();
}

void MouseFunc(int button, int state, int x, int y)
{
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitWindowSize(dim, dim);

	glutInitWindowPosition(100, 100);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutCreateWindow(argv[0]);

	Init();

	glutReshapeFunc(Reshape);

	glutKeyboardFunc(KeyboardFunc);

	glutMouseFunc(MouseFunc);

	glutDisplayFunc(Display);

	glutMainLoop();

	return 0;
}


