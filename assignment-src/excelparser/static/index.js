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
