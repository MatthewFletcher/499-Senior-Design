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
