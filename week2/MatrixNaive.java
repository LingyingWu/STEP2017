class MatrixNaive {
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
		int i, j, k;
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				a[i][j] = i * n + j;
				b[i][j] = j * n + i;
				c[i][j] = 0;
			}
		}

		// long begin = System.currentTimeMillis();
		long begin = System.nanoTime();

		/**************************************/
		/* Write code to calculate C = A * B. */
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				for (k = 0; k < n; k++) {
					c[i][j] += a[i][k] * b[k][j];
				}
			}
		}
		/**************************************/

		// long end = System.currentTimeMillis();
		// System.out.printf("time: %.6f sec\n", (end - begin) / 1000.0);
		long end = System.nanoTime();
		System.out.printf("time: %.6f millisec\n", (end - begin) / 1000000.0);

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

	public static void printMatrix(double[][] x) {
		int n = x.length;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.printf("%3.0f  ", x[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
}