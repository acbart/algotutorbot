# Python program for weighted job scheduling using Dynamic
# Programming and Binary Search

# Class to represent a job (simple data-only class)
class Job:
    def __init__(self, start: int, finish: int, profit: int):
        self.start: int = start
        self.finish: int = finish
        self.profit: int = profit


# A Binary Search based function to find the latest job
# (before current job) that doesn't conflict with current
# job. "index" is index of the current job. This function
# returns -1 if all jobs before index conflict with it.
def binary_search(job, start_index):
    # https://en.wikipedia.org/wiki/Binary_search_algorithm

    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start_index - 1

    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1


# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(jobs: list[Job]) -> int:
    # Create an array to store solutions of subproblems. job_profits[i]
    # stores the profit for jobs till jobs[i] (including jobs[i])
    n = len(jobs)
    job_profits = [0 for _ in range(n)]

    jobs = sorted(jobs, key=lambda a_job: a_job.start)
    job_profits[0] = jobs[0].profit

    # Fill entries in table[] using recursive property
    for i in range(1, n):
        # Find profit including the current job
        profit_if_included = jobs[i].profit
        next_compatible_job_index = binary_search(jobs, i)
        if next_compatible_job_index != -1:
            profit_if_included += job_profits[next_compatible_job_index]
        else:
            pass  # All previous jobs conflict with this one!

        # Store maximum of including and excluding the job
        job_profits[i] = max(profit_if_included, job_profits[i - 1])

    return job_profits[n - 1]


# Driver code to test above function
example_jobs = [Job(1, 2, 50), Job(3, 5, 20),
                Job(6, 19, 100), Job(2, 100, 200)]
print("Optimal profit is", schedule(example_jobs))