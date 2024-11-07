import java.util.Scanner;
class SjfNp
{
   public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    System.out.println("Enter no. of process : ");
    int n = sc.nextInt();
    int pid[] = new int[n]; 
    int at[] = new int[n];
    int bt[] = new int[n];
    int ct[] = new int[n];
    int tat[] = new int[n];
    int wt[] = new int[n];
    int f[] = new int[n];
    float avgwt = 0, avgtat = 0;

    for(int i = 0; i < n; i++)
    {
      System.out.println("Enter process id: ");
      pid[i] = sc.nextInt();

      System.out.println("Enter Arrival time: ");
      at[i] = sc.nextInt();

      System.out.println("Enter Burst time: ");
      bt[i] = sc.nextInt();
      
      f[i] = 0;
    }
    sc.close();

    int st = 0;
    int total = 0;

    while(true)
    {
       if(total == n)
            break;
        int c = n;
        int min = 99;
        for(int i = 0; i < n; i++)
        {
            if(at[i] <= st && f[i] == 0 && bt[i] < min)
            {
                c = i;
                min = bt[i];
            }
        }

        if(c == n)
        {
            st += 1;
        }
        else
        {
            ct[c] = st + bt[c];
            f[c] = 1;
            st = ct[c];
            total++;
        }     
    }

    for(int k = 0; k < n; k++)
    {
        tat[k] = ct[k] - at[k];
        wt[k] = tat[k] - bt[k];
        avgwt += wt[k];
        avgtat += tat[k];
    }
    
    System.out.println("Process\tArrival time\tBurst time\tCompletion Time\tTurn around time\tWaiting time");
    System.out.println(
            "-------------------------------------------------------------------------------------");
    for(int j = 0; j < n; j++)
    {
        System.out.println(pid[j] + "\t\t" + at[j] + "\t\t" + bt[j] + "\t\t" + ct[j] + "\t\t" + tat[j] + "\t\t\t" + wt[j]);
    }
    
    System.out.println("\nAverage Turn Around Time: " + (avgtat / n));
    System.out.println("Average Waiting Time: " + (avgwt / n));
   }
}
