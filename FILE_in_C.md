Below is a list of common C file I/O functions, with their parameters and examples.

### 1. **`fgets()`**

* **Purpose**: Reads a string (line) from a file or input stream.

* **Prototype**:

  ```c
  char *fgets(char *str, int num, FILE *stream);
  ```

* **Parameters**:

  * `str`: Pointer to the buffer where the input will be stored.
  * `num`: Maximum number of characters to read (including the null terminator).
  * `stream`: Input stream (e.g., `stdin`, `file pointer`).

* **Example**:

  ```c
  char buffer[100];
  fgets(buffer, sizeof(buffer), stdin);  // Reads input from the user
  ```

---

### 2. **`fputc()`**

* **Purpose**: Writes a single character to a file.

* **Prototype**:

  ```c
  int fputc(int char, FILE *stream);
  ```

* **Parameters**:

  * `char`: Character to be written.
  * `stream`: The output file stream.

* **Example**:

  ```c
  fputc('A', stdout);  // Writes 'A' to the standard output
  ```

---

### 3. **`fputs()`**

* **Purpose**: Writes a string to a file.

* **Prototype**:

  ```c
  int fputs(const char *str, FILE *stream);
  ```

* **Parameters**:

  * `str`: String to be written.
  * `stream`: The output file stream.

* **Example**:

  ```c
  fputs("Hello, World!", stdout);  // Writes string to standard output
  ```

---

### 4. **`fscanf()`**

* **Purpose**: Reads formatted input from a file.

* **Prototype**:

  ```c
  int fscanf(FILE *stream, const char *format, ...);
  ```

* **Parameters**:

  * `stream`: The input file stream.
  * `format`: Format string (e.g., `"%d", "%s"`).
  * `...`: Additional arguments to store the read values.

* **Example**:

  ```c
  int num;
  fscanf(stdin, "%d", &num);  // Reads an integer from user input
  ```

---

### 5. **`fprintf()`**

* **Purpose**: Writes formatted output to a file.

* **Prototype**:

  ```c
  int fprintf(FILE *stream, const char *format, ...);
  ```

* **Parameters**:

  * `stream`: The output file stream.
  * `format`: Format string.
  * `...`: Additional arguments to print.

* **Example**:

  ```c
  fprintf(stdout, "Value: %d\n", 42);  // Writes formatted output to stdout
  ```

---

### 6. **`fread()`**

* **Purpose**: Reads binary data from a file.

* **Prototype**:

  ```c
  size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
  ```

* **Parameters**:

  * `ptr`: Pointer to a buffer where the data will be stored.
  * `size`: Size of each element to read.
  * `count`: Number of elements to read.
  * `stream`: The input file stream.

* **Example**:

  ```c
  char buffer[10];
  fread(buffer, sizeof(char), 10, stdin);  // Reads 10 bytes from stdin
  ```

---

### 7. **`fwrite()`**

* **Purpose**: Writes binary data to a file.

* **Prototype**:

  ```c
  size_t fwrite(const void *ptr, size_t size, size_t count, FILE *stream);
  ```

* **Parameters**:

  * `ptr`: Pointer to the data to be written.
  * `size`: Size of each element to write.
  * `count`: Number of elements to write.
  * `stream`: The output file stream.

* **Example**:

  ```c
  int data = 100;
  fwrite(&data, sizeof(int), 1, stdout);  // Writes an integer to stdout
  ```

---

### 8. **`fseek()`**

* **Purpose**: Moves the file pointer to a specific location.

* **Prototype**:

  ```c
  int fseek(FILE *stream, long offset, int whence);
  ```

* **Parameters**:

  * `stream`: The file stream.
  * `offset`: Number of bytes to move.
  * `whence`: Position from where to move (e.g., `SEEK_SET`, `SEEK_CUR`, `SEEK_END`).

* **Example**:

  ```c
  fseek(file, 0, SEEK_END);  // Move file pointer to the end of the file
  ```

---

### 9. **`ftell()`**

* **Purpose**: Returns the current position of the file pointer.

* **Prototype**:

  ```c
  long ftell(FILE *stream);
  ```

* **Parameters**:

  * `stream`: The file stream.

* **Example**:

  ```c
  long pos = ftell(file);  // Get the current position of the file pointer
  ```

---

### 10. **`feof()`**

* **Purpose**: Checks if the end of the file is reached.

* **Prototype**:

  ```c
  int feof(FILE *stream);
  ```

* **Parameters**:

  * `stream`: The file stream.

* **Example**:

  ```c
  if (feof(file)) {
      printf("End of file reached.\n");
  }
  ```

---

### 11. **`ferror()`**

* **Purpose**: Checks if an error occurred while reading or writing.

* **Prototype**:

  ```c
  int ferror(FILE *stream);
  ```

* **Parameters**:

  * `stream`: The file stream.

* **Example**:

  ```c
  if (ferror(file)) {
      printf("Error occurred while reading the file.\n");
  }
  ```

---

### 12. **`rewind()`**

* **Purpose**: Moves the file pointer to the beginning of the file.

* **Prototype**:

  ```c
  void rewind(FILE *stream);
  ```

* **Parameters**:

  * `stream`: The file stream.

* **Example**:

  ```c
  rewind(file);  // Move the file pointer to the beginning
  ```

---

### 13. **`remove()`**

* **Purpose**: Deletes a file.

* **Prototype**:

  ```c
  int remove(const char *filename);
  ```

* **Parameters**:

  * `filename`: Name of the file to be deleted.

* **Example**:

  ```c
  remove("test.txt");  // Deletes the file "test.txt"
  ```

---

### 14. **`rename()`**

* **Purpose**: Renames or moves a file.

* **Prototype**:

  ```c
  int rename(const char *oldname, const char *newname);
  ```

* **Parameters**:

  * `oldname`: Current name of the file.
  * `newname`: New name for the file.

* **Example**:

  ```c
  rename("oldname.txt", "newname.txt");  // Renames the file
  ```

---

### Summary Table

| Function    | Purpose                  | Key Parameters                                                   | Example                                  |
| ----------- | ------------------------ | ---------------------------------------------------------------- | ---------------------------------------- |
| `fgets()`   | Read a string            | `char *str`, `int num`, `FILE *stream`                           | `fgets(buffer, 100, stdin)`              |
| `fputc()`   | Write a single character | `int char`, `FILE *stream`                                       | `fputc('A', stdout)`                     |
| `fputs()`   | Write a string           | `const char *str`, `FILE *stream`                                | `fputs("Hello", stdout)`                 |
| `fscanf()`  | Read formatted input     | `FILE *stream`, `const char *format`, `...`                      | `fscanf(stdin, "%d", &x)`                |
| `fprintf()` | Write formatted output   | `FILE *stream`, `const char *format`, `...`                      | `fprintf(stdout, "Value: %d", x)`        |
| `fread()`   | Read binary data         | `void *ptr`, `size_t size`, `size_t count`, `FILE *stream`       | `fread(buffer, sizeof(char), 10, file)`  |
| `fwrite()`  | Write binary data        | `const void *ptr`, `size_t size`, `size_t count`, `FILE *stream` | `fwrite(buffer, sizeof(char), 10, file)` |
| `fseek()`   | Set file pointer         | `FILE *stream`, `long offset`, `int whence`                      | `fseek(file, 0, SEEK_END)`               |
| `ftell()`   | Get                      |                                                                  |                                          |

