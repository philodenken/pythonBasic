def vector_size_check(*vector_variables):
    vector_len_list = [len(v) for v in vector_variables]

    vector_len_set = set(vector_len_list)

    if(len(vector_len_set) == 1):
        result = True
    else:
        result = False

    return result


def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError

    vector_add_list=[sum(v) for v in zip(*vector_variables)]
    return vector_add_list


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError

    vector_sub_list=[v[0]-sum(v[1:]) for v in zip(*vector_variables)]
    return vector_sub_list


def scalar_vector_product(alpha, vector_variable):

    vector_scal_pro_list=[alpha * element for element in vector_variable]
    return vector_scal_pro_list


def matrix_size_check(*matrix_variables):
    mat_len_set = [len(set(v)) for v in zip(*[[len(m), len(m[0])] for m in matrix_variables])]

    if(mat_len_set[0]==1 and mat_len_set[1]==1):
        result = True
    else:
        result = False

    return result


def is_matrix_equal(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError

    result = True

    mat_equal_list = [[len(set(element)) for element in zip(*m) ]for m in zip(*matrix_variables)]

    for row in mat_equal_list:
        for col in row:
            if(col != 1):
                result =False

    return result


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError

    mat_add_list = [[sum(element) for element in zip(*m)] for m in zip(*matrix_variables)]

    return mat_add_list


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError

    mat_sub_list = [[element[0]-sum(element[1:]) for element in zip(*m)] for m in zip(*matrix_variables)]

    return mat_sub_list


def matrix_transpose(matrix_variable):
    mat_trans_list = [[element for element in m]for m in zip(*matrix_variable)]
    return mat_trans_list


def scalar_matrix_product(alpha, matrix_variable):
    mat_scal_prod_list = [[alpha * element for element in row]for row in matrix_variable]
    return mat_scal_prod_list


def is_product_availability_matrix(matrix_a, matrix_b):
    mat_pro_set = [len([v for v in zip(*matrix_a)]), len(matrix_b)]

    print(mat_pro_set)

    if (len(set(mat_pro_set))==1):
        result = True
    else:
        result = False

    return result


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError

    mat_prod_list = [[sum( a*b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)] for row_a in matrix_a]

    return mat_prod_list

def main():

    mat_x=[[2,2],[2,2],[2,2]]
    mat_y=[[2,5],[2,1]]
    mat_z=[[1,1,2],[2,1,1]]

    print(is_product_availability_matrix(mat_x, mat_z))
    print(matrix_product(mat_x, mat_z))
if(__name__ == "__main__"):
    main()
