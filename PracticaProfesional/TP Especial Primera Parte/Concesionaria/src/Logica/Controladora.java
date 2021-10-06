package Logica;

import java.util.Date;

public class Controladora {

    public int getAntiguedad(int modelo) {

        Date date = new Date();

        int currentYear = date.getYear() + 1900;

        return currentYear - modelo;

    }
}
