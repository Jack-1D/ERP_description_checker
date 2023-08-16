// const port = chrome.runtime.connect({ name: "popup" });
// while (true) {
//     port.postMessage({ "msg": "hi" });
//     port.onMessage.addListener((msg) => {
//         console.log(msg);
//         port.postMessage({ "msg": "hihi" });
//     })
// }
// while (true) {
//     chrome.runtime.sendMessage({ "msg": "hhhhhhhhhh" }, (msg) => {
//         console.log(msg);
//     });
// }
console.log("aaadjhsfjzhs");
chrome.runtime.sendMessage(
    { action: 'donAutoSwipe', stats: me.options.stats, }, function (response) {  console.log(response); } );
// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//     dt = document.getElementsByClassName('container thumb')[0].getElementsByTagName('fieldset')[1].getElementsByClassName('side_by_side_text')[3].getElementsByTagName('dt')[0];
  
//     if (request.from === 'popup.js') {
//       // 可以在 sendMessage 的 callback 中取得，此 sendResponse 的內容
//       // 需要注意若在多個地方呼叫同時呼叫 sendResponse，將只會收到一個
//       sendResponse({
//         "dt": dt,
//       });
//     }
//   });