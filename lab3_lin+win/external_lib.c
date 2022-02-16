#include <stdio.h>
#include <math.h>

float test_ret_float(float val) {
    float coef = 2.1;
    return val*coef;
}

int test_ret_int(int val) {
	int coef = 7;
    return val*coef;
}

double test_ret_double(double val) {
	double coef = 3.6;
	return val*coef;
}

char *test_ret_char(char *val) {
	return val+1;
}

void test_display(char* char_val, int int_val, float float_val, double double_val) {
	printf("Char %s,\t int %d,\t float %f,\t double %lf\n", char_val, int_val, float_val, double_val);
}