import java.util.Random;

public class Benchmarking {
    public Benchmarking(){
        long currentMills = System.currentTimeMillis();
        long currentNano = System.nanoTime();

        System.out.println(currentMills);
        System.out.println(currentNano);
    }

    private int[] generarArregloAleatorio(int tamano) {
        int[] array = new int[tamano];
        Random rand = new Random();

        for (int i = 0; i < tamano; i++) {
            array[i] = rand.nextInt(100_000); // Números del 0 al 99,999
        }

        return array;
    }

    public double medirConCurrentTimeMills(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTimeMills(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        double tiempoSegundos = (fin - inicio) / 1_000_000_000.0;
        return tiempoSegundos;
    }
}
