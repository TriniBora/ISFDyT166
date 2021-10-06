package Logica;

import java.util.ArrayList;
import java.util.List;

public class Concesionaria {

        public static void main(String[] args) {
            
            Auto auto = new Auto(001, 125000.0, "diesel", 2000, "Ford", true, "auto");
            Camioneta camioneta = new Camioneta(002, 138000.0, "nafta", 1990, "Chevrolet", false, "camioneta");
            Moto moto = new Moto(003, 25000.0, "nafta", 2010, "Honda", true, "moto");
            Auto auto2 = new Auto(004, 99999.0, "nafta", 2012, "Citroen", true, "auto");
            Camioneta camioneta2 = new Camioneta(005, 73598.6, "diesel", 2006, "Ford", true, "camioneta");
            Moto moto2 = new Moto(006, 4258.5, "nafta", 2020, "Zanella", false, "moto");            
               
            System.out.printf("Desgaste Auto: %.2f", auto.desgaste());
            System.out.println("");
            System.out.printf("Desgaste Camioneta: %.2f", camioneta.desgaste());
            System.out.println("");
            System.out.printf("Desgaste Moto: : %.2f", moto.desgaste());
            System.out.println("");
            
            
            Horario horario1 = new Horario("Lunes", "09:00", "18:00");
            Horario horario2 = new Horario("Martes", "09:00", "18:00");
            Horario horario3 = new Horario("Miércoles", "09:00", "18:00");
            Horario horario4 = new Horario("Jueves", "09:00", "18:00");
            Horario horario5 = new Horario("Viernes", "09:00", "18:00");
            Horario horario6 = new Horario("Sábado", "09:00", "13:00");
            
            List<Horario> listaHorarios1 = new ArrayList <Horario>();
            listaHorarios1.add(horario1);
            listaHorarios1.add(horario3);
            listaHorarios1.add(horario5);
            listaHorarios1.add(horario6);
            
            List<Horario> listaHorarios2 = new ArrayList <Horario>();
            listaHorarios1.add(horario1);
            listaHorarios1.add(horario2);
            listaHorarios1.add(horario3);
            listaHorarios1.add(horario4);
            listaHorarios1.add(horario5);
            listaHorarios1.add(horario6);
            
            List<Vehiculo> listaVehiculos1 = new ArrayList <Vehiculo>();
            listaVehiculos1.add(auto);
            listaVehiculos1.add(auto2);
            listaVehiculos1.add(camioneta2);
            
            List<Vehiculo> listaVehiculos2 = new ArrayList <Vehiculo>();
            listaVehiculos2.add(moto);
            listaVehiculos2.add(moto2);
            listaVehiculos2.add(camioneta);
            listaVehiculos2.add(camioneta2);
            
            
            Sucursal suc1 = new Sucursal(1234, "Sucursal 1", "Tandil", "Alem 222", listaHorarios1, listaVehiculos1);
            Sucursal suc2 = new Sucursal(5678, "Sucursal 2", "Azul", "San Marín 420", listaHorarios2, listaVehiculos2);
            
            System.out.println("Catálogo de vehículos de la sucursal " + suc1.getNombre() + ": ");
            
            for (int i=0; i<suc1.getListaVehiculos().size(); i++){
                System.out.println("Id: " + suc1.getListaVehiculos().get(i).id_vehiculo + " Modelo: " + suc1.getListaVehiculos().get(i).modelo + " Categoría: " + suc1.getListaVehiculos().get(i).categoria);
            }
            
            System.out.println("Catálogo de vehículos de la sucursal " + suc2.getNombre() + ": ");
            
            for (int i=0; i<suc2.getListaVehiculos().size(); i++){
                System.out.println("Id: " + suc2.getListaVehiculos().get(i).id_vehiculo + " Modelo: " + suc2.getListaVehiculos().get(i).modelo + " Categoría: " + suc2.getListaVehiculos().get(i).categoria);
            }
            
            
            
    }
    
}
