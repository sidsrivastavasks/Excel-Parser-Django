function searchData() {
    let filter = document.getElementById("search-box").value.toUpperCase();

    let myTable = document.getElementById("myTable");

    let tr = myTable.querySelectorAll("[id=sort]");

    for (var i = 0; i < tr.length; i++) {
        let td = tr[i].getElementsByTagName("td")[1];

        if (td) {
            let name = td.textContent || td.innerHTML;

            if (name.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function sortName(indx) {
    let myTable = document.getElementById("myTable");

    let tbody = myTable.querySelector("tbody");
    let rows = tbody.querySelectorAll("[id=sort]");

    rows = rows.isArray ? rows : Object.values(rows);
    function compare(a, b) {
        aText = a.children[indx].innerHTML.toUpperCase().trim();
        bText = b.children[indx].innerHTML.toUpperCase().trim();

        return aText < bText ? -1 : 1;
    }

    rows.sort(compare);
    tbody.innerHTML = "";

    let i = 0;
    while (i < rows.length) {
        tbody.appendChild(rows[i]);
        i++;
    }
}

document
    .getElementById("file-input-form")
    .addEventListener("submit", function (event) {
        event.preventDefault(); // prevent the form from submitting in the usual way

        var file_input = document.getElementById("my-file");
        var file = file_input.files[0];

        var form_data = new FormData();
        form_data.append("file", file);

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "excel/add-product", true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Check for errors in the response
                    var response = JSON.parse(xhr.responseText);
                    if (response.error) {
                        alert(response.error);
                    } else {
                        // Redirect to the home page
                        window.location.href = "/excel";
                    }
                } else {
                    // Handle errors
                    console.error(xhr.status);
                }
            }
        };
        xhr.send(form_data);
    });
