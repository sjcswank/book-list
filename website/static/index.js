function deleteBook(bookId) {
          fetch("/delete-book", {
            method: "POST",
            body: JSON.stringify({ bookId: bookId }),
          }).then((_res) => {
            window.location.href = "/";
            });
          }

function update_read(bookId, filter) {
            console.log(bookId)
          fetch("/update-read", {
            method: "POST",
            body: JSON.stringify({ bookId: bookId }),
          }).then((_res) => {
            window.location.href = "/?filter=" + filter;
            });
          }