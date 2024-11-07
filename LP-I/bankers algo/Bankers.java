import java.util.*;

public class Bankers {
    private int[][] need, allocate, max, available;
    private int no_proc, no_res;

    private void input() {
        Scanner in = new Scanner(System.in);

        System.out.print("\nNo. of Resources: ");
        no_res = in.nextInt();
        System.out.print("\nNo. of Processes: ");
        no_proc = in.nextInt();

        need = new int[no_proc][no_res];
        max = new int[no_proc][no_res];
        allocate = new int[no_proc][no_res];
        available = new int[1][no_res];

        /* Input the allocation matrix */
        System.out.print("\nAllocation Matrix:\n");
        for (int i = 0; i < no_proc; i++) {
            for (int j = 0; j < no_res; j++) {
                allocate[i][j] = in.nextInt();
            }
        }                                                    

        /* Input the max matrix */
        System.out.print("\nMaximum Need:\n");
        for (int i = 0; i < no_proc; i++) {
            for (int j = 0; j < no_res; j++) {
                max[i][j] = in.nextInt();
            }
        }

        /* Input the available resources */
        System.out.print("\nAvailable resources:\n");
        for (int i = 0; i < no_res; i++) {
            available[0][i] = in.nextInt();
        }

        in.close();
    }

    /* Calculate the need matrix */
    private void find_need() {
        for (int i = 0; i < no_proc; i++) {
            for (int j = 0; j < no_res; j++) {
                need[i][j] = max[i][j] - allocate[i][j];
            }
        }
    }

    /* Check if all resources for a process can be allocated */
    private boolean check_resource_allocation(int row) {    //specific process ka liya resource alloacte hu skta hai ya nahi
        for (int i = 0; i < no_res; i++) {
            if (available[0][i] < need[row][i]) {
                return false;
            }
        }
        return true;
    }

    public void is_Safe() {
        int j = 0;
        input();
        find_need();
        boolean[] done = new boolean[no_proc];
        boolean allocated;

        while (j < no_proc) {    //check all process safely execute
            allocated = false;

            for (int i = 0; i < no_proc; i++) {
                if (!done[i] && check_resource_allocation(i)) {
                    for (int k = 0; k < no_res; k++) {
                        available[0][k] = available[0][k] - need[i][k] + max[i][k];
                    }

                    System.out.println("\nAllocated Process: " + i);
                    allocated = done[i] = true;
                    j++;
                }
            }

            if (!allocated) {
                break;
            }
        }

        if (j == no_proc) {
            System.out.println("\nSafely Allocated\n");
        } else {
            System.out.println("\nAll processes can't be allocated safely\n");
        }
    }

    /* Beginning of the main function */
    public static void main(String args[]) {
        new Bankers().is_Safe();
    }
}


//processes -5, resources - 3
//Allocation  max need   Available
//0 1 0       7 5 3      3 3 2
//2 0 0       3 2 2      
//3 0 2       9 0 2
//2 1 1       4 2 2 
//0 0 2       5 3 3
