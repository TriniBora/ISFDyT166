package figura;

public class Rectangulo extends Figura{
    
    private int base;
    private int altura;

    public Rectangulo(int base, int altura, String nombre) {
        super(nombre);
        this.base = base;
        this.altura = altura;
    }

    @Override
    public float mostrarArea() {
        return base*altura;
    }

}
