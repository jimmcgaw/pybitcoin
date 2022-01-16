from multiprocessing.sharedctypes import Value
import pytest

from ..field_element import FieldElement


class TestFieldElement:
    def test_cannot_initialize_with_negative_value(self):
        with pytest.raises(ValueError):
            FieldElement(-1, 13)

    def test_cannot_init_with_value_exceeding_prime(self):
        with pytest.raises(ValueError):
            FieldElement(20, 13)

    def test_field_elements_diff_primes_not_equal(self):
        fe1 = FieldElement(6, 13)
        fe2 = FieldElement(6, 16)
        assert not fe1 == fe2
        assert fe1 != fe2

    def test_field_elements_same_value_and_prime_are_equal(self):
        fe1 = FieldElement(6, 13)
        fe2 = FieldElement(6, 13)
        assert fe1 == fe2
        assert not fe1 != fe2

    def test_add_elements_same_field_modulo(self):
        fe1 = FieldElement(11, 13)
        fe2 = FieldElement(6, 13)
        assert (fe1 + fe2) == FieldElement(4, 13)

    def test_add_field_elements_diff_primes_raises_type_error(self):
        fe1 = FieldElement(6, 13)
        fe2 = FieldElement(6, 16)
        with pytest.raises(TypeError):
            fe1 + fe2

    def test_multiply_elements_same_field_modulo(self):
        fe1 = FieldElement(12, 13)
        fe2 = FieldElement(3, 13)
        assert (fe1 * fe2) == FieldElement(10, 13)

    def test_multiply_field_elements_diff_primes_raises_type_error(self):
        fe1 = FieldElement(12, 13)
        fe2 = FieldElement(3, 16)
        with pytest.raises(TypeError):
            fe1 * fe2

    def test_square_field_element(self):
        # 7 ** 2 % 39 == 10
        assert FieldElement(7, 13) ** 2 == FieldElement(10, 13)
