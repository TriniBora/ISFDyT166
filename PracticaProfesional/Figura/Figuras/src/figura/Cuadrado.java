package figura;

public class Cuadrado extends Figura {
    
    private int lado;

    public Cuadrado(int lado, String nombre) {
        super(nombre);
        this.lado = lado;
    }

    @Override
    public float mostrarArea() {
        return lado*lado;
    }

  }
