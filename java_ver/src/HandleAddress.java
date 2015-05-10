/**
 * Created by Mo on 2015-05-04.
 */

import org.jsoup.*;
import org.jsoup.nodes.Document;
import java.io.IOException;
import java.util.ArrayList;
import org.jsoup.select.Elements;

public class HandleAddress {
    ArrayList addressList = new ArrayList();
    private static String url = "https://memo.ink/uwall/days.html";

    public ArrayList fetchPage() {
        Document page = null;
        Elements address = null;

        try {
            page = Jsoup.connect(url).get();
        }
        catch (IOException e) {
            System.out.println(e);
        }

        try {
            address = page.select("p#1");
        }
        catch (NullPointerException e) {
            System.out.println(e);
        }

        for (int i = 0; i < address.size(); i++) {
            addressList.add(i, address.eq(i).html());
        }

        System.out.println(address); //带标签结果
        //System.out.println(address.size());  该页链接总数
        //System.out.println(address.html());  该页链接
        return addressList;
    }

    public static void main (String[] args) {
        HandleAddress a = new HandleAddress();
        a.fetchPage();
    }
}

