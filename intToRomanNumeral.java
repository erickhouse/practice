package com.company;

import java.util.*;

public class Main {

    public static String intToRoman(int num) {

        Map<Integer, String> roman = new LinkedHashMap<>();
        roman.put(1000, "M");
        roman.put(900, "CM");
        roman.put(500, "D");
        roman.put(400, "CD");
        roman.put(100, "C");
        roman.put(90, "XC");
        roman.put(50, "L");
        roman.put(40, "XL");
        roman.put(10, "X");
        roman.put(9, "IX");
        roman.put(5, "V");
        roman.put(4, "IV");
        roman.put(1, "I");

        String result = "";
        Integer curr = num;

        while(curr != 0){
            for(int numeral : roman.keySet()) {
                int res = (curr - numeral);

                if(res >= 0){
                    result += roman.get(numeral);
                    curr = res;
                    break;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {

	    System.out.println(intToRoman(3999));
    }
}

