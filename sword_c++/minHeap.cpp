//
// Created by 李先生 on 2018/8/30.
//
// https://blog.csdn.net/wedy542700927/article/details/70616673
#include <vector>
#include <iostream>
using namespace std;

class MaxHeap
{
private:
    vector<int>heap;
    int size;

public:
    void make_heap(vector<int> &nums, int s)
    {
        //从最后一个节点的父节点 开始堆化
        for (int i = size/2 - 1; i>= 0; i--)
        {
            down(i);
        }
    }

    void push(int num)
    {
        heap.push_back(num);
        size ++ ;
        up(size - 1);
    }

    int pop()
    {
        int result = heap[0];
        heap[0] = heap[size - 1];
        heap.pop_back();
        size -- ;
        down(0);
        return  result;
    }

    void down(int index)
    {
        int temp = heap[index];
        index = index *2 + 1; //分别对应父节点的字子节点；

        while (index < size)
        {
            if (index+1 < size && heap[index] < heap[index+1]) index ++;

            //始终index指向最大的子节点

            if (heap[index] < temp) break;
            else
            {
                //将最大值 赋给 父节点的值
                heap[(index - 1) / 2] = heap[index];
                index = index*2 + 1;
            }
        }
        heap[(index - 1) / 2] = temp;
    }

    void up(int index)
    {
        int temp = heap[index];
        while (index > 0 && temp > heap[(index-1)/2] )
        {
            heap[index] = heap[(index - 1)/2];
            index = (index-1)/2;
        }
        heap[index] = temp;
    }
};

