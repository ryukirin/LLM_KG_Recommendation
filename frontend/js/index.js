function showStars(star, container_id) {
    // 计算实心星星和空心星星的数量
    var solidStars = Math.floor(star);
    var halfStar = star % 1 !== 0;
    var emptyStars = Math.floor(5 - star);

    // 获取星星容器
    var starContainer = document.getElementById(container_id);

    // 动态生成实心星星
    for (var i = 0; i < solidStars; i++) {
        var solidStar = document.createElement('i');
        solidStar.className = 'bi bi-star-fill';
        starContainer.appendChild(solidStar);
    }

    // 如果存在半颗星，则生成半颗星
    if (halfStar) {
        var halfStar = document.createElement('i');
        halfStar.className = 'bi bi-star-half';
        starContainer.appendChild(halfStar);
    }

    // 动态生成空心星星
    for (var j = 0; j < emptyStars; j++) {
        var emptyStar = document.createElement('i');
        emptyStar.className = 'bi bi-star';
        starContainer.appendChild(emptyStar);
    }
}
// 页面加载完成后执行
$(document).ready(function () {
    // 发送 Ajax 请求
    $.ajax({
        url: "http://127.0.0.1:80/get_data",
        type: "GET",
        success: function (response) {
            // 处理后端返回的数据
            var data = response.map(function (str) {
                return JSON.parse(str);
            });
            console.log("loading page items...");
            // 将数据显示在页面上
            for (var i = 0; i < data.length; i++) {
                var cardId = i + 1;
                // 替换 HTML 元素的内容
                $("#productImage" + cardId).attr("src", "img/" + data[i].node_id + ".jpg");
                $("#productTitle" + cardId).text(data[i].title);
                $("#productBrand" + cardId).text(data[i].brand);
                $("#detailPage" + cardId).attr("href", data[i].url);
                $("#star-rating" + cardId).text(data[i].star);
                showStars(parseFloat(data[i].star), "star-rating" + cardId)
            }
            console.log("Done!🎉")
        },
        error: function (error) {
            console.log(error);
        }
    });
});
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})


document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('button-modal').addEventListener('click', function () {

        // 获取输入框中的文字
        var inputValue = document.getElementById('inputText').value;
        console.log("user speech:" + inputValue)

        // 将页面恢复初始状态
        for (var i = 0; i < 3; i++) {
            var cardId = i + 1;
            // 替换 HTML 元素的内容
            $("#recoproductImage" + cardId).attr("src", "img/loading.gif");
            $("#recoproductTitle" + cardId).text("loading...");
            $("#recoproductBrand" + cardId).text("loading...");
            $("#recodetailPage" + cardId).attr("href", "#");
            $("#reco-star-rating" + cardId).text("loading...");
            showStars(0.0, "reco-star-rating" + cardId)
        }
        $("#ai-reply").text("生成中...");
        // 将reco_list显示在页面上
        for (var i = 0; i < 3; i++) {
            var cardId = i + 1;
            // 替换 HTML 元素的内容
            $("#other_recoproductImage" + cardId).attr("src", "img/loading.gif");
            $("#other_recoproductTitle" + cardId).text("loading...");
            $("#other_recoproductBrand" + cardId).text("loading...");
            $("#other_recodetailPage" + cardId).attr("href", "#");
            $("#other_reco-star-rating" + cardId).text("loading...");
            showStars(0.0, "other_reco-star-rating" + cardId)
        }

        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:80/send_speech',
            headers: {
                'Content-Type': 'application/json'
            },
            dataType: 'json',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ "speech": inputValue }),
            success: function (data) {
                // 显示 modal-list
                document.getElementById("modal-list").style.display = "";
                console.log("send to system!")
                console.log(JSON.stringify({ "speech": inputValue }))

                console.log("Asking for AI...");
                $.ajax({
                    url: "http://127.0.0.1:80/get_reply",
                    type: "GET",
                    success: function (response) {
                        // 处理后端返回的数据
                        var data = response
                        console.log("data:" + data)
                        var reco_list = data.reco_list
                        console.log("reco_list:" + reco_list)
                        var other_reco_list = data.other_reco_list
                        console.log("other_reco_list:" + typeof (other_reco_list[0]))
                        var ai_reply = data.reply
                        console.log("ai_reply:" + ai_reply)
                        console.log("Loading recommend list...");

                        // 将reco_list显示在页面上
                        if (reco_list.length > 0) {
                            document.getElementById("reco_title").style.display = "";
                            document.getElementById("reco_list").style.display = "";
                            for (var i = 0; i < reco_list.length; i++) {
                                var cardId = i + 1;
                                // 替换 HTML 元素的内容
                                $("#recoproductImage" + cardId).attr("src", "img/" + JSON.parse(reco_list[i]).node_id + ".jpg");
                                $("#recoproductTitle" + cardId).text(JSON.parse(reco_list[i]).title);
                                $("#recoproductBrand" + cardId).text(JSON.parse(reco_list[i]).brand);
                                $("#recodetailPage" + cardId).attr("href", JSON.parse(reco_list[i]).url);
                                $("#reco-star-rating" + cardId).text(JSON.parse(reco_list[i]).star);
                                showStars(parseFloat(JSON.parse(reco_list[i]).star), "reco-star-rating" + cardId)
                            }
                        }
                        else {
                            console.log("No recommend list 🙇‍♂️");
                            document.getElementById("reco_title").style.display = "none";
                            document.getElementById("reco_list").style.display = "none";
                        }
                        console.log("Loading AI reply...");
                        $("#ai-reply").text(ai_reply);
                        console.log("Done!")
                        console.log("Loading other recommend list...");
                        // 将other_reco_list显示在页面上
                        if (other_reco_list.length > 0) {
                            document.getElementById("other_reco_title").style.display = "";
                            document.getElementById("other_reco_list").style.display = "";
                            for (var i = 0; i < other_reco_list.length; i++) {
                                var cardId = i + 1;
                                // 替换 HTML 元素的内容
                                $("#other_recoproductImage" + cardId).attr("src", "img/" + JSON.parse(other_reco_list[i]).node_id + ".jpg");
                                $("#other_recoproductTitle" + cardId).text(JSON.parse(other_reco_list[i]).title);
                                $("#other_recoproductBrand" + cardId).text(JSON.parse(other_reco_list[i]).brand);
                                $("#other_recodetailPage" + cardId).attr("href", JSON.parse(other_reco_list[i]).url);
                                $("#other_reco-star-rating" + cardId).text(JSON.parse(other_reco_list[i]).star);
                                showStars(parseFloat(JSON.parse(other_reco_list[i]).star), "other_reco-star-rating" + cardId)
                            }
                        }
                        else {
                            console.log("No other recommend list 🙇‍♂️");
                            document.getElementById("other_reco_title").style.display = "none";
                            document.getElementById("other_reco_list").style.display = "none";
                        }
                        console.log("Done!🎉")
                    },
                    error: function (error) {
                        console.log(error);
                    }
                });
            },
            error: function (xhr, textStatus, errorThrown) {
                console.error("Error sending request:", errorThrown);
            }
        });
    });
})