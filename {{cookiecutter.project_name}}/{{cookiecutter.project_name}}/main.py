from pydantic import BaseModel


class HelloWorld(BaseModel):
    name: str = "World"

    def greet(self):
        return f"Hello, {self.name}!"


def main():
    hello = HelloWorld()
    print(hello.greet())


if __name__ == "__main__":
    main()
