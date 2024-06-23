# pynest_updater

    * "PynestUpdater" is a Python tool for traversing and updating nested JSON structures, 
    facilitating efficient address modifications and deep-level path updates.

     
       - "PynestUpdater" is a Python tool designed for efficient traversal and updating of nested structures within JSON data. 
       - This utility enables users to explore inner levels of JSON objects and perform targeted updates, 
       making it particularly useful for tasks such as modifying addresses or updating specific paths within complex nested JSON structures. 
       - The tool provides a streamlined approach to navigate and manipulate nested data, 
       enhancing the ease of working with deeply nested JSON objects.

# JSON Path Traversal and Update

      - This Python script allows you to traverse a JSON structure recursively and update the path in each node. 
      - It's useful for tasks like updating addresses or populating address fields in a nested JSON.


 * Input sample data.
```json
[
  {
    "person": "abc",
    "city": "united states",
    "facebooklink": "link",
    "united states": [
      {
        "person": "cdf",
        "city": "ohio",
        "facebooklink": "link",
        "ohio": [
          {
            "person": "efg",
            "city": "clevland",
            "facebooklink": "link",
            "clevland": [
              {
                "person": "jkl",
                "city": "Street A",
                "facebooklink": "link",
                "Street A": [
                  {
                    "person": "jkl",
                    "city": "House 1",
                    "facebooklink": "link"
                  }
                ]
              }
            ]
          },
          {
            "person": "ghi",
            "city": "columbus",
            "facebooklink": "link"
          }
        ]
      },
      {
        "person": "abc",
        "city": "washington",
        "facebooklink": "link"
      }
    ]
  }
]
```

 * Output sample data.
```json
[
  {
    "person": "abc",
    "city": "united states",
    "facebooklink": "link",
    "address": "united states",
    "united states": [
      {
        "person": "cdf",
        "city": "ohio",
        "facebooklink": "link",
        "address": "united states/ohio",
        "ohio": [
          {
            "person": "efg",
            "city": "clevland",
            "facebooklink": "link",
            "address": "united states/ohio/clevland",
            "clevland": [
              {
                "person": "jkl",
                "city": "Street A",
                "facebooklink": "link",
                "address": "united states/ohio/clevland/Street A",
                "Street A": [
                  {
                    "person": "jkl",
                    "city": "House 1",
                    "facebooklink": "link",
                    "address": "united states/ohio/clevland/Street A/House 1"
                  }
                ]
              }
            ]
          },
          {
            "person": "ghi",
            "city": "columbus",
            "facebooklink": "link",
            "address": "united states/ohio/columbus"
          }
        ]
      },
      {
        "person": "abc",
        "city": "washington",
        "facebooklink": "link",
        "address": "united states/washington"
      }
    ]
  }
]
```



## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/itsmehara/pynest_updater.git
   cd pynest_updater
   ```

## Contributions
    Feel free to contribute to this project by opening issues or submitting pull requests. 
    All contributions are welcome!

## License
    This project is licensed under the MIT License.

## Online reference.

    This question is answered in this link:

    [stack overflow link](https://stackoverflow.com/questions/77887573/how-to-auto-populate-the-address-in-json)


https://stackoverflow.com/questions/77887573/how-to-auto-populate-the-address-in-json

