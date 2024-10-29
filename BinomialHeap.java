/**
 * BinomialHeap
 *
 * An implementation of binomial heap over non-negative integers.
 * Based on exercise from previous semester.
 */

public class BinomialHeap
{
    public int size;
    public HeapNode last;
    public HeapNode min;


    public BinomialHeap(HeapNode last) {
        if (last != null) {
            this.last = last;
            HeapNode start = last.next;
            this.last.next = null;
            this.size = 0;
            this.min = start;
            HeapNode curr = start;
            while (curr != null) {
                this.size += (int) Math.pow(2, curr.rank);
                this.min = this.min.item.key < curr.item.key ? this.min : curr;
                curr.parent = null;
                curr = curr.next;
            }
            this.last.next = start;
        }
        else {
            this.last = null;
            this.size = 0;
            this.min = null;
            return;
        }


    }




    /*default constructor*/
    public BinomialHeap(){
        this.last = null;
        this.min = null;
        this.size = 0;
    }



    /**
     *
     * pre: key > 0
     *
     * Insert (key,info) into the heap and return the newly generated HeapItem.
     *
     */

    public HeapItem insert(int key, String info)
    {
        HeapNode inserted = new HeapNode(key, info, null, null, null, 0);
        HeapItem returned = inserted.item;
        this.size += 1;
        if (this.last == null) {
            this.last = inserted;
            inserted.next = inserted;
            this.min = inserted;
            return inserted.item;
        }
        /* Changed */
        if ((this.size) % 2 == 1) {
            HeapNode tmp = this.last.next;
            this.last.next = inserted;
            inserted.next = tmp;
            return inserted.item;
        }

        inserted.next = this.last.next;
        this.last.next = inserted;
        HeapNode new_min = this.ReorganizeHeap();
        this.min = new_min;
        return returned;
    }

    /**
     *
     * Delete the minimal item
     *
     */
    public void deleteMin()
    {
        BinomialHeap sub_heap = new BinomialHeap(this.min.child);
        if (this.last == this.last.next) {
            this.min = null;
            this.last = null;
        }
        else {
            HeapNode curr = this.last;
            while (curr.next != this.min) {
                curr = curr.next;
            }
            if (this.last == curr.next)
                this.last = curr;

            curr.next = curr.next.next;
        }
        this.size = this.size - sub_heap.size - 1;


        this.meld(sub_heap);
        return;
    }


    /**
     *
     * Return the minimal HeapItem
     *
     */
    public HeapItem findMin()
    {
        HeapItem item = this.min.item;
        return item;
    }

    /**
     *
     * pre: 0 < diff < item.key
     *
     * Decrease the key of item by diff and fix the heap.
     *
     */
    public void decreaseKey(HeapItem item, int diff)
    {
        HeapItem new_min;
        if(Integer.MAX_VALUE != diff)
            item.key -= diff;
        else
            item.key = Integer.MIN_VALUE;

        if(item.key < this.min.item.key)
            new_min = item;
        else
            new_min = this.min.item;
        this.MoveUp(item.node);
        this.min = new_min.node;
        return ;
    }

    /**
     *
     * Delete the item from the heap.
     *
     */
    public void delete(HeapItem item)
    {
        this.decreaseKey(item, Integer.MAX_VALUE);
        this.deleteMin();
    }

    /**
     *
     * Meld the heap with heap2
     *
     */
    public void meld(BinomialHeap heap2)
    {


        if (heap2.empty()) {
            this.min = this.findMin2();
            return;
        }

        if (this.empty()) {
            this.last = heap2.last;
            this.min = heap2.min;
            this.size = heap2.size;
            return;
        }


        this.size += heap2.size;
        HeapNode node_a = this.last.next;
        HeapNode node_b = heap2.last.next;
        boolean advanced_a = false;
        HeapNode source_node = new HeapNode();
        boolean advanced_b = false;
        HeapNode new_start = null;
        while (!(advanced_a && node_a == this.last.next) && !(advanced_b && node_b == heap2.last.next)) {
            if (node_a.rank < node_b.rank) {
                if (new_start == null) {
                    new_start = node_a;
                }
                if (node_a == this.last.next) {
                    advanced_a = true;
                }

                source_node.next = node_a;
                source_node = node_a;
                node_a = node_a.next;
            } else {
                if (new_start == null) {
                    new_start = node_b;
                }

                if (node_b == heap2.last.next) {
                    advanced_b = true;
                }

                source_node.next = node_b;
                source_node = node_b;
                node_b = node_b.next;
            }
        }
        if (source_node == this.last) {
            source_node.next = node_b;
            this.last = heap2.last;
        } else {
            source_node.next = node_a;
        }
        this.last.next = new_start;
        HeapNode new_min = this.ReorganizeHeap();
        this.min = new_min;
        return;
    }



    private HeapNode ReorganizeHeap() {
        if (this.size == 0) {
            return null;
        }
        if (this.size == 1) {
            this.min = this.last;
            return this.last;
        }

        HeapNode start = null;
        HeapNode prev = null;
        HeapNode root = this.last.next;
        HeapNode nextr = root.next;
        this.last.next = null;
        HeapNode new_min = null;

        while (nextr != null) {

            if (root.rank != nextr.rank) {
                if (start == null) {
                    start = root;
                }
                prev = root;
                root = root.next;
                nextr = root.next;
                continue;
            }

            if (nextr != this.last && nextr.rank == nextr.next.rank) {
                if (start == null) {
                    start = root;
                }
                root.next = HeapNode.Join(nextr, nextr.next, root);
                prev = root;
                root = root.next;
                nextr = root.next;
                continue;
            }

            HeapNode res = HeapNode.Join(root, nextr, prev);
            if (start == root || start == null) {
                start = res;
            }
            root = res;
            nextr = root.next;

        }
        this.last = root;
        this.last.next = start;
        new_min = this.findMin2();
        return new_min;
    }

    /**
     *
     * Get the new minimum value after deleting minimum
     * Time complexity: O(log(n))
     *
     */
    private HeapNode findMin2() {
        if (this.size() == 0) {
            return null;
        }
        HeapNode start = this.last.next;
        this.last.next = null;
        HeapNode curr = start;
        HeapNode new_min = curr;

        while (curr != null) {
            if (new_min.item.key >= curr.item.key){
                new_min = curr;
            }

            curr = curr.next;
        }

        this.last.next = start;
        return new_min;
    }


    /**
     *
     * Return the number of elements in the heap
     *
     */
    public int size()
    {
        return this.size;
    }



    private void MoveUp(HeapNode x) {
        HeapNode parent = x.parent;
        while (parent != null && x.item.key < parent.item.key) {
            HeapItem tmp = parent.item;
            parent.item = x.item;
            x.item.node = parent;
            x.item = tmp;
            tmp.node = x;
            x = parent;
            parent = x.parent;
        }
        return;
    }

    /**
     *
     * The method returns true if and only if the heap
     * is empty.
     *
     */
    public boolean empty()
    {
        return (this.size ==0);
    }

    /**
     *
     * Return the number of trees in the heap.
     *
     */
    public int numTrees()
    {

        int res = 0;
        int balance = this.size;
        while (balance > 0) {
            balance = balance / 2;
            if (balance % 2 == 1) {
                res += 1;
            }
        }
        return res;
    }



    /**
     * Class implementing a node in a Binomial Heap.
     *
     */
    public class HeapNode{
        public HeapItem item;
        public HeapNode child;
        public HeapNode next;
        public HeapNode parent;
        public int rank;
        public HeapNode(int key, String info, HeapNode child, HeapNode next, HeapNode parent, int rank) {
            this.item = new HeapItem(this, key, info);
            this.child = child;
            this.next = next;
            this.parent = parent;
            this.rank = rank;
        }

        public HeapNode() {
            this.item = null;
            this.child = null;
            this.next = null;
            this.parent = null;
            this.rank = 0;
        }

        /**
         *
         * @param node1: HeapNode 1
         * @param node2: HeapNode 2
         * @param prev:  The previous HeapNode to node1
         * @return: The new root after link
         *
         *          Time complexity: O(1)
         */
        public static HeapNode Join(HeapNode node1, HeapNode node2, HeapNode prev) {
            boolean flag = false;

            HeapNode small = node1;
            HeapNode big = node2;

            if (small.item.key > big.item.key) {
                HeapNode tmp = small;
                small = big;
                big = tmp;
                if (prev != null) {
                    prev.next = small;
                }
                flag = true;
            }
            if (!flag) {
                small.next = big.next;
            }
            if(small.child != null) {
                big.next = small.child.next;
                small.child.next = big;
                small.child = big;
                big.parent = small;

            } else {
                small.child = big;
                big.next = big;
                big.parent = small;
            }

            small.rank += 1;

            return small;
        }

    }

    /**
     * Class implementing an item in a Binomial Heap.
     *
     */

    public class HeapItem {
        public HeapNode node;
        public int key;
        public String info;

        public HeapItem(HeapNode node, int key, String info) {
            this.node = node;
            this.key = key;
            this.info = info;
        }

        public HeapItem() {
            this.node = null;
            this.key = 0;
            this.info = "";
        }

    }
}

