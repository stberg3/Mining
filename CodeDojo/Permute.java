// Permute.java

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Permute<Type> {
  private ArrayList<Type[]> permutations;

  private Type[] swap(Type[] arr, int index_a, int index_b){
    Type temp = arr[index_a];

    arr[index_a] = arr[index_b];
    arr[index_b] = temp;

    return arr;
  }

  public List<Type[]> permute(Type[] arr){
    permutations = new ArrayList<Type[]>();
    permute(arr, 0);

    return permutations;
  }

  public void permute(Type[] arr, int startIndex){
    // System.out.print("\npermuting: ");
    // for( Type a : arr) System.out.print(a+" ");

    if(startIndex < arr.length){
      int swapIndex = startIndex;
      for(int i=startIndex; i<arr.length; i++){
        swap(arr, startIndex, swapIndex);
        permute(arr, startIndex+1);
        swap(arr, startIndex, swapIndex);
        swapIndex++;
      }
    }
    else {
      permutations.add(arr);
      String output = "";
      System.out.print("arr: ");
      for( Type s : permutations.get(permutations.size()-1)){
        System.out.print(s+" ");
        output += (s.toString());
      }
      System.out.println();
      System.out.println(output);
    }
  }

  public static void main(String[] args){
    String input;
    Scanner scanner = new Scanner(System.in);

    if(args.length == 1) input = args[0];
    else input = scanner.next();

    String[] chrs = input.split("(?!^)");
    Permute<String> p = new Permute<String>();

    List<String[]> strings = p.permute(chrs);

    // System.out.println("-------MAIN()-------");
    //
    // for(int i=0; i < strings.size(); i++){
    //   String output = "";
    //   for( String s : strings.get(i)){
    //     output += (s.toString());
    //   }
    //   System.out.println(output + " "+i+" of "+ strings.size());
    // }
  }
}
