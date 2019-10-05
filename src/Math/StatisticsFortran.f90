subroutine mean(arr, n, output)
    integer ::  n, i
    real(8), dimension(n)   ::  arr, arr_c
    real(8) ::  output


    !f2py intent(in)    ::  arr
    !f2py intent(hide), depend(arr) ::  n = shape(arr)
    !f2py intent(out) output
        
    
    !Make deep copy of array  
    arr_c = arr
    

    output = 0

    !Loop through array
    do i=1,N
        !Accumulate sum of array
        output = output + arr_c(i)
    end do
    
    !Calculate mean
    output = output / n

    end subroutine

subroutine var(arr, n, output)
    implicit none
    integer ::  n,i
    real(8), dimension(n)   ::  arr, arr_c
    real(8) ::  output

    real(8) ::  mean_val, sum

    !f2py intent(in)    ::  arr
    !f2py intent(hide), depend(arr) ::  n = shape(arr)
    !f2py intent(out) output
    
    !Make deep copy of array 
    arr_c = arr 

    !Call mean subroutine to get mean value 
    call mean(arr_c, n, mean_val)

    !mean_val now holds mean value

    sum = 0
    !Loop through array
    do i=1,N
        !Calculate variance by accumulative sum of square of difference
        !between mean and value
        sum = sum + ((arr_c(i) - mean_val) * (arr_c(i) - mean_val))
    end do

        output = sum / n
        
    end subroutine

subroutine stddev(arr,n,output)
    implicit none
    integer ::  n
    real(8), dimension(n)   ::  arr, arr_c
    real(8) ::  output

    !f2py intent(in)    ::  arr
    !f2py intent(hide), depend(arr) ::  n = shape(arr)
    !f2py intent(out) output
    
    !Make deep copy of array 
    arr_c = arr 

    call var(arr_c,n,output)
    
    output = SQRT(output)

    end subroutine

subroutine pearson(arr_x, arr_y, n, output)
    implicit none
    integer ::  n, i
    real(8), dimension(n)   ::  arr_x, arr_y
    real(8) ::  x_mean, y_mean, numerator
    real(8) ::  x_sum, y_sum
    real(8) ::  xi,yi
    real(8) ::  output

    !f2py intent(in)    ::  arr
    !f2py intent(hide), depend(arr_x) ::  n = shape(arr_x)
    !f2py intent(out) output

    !Set x and y array means 
    call mean(arr_x, n, x_mean)
    call mean(arr_y, n, y_mean)
    
    
    numerator = 0
    x_sum = 0
    y_sum = 0
    do i=1,N

        !Set array 
        xi = arr_x(i)
        yi = arr_y(i)
        
        !Numerator calculation
        numerator = numerator + ((xi - x_mean) * (yi - y_mean))

        !Looped Denominator calculation
        x_sum = x_sum +  (xi - x_mean) * (xi - x_mean) 
        y_sum = y_sum +  (yi - y_mean) * (yi - y_mean) 
    end do
   
    !Get square root and calculate final denom value
    output = numerator / SQRT(x_sum * y_sum)

    end subroutine

subroutine linear(arr_x, arr_y, n, slope, y_int)
    implicit none
    integer ::  n
    real(8), dimension(n)   ::  arr_x, arr_y
    real(8) ::  x_mean, y_mean
    real(8) ::  x_std, y_std
    real(8) ::  p
    real(8) ::  slope, y_int

    !f2py intent(in)    ::  arr_x, arr_y
    !f2py intent(hide), depend(arr_x) ::  n = shape(arr_x)
    !f2py intent(out) slope, y_int
    
    !Calculate mean
    call mean(arr_x,n,x_mean)
    call mean(arr_y,n,y_mean)

    !Calculate std dev
    call stddev(arr_x, n, x_std)
    call stddev(arr_y, n, y_std)


    !Calculate pearson correlation
    call pearson(arr_x, arr_y, n, p)
    
    y_int = p * y_std/x_std

    slope = y_mean - y_int * x_mean



    end subroutine





















