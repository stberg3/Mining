// MinHeap.java
/*
ex:
        1
    3      5
 10   7   6   11

 array = [1, 3, 5, 10, 7, 6, 11]
          0  1  2   3  4  5   6
*/


import java.util.Scanner;

public class MinHeap {
    private final int INIT_SIZE = 10;
    private int[] minHeapArray;
    private int size;


    public MinHeap(){
      minHeapArray = new int[INIT_SIZE];
    }

    private void ensureCapacity(){
      if(size >= minHeapArray.length){
        int[] new_array = new int[size*2];
        for(int i=0; i < size; i++) new_array[i] = minHeapArray[i];
        minHeapArray = new_array;
      }
    }

    private void swap(int indexA, int indexB){
      int temp = minHeapArray[indexA];
      minHeapArray[indexA] = minHeapArray[indexB];
      minHeapArray[indexB] = temp;
    }

    private void siftUp(){
      int index = size-1;
      int temp;

      System.out.print(".");
      while(hasParent(index)){
        System.out.print(".");
        if(minHeapArray[index]<getParent(index)) break;
        temp = minHeapArray[index];
        minHeapArray[index] = minHeapArray[getParentIndex(index)];
        minHeapArray[getParentIndex(index)] = temp;
        swap(index, getParentIndex(index));
        index = getParentIndex(index);
      }

      System.out.println();
    } // end siftUp()

    private void siftDown(){
      int largerIndex = 0;
      int currentIndex = 0;
      int largerValue = minHeapArray[0];
      int temp;

      while(hasLeftChild(currentIndex)){
        if(largerValue < getLeftChild(currentIndex)){
          largerValue = getLeftChild(currentIndex);
          largerIndex = getLeftChildIndex(currentIndex);
        }
        else
          break;

        if(hasRightChild(currentIndex) && largerValue < getRightChild(currentIndex)){
            largerIndex = getRightChildIndex(currentIndex);
            largerValue = getRightChild(currentIndex);
        }

        swap(currentIndex, largerIndex);
        currentIndex = largerIndex;
      }
    } // end siftDown

    public void insert(int value){
      ensureCapacity();
      minHeapArray[size] = value;
      size++;
      siftUp();
    }

    public boolean isEmpty(){
      return size == 0;
    }

    public int getMin(){
      if(isEmpty()) {
        throw new IllegalStateException("Heap is empty - no min value");
      }

      return minHeapArray[0];
    }

    private int getParent(int index){
      if(!hasParent(index))
        throw new IllegalStateException("Node has no parent");

      return minHeapArray[getParentIndex(index)];
    }

    private int getLeftChild(int index){
      if(!hasLeftChild(index))
          throw new IllegalStateException("Node has no left child");
      return minHeapArray[getLeftChildIndex(index)];
    }

    private int getRightChild(int index){
      if(!hasRightChild(index))
        throw new IllegalStateException("Node has no right child");

      return minHeapArray[getRightChildIndex(index)];
    }

    private boolean hasParent(int index){ return index>0; }
    private boolean hasLeftChild(int index){ return getLeftChildIndex(index) < size; }
    private boolean hasRightChild(int index){ return getRightChildIndex(index) < size; }

    private int getParentIndex(int index){ return (index-1)/2; }
    private int getLeftChildIndex(int index){ return index*2+1; }
    private int getRightChildIndex(int index){ return index*2+2; }

    public static void main(String args[]){
      MinHeap heap = new MinHeap();
      Scanner scan = new Scanner(System.in);
      int n = scan.nextInt();

      for(int i=0; i<n; i++){
        heap.insert(scan.nextInt());
      }

      System.out.println("Heap min: "+ heap.getMin());

    }
}
