var media, n1, n2 ;

n1 = prompt ("Informe a PRIMEIRA nota: ") ;
n2 = prompt ("Informe a SEGUNDA nota: ") ;

media = (n1 + n2)/ 2; 

if ( media > 7 ) 
{
    console.log ("APROVADO!");

} 
else
{
    if ( media < 7 ) 
    {
       console.log("Você precisa dessa Nota Mínima para ser aprovado",);
    }
}
