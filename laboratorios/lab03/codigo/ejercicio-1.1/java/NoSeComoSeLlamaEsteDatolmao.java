import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

public class NoSeComoSeLlamaEsteDatolmao {

    HashMap<Long, LinkedList<Arco>> map = new HashMap<>();
    HashMap<Long, Vertice> vertices;
    ArrayList<Arco> arcos;

    NoSeComoSeLlamaEsteDatolmao(HashMap<Long, Vertice> vertices, ArrayList<Arco> arcos){
        this.vertices = vertices;
        this.arcos = arcos;
    }

    HashMap<Long, LinkedList<Arco>> magia() {
        

        for (int i = 0; i < arcos.size(); i++) { //M = cantidad de arcos :D
            Arco arc = arcos.get(i); 
            addArco(arc); //M*N;
        }

        return map;
    }

    public void addArco(Arco arco){ //N; = N vertices no repetidos :D


        if(!map.containsKey(this.vertices.get(arco.origen).getID())){  
            LinkedList<Arco>  arc = new LinkedList<>();
            arc.add(arco);
            map.put(arco.origen, arc);
        }else{
            LinkedList<Arco>  arc = map.get(arco.origen);
            arc.add(arco);
            

            map.put(arco.origen, arc);
        }

    }

}
