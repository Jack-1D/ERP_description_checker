const submit_button = document.getElementById("submit_button");
const erp_input = document.getElementById("erp");
const factory_input = document.getElementById("factory");
const product_type_input = document.getElementById("product_type");
const connect_button = document.getElementById("connect");
const name_check_output_box = document.getElementById("name_check_error");
const name_result_color = document.getElementById("name_result");
const name_result_text = document.getElementById("name_result_text");

function openURL() {
    window.open("https://172.30.202.88:5000/");
}
// localStorage.setItem("connected", "no");
connect_button.addEventListener("click", openURL);
// test = fetch("https://172.30.200.103:5000/", {
//     method: 'GET',
//     headers: new Headers()
// })
//     .then(response => {
//         console.log(typeof (response.status));
//         if (response.status == '200') {
//             console.log("aaaa");
//             localStorage.setItem("connected", "yes");
//         }
//     })
// if (localStorage.getItem("connected") == "yes") {
//     connect_button.style = "display:none";
// }
// else {
//     connect_button.style = "display:";
// }

function saveERP(e) {
    let erp = erp_input.value;
    let factory = factory_input.checked;
    let product_type = product_type_input.checked;
    localStorage.setItem('erp', erp);
    localStorage.setItem('factory', factory.toString());
    localStorage.setItem('product_type', product_type.toString());
}
erp_input.value = localStorage.getItem('erp');
factory_input.checked = localStorage.getItem('factory') == 'true' ? true : false;
product_type_input.checked = localStorage.getItem('product_type') == 'true' ? true : false;


submit_button.addEventListener("click", (e) => {
    e.preventDefault();
    saveERP(e);
});
submit_button.addEventListener("click", async (e) => {
    e.preventDefault();
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: analyze,
        args: [erp_input.value, factory_input.checked ? "TPMC" : "SHMC", product_type_input.checked ? "0" : "1"]
    },

        (analyze_result) => {
            let name_check_result = true;
            let name_check_result_error_msg = "";

            console.log(analyze_result[0]);
            for (const [key, value] of Object.entries(analyze_result[0].result.name_check_result)) {
                if (!value["status"]) {
                    name_check_result = false;
                    name_check_result_error_msg += value["error_msg"] + '\n';
                }
            }
            name_result_color.style.backgroundColor = name_check_result ? '#53FF53' : '#FF2D2D';
            name_result_text.innerText = name_check_result ? 'PASS' : 'FAIL';
            name_check_output_box.innerText = name_check_result_error_msg;
        });

});

function analyze(erp, factory, product_type) {
    var BOM = [];
    var Item = document.getElementById("ITEMTABLE_BOM").getElementsByClassName("GMPageOne")[1].getElementsByClassName("GMSection")[0].getElementsByTagName("tbody")[0].children;
    for (var i = 0; i < Item.length; i++) {
        if (Item[i].hasAttribute('class')) {
            if (Item[i].attributes['class'].value == "GMDataRow") {
                var row_context = Item[i].innerText;
                row_context = row_context.split("\t");
                var Findnum = row_context[2].trim();
                var itemNumber = row_context[4].trim();
                var SAPRelese = row_context[25].trim();
                var Substitute = row_context[9].trim();
                var Qty = row_context[10].trim();
                BOM.push({ "Findnum": Findnum, "itemNumber": itemNumber, "SAPRelese": SAPRelese, "Substitute": Substitute, "Qty": Qty })
            }
        }
    }
    console.clear();
    console.log(BOM);

    check_result = fetch("https://172.30.202.88:5000/", {
        method: 'POST',
        headers: { "Content-type": "application/x-www-form-urlencoded; charset=UTF-8" },
        body: JSON.stringify({
            'BOM': BOM,
            "erp": erp.replace(/[+]/g, "plus"),
            "factory": factory,
            "product_type": product_type
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            return data;
        });
    return check_result;
}