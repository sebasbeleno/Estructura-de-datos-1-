public class Vertice {
    
    private long id;
    private double x;
    private double y;

    Vertice(long id, double x, double y){
        this.x = x;
        this.y = y;
        this.id = id;
    }

    public String toString(){
        return "El vertice tiene como cordenadas x: " + this.x + ", y: " + this.y;
    }

    public long getID(){
        return this.id;
    }

}
