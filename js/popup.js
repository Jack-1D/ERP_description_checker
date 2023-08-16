const submit_button = document.getElementById("submit_button");
const erp_input = document.getElementById("erp");
const factory_input = document.getElementById("factory");
const product_type_input = document.getElementById("product_type");
const connect_button = document.getElementById("connect");

const name_result_color = document.getElementById("name_result");
const name_result_text = document.getElementById("name_result_text");
const name_check_output_box = document.getElementById("name_check_error");

const bom_result_color = document.getElementById("bom_result");
const bom_result_text = document.getElementById("bom_result_text");
const bom_check_output_box = document.getElementById("bom_check_error");

// 自動抓取網頁上的ERP description、factory、type
chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        func: getElement,
    },
        (element) => {
            let result = element[0].result;
            if (JSON.stringify(result) != '{}') {
                localStorage.setItem('erp', result.name);
                localStorage.setItem('factory', result.factory == "TPMC" ? 'true' : 'false');
                localStorage.setItem('product_type', result.type[0] == "1" ? 'true' : 'false');
            }
            getLocalStorage();
        })
});

function getElement() {
    try {
        let name = "";
        let pre_text = document.getElementsByClassName("container thumb")[0].getElementsByTagName('fieldset')[1].getElementsByClassName('side_by_side_text')[2];
        for (let i = 0; i < 3; i++) {
            name += pre_text.getElementsByTagName('dt')[i].innerText;
            name += pre_text.getElementsByTagName('dd')[i].innerText;
        }
        let factory = pre_text.getElementsByTagName('dd')[5].innerText;
        let type = pre_text.getElementsByTagName('dd')[7].innerText;
        return { "name": name, "factory": factory, "type": type };
    } catch {
        return {};
    }
}

// 連結background.js
const port = chrome.runtime.connect({ name: "popup" });

// 建立安全連線後，連線按鈕消失
var connected = fetch("https://172.30.202.88:5000/", {
    method: 'GET',
    headers: { "Content-type": "application/x-www-form-urlencoded; charset=UTF-8" }
})
    .then(response => response.json())
    .then(data => {
        if (data.connected == true) return true;
    })
    .catch(() => { return false })
connected.then(data => { if (data) connect_button.style = "display:none"; });

connect_button.addEventListener("click", async (e) => {
    e.preventDefault();
    openURL();
});
function openURL() {
    window.open("https://172.30.202.88:5000/");
    connected = fetch("https://172.30.202.88:5000/", {
        method: 'GET',
        headers: { "Content-type": "application/x-www-form-urlencoded; charset=UTF-8" }
    })
        .then(response => response.json())
        .then(data => {
            if (data.connected == true) return true;
        })
        .catch(() => { return false; })
    connected.then(data => { if (data) connect_button.style = "display:none"; });
}

// 按下提交後會暫存結果
submit_button.addEventListener("click", (e) => {
    e.preventDefault();
    saveERP(e);
});
function saveERP(e) {
    localStorage.setItem('erp', erp_input.value);
    localStorage.setItem('factory', factory_input.checked.toString());
    localStorage.setItem('product_type', product_type_input.checked.toString());
    getLocalStorage();
}

function getLocalStorage() {
    erp_input.value = localStorage.getItem('erp');
    factory_input.checked = localStorage.getItem('factory') == 'true' ? true : false;
    product_type_input.checked = localStorage.getItem('product_type') == 'true' ? true : false;
    name_result_color.style.backgroundColor = localStorage.getItem('name_result_color');
    name_result_text.innerText = localStorage.getItem('name_result_text');
    name_check_output_box.innerText = localStorage.getItem('name_check_output');
    bom_result_color.style.backgroundColor = localStorage.getItem('bom_result_color');
    bom_result_text.innerText = localStorage.getItem('bom_result_text');
    bom_check_output_box.innerText = localStorage.getItem('bom_check_output');
}

// 主要程式
submit_button.addEventListener("click", async (e) => {
    e.preventDefault();
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: analyze,
        args: [erp_input.value, factory_input.checked ? "TPMC" : "SHMC", product_type_input.checked ? "1" : "0"]
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
            localStorage.setItem('name_result_color', name_check_result ? '#53FF53' : '#FF2D2D');
            name_result_color.style.backgroundColor = localStorage.getItem('name_result_color');
            localStorage.setItem('name_result_text', name_check_result ? 'PASS' : 'FAIL');
            name_result_text.innerText = localStorage.getItem('name_result_text');
            localStorage.setItem('name_check_output', name_check_result_error_msg);
            name_check_output_box.innerText = localStorage.getItem('name_check_output');

            localStorage.setItem('bom_result_color', analyze_result[0].result.BOM_check_result.extra_problem.length == 0 ? '#53FF53' : '#FF2D2D');
            bom_result_color.style.backgroundColor = localStorage.getItem('bom_result_color');
            localStorage.setItem('bom_result_text', analyze_result[0].result.BOM_check_result.extra_problem.length == 0 ? 'PASS' : 'FAIL');
            bom_result_text.innerText = localStorage.getItem('bom_result_text');
            localStorage.setItem('bom_check_output', analyze_result[0].result.BOM_check_result.extra_problem);
            bom_check_output_box.innerText = localStorage.getItem('bom_check_output');
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
            "erp": erp.replace(/[+]/g, "plus"),     // + 號傳輸後會不見
            "factory": factory,
            "product_type": product_type
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            for (var i = 1; i < Item.length; i++) {
                let bom_result = data['BOM_check_result']['BOM'][i - 1];
                console.log(bom_result);
                if (Item[i].hasAttribute('style')) {
                    if (Item[i].style.display == "none")
                        Item[i].style.display = '';
                }
                if ((Item[i].hasAttribute('style') && Item[i].getElementsByTagName("tr"))) {
                    var Item2 = Item[i];
                    if (bom_result.result == "uncheck") {
                        var cells = Item2.getElementsByTagName("td");
                        for (var j = 0; j < cells.length; j++) {
                            cells[j].style.backgroundColor = '#95CACA';
                        }
                    } else if (bom_result.result == "pass") {
                        var cells = Item2.getElementsByTagName("td");
                        for (var j = 0; j < cells.length; j++) {
                            cells[j].style.backgroundColor = "#28FF28";
                        }
                    } else if (bom_result.result == "warning") {
                        var cells = Item2.getElementsByTagName("td");
                        for (var j = 0; j < cells.length; j++) {
                            cells[j].style.backgroundColor = "#FFFF37";
                        }
                    } else if (bom_result.result == "fail") {
                        var cells = Item2.getElementsByTagName("td");
                        for (var j = 0; j < cells.length; j++) {
                            cells[j].style.backgroundColor = "#FF9797";
                        }
                    }
                }
            }
            return data;
        });
    return check_result;
}