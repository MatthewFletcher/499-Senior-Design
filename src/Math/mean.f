C FILE: MEAN.F
        SUBROUTINE MEAN(A,N)
C
C       CALCULATE MEAN OF ARRAY
C
            INTEGER :: I
            INTEGER :: N
            LOGICAL :: E
            CHARACTER(LEN=100)::FILENAME
            REAL    :: SUM
            REAL    :: AVG

C           https://stackoverflow.com/questions/10520819/what-does-real8-mean
            REAL*8 A(N)
            
            DO I=1,N
                SUM = SUM + A(I)
            ENDDO

            AVG = SUM / N


            FILENAME = "./DATA1.DAT"
            ! https://stackoverflow.com/questions/9522933/test-whether-a-directory-exists-or-not
            INQUIRE(FILE=FILENAME, EXIST=E)

            IF ( E ) THEN
                open(newunit=write_unit,access='sequential',&
                    &file=FILENAME,position='append',&
                    & status='old',action='write')
                WRITE(1,*) "Average value: ", AVG
            ELSE
                open(1, file = 'data1.dat', status = 'new')
                WRITE(1,*) "Average value: ", AVG
            END IF
            
            close(1)

        END
C END FILE MEAN.F
