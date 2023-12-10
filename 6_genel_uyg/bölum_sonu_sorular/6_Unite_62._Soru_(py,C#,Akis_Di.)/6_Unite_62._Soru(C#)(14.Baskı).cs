using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_Unite_62._Soru_C__
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Kodu yazan Oğuzhan Demirbaş
            // Kodun yazılma tarihi 9.12.2023

            //Hilbert sayısı:Bir eksiği 4'e tam bölünebilen pozitif tam sayılardır.

            Console.Write("Kaç adet 'HİLBERT' sayısı oluşturmak istersiniz :");
            //String ifadeyi convert ettik integer değere çevirdik
            int N= Convert.ToInt32(Console.ReadLine());
            //say-lis adında boş liste oluşturduk
            List<int> say_lis = new List<int>();
            //k değerini 1'den başlattık N den küçük eşit olana kadar döngüye soktuk ve i++ komutu ile 1 arttırdık
            for (int k = 1; k <= N; k++)
            {
                int sayi = k * 4 + 1;  
            //say_lis'te sayi değerini ekledik
                say_lis.Add(sayi);        
            }
            // foreach say_lis üzerinde dolaşarak her veriyi teker teker yazdırır
            foreach (var say in say_lis)
            {
                Console.Write(say+"\n");
            }
            Console.ReadKey();          
        }
    }
}
