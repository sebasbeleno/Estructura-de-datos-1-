import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.*;
/**
 * Title: LectorDeDatos source code (modified)
 * Author: mauriciotoro
 * Date: 2020
 * Availability: https://github.com/mauriciotoro/ST0245-Eafit/blob/master/laboratorios/lab03/codigo_estudiante/codigo/ejercicio-1.1/java/LectorDatos.java
 * 
 */
public class LectorDatos{
    private String folderPath;
    
    public LectorDatos(String folderPath) {
        this.folderPath = folderPath;
    }
    
     public HashMap<Long, Vertice> LeerVertices() {
        
        HashMap<Long, Vertice> vertices = new HashMap<Long, Vertice>();
    
        String filePath = this.folderPath + "/Vertices.txt";

        try{
            FileReader f  = new FileReader(filePath);
            
            BufferedReader b = new BufferedReader(f);
            String line;
            int lineCount = 0;
            while((line = b.readLine()) != null) {
                if(lineCount != 0) {
                    String[] data = line.split(" ");
                    Long id = Long.parseLong(data[0]);

                    double x = Double.parseDouble(data[1]);
                    double y = Double.parseDouble(data[2]);
                    
                    Vertice v = new Vertice(id, x, y);
                    vertices.put(id, v);


                }
                lineCount++;
            }
            b.close();
            return vertices;
        }catch (IOException e) {
            System.out.println("Asegurece de tener el documento ''Vertices''");
        }
        return vertices;
    } 
    
     
    public ArrayList<Arco> leerArcos() {

        String filePath = this.folderPath + "/Arcos.txt";

        ArrayList<Arco> arr = new ArrayList<Arco>();

        try{
            FileReader f  = new FileReader(filePath);
            BufferedReader b = new BufferedReader(f);
            String line;
            int lineCount = 0;
            while((line = b.readLine()) != null) {
                if(lineCount != 0) {
                    String[] data = line.split(" ");
                    
                    long idInicio = Long.parseLong(data[0]);
                    long idFinal = Long.parseLong(data[1]); 
                    double distancia = Double.parseDouble(data[2]);

                    String nombre = "";
                    for (int i = 3; i < data.length; i++) {
                        nombre += data[i] ;
                    }
                    Arco arco = new Arco(idInicio, idFinal, distancia, nombre);

                    arr.add(arco);

                }
                lineCount++;
            }
            b.close();
            return arr;
        }catch (IOException e) {
            System.out.println("Asegurece de tener el documento ''Arcos''");
        };
        return arr;

    }
    
}
