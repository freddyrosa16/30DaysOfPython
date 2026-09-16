import statistics
from collections import Counter


# Exercises: Level 1

# 1. Build a Statistics class that stores numeric data on each instance.
# Implement these methods yourself, reusing methods where helpful:
# count(), sum(), min(), max(), range(), mean(), median(), mode(),
# std(), var(), freq_dist(), and describe().
# Also support percentile(p); choose and document a percentile convention
# because the lesson does not specify one.
# Return frequencies as (percentage, value) pairs, highest frequency first.
# Have describe() summarize the calculated statistics in readable text.
# Instantiate your class with these ages and call each method:
# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
#         33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
# Checks: count 25; sum 744; minimum 24; maximum 38; median 29.
# Clarification: the exact mean is 29.76; the lesson displays it rounded.
# Use population variance to match its example (approximately 17.5),
# despite the prompt calling the data a sample.

# Write your answer below.
class Statistics:
    def __init__(self, ages):
        self.ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

    def count(self, ages):
        return len(ages)

    def sum(self, ages):
        return sum(ages)

    def min(self, ages):
        return min(ages)

    def max(self, ages):
        return max(ages)

    def range(self, ages):
        return self.max(ages) - self.min(ages)

    def mean(self, ages):
        return statistics.mean(ages)

    def median(self, ages):
        return statistics.median(ages)

    def mode(self, ages):
        return statistics.mode(ages)

    def std(self, ages):
        return statistics.pstdev(ages)

    def var(self, ages):
        return statistics.variance(ages)

    def freq_dist(self, ages):
        return Counter(ages)

    def percentile(self, p, ages):
        if not 0 <= p <= 100:
            raise ValueError("Percentile must be between 0 and 100.")
        if not ages:
            raise ValueError("At least one age is required.")

        sorting_ages = sorted(ages)
        position = (p / 100) * (len(ages) - 1)
        lower_index = int(position)

        fraction = position - lower_index
        if fraction == 0:
            return sorting_ages[lower_index]

        lower_value = sorting_ages[lower_index]
        upper_value = sorting_ages[lower_index + 1]
        return lower_value + fraction * (upper_value - lower_value)


    def describe(self, ages):
        return (
            f"Count: {self.count(ages)}\n"
            f"Sum: {self.sum(ages)}\n"
            f"Min: {self.min(ages)}\n"
            f"Max: {self.max(ages)}\n"
            f"Range: {self.range(ages)}\n"
            f"Mean: {self.mean(ages)}\n"
            f"Median: {self.median(ages)}\n"
            f"Mode: {self.mode(ages)}\n"
            f"Variance: {self.var(ages)}\n"
            f"Standard Deviation: {self.std(ages)}\n"
            f"Frequency Distribution: {self.freq_dist(ages)}"
        )


# Exercises: Level 2

# 1. Build PersonAccount with firstname, lastname, incomes, and expenses.
# Store income and expense entries as sets of (amount, description) pairs.
# Implement total_income(), total_expense(), account_info(),
# add_income(amount, description), add_expense(amount, description),
# and account_balance(). The balance is income minus expenses.
# Create an account, add entries, and display its summary and balance.

# Write your answer below.
