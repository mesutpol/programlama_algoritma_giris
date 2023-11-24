using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_Unite_1_Soru_C__
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Kodu yazan Oğuzhan Demirbaş
            //Kodun yazılma tarihi 24.11.2023

            int a, h, Alan;//Kullanacağımız değişkenleri int olarak tanımlıyoruz
            Console.Write("Üçgende yüksekliğin indiği kenarı girin :");//WriteLine yerine Write kullanarak yükseklik bilgisini yanına yan satırda yazdırıyoruz

            a = Convert.ToInt32(Console.ReadLine());//string ifadeyi convert fonk. ile integer ifadeye çevirdik.
            Console.Write("Üçgenin yüksekliğini griniz :");
            h = Convert.ToInt32(Console.ReadLine());
            Alan = (a * h) / 2;
            Console.Write("Üçgenin alanı : " + Alan);//Hesapladığımız alanı yazdırdık.
            Console.ReadKey();//Ekrandan sürekli gözükmesini sağladık.

        }
    }
}
