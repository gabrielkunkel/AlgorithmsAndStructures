package com.gabrielkunkel.challenges.twopointers;

public class IsPalindrome {

    public static boolean offTheCuff(String s) {

        var left = 0;
        var right = s.length() - 1;

        while (left < right) {
            // Skip non-alphanumeric characters
            while(left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            while(left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // Compare characters
            if(left < right) {
                if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                    // Characters do not match; hence, it's not a palindrome
                    return false;
                }
                // Move pointers inward
                left++;
                right--;
            }
        }

        // If the whole string was traversed without mismatch, it's a palindrome
        return true;
    }


}
