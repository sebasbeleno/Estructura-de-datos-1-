public class Arco {
    
    public long origen;
    public long destino;
    public double distancia;
    public String nombre;

    Arco(long origen, long destino, double distancia, String nombre){
        this.distancia = distancia;
        this.nombre = nombre;
        this.origen = origen;
        this.destino = destino;
    }

    void imprimirArco(){
        System.out.println("El origen del arco: " + this.origen + ", su final es: " + this.destino + ", se llama: " + this.nombre + ", su distancia es: " + this.distancia);
    }



}
