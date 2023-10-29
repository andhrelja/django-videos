const ScholarSenioritySelect = document.getElementById("id_category_type");
var ClassSelect = document.getElementById("id_category_subtype");

function toggleVideoCategories() {
    Array.from(ClassSelect.childNodes).forEach((childNode) => ClassSelect.removeChild(childNode));
    fetch("/videos/categories")
        .then((categories) => categories.json())
        .then((categories) => {
            // console.log(categories);
            var selected = categories[ScholarSenioritySelect.selectedIndex];
            console.log(selected)
            var i = 0;
            selected.classes.map((className) => {
                i += 1;
                var option = document.createElement('option');
                option.value = i.toString();
                option.text = className;
                ClassSelect.appendChild(option)
            });

        });
}
