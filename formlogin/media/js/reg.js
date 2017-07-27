/**
 * Created by peter on 2017/7/27.
 */
$('#submit_btn').click(function () {
    $('#form').ajaxSubmit(function (data) {
        $('#submit_btn').attr('disabled', false);
            alert(data);
            $('input[type=text').val('');
    });
});

$("#back").click(function () {
    location.href = '/';
})