from tasks import add, mul

# Example usage of Celery tasks
result = add.delay(4, 4)
print(f"Task ID: {result.id}")
print(f"Result: {result.get()}")

result = mul.delay(4, 4)
print(f"Task ID: {result.id}")
print(f"Result: {result.get()}")
