package Logica;

public class Moto extends Vehiculo {

    public Moto() {
    }

    public Moto(long id_vehiculo, double kilometraje, String tipoCombustible, int modelo, String marca, boolean serviceAlDia, String categoria) {
        super(id_vehiculo, kilometraje, tipoCombustible, modelo, marca, serviceAlDia, categoria);
    }

    public double getId_vehiculo() {
        return id_vehiculo;
    }

    public void setId_vehiculo(long id_vehiculo) {
        this.id_vehiculo = id_vehiculo;
    }

    public double getKilometraje() {
        return kilometraje;
    }

    public void setKilometraje(double kilometraje) {
        this.kilometraje = kilometraje;
    }

    public String getTipoCombustible() {
        return tipoCombustible;
    }

    public void setTipoCombustible(String tipoCombustible) {
        this.tipoCombustible = tipoCombustible;
    }

    public int getModelo() {
        return modelo;
    }

    public void setModelo(int modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public boolean isServiceAlDia() {
        return serviceAlDia;
    }

    public void setServiceAlDia(boolean serviceAlDia) {
        this.serviceAlDia = serviceAlDia;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }
    
    

    @Override
    public double desgaste() {
        Controladora ctrl = new Controladora();

        int antiguedad = ctrl.getAntiguedad(this.getModelo());

        double desgaste = this.getKilometraje() / antiguedad;

        if (this.isServiceAlDia() == true && this.getKilometraje() < 30000) {
            return desgaste / 1000;
        } else {
            return desgaste / 10;
        }

    }

}
