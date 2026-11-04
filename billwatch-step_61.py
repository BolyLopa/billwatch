# === Stage 61: Add performance timing for core list and search operations ===
# Project: BillWatch
import time

def time_operation(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start

def benchmark_list_add(bills, new_bill):
    result, elapsed = time_operation(bills.append, new_bill)
    return result, elapsed

def benchmark_list_get(bills, index):
    result, elapsed = time_operation(bills.__getitem__, index)
    return result, elapsed

def benchmark_list_contains(bills, bill_id):
    result, elapsed = time_operation(any, (b['id'] == bill_id for b in bills))
    return result, elapsed

def benchmark_list_remove(bills, bill_id):
    result, elapsed = time_operation(lambda bl: bl.remove(next(b for b in bl if b['id'] == bill_id)), bills)
    return result, elapsed

def benchmark_list_update(bills, index, updated_bill):
    result, elapsed = time_operation(bills.__setitem__, index, updated_bill)
    return result, elapsed

def benchmark_list_len(bills):
    result, elapsed = time_operation(len, bills)
    return result, elapsed

def benchmark_list_index(bills, bill_id):
    result, elapsed = time_operation(lambda bl: bl.index(next(b for b in bl if b['id'] == bill_id)), bills)
    return result, elapsed

def benchmark_list_pop(bills):
    result, elapsed = time_operation(bills.pop)
    return result, elapsed

def benchmark_list_clear(bills):
    result, elapsed = time_operation(bills.clear)
    return result, elapsed

def benchmark_list_count(bills, bill_id):
    result, elapsed = time_operation(lambda bl: sum(1 for b in bl if b['id'] == bill_id), bills)
    return result, elapsed

def benchmark_list_sort(bills, key):
    result, elapsed = time_operation(sorted, bills, key=key)
    return result, elapsed

def benchmark_list_reverse(bills):
    result, elapsed = time_operation(bills.reverse)
    return result, elapsed

def benchmark_list_iter(bills):
    result, elapsed = time_operation(list, bills)
    return result, elapsed

def benchmark_list_slice(bills, start, stop):
    result, elapsed = time_operation(lambda bl: bl[start:stop], bills)
    return result, elapsed

def benchmark_list_copy(bills):
    result, elapsed = time_operation(bills.copy)
    return result, elapsed

def benchmark_list_insert(bills, index, new_bill):
    result, elapsed = time_operation(bills.insert, index, new_bill)
    return result, elapsed

def benchmark_list_extend(bills, new_bills):
    result, elapsed = time_operation(bills.extend, new_bills)
    return result, elapsed

def benchmark_list_index_of(bills, bill_id):
    result, elapsed = time_operation(lambda bl: bl.index(next(b for b in bl if b['id'] == bill_id)), bills)
    return result, elapsed
