public class app{
    public static void main(String[] args){
        double[] numeros={1,5,4,3,2};
        System.out.println("la mediana es : "+promedio(numeros));
    }
    
    public static double promedio(double[] numeros){
        if(numeros.length==0){
            System.out.println("no se puede calcular la mediana de un arreglo vácio");
            return 0;
        }
        
        //ordena primero el arreglo
        double temp=0d;
        int posMenor=0;
        for (int i=0;i<numeros.length;i++) {
            posMenor=i;
            for (int j=i;j<numeros.length;j++) {
                if(numeros[j]<numeros[posMenor]){
                    posMenor=j;
                }
            }
            temp=numeros[i];
            numeros[i]=numeros[posMenor];
            numeros[posMenor]=temp;
        }
        
        
        //retorna la mediana con el arreglo ordenado
        if(numeros.length%2==0){
            return (numeros[numeros.length/2]+numeros[numeros.length/2-1])/2;
        }else{
            return numeros[numeros.length/2];
        }
    }
}