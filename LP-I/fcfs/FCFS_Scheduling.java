import java.util.Scanner;

public class FCFS_Scheduling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        float avgtat = 0, avgwt = 0;

        System.out.println("*First Come First Serve Scheduling*");
        System.out.print("Enter number of Processes: ");
        n = scanner.nextInt();

        int[] process = new int[n];
        int[] arrivalTime = new int[n];
        int[] burstTime = new int[n];
        int[] completionTime = new int[n];
        int[] TAT = new int[n]; // Turn Around Time
        int[] waitingTime = new int[n];

        // Input Arrival and Burst times
        for (int i = 0; i < n; i++) {
            process[i] = i + 1;
            System.out.print("\nEnter Arrival time for process " + (i + 1) + ": ");
            arrivalTime[i] = scanner.nextInt();
            System.out.print("Enter Burst time for process " + (i + 1) + ": ");
            burstTime[i] = scanner.nextInt();
        }

        // Sort processes by Arrival Time
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arrivalTime[i] > arrivalTime[j]) {
                    // Swap process number
                    int temp = process[i];
                    process[i] = process[j];
                    process[j] = temp;

                    // Swap arrival time
                    temp = arrivalTime[i];
                    arrivalTime[i] = arrivalTime[j];
                    arrivalTime[j] = temp;

                    // Swap burst time
                    temp = burstTime[i];
                    burstTime[i] = burstTime[j];
                    burstTime[j] = temp;
                }
            }
        }

        // Calculate completion time
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                completionTime[i] = arrivalTime[i] + burstTime[i];
            } else {
                if (arrivalTime[i] > completionTime[i - 1]) {
                    completionTime[i] = arrivalTime[i] + burstTime[i];
                } else {
                    completionTime[i] = completionTime[i - 1] + burstTime[i];
                }
            }
        }

        // Output header
        System.out.println("*First Come First Serve Scheduling*");
        System.out.println("Processor\tArrival time\tBurst time\tCompletion Time\tTurn around time\tWaiting time");
        System.out.println("---------------------------------------------------------------------------------------------------------");

        // Calculate TAT and Waiting Time and print details
        for (int i = 0; i < n; i++) {
            TAT[i] = completionTime[i] - arrivalTime[i]; // Turn Around Time
            waitingTime[i] = TAT[i] - burstTime[i];      // Waiting Time

            avgtat += TAT[i];
            avgwt += waitingTime[i];

            // Print process details
            System.out.println("P" + process[i] + "\t\t" + arrivalTime[i] + "ms\t\t" + burstTime[i] + "ms\t\t" + completionTime[i]
                    + "ms\t\t\t" + TAT[i] + "ms\t\t\t" + waitingTime[i] + "ms");
        }

        // Print average times
        System.out.println("Average Turn around time of Processes: " + (avgtat / n) + "ms");
        System.out.println("Average waiting time of Processes: " + (avgwt / n) + "ms");

        scanner.close();
    }
}