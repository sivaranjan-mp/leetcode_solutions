class Solution {
    public boolean isPalindrome(String s) {
        String a = s.replaceAll("[^a-zA-Z0-9]", "");
       
        String reversed = "";

        for (int i = a.length() - 1; i >= 0; i--) {
            reversed = reversed + a.charAt(i);
        }

        return a.equalsIgnoreCase(reversed);

    }
}