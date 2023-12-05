//Kodu geliştiren Oğuzhan Demirbaş
//Geliştirilme tarihi 5.11.2023
//Geliştirilme amacı :6 Dilde aynı algoritmayı çalıştırarak arasıdnaki farkları görmek

import java.util.Scanner;//import java.util.Scanner; ifadesi, Java programlarında kullanılabilen bir sınıf olan Scanner'ı programa dahil etmek için kullanılır. 

public class Yıldız {//Yıldız adında bir sınıf belirledik
    public static void main(String[] args) {//Çalışmayı başlat
        Scanner scanner = new Scanner(System.in);

        System.out.print("Satır sayısını girin: ");
        int Satir_sayisi = scanner.nextInt();//kullanılarak bir kullanıcıdan satır sayısı tamsayı olarak alınır

        System.out.print("Sütun sayısını girin: ");
        int Sutun_sayisi = scanner.nextInt();//kullanılarak bir kullanıcıdan sütun sayısı tamsayı olarak alınır

        for (int i = 0; i < Satir_sayisi; i++) {//Dıştaki for döngüsü, i değişkeni kullanarak Satir_sayisi sayısı kadar tekrarlanır. Bu, kaç satır olduğunu belirtir.

            for (int j = 0; j < Sutun_sayisi; j++) {//İçteki for döngüsü, j değişkeni kullanarak Sutun_sayisi sayısı kadar tekrarlanır. Bu, her satırda kaç yıldız (*) karakterinin olacağını belirtir.

                System.out.print("*");//ekrana bir yıldız karakterini yazdırmak için kullanılır.
            }
            System.out.println(); // Her satırın sonunda yeni bir satıra geç
        }
    }
}