function check() {
    return $("#live-translate-check").is(':checked');
}

function onAnimation() {
    $("#animate-id").finish()
        .empty()
        .append("开")
        .css("opacity", "0")


        .animate({
            opacity: '1'
        }, 1000)

        .animate({
            opacity: '0'
        }, 500, function () {
            $(this).empty();
            $(this).append("自动翻译");
        })


        .animate({
            opacity: '1'
        }, 500)
}

function offAnimation() {
    $("#animate-id").finish()
        .empty()
        .append("关")
        .css("opacity", "0")


        .animate({
            opacity: '1'
        }, 1000)

        .animate({
            opacity: '0'
        }, 500, function () {
            $(this).empty();
            $(this).append("自动翻译");
        })


        .animate({
            opacity: '1'
        }, 500)
}

function showWait() {
    $("#translate-result dl").empty();
    $("#picture-display-div").empty();
    $("#pron-div").empty();
    $("#exchange table").empty();
    $("#example dl").empty();

    $("#translate-result dl").append(`<dt>请稍等...</dt>`);
    $("#exchange table").append(`<dt>请稍等...</dt>`);
    $("#example dl").append(`<dt>请稍等...</dt>`);
}

function ajaxTranslate(translateText) {
    $.ajax({
        type: 'GET',
        url: "/get/ajax/translate",
        data: {"translateText": translateText},
        success: function (response) {
            var instance = JSON.parse(response["forjson"]);
            var picUrl = JSON.parse(response["picUrl"]);
            presentResult(translateText, instance, picUrl);
        }
    });
}

function presentResult(getText, result, urlRes) {
    $("#translate-result dl").empty();
    $("#picture-display-div").empty();
    $("#pron-div").empty();
    $("#exchange table").empty();
    $("#example dl").empty();

    let resultJson = result['json'];
    let resultXml = result['xml'];

    if (getText.length != 0) {
        if (resultJson.hasOwnProperty("word_name")) {
            showMeanAndPron(resultJson, urlRes);
            showExchange(resultJson);
            showExample(resultXml);
        } else {
            $("#translate-result dl").append(`<tr><td>抱歉，啥也没找到，请输入的英文单词正确</td></tr>`);
            $("#exchange table").append(`<tr><td>抱歉，啥也没找到，请输入的英文单词正确</td></tr>`);
            $("#example dl").append(`<tr><td>抱歉，啥也没找到，请输入的英文单词正确<tr><td>`);
        }
    }
}

function showMeanAndPron(resultJson, urlRes) {
    for (parts of resultJson['symbols'][0]['parts']) {
        $("#translate-result dl").append(`<dt class="part">${parts['part']}</dt>`);
        for (mean of parts['means']) {
            $("#translate-result dl").append(`<dd class="mean">${mean}</dd>`);
        }
    }
    $("#picture-display-div").append(
        `<img id="picture" src=${urlRes['url'][0]} width="100%"/>`
    )

    if (resultJson['symbols'][0]['ph_en']) {
        $("#pron-div").append(
            `<label class="pron-button-label" for="ph_en" style="vertical-align:sub">英音</label>
                         <button class="pron-button btn btn-link" id="ph_en" style="vertical-align:sub">${resultJson['symbols'][0]['ph_en']}</button>`
        )
    }

    if (resultJson['symbols'][0]['ph_am']) {
        $("#pron-div").append(
            `<label class="pron-button-label" for="ph_am" style="vertical-align:sub">美音</label>
                         <button class="pron-button btn btn-link" id="ph_am" style="vertical-align:sub">${resultJson['symbols'][0]['ph_am']}</button>`
        )
    }

    var phEnAudio = document.createElement('audio');
    var phAmAudio = document.createElement('audio');

    $("#ph_en").click(function () {
            phEnAudio.setAttribute('src', resultJson['symbols'][0]['ph_en_mp3']);
            phEnAudio.pause();
            phEnAudio.currentTime = 0;
            phEnAudio.play();
        }
    );

    $("#ph_am").click(function () {
            phAmAudio.setAttribute('src', resultJson['symbols'][0]['ph_am_mp3']);
            phAmAudio.pause();
            phAmAudio.currentTime = 0;
            phAmAudio.play();
        }
    );
}

function showExchange(resultJson) {
    let exchangeDict = {
        "word_pl": "复数",
        "word_third": "第三人称单数",
        "word_past": "过去式",
        "word_done": "过去分词",
        "word_ing": "ing形式",
        "word_er": "比较级",
        "word_est": "最高级",
    }

    for (let exchange of Object.keys(resultJson['exchange'])) {
        if (resultJson['exchange'][exchange]) {
            let exchangeResultTd = "";
            for (exchangeResult of resultJson['exchange'][exchange]) {
                exchangeResult += "; ";
                exchangeResultTd += exchangeResult;
            }

            $("#exchange table").append(`<tr><th scope="row" class="exchange-th">${exchangeDict[exchange]}</th><td class="exchange-td">${exchangeResultTd}</td></tr>`);
        }
    }
}

function showExample(resultXml) {
    if (resultXml['dict'].hasOwnProperty('sent')) {
        for (sent of resultXml['dict']['sent']) {
            $("#example dl").append(`<dt class='orig'>${sent['orig']}</dt>`);
            $("#example dl").append(`<dd class="trans">${sent['trans']}</dd>`);
        }
    }
}

$(function () {
    if ($.cookie("checkbox") == "false") {
        $('#live-translate-check').attr("checked", false);
        offAnimation();
    } else {
        $('#live-translate-check').attr("checked", true);
        onAnimation();
    }


    if ($.cookie("input")) {
        $("#input-text").val($.cookie("input"));
        let translateText = $("#input-text").val();
        ajaxTranslate(translateText);
    }


    var queue = 0;
    $("#input-text").on('keyup', function (event) {
        let check_status = check();
        if (check_status == true) {
            clearTimeout(queue);
            queue = setTimeout(function () {
              if ((event.keyCode >= 48 && event.keyCode <= 57) || (event.keyCode >= 65 && event.keyCode <= 90) || event.keyCode == 13 || event.keyCode == 32 || event.keyCode == 8){
                showWait();}
                let translateText = $("#input-text").val();
                ajaxTranslate(translateText);
            }, 400);
        }
    });

    $(document).keyup(function (event) {
        if (event.keyCode == 13) {
            $("#translate-button").trigger("click");
        }
    });

    $("#translate-button").click(function (e) {
        showWait();
        let translateText = $("#input-text").val();
        ajaxTranslate(translateText);
    });

    $("#live-translate-check").change(function (e) {
        if (check() == true) {
            showWait();
            let translateText = $("#input-text").val();
            ajaxTranslate(translateText);
            onAnimation();
        } else {
            offAnimation();
        }
    });
});

$(window).on('beforeunload', function () {
    $.cookie("input", $("#input-text").val());
    $.cookie("checkbox", $("#live-translate-check").is(':checked'));
});
