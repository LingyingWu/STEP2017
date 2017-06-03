class MatrixStrassen {
	public static void main(String args[]) {
		if (args.length != 1) {
			System.out.println("usage: java Matrix N");
			return;
		}
		int n = Integer.parseInt(args[0]);

		double[][] a = new double[n][n]; // Matrix A
		double[][] b = new double[n][n]; // Matrix B
		double[][] c = new double[n][n]; // Matrix C

		// Initialize the matrices to some values.
		int i, j;
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				a[i][j] = i * n + j;
				b[i][j] = j * n + i;
				c[i][j] = 0;
			}
		}

		long begin = System.currentTimeMillis();
		// long begin = System.nanoTime();

		/**************************************/
		/* Write code to calculate C = A * B. */
		c = strassen(a, b);
		/**************************************/

		long end = System.currentTimeMillis();
		System.out.printf("time: %.6f sec\n", (end - begin) / 1000.0);
		// long end = System.nanoTime();
		// System.out.printf("time: %.6f millisec\n", (end - begin) /
		// 1000000.0);

		// Print C for debugging. Comment out the print before measuring the
		// execution time.
		double sum = 0;
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				sum += c[i][j];
				// System.out.printf("c[%d][%d]=%f\n", i, j, c[i][j]);
			}
		}
		// printMatrix(a);
		// printMatrix(b);
		// printMatrix(c);

		// Print out the sum of all values in C.
		// This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
		System.out.printf("sum: %.6f\n", sum);
	}

	public static double[][] strassen(double[][] a, double[][] b) {
		int n = a.length;
		double[][] result = new double[n][n];

		if (n % 2 != 0 && n != 1) {
			double[][] a_new = new double[n + 1][n + 1];
			double[][] b_new = new double[n + 1][n + 1];
			double[][] temp = new double[n + 1][n + 1];

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					a_new[i][j] = a[i][j];
					b_new[i][j] = b[i][j];
				}
			}
			temp = strassen(a_new, b_new);
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					result[i][j] = temp[i][j];
			return result;
		}
		if (n == 1) {
			result[0][0] = a[0][0] * b[0][0];
		} else {

			double[][] a11 = new double[n / 2][n / 2];
			double[][] a12 = new double[n / 2][n / 2];
			double[][] a21 = new double[n / 2][n / 2];
			double[][] a22 = new double[n / 2][n / 2];
			double[][] b11 = new double[n / 2][n / 2];
			double[][] b12 = new double[n / 2][n / 2];
			double[][] b21 = new double[n / 2][n / 2];
			double[][] b22 = new double[n / 2][n / 2];

			divide(a, a11, 0, 0);
			divide(a, a12, 0, n / 2);
			divide(a, a21, n / 2, 0);
			divide(a, a22, n / 2, n / 2);
			divide(b, b11, 0, 0);
			divide(b, b12, 0, n / 2);
			divide(b, b21, n / 2, 0);
			divide(b, b22, n / 2, n / 2);

			double[][] m1 = strassen(add(a11, a22), add(b11, b22));
			double[][] m2 = strassen(add(a21, a22), b11);
			double[][] m3 = strassen(a11, sub(b12, b22));
			double[][] m4 = strassen(a22, sub(b21, b11));
			double[][] m5 = strassen(add(a11, a12), b22);
			double[][] m6 = strassen(sub(a21, a11), add(b11, b12));
			double[][] m7 = strassen(sub(a12, a22), add(b21, b22));

			double[][] c11 = add(sub(add(m1, m4), m5), m7);
			double[][] c12 = add(m3, m5);
			double[][] c21 = add(m2, m4);
			double[][] c22 = add(sub(add(m1, m3), m2), m6);

			combine(c11, result, 0, 0);
			combine(c12, result, 0, n / 2);
			combine(c21, result, n / 2, 0);
			combine(c22, result, n / 2, n / 2);
		}

		return result;
	}

	public static double[][] add(double[][] x, double[][] y) {
		int n = x.length;
		double[][] result = new double[n][n];

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				result[i][j] = x[i][j] + y[i][j];

		return result;
	}

	public static double[][] sub(double[][] x, double[][] y) {
		int n = x.length;
		double[][] result = new double[n][n];

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				result[i][j] = x[i][j] - y[i][j];

		return result;
	}

	public static void divide(double[][] origin, double[][] result, int row, int col) {
		for (int ix = 0, iy = row; ix < result.length; ix++, iy++)
			for (int jx = 0, jy = col; jx < result.length; jx++, jy++)
				result[ix][jx] = origin[iy][jy];
	}

	public static void combine(double[][] origin, double[][] result, int row, int col) {
		for (int ix = 0, iy = row; ix < origin.length; ix++, iy++)
			for (int jx = 0, jy = col; jx < origin.length; jx++, jy++)
				result[iy][jy] = origin[ix][jx];
	}

	public static void printMatrix(double[][] x) {
		int n = x.length;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.printf("%4.0f  ", x[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
}