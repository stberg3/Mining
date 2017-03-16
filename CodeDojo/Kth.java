// Kth.java

public class Kth {
  public static void main(String[] args) {
    final int max = 10;
    int index;
    int back_index;
    if(args.length != 1 || Integer.parseInt(args[0]) > 10)
      throw new IllegalArgumentException(
        String.format("Usage: java Kth <number (0-%d)>", max-1));
    else{
      back_index = Integer.parseInt(args[0]);
      index = max - 1 - back_index;
    }

    Stack<Integer> ll = new Stack<Integer>();

    for(int i=0; i<max; i++) ll.push(i);

    System.out.println(ll);
    ll.remove(back_index);
    System.out.println(ll);
  }
}
