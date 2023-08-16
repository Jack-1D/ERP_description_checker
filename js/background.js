// chrome.runtime.onConnect.addListener(function (port) {
    // if (port.name === "popup") {
    // chrome.storage.local.set({ "connect": "true" }, function () {
    //     console.log("set");
    // });
    // // console.log(chrome.storage.local.get());
    // // localStorage.setItem("connect", 'true');
    // port.onDisconnect.addListener(function () {
    //     console.log("popup has been closed");
    //     chrome.storage.local.get("connect", function (items) {
    //         console.log("get");
    //         console.log(items);
    //     });
    //     // localStorage.removeItem("connect");
    // });
    // }
// });