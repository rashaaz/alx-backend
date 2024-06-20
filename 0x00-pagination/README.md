# 0x00. Pagination

## Project Overview

This project focuses on implementing pagination techniques for a dataset. You will learn how to paginate a dataset using simple page and page_size parameters, how to paginate with hypermedia metadata, and how to paginate in a deletion-resilient manner.

### Project Duration

- **Start:** Jun 20, 2024 6:00 AM
- **End:** Jun 25, 2024 6:00 AM
- **Checker Release:** Jun 21, 2024 12:00 PM

## Learning Objectives

By the end of this project, you will be able to:

- Paginate a dataset with simple `page` and `page_size` parameters.
- Paginate a dataset with hypermedia metadata.
- Implement pagination in a deletion-resilient manner.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project directory is mandatory.
- Your code should use the pycodestyle style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- All functions and coroutines must be type-annotated.

## Setup

Use the provided `Popular_Baby_Names.csv` file for this project.

## Tasks

### Task 0: Simple helper function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`. The function should return a tuple containing a start index and an end index corresponding to the range of indexes to return in a list for those pagination parameters.

```python
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    # Implementation

