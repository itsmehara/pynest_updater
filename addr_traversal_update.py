input_data = [
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


PARENT_TOP = ""
address = 'address'


def update_address(parent_node, my_path=PARENT_TOP):
    if isinstance(parent_node, list):
        for child_node in parent_node:
            if isinstance(child_node, dict):
                city = child_node.get("city")
                new_path = f"{my_path}/{city}" if my_path else city
                child_node[address] = new_path
                grand_child = child_node.get(city)
                update_address(grand_child, new_path)
    elif isinstance(parent_node, dict):
        city = parent_node.get("city")
        new_path = f"{my_path}/{city}" if my_path else city
        parent_node[address] = new_path
        child = parent_node.get(city)
        update_address(child, new_path)
    else:
        pass
    return parent_node


if __name__ == '__main__':
    update_address(input_data)
    # output = json.dumps(json.loads(str(given_data)), indent=2)
    print(input_data)