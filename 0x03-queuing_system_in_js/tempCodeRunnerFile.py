class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues:
    @staticmethod
    def get_array():
        return [1, 2, 3, 4, 5]

    @staticmethod
    def get_expected_result():
        return 0


class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        return [1, 2, 3, 1, 4, 5]

    @staticmethod
    def get_expected_result():
        return 0