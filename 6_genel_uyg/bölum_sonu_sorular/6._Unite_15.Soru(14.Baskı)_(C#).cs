using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_Unite_15._Soru_C__
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //Kodu yazan Oğuzhan Demirbaş
            //Kodun yazılma tarihi 26.11.2023

            Console.Write("Bir 'E' değeri girin :");//25.Kod satırına kadar bize soruda verilen değişkenleri kullanıcıdan istedik ve double türüne çevirdik.
            double E = Convert.ToDouble(Console.ReadLine());
            Console.Write("Bir 'R1' değeri girin :");
            double R1 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Bir 'R2' değeri girin :");
            double R2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Bir 'R3' değeri girin :");
            double R3 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Bir 'R4' değeri girin :");
            double R4 = Convert.ToDouble(Console.ReadLine());

            double I = E / (R1 + R2 + R3 + R4);
            double VR1 = R1 * I;
            double PR2 = I * I * R2;

            Console.WriteLine($"VR1 :{VR1} \nPR2 :{PR2} \nI :{I}");//Burada süslü parantez içine değişkenleri çağırdık.
            Console.ReadKey();
        }
    }
}
