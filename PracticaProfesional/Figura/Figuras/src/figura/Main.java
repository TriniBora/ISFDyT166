
package figura;

public class Main {

    public static void main(String[] args) {
        
        Figura figura1 = new Cuadrado(20, "cuadrado");
        Figura figura2 = new Rectangulo(10, 25, "rectangulo");
        Figura figura3 = new Circulo(5, "circulo");
        
        float area1 = figura1.mostrarArea();
        String nombre1 = figura1.getNombre();
        System.out.println("Figura: " + nombre1 + ", área: " + area1);
        
        float area2 = figura2.mostrarArea();
        String nombre2 = figura2.getNombre();
        System.out.println("Figura: " + nombre2 + ", área: " + area2);
        
        float area3 = figura3.mostrarArea();
        String nombre3 = figura3.getNombre();
        System.out.println("Figura: " + nombre3 + ", área: " + area3);
    }
}