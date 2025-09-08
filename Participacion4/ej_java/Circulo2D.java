package Participacion4.ej_java;

/**
 * @author HAYDER
 */
public class Circulo2D {
    public double x;
    public double y;
    public double radio;

    public Circulo2D() {
        this.x = 0;
        this.y = 0;
        this.radio = 1;
    }

    public Circulo2D(double x, double y, double radio) {
        this.x = x;
        this.y = y;
        this.radio = radio;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getRadio() {
        return radio;
    }

    public double getArea() {
        return Math.PI * radio * radio;
    }

    public double getPerimetro() {
        return 2 * Math.PI * radio;
    }

    public boolean contiene(double xPunto, double yPunto) {
        double distancia = Math.sqrt(Math.pow(xPunto - this.x, 2) + Math.pow(yPunto - this.y, 2));
        return distancia <= this.radio;
    }

    public boolean contiene(Circulo2D circulo) {
        double distanciaCentros = Math.sqrt(Math.pow(circulo.x - this.x, 2) + Math.pow(circulo.y - this.y, 2));
        return distanciaCentros + circulo.radio <= this.radio;
    }

    public boolean sobrepone(Circulo2D circulo) {
        double distanciaCentros = Math.sqrt(Math.pow(circulo.x - this.x, 2) + Math.pow(circulo.y - this.y, 2));
        return distanciaCentros <= this.radio + circulo.radio &&
            distanciaCentros + Math.min(this.radio, circulo.radio) >= Math.max(this.radio, circulo.radio);
    }
}

