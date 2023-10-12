using System.Diagnostics;
using System;

namespace programlama_algoritma_giris
{
    internal class Program
    {
        static void Main(string[] args)
        {

            try // try-catch bloğu ile kullanıcıdan alınan değerin float olup olmadığı kontrol ediliyor.
            {
                Console.Write("Lütfen bir değer girin: "); // Kullanıcıdan bir değer isteniyor.
                string userInput = Console.ReadLine(); // Girilen değer string olarak alınıyor.

                float floatValue = float.Parse(userInput); // Girilen değer float olarak değişkene atanıyor.

                if(floatValue < 50) // Girilen değer 50'den küçükse ekrana "Girdiğiniz Sayı 50'den Küçük." yazdırılıyor.
                {
                    Console.WriteLine("Girdiğiniz Sayı 50'den Küçük.");
                }
                else if (floatValue > 50) // Girilen değer 50'den büyükse ekrana "Girdiğiniz Sayı 50'den Büyük." yazdırılıyor.
                {
                    Console.WriteLine("Girdiğiniz Sayı 50'den Büyük.");
                } else // Girilen değer 50'ye eşitse ekrana "Girdiğiniz Sayı 50'ye Eşit." yazdırılıyor.
                {
                    Console.WriteLine("Girdiğiniz sayı 50'ye eşit.");
                }
            }
            catch (FormatException) // Girilen değer float değilse ekrana "Hatalı giriş! Bir float değer girin." yazdırılıyor.
            {
                Console.WriteLine("Hatalı giriş! Bir float değer girin."); // Hata mesajı.
            }
        }
    }
}