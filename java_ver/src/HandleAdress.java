/**
 * Created by Mo on 2015-05-04.
 */

import org.jsoup.*;
import org.jsoup.nodes.Document;
import java.io.IOException;

import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.client.params.HttpClientParams;

public class HandleAdress {
    String [] addressList = new String[10];
    private static String url = "https://memo.ink/uwall/hello.html";

    public String fetchPage() {
        Document page = null;
        String sourcePage = null;

        try {
            page = Jsoup.connect(url).get();
        }
        catch (IOException e) {
            System.out.println(e);
        }

        try {
            sourcePage = page.html();
        }
        catch (NullPointerException e) {
            System.out.println(e);
        }
        System.out.println(sourcePage);
        return sourcePage;
    }

    public static void main (String[] args) {
        HandleAdress a = new HandleAdress();
        a.fetchPage();
    }
}

