// LinkedList.java

import java.util.Iterator;
import java.util.HashSet;
import java.util.Scanner;
import java.lang.Iterable;

public class Stack<Type> implements Iterable<Type> {
  private int length;

  private class Node {
    public Node next;
    public Type data;

    public Node(Type data){
      this.next = null;
      this.data = data;
    }
  }

  public String toString(){
    Node probe = head.next;
    String s =  "[";

    while(probe != null){
      if(probe.next != null)
        s+=String.format("%d, ", probe.data);
      else
        s+=String.format("%d", probe.data);
      probe = probe.next;
    }

    s += "]";

    return s;
  }

  public Type get(int index){
    if(index >= size()) throw new IllegalArgumentException("Index OOB");
    Node probe = head;

    for(int i=0; i<index+1; i++){
        probe = probe.next;
    }

    return probe.data;
  }

  public boolean isEmpty(){ return size() == 0; }

  public Type remove(int index){
    if(index >= size() || index < 0) throw new IllegalArgumentException("Index OOB");
    if(isEmpty()) throw new IllegalStateException("List empty");

    Node l_probe = head;
    Node r_probe = head.next;


    for(int i=0; i<index; i++){
        l_probe = r_probe;
        r_probe = r_probe.next;
    }

    Type data = r_probe.data;

    l_probe.next=r_probe.next;

    return data;
  }

  private Node head;

  public Node Head(){
    return head;
  }

  private class StackIterator implements Iterator<Type> {
    private Node my_head = head;
    public boolean hasNext() { return ! (my_head.next==null); }
    public Type next() {
      Type data = head.next.data;
      my_head = my_head.next;
      return data;
    }
  }

  public Iterator<Type> iterator(){ return new StackIterator(); }

  public Stack(){
    head = new Node(null);
    head.next = null;
    head.data = null;
    length = 0;
  }

  public Type peek(){
    if(head.next == null){
      throw new IllegalStateException("Cannot peek: List empty");
    }
    else {
      return head.next.data;
    }
  }

  public Type pop(){
    if(head.next == null){
      throw new IllegalStateException("Cannot pop: List empty");
    }
    else {
      // System.out.println("Popping head.next:\t"+ head.next.data + "\tsz: "+length);
      Node poppee = head.next;
      head.next = poppee.next;
      length--;
      return poppee.data;
    }
  }

  public void push(Type data){
    Node nnode = new Node(data);
    nnode.next = head.next;
    head.next = nnode;
    length++;

    // System.out.println("Pushed head.next:\t"+ head.next.data + "\tsz: "+length);
  }

  public void removeDuplicates(){
    HashSet<Type> entries = new HashSet<Type>();
    Node l_probe = head;
    Node r_probe = head.next;
    if(r_probe == null) return;

    while(r_probe != null) {
      System.out.println(r_probe.data +" in set?\t"+entries.contains(r_probe.data));
      if(entries.contains(r_probe.data)){
        l_probe.next = r_probe.next;
      }
      else {
        entries.add(r_probe.data);
        l_probe = r_probe;
      }
      r_probe = r_probe.next;
    }

    for(Type el : entries) System.out.print(el+" ");
    System.out.println();
  }

  public int size(){
    return length;
  }

  // public static void main(String[] args){
  //   int n;
  //   Stack<String> ll = new Stack<String>();
  //   if(args.length > 0){
  //     n = args.length - 0;
  //   } else
  //     throw new IllegalArgumentException(
  //       String.format("Usage: %s %s <at least one token>", "java", "Stack"));
  //
  //   for(int i=0; i<args.length; i++) {
  //     ll.push(args[i]);
  //   }
  //
  //   ll.removeDuplicates();
  //
  //   for(String el : ll){
  //     System.out.println(ll.pop());
  //   }
  // }
}
