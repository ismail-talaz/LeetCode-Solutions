#include <stdio.h>

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int i=0;
    int column=0,rown=0,temp;
    
    for (i=0;i<(matrixSize*matrixSize);i++) {
        column=i%matrixSize;
        rown=i/matrixSize;
        if (column>rown) {                                        /* TRANSPOSE MATRIX */
            temp=matrix[rown][column];
            matrix[rown][column]=matrix[column][rown];
            matrix[column][rown]=temp;
        }   
    }
    for (i=0;i<(matrixSize*matrixSize);i++) { 
        column=i%matrixSize;         
        rown=i/matrixSize;                                          /* SWAP COLUMNS WRT MIDDLE AXIS OF THE MATRIX*/
        if (column<(matrixSize/2)) {
            temp=matrix[rown][column];
            matrix[rown][column]=matrix[rown][matrixSize-column-1];
            matrix[rown][matrixSize-column-1]=temp;
        }
        
    }
}
