
from typing import List
import numpy as np

class DecisionEngine:

    @staticmethod
    def calculate_vector_rows(matrix, item_count):
        for x in range(item_count):
            total_row_value = 0.0

            for y in range(item_count):
                cell_value = matrix[x, y]
                total_row_value += cell_value
                if x == (item_count - 1):
                    matrix[item_count, y] = total_row_value / item_count

        return matrix

    @staticmethod
    def create_multiplied_normalized_matrix(matrix, item_count):
        for x in range(item_count):
            bottom_cell = matrix[x, item_count]

            for y in range(item_count):
                cell_value = matrix[x, y]
                new_cell_value = cell_value / bottom_cell
                matrix[x, y] = new_cell_value

        return matrix

    @staticmethod
    def set_values_on_normed_matrix(values, matrix: List, item_count):
        def get_inverse(a):
            inverse = np.reciprocal(a)
            return inverse
        count = 0

        for x in range(item_count):
            for y in range(item_count):
                if x >= y:
                    continue
                value = values[count]
                if value < 0:
                    absolute = abs(value)
                    new_value = get_inverse(absolute)
                    matrix[x][y] = new_value
                    matrix[y][x] = absolute
                else:
                    absolute = abs(value)
                    new_value = get_inverse(absolue)
                    matrix[x][y] = absolute
                    matrix[y][x] = new_value
                count += 1

        return matrix

    @staticmethod
    def add_column_totals(matrix, item_count):
        for x in range(item_count):
            column_total_value = 0

            for y in range(item_count):
                column_total_value += (matrix[x, y])

                if y == (item_count - 1):
                    matrix[x, item_count] = column_total_value
        return matrix

    @staticmethod
    def normalize_matrix(matrix, item_count):
        print(matrix)
        try:
            for i in range(item_count):
                matrix[i][i] = (1.0)
            return matrix
        except Exception as e:
            print('didnt work')

    def track_decision(self, values, item_count):
        comparison_matrix = [(item_count + 1), (item_count + 1)]
        normalized_matrix = self.normalize_matrix(comparison_matrix, item_count)
        matrix_with_set_array_values = self.set_values_on_normed_matrix(values, normalized_matrix, item_count)

        matrix_with_added_columns = self.add_column_totals(matrix_with_set_array_values, item_count)
        multiplied_matrix = self.create_multiplied_normalized_matrix(matrix_with_added_columns, item_count)

        matrix_with_evector_rows = self.calculate_vector_rows(multiplied_matrix, item_count)

        return matrix_with_evector_rows
