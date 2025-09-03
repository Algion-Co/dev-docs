## Mixins

```python
class A:
    def __init__(self, a_arg, *args, **kwargs):
        # Re-add any used argument to arguments list
        kwargs["a_arg"] = "a_arg"

        # Forward unused arguments to next method in MRO
        super().__init__(*args, **kwargs)

        print(f"Hello from class A with arg {a_arg}.")

class B:
    def __init__(self, b_arg, a_arg, *args, **kwargs):
        print(f"Hello from class B with arg {b_arg}.")
        print(a_arg)


class C(A, B):
    def __init__(self, a_arg, b_arg):
        super().__init__(a_arg, b_arg)

c = C("a_arg", "b_arg")
```
