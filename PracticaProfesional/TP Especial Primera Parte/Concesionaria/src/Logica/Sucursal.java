package Logica;

import java.util.List;

public class Sucursal {
    
    private long id_sucursal;
    private String nombre;
    private String localidad;
    private String direccion;
    private List<Horario> listaHorarios;
    private List<Vehiculo> listaVehiculos;

    public Sucursal() {
    }

    public Sucursal(long id_sucursal, String nombre, String localidad, String direccion, List<Horario> listaHorarios, List<Vehiculo> listaVehiculos) {
        this.id_sucursal = id_sucursal;
        this.nombre = nombre;
        this.localidad = localidad;
        this.direccion = direccion;
        this.listaHorarios = listaHorarios;
        this.listaVehiculos = listaVehiculos;
    }

    public double getId_sucursal() {
        return id_sucursal;
    }

    public void setId_sucursal(long id_sucursal) {
        this.id_sucursal = id_sucursal;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getLocalidad() {
        return localidad;
    }

    public void setLocalidad(String localidad) {
        this.localidad = localidad;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public List<Horario> getListaHorarios() {
        return listaHorarios;
    }

    public void setListaHorarios(List<Horario> listaHorarios) {
        this.listaHorarios = listaHorarios;
    }

    public List<Vehiculo> getListaVehiculos() {
        return listaVehiculos;
    }

    public void setListaVehiculos(List<Vehiculo> listaVehiculos) {
        this.listaVehiculos = listaVehiculos;
    }

     
    
    
}
