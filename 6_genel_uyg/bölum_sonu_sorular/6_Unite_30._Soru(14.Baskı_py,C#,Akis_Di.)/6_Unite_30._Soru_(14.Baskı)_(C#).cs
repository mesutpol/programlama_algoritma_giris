using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_Unite_30._Soru__14.Baskı___C__
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Kodu yazan Oğuzhan Demirbaş
            //Kodun yazılma tarihi 13.12.2023
            //Kod geliştirilerek geçen ay ve yıl değerleri de eklendi

            // Kullanıcıdan doğum yılını girmesini istenir ve integera çevirilir(convert ile)
            Console.Write("Doğum yılınızı giriniz :");
            int dog_yili =Convert.ToInt32(Console.ReadLine());

            // Kullanıcıdan doğduğu günü girmesini istenir ve integera çevirilir(convert ile)
            Console.Write("Doğduğunuz günü giriniz :");
            int dog_gun = Convert.ToInt32(Console.ReadLine());

            // Kullanıcıdan doğduğu ayı girmesini istenir ve integera çevirilir(convert ile)
            Console.Write("Doğduğunuz ayı giriniz :");
            int dog_ayi = Convert.ToInt32(Console.ReadLine());

            // Bugünün tarihini alır.
            DateTime bugun = DateTime.Today;

            // Kullanıcının girdiği doğum yılı, ayı ve günü kullanarak bir tarih nesnesi oluşturur.
            DateTime dogum_gunu = new DateTime(dog_yili, dog_ayi,dog_gun);

            // Bugün ile doğum tarihi arasındaki farkı hesaplar.
            TimeSpan fark = bugun - dogum_gunu;

            // Yaş hesaplaması yapar.(sadece yıl ile yapılır)
            int yas = bugun.Year - dogum_gunu.Year;

            // Ay hesaplaması yapar. Yaşın 12 ile çarpılması ile elde edilir.
            int ay = yas * 12;

            // Sonuçları ekrana yazdırdık.
            Console.WriteLine($"Bugünün tarihi: {bugun.ToShortDateString()}");
            Console.WriteLine($"Doğum tarihiniz: {dogum_gunu.ToShortDateString()}");
            Console.WriteLine($"Yaşınız: {yas} Yıldır hayattasınız \n{fark.Days} Gündür hayattasınız \n{ay} Aydır hayattasınız");

            // Kullanıcının bir tuşa basmasını bekler (uygulamanın kapatılmaması için,ekranda tutar değerleri).
            Console.ReadKey();


        }
    }
}
