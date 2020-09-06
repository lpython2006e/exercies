/**
 * get data from file data.json
 * */
$(document).ready(function () {
    $.getJSON('data.json', function (data) {
        localStorage.getItem('Students');
        let student_data = '';
        $.each(data, function (key, value) {
            student_data += '<tr data-id = "' + value.id + '" data-name = "' + value.name + '" data-birthday = "' + value.birthday + '" data-sex = "' + value.sex + '" data-email = "' + value.email + '" data-age = "' + value.age + '" data-state = "' + value.state + '">';
            student_data += '<td>' + value.id + '</td>';
            student_data += '<td>' + value.name + '</td>';
            student_data += '<td>' + value.birthday + '</td>';
            student_data += '<td>' + value.sex + '</td>';
            student_data += '<td>' + value.email + '</td>';
            student_data += '<td>' + value.age + '</td>';
            student_data += '<td>' + value.state + '</td>';
            student_data += '<td>';
            student_data += '<button class="btn btn-info btn-xs btn-edit">' + "Edit" + '</button>';
            student_data += '<button class="btn btn-danger btn-xs btn-delete">' + "Delete" + '</button>';
            student_data += '</td>';
        });
        $('#tBody').append(student_data);
        localStorage.setItem('Students', JSON.stringify(data))
    });
});

/**
 * check input feild sex, state in selections and return value
 * */
function check() {
    var sex = $('select option').val();
    if (sex == 0) {
        return $('option').css(selected);
    } else {
        return $('option').css(selected);
    }
}

// function checkState() {
//     var sex = $("input[name='state']").val();
//     if (sex == 0) {
//         return "Đang học";
//     } else {
//         return "Đi làm";
//     }
// }

/**
 * create function set value input empty
 * */
function focusInputAdd() {
    $("input[name='id']").val('');
    $("input[name='name']").val('');
    $("input[name='birthday']").val('');
    $("input[name='sex']").val('');
    $("input[name='email']").val('');
    $("input[name='age']").val('');
    $("input[name='state']").val('');
}

/**
 * get Age from curent year and birthday strudent
 */
function getAge() {
    var current = new Date().getFullYear();
    var birthday = $("input[name='birthday']").val();
    birthday = new Date(birthday).getFullYear();
    return current - birthday;
}


$("form").submit(function (e) {
    e.preventDefault();
    var id = $("input[name='id']").val();
    var name = $("input[name='name']").val();
    var birthday = $("input[name='birthday']").val();
    var sex = $("input[name='sex']").val();
    var email = $("input[name='email']").val();
    var age = $("input[name='age']").val();
    var state = $("input[name='state']").val();

    $(".data-table tbody").append(`<tr 
        data-id='${id}' 
        data-name='${name}' 
        data-birthday ='${birthday}' 
        data-sex='${sex}'
        data-email='${email}'
        data-age='${getAge()}'
        data-state='${state}'>
        
        <td>${id}</td>
        <td>${name}</td>
        <td>${birthday}</td>
        <td>
            ${check()}
        </td>
        <td>${email}</td>
        <td>${getAge()}</td>
        <td>${check()}</td>
        <td>
            <button class='btn btn-info btn-xs btn-edit'>Edit</button>
            <button class='btn btn-danger btn-xs btn-delete'>Delete</button>
        </td>
    </tr>`);

    focusInputAdd();
});

$("body").on("click", ".btn-delete", function () {
    $(this).parents("tr").remove();
});


$("body").on("click", ".btn-edit", function () {
    var parents_tr = $(this).parents("tr");
    var id = parents_tr.attr('data-id');
    var name = parents_tr.attr('data-name');
    var birthday = parents_tr.attr('data-birthday');
    var sex = parents_tr.attr('data-sex');
    var email = parents_tr.attr('data-email');
    var age = parents_tr.attr('data-age');
    var state = parents_tr.attr('data-state');

    parents_tr.find("td:eq(0)").html('<input name="edit_id" value="' + id + '">');
    parents_tr.find("td:eq(1)").html('<input name="edit_name" value="' + name + '">');
    parents_tr.find("td:eq(2)").html('<input type="date" name="edit_birthday" value="' + birthday + '">');
    parents_tr.find("td:eq(3)").html('<select name="edit_sex" value="' + sex + '"><option value="0">Nam</option><option value="1">Nữ</option> </select>');
    parents_tr.find("td:eq(4)").html('<input type="email" name="edit_email" value="' + email + '">');
    parents_tr.find("td:eq(5)").html('<input class="col-sm-10"  value="' + age + '" disabled>');
    parents_tr.find("td:eq(6)").html('<select name="edit_state" value="' + state + '"> <option value="0">Đi học</option><option value="1">Đi làm</option> </select>');
    parents_tr.find("td:eq(7)").prepend("<button class='btn btn-info btn-xs btn-update'>Update</button><button class='btn btn-warning btn-xs btn-cancel'>Cancel</button>")
    $(this).hide();
});

$("body").on("click", ".btn-cancel", function () {
    let id = $(this).parents("tr").attr('data-id');
    let name = $(this).parents("tr").attr('data-name');
    let birthday = $(this).parents("tr").attr('data-birthday');
    let sex = $(this).parents("tr").attr('data-sex');
    let email = $(this).parents("tr").attr('data-email');
    let age = $(this).parents("tr").attr('data-age');
    let state = $(this).parents("tr").attr('data-state');


    $(this).parents("tr").find("td:eq(0)").text(id);
    $(this).parents("tr").find("td:eq(1)").text(name);
    $(this).parents("tr").find("td:eq(2)").text(birthday);
    $(this).parents("tr").find("td:eq(3)").text(sex);
    $(this).parents("tr").find("td:eq(4)").text(email);
    $(this).parents("tr").find("td:eq(5)").text(age);
    $(this).parents("tr").find("td:eq(6)").text(state);
    $(this).parents("tr").find(".btn-edit").show();
    $(this).parents("tr").find(".btn-update").remove();
    $(this).parents("tr").find(".btn-cancel").remove();
});

$("body").on("click", ".btn-update", function () {
    var name = $(this).parents("tr").find("input[name='edit_name']").val();
    var email = $(this).parents("tr").find("input[name='edit_email']").val();

    $(this).parents("tr").find("td:eq(0)").text(id);
    $(this).parents("tr").find("td:eq(1)").text(name);
    $(this).parents("tr").find("td:eq(2)").text(birthday);
    $(this).parents("tr").find("td:eq(3)").text(sex);
    $(this).parents("tr").find("td:eq(4)").text(email);
    $(this).parents("tr").find("td:eq(5)").text(age);
    $(this).parents("tr").find("td:eq(6)").text(state);

    $(this).parents("tr").attr('data-id', id);
    $(this).parents("tr").attr('data-name', name);
    $(this).parents("tr").attr('data-birthday', birthday);
    $(this).parents("tr").attr('data-sex', sex);
    $(this).parents("tr").attr('data-email', email);
    $(this).parents("tr").attr('data-age', age);
    $(this).parents("tr").attr('data-state', state);

    $(this).parents("tr").find(".btn-edit").show();
    $(this).parents("tr").find(".btn-cancel").remove();
    $(this).parents("tr").find(".btn-update").remove();
});