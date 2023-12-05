//Kodu geliştiren Oğuzhan Demirbaş
//Geliştirilme tarihi 5.11.2023
//Geliştirilme amacı :6 Dilde aynı algoritmayı çalıştırarak arasıdnaki farkları görmek


#include <stdio.h>//Her C programına standart giriş/çıkış işlemlerini yapan stdio.h dosyası çağrılır

int main() {
    int Satır_yıldız, Sutun_yıldız;

    printf("Satır sayısını girin: ");//Kullanıcıdan satır bilgisi iste
    scanf("%d", &Satır_yıldız);// klavyeden girilen satır sayıyısını alın

    printf("Sütun sayısını girin: ");//Kullanıcıdan sütün bilgisi iste
    scanf("%d", &Sutun_yıldız);//klavyeden girilen sütün sayıyısını alın

    // Satır ve sütunları dolaşarak '*' karakterleri ile doldur
    for (int i = 0; i < Satır_yıldız; i++) {//For döngüsü ile i'yi "0" dan başlat satır sayısınadan küçük olana kadar 1 arttır
        for (int j = 0; j < Sutun_yıldız; j++) {//For döngüsü ile j'yi "0" dan başlat sütün sayısıdan küçük olana kadar 1 arttır
            printf("*");
        }
        printf("\n"); // Her satırın sonunda yeni satıra geç
    }

    return 0;//Bu ifade, programın sonunda kullanılır ve programın sona erdiğini ve başarılı bir şekilde çalıştığını belirtir.
}