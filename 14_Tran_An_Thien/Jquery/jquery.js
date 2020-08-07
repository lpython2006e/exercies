$(document).ready(function () {
    $('.text').addClass('important');
});

$(document).ready(function () {
    $('#nav > li').addClass('highlight');
});

$(document).ready(function () {
    $('#nav > li').addClass('highlight');
    $('#nav li:not(.highlight)').addClass('background');
});
// use insertAfter method
$(document).ready(function () {
    $('<a href="#top">Back to top</a>')
        .insertAfter('div.primary p');

    // chèn điểm dừng (top) vào ngay trước thẻ <body> (đầu trang web)
    $('body').before('<a id="top" name="top"></a>');
    // di chuyển nội dung xuống dưới
    // $('p.text').insertBefore('#footer').attr('style', 'display: block;');
});

// use After method
// $(document).ready(function() {
//     $('div.primary p').after('<a href="#top">back to top</a>');
// });
/**
 * Sự khác nhau giưa hai phương thức trên là, khi ta ta thêm các phương thức khác nữa đằng sau thì thì với
 * .insertAfter() sẽ tiếp tục làm việc với thẻ <a>, còn với .after() thì thẻ <a> không bị ảnh hưởng,
 * chỉ ảnh hưởng đến đến những phần tử thuộc \'div.chapter p\' mà thôi.
 */

//  Server request Ajax
/**
 * hàm load dữ liệu từ file result.html
 */
// $(document).ready(function() {
//     $("#driver").click(function(event){
//        $('#stage').load('/jquery/result.html');
//     });
//  });

/***
 * có thể load dữ liệu từ file json
 */

$(document).ready(function () {
    $("#driver").click(function (event) {

        $.getJSON('/jquery/result.json', function (jd, status, jqXHR) {
            console.log(status);
            console.log(jqXHR);
            $('#stage').html('<p> Name: ' + jd.name + '</p>');
            $('#stage').append('<p>Age : ' + jd.age + '</p>');
            $('#stage').append('<p> Sex: ' + jd.sex + '</p>');
        });

    });
});