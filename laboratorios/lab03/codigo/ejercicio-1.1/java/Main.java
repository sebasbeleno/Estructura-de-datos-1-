import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

/**
 * I dont know how this works, but works :D
 *
 * @author Sebastian Beleño
 * @version 1.0
 */
public class Main
{
    public static void main(String[] args) {

        LectorDatos d = new LectorDatos("D:/Universidad/ST0245-001/laboratorios/lab03/codigo/ejercicio-1.1/java");
        
        HashMap<Long, Vertice>  vertices = d.LeerVertices();
        ArrayList<Arco> arcos = d.leerArcos();
        
        NoSeComoSeLlamaEsteDatolmao NoSeComoSeLlamaEsteDatolmao = new NoSeComoSeLlamaEsteDatolmao(vertices, arcos);
        HashMap<Long, LinkedList<Arco>> mapa = NoSeComoSeLlamaEsteDatolmao.magia(); //M*N = M la cantidad de arcos N = Vertices 


        System.out.println("Vertices: " + vertices.size());
        System.out.println("Arcos: " + arcos.size());
        LinkedList<Arco> algo = mapa.get(new Long("330249854"));

        System.out.println(algo.size());

         for (int i = 0; i < algo.size(); i++) {
            algo.get(i).imprimirArco();
        } 
        System.out.println("Tamaño del mapa: " + mapa.size());

        /**
         * https://www.bigocheatsheet.com/
         */
    }
}
