
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "glut.h"

// dimensiunea ferestrei in pixeli
#define dim 300

unsigned char prevKey;

// concoida lui Nicomede (concoida dreptei)
// $x = a + b \cdot cos(t), y = a \cdot tg(t) + b \cdot sin(t)$. sau
// $x = a - b \cdot cos(t), y = a \cdot tg(t) - b \cdot sin(t)$. unde
// $t \in (-\pi / 2, \pi / 2)$
void Display1() {
	double xmax, ymax, xmin, ymin;
	double a = 1, b = 2;
	double pi = 4 * atan(1.0);
	double ratia = 0.05;
	double t;

	// calculul valorilor maxime/minime ptr. x si y
	// aceste valori vor fi folosite ulterior la scalare
	xmax = a - b - 1;
	xmin = a + b + 1;
	ymax = ymin = 0;
	for (t = -pi / 2 + ratia; t < pi / 2; t += ratia) {
		double x1, y1, x2, y2;
		x1 = a + b * cos(t);
		xmax = (xmax < x1) ? x1 : xmax;
		xmin = (xmin > x1) ? x1 : xmin;

		x2 = a - b * cos(t);
		xmax = (xmax < x2) ? x2 : xmax;
		xmin = (xmin > x2) ? x2 : xmin;

		y1 = a * tan(t) + b * sin(t);
		ymax = (ymax < y1) ? y1 : ymax;
		ymin = (ymin > y1) ? y1 : ymin;

		y2 = a * tan(t) - b * sin(t);
		ymax = (ymax < y2) ? y2 : ymax;
		ymin = (ymin > y2) ? y2 : ymin;
	}

	xmax = (fabs(xmax) > fabs(xmin)) ? fabs(xmax) : fabs(xmin);
	ymax = (fabs(ymax) > fabs(ymin)) ? fabs(ymax) : fabs(ymin);

	// afisarea punctelor propriu-zise precedata de scalare
	glColor3f(1, 0.1, 0.1); // rosu
	glBegin(GL_LINE_STRIP);
	for (t = -pi / 2 + ratia; t < pi / 2; t += ratia) {
		double x1, y1, x2, y2;
		x1 = (a + b * cos(t)) / xmax;
		x2 = (a - b * cos(t)) / xmax;
		y1 = (a * tan(t) + b * sin(t)) / ymax;
		y2 = (a * tan(t) - b * sin(t)) / ymax;

		glVertex2f(x1, y1);
	}
	glEnd();

	glBegin(GL_LINE_STRIP);
	for (t = -pi / 2 + ratia; t < pi / 2; t += ratia) {
		double x1, y1, x2, y2;
		x1 = (a + b * cos(t)) / xmax;
		x2 = (a - b * cos(t)) / xmax;
		y1 = (a * tan(t) + b * sin(t)) / ymax;
		y2 = (a * tan(t) - b * sin(t)) / ymax;

		glVertex2f(x2, y2);
	}
	glEnd();
}

// graficul functiei 
// $f(x) = \bar sin(x) \bar \cdot e^{-sin(x)}, x \in \langle 0, 8 \cdot \pi \rangle$, 
void Display2() {
	double pi = 4 * atan(1.0);
	double xmax = 8 * pi;
	double ymax = exp(1.1);
	double ratia = 0.05;
	// afisarea punctelor propriu-zise precedata de scalare
	glColor3f(1, 0.1, 0.1); // rosu
	glBegin(GL_LINE_STRIP);
	for (double x = 0; x < xmax; x += ratia) {
		double x1, y1;
		x1 = x / xmax;
		y1 = (fabs(sin(x)) * exp(-sin(x))) / ymax;

		glVertex2f(x1, y1);
	}
	glEnd();
}

void Display2_1() 
{
	int xmax = 100;
	double ymax = -1;
	double ratia = 2.5;
	for (double x = ratia; x <= xmax; x += ratia)
	{
		double y;
		double rotunjire = round(x);
		y = (fabs(rotunjire - x)) / x;
		ymax = (ymax < y) ? y : ymax;
	}

	glColor3f(1, 0.1, 0.1); // rosu
	glBegin(GL_LINE_STRIP);
	glVertex2f(0, 1);
	for (double x = ratia; x <= xmax; x += ratia)
	{
		double rotunjire = round(x);
		double y;
		y = (fabs(rotunjire - x)) / x;
		y = y / ymax;
		if (y == 1)
			y = 0.99;
		glVertex2f(x / xmax, y);
	}
	glEnd();
}

void Display2_2_3()
{
	double a = 0.1;
	double b = 0.2;
	double ratia = 0.05;
	double xmax = -9999999, ymax = -9999999;
	double start = -10;
	double finish = 10;
	for (double t = start; t <= finish; t += ratia)
	{
		double x, y;
		x = a*t - b*sin(t);
		y = a - b*cos(t);
		ymax = (ymax < y) ? y : ymax;
		xmax = (xmax < x) ? x : xmax;
	}

	glColor3f(1, 0.1, 0.1); // rosu
	glBegin(GL_LINE_STRIP);
	for (double t = start; t <= finish; t += ratia)
	{
		double x, y;
		x = a*t - b*sin(t);
		y = a - b*cos(t);
		glVertex2f(x, y);
	}
	glEnd();
}

void Display2_2_4()
{
	double R = 0.1;
	double r = 0.3;
	double pi = 4 * atan(1.0);
	double xmax = 2 * pi;
	double ratia = 0.05;

	glColor3f(1, 0.1, 0.1); // rosu
	glBegin(GL_LINE_STRIP);
	for (double t = 0; t <= xmax; t += ratia)
	{
		double x, y;
		x = (R + r)*cos(r / R * t) - r*cos(t + r / R * t);
		y = (R + r)*sin(r / R * t) - r*sin(t + r / R *t);
		glVertex2f(x, y);
	}
	glEnd();
}

void Display2_2_5()
{
	double R = 0.1;
	double r = 0.3;
	double pi = 4 * atan(1.0);
	double xmax = 2 * pi;
	double ratia = 0.05;

	glColor3f(1, 0.1, 0.1); // rosu
	glBegin(GL_LINE_STRIP);
	for (double t = 0; t <= xmax; t += ratia)
	{
		double x, y;
		x = (R - r)*cos(r / R*t) - r*cos(t - r / R*t);
		y = (R - r)*sin(r / R*t) - r*sin(t - r / R*t);
		glVertex2f(x, y);
	}
	glEnd();
}
void Init(void) {

	glClearColor(1.0, 1.0, 1.0, 1.0);

	glLineWidth(1);

	//   glPointSize(4);

	glPolygonMode(GL_FRONT, GL_LINE);
}

void Display(void) {
	glClear(GL_COLOR_BUFFER_BIT);

	switch (prevKey) {
	case '1':
		Display1();
		break;
	case '2':
		Display2();
		break;
	case '3':
		Display2_1();
		break;
	case '6':
		Display2_2_3();
		break;
	case '7':
		Display2_2_4();
		break;
	case '8':
		Display2_2_5();
		break;
	default:
		break;
	}

	glFlush();
}

void Reshape(int w, int h) {
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
}

void KeyboardFunc(unsigned char key, int x, int y) {
	prevKey = key;
	if (key == 27) // escape
		exit(0);
	glutPostRedisplay();
}

void MouseFunc(int button, int state, int x, int y) {
}

int main(int argc, char** argv) {

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
