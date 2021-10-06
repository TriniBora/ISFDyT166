package figura;

public abstract class Figura {
    
    //  atributos
    private String nombre;
    
    
    // metodos
    public Figura(String nombre){
        this.nombre = nombre;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    
    public float mostrarArea(){
        return 0;
    }
    
    
}
