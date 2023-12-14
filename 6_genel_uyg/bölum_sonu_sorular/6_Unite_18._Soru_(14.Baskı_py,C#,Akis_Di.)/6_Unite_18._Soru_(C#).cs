using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_Unite_18._Soru__C__
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Bir sayı giriniz");
            int Sayi = Convert.ToInt32(Console.ReadLine());
            string Sayi_str = Convert.ToString(Sayi);

            List<int> liste = new List<int>();

            for (int i=0; i < Sayi_str.Length; i++)
            {
                liste.Add(Convert.ToInt32(Sayi_str[i]));
            }
            int Toplam = liste.Sum();
            Console.Write("Toplam :",Toplam);
            Console.ReadKey();





        }
    }
}
