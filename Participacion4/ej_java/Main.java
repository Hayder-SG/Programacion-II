package Participacion4.ej_java;


public class Main {
    public static void main(String[] args) {
        Circulo2D c1 = new Circulo2D(2, 0, 1);

        System.out.println("area de c1: " + c1.getArea());
        System.out.println("perimetro de c1: " + c1.getPerimetro());

        // Probar contiene(x, y)
        System.out.println("c1.contiene(2.5, 0): " + c1.contiene(2.5, 0));

        // Probar contiene(circulo)
        Circulo2D c2 = new Circulo2D(2, 0, 0.5);
        System.out.println("c1.contiene(c2): " + c1.contiene(c2));

        // Probar sobrepone(circulo)
        Circulo2D c3 = new Circulo2D(0, 0, 2);
        System.out.println("c1.sobrepone(c3): " + c1.sobrepone(c3));
    }
}


