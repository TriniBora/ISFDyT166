package figura;

public class Circulo extends Figura{
    
    private int radio;

    public Circulo(int radio, String nombre) {
        super(nombre);
        this.radio = radio;
    }

    @Override
    public float mostrarArea() {
        return 3.14f*radio*radio;
    }

    
    
    
}
