// function editBook(bookId) {
//     const book = fetch(`http://localhost:5000/books/${bookId}`)
//       .then((response) => response.json())
//       .then((data) => {
//         document.getElementById("editBookId").value = data.id;
//         document.getElementById("editTitle").value = data.title;
//         document.getElementById("editAuthor").value = data.author;
//         document.getElementById("editPrice").value = data.price;
//         createBookForm.style.display = "none";
//         editBookForm.style.display = "block";
//       })
//       .catch((error) => {
//         console.error("Error fetching book for editing:", error);
//       });
//   }
  
//   function cancelEdit() {
//     editBookForm.style.display = "none";
//     createBookForm.style.display = "block";
//   }
  
//   function updateBook(event) {
//     event.preventDefault();
//     const bookId = document.getElementById("editBookId").value;
//     const title = document.getElementById("editTitle").value;
//     const author = document.getElementById("editAuthor").value;
//     const price = parseFloat(document.getElementById("editPrice").value);
  
//     fetch(`http://localhost:5000/books/${bookId}`, {
//       method: "PUT",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ title, author, price }),
//     })
//       .then(() => {
//         editBookForm.reset();
//         cancelEdit();
//         fetchBooks();
//       })
//       .catch((error) => {
//         console.error("Error updating book:", error);
//       });
//   }
  
//   // ... existing event listeners ...
  
//   const bookListElement = document.getElementById("bookList");
  
//   function createBookRow(book) {
//     const row = document.createElement("tr");
//     row.innerHTML = `
//       <td>${book.title}</td>
//       <td>${book.author}</td>
//       <td>${book.price}</td>
//       <td>
//         <button data-edit-book="${book.id}" class="editButton">Edit</button>
//         <button data-delete-book="${book.id}" class="deleteButton">Delete</button>
//       </td>
//     `;
//     return row;
//   }
  
//   function displayBooks(books) {
//     bookListElement.innerHTML = "";
//     books.forEach((book) => {
//       const row = createBookRow(book);
//       bookListElement.appendChild(row);
//     });
//   }
  
//   function handleEditButtonClick(event) {
//     const button = event.target;
//     if (button.classList.contains("editButton")) {
//       const bookId = button.getAttribute("data-edit-book");
//       editBook(bookId);
//     }
//   }
  
//   bookListElement.addEventListener("click", handleEditButtonClick);