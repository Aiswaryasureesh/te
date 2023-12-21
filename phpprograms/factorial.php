 

class IsPrime
{       
    function check($num)
    {
        for ($i = 2; $i < $num; $i++)
        {
            if ($num % $i == 0) 
            {
                echo 'NOT prime';
                break;
            }               
        }
        echo 'Prime';           
    }       
}

$x = new IsPrime();
$x->check(4);

   