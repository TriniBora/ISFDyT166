package Logica;

public abstract class Vehiculo {
    
    long id_vehiculo;
    double kilometraje;
    String tipoCombustible;
    int  modelo;
    String marca;
    boolean serviceAlDia;
    String categoria;

    public Vehiculo() {
    }

    public Vehiculo(long id_vehiculo, double kilometraje, String tipoCombustible, int modelo, String marca, boolean serviceAlDia, String categoria) {
        this.id_vehiculo = id_vehiculo;
        this.kilometraje = kilometraje;
        this.tipoCombustible = tipoCombustible;
        this.modelo = modelo;
        this.marca = marca;
        this.serviceAlDia = serviceAlDia;
        this.categoria = categoria;
    }
    

    public abstract double desgaste();  
    
}
