//Kodu geliştiren Oğuzhan Demirbaş
//Geliştirilme tarihi 5.11.2023
//Geliştirilme amacı :6 Dilde aynı algoritmayı çalıştırarak arasıdnaki farkları görmek

using System;

class Program 
{
    static void Main() 
    {
        Console.Write("Satır sayısını girin: ");//Kullanıcıdan satır sayısı alınır
        int Satır_yıldız = int.Parse(Console.ReadLine());//Kullanıcıdan alınan metni tam sayıya dönüştür ve Satır_yıldız adlı değişkene kaydediyoruz

        Console.Write("Sütun sayısını girin: ");
        int Sutun_yıldız = int.Parse(Console.ReadLine());////Kullanıcıdan alınan metni tam sayıya dönüştür ve Sutun_yıldız adlı değişkene kaydediyoruz

        for (int i = 0; i < Satır_yıldız; i++)//Dıştaki for döngüsü, i değişkeni kullanarak Satır_yıldız sayısı kadar tekrarlanır. Bu, kaç satır olduğunu belirtir.
        {
            for (int j = 0; j < Sutun_yıldız; j++)//İçteki for döngüsü, j değişkeni kullanarak Sutun_yıldız sayısı kadar tekrarlanır. Bu, her satırda kaç yıldız (*) karakterinin olacağını belirtir.
            {
                Console.Write("*"); //Ekrana "*" Yazdır
            }
            Console.WriteLine(); //Her satırın sonunda yeni bir satıra geç
        }
    }
}