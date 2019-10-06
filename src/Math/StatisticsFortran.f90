!https://notmatthancock.github.io/2017/02/10/calling-fortran-from-python.html

!This file contains subroutines for the statistics and regressions functions
!used in the Stats_Wizard.py program. 

subroutine mean(arr, n, output)
    integer ::  n, i
    real(8), dimension(n)   ::  arr, arr_c
    real(8) ::  output

    !f2py intent(in)    ::  arr
    !f2py intent(hide), depend(arr) ::  n = shape(arr)
    !f2py intent(out) output
    
    !Make deep copy of array  
    arr_c = arr

    !Initialize to zero
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
    
    !Calculation of y intercept
    y_int = p * y_std/x_std
    
    !Calculation of slope 
    slope = y_mean - y_int * x_mean

    end subroutine


subroutine binomial(p,n,x_suc,output)
    implicit none

    real ::  n, x_suc

    real, parameter :: pi = 3.1415927
    real, parameter :: e = 2.71828

    real(8) ::  p, q
    real(8), intent(out) ::  output
    real(8) ::  s, m

    !p = success, q = failure

    !Calculate probability of failure
    q = 1 - p

    !p, q, and n are set. 
   
    !calculate mu
    s = SQRT(n*p*q)

        
        contains
            !
            !######################################################
            !For any x, calculate the corresponding pdf value
            real(8) function norm(x)
            real :: f
            real,intent(in) :: x
                f = 1/SQRT(2 * pi) * e ** ((-x**2)/2)
            end function

            !######################################################
            real(8) function integrnorm(b)
                real :: f
            real, intent(in) :: b
                real :: integral
                real :: idxa, idxb, delta, a
                integer::i
                real, parameter :: precisionfactor = 100
                real, parameter :: start = -5
                delta = (b - start)/precisionfactor
                integral = 0 
                do i=-500,500
                    idxa = norm(i/100.0)
                    idxb = norm((i+1)/100.0)
                    integral = integral + delta * (idxa + idxb)/2 
              end do
           end function 

    end subroutine

subroutine signtest(arr1, arr2, n, z_val)
    implicit none 

    !f2py intent(in)    ::  arr_1, arr_2
    !f2py intent(hide), depend(arr_x) ::  n = shape(arr_x)
    !f2py intent(out) z_val

    integer ::  n, i
    real(8), dimension(n)   ::  arr1, arr2
    real(8) ::  p_val
    real(8) ::  diff
    integer ::  sig_ct, pos_ct, neg_ct, zer_ct
    real(8) ::  null_prob
    real(8) ::  succ_ct
    real(8) ::  new_n
    real(8) ::  z_val
    real(8) ::  m,s

    
    new_n = 0
    pos_ct = 0
    neg_ct = 0
    zer_ct = 0
    

    !Count sign changes
    do i=1,n
        diff = arr1(i) - arr2(i)
        if (diff > 0) then
            pos_ct = pos_ct + 1
        else if (diff < 0) then
            neg_ct = neg_ct + 1 
        else
            zer_ct = zer_ct + 1
        end if 

        if (diff .NE. 0) then
            new_n = new_n + 1
        end if
    end do 

    if (pos_ct < neg_ct) then
        sig_ct = neg_ct
    else if (neg_ct < pos_ct) then
        sig_ct = pos_ct 
    else
        sig_ct = pos_ct
    end if 
    
   
    !Null Hypothesis: sign difference is 50% 
    null_prob = 0.5
     
    
    m = new_n * null_prob
    s = SQRT(new_n * null_prob * (1-null_prob))
    
    z_val = ((sig_ct - null_prob) - m)/s

    
    end subroutine
