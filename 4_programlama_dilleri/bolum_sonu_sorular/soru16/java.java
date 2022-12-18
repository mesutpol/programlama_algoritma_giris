import java.io.*;
class IsimYazdirma{						       
    public static void main(String args[]) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        PrintName pn=new PrintName();			
        System.out.print("Isminizi Giriniz : ");
        String nameread=br.readLine();
	pn.setWish(nameread);

    }
}
