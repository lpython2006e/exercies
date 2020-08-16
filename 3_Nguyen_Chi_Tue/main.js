var data = JSON.parse(localStorage.getItem('save'))
if (data === null) {
    data = [];
}
$(document).ready(function () {
    // load data
    var tableBody = $('#tBody');

    function render() {
        tableBody.empty();
        let currentIndex = 0;
        $.each(data, function (index, item) {
            currentIndex++;
            tableBody.append(`
                <tr id="tr${currentIndex}">
                   <td>${currentIndex}</td>
                   <td id="name${currentIndex}">${item.htsv}</td>
                   <td id="birthday${currentIndex}">${item.ns}</td>
                   <td id="mail${currentIndex}">${item.email}</td>
                   <td id="age${currentIndex}">${item.tuoi}</td>
                   <td id="sex${currentIndex}">${item.gt}</td>
                   <td id="status${currentIndex}">${item.tt}</td>
                   <td>
                      <button id="btn${currentIndex}" class="btn-yes"><span><i class="fas fa-pen"></i></span></button>
                      <button id="btn-remove${currentIndex}" class="btn-remove"><span><i class="fas fa-trash"></i></span></button>
                      <button id="show${currentIndex}" class="btn-show"><span><i class="fas fa-check"></i></span></button>
                      <button id="hide${currentIndex}" class="btn-hide"><span><i class="fas fa-times"></i></span></button>
                   </td>
                </tr>
                `)
        })
    }

    render();
    //yes
    $(document).on('click', '.btn-yes', function () {
        var index = $(this).attr("id");
        index = index.slice(index.length - 1)
        var currentName = $("#name" + index).text()
        var currentBirthday = $("#birthday" + index).text()
        var currentEmail = $("#mail" + index).text()
        var currentSex = $("#sex" + index).text()
        var currentStatus = $("#status" + index).text()
        $("#name" + index).html("<input type='text' value='" + currentName + "' id='nameInput'>")
        $("#birthday" + index).html("<input type = 'text' id='datepicker' value= '" + currentBirthday + "'>");
        $("#datepicker").datepicker();
        $("#mail" + index).html("<input type='text' value='" + currentEmail + "' id='mailInput'>")
        $("#sex" + index).html(`
<select id="gioitinh">
   <option value="Male">Male</option>
   <option value="Female">Female</option>
</select>
`);
        $("#status" + index).html(`
<select id="statusInput">
   <option value="School">School</option>
   <option value="Work">Work</option>
</select>
`);
        $("#show" + index).css("display", "inline-block")
        $("#btn" + index).css("display", "none")
        $("#btn-remove" + index).css("display", "none")
        $("#hide" + index).css("display", "inline-block")
    });
    //hide
    $(document).on('click', '.btn-hide', function () {
        var index = $(this).attr("id");
        index = index.slice(index.length - 1)
        var currentName = document.getElementById("nameInput").defaultValue // không biết cú pháp jqery
        var currentBirthday = document.getElementById("datepicker").defaultValue
        var currentEmail = document.getElementById("mailInput").defaultValue
        var currentSex = $("#gioitinh").val() // chưa fix đc
        var currentStatus = $("#statusInput").val() // chưa fix đc
        $("#show" + index).css("display", "none")
        $("#btn" + index).css("display", "inline-block")
        $("#btn-remove" + index).css("display", "inline-block")
        $("#hide" + index).css("display", "none")
        $("#name" + index).html(`${currentName}`)
        $("#birthday" + index).html(`${currentBirthday}`);
        $("#mail" + index).html(`${currentEmail}`)
        $("#sex" + index).html(`${currentSex}`);
        $("#status" + index).html(`${currentStatus}`);
    });
    //show
    $(document).on('click', '.btn-show', function () {
        var index = $(this).attr("id");
        index = index.slice(index.length - 1)
        var currentName = $("#nameInput").val()
        var currentBirthday = $("#datepicker").val();
        var currentEmail = $("#mailInput").val()
        var currentSex = $("#gioitinh").val()
        var currentStatus = $("#statusInput").val()
        if (currentName.length === 0 || currentEmail.length === 0 || currentBirthday.length === 0) {
            alert('nhap lai');
        }
        if (currentName.length !== 0 && currentEmail.length !== 0 && currentBirthday.length !== 0) {
            var now = Number(currentBirthday.slice(6, 10));
            var d = new Date();
            var n = d.getFullYear()
            $("#age" + index).html(`${n - now}`);
            $("#show" + index).css("display", "none")
            $("#btn" + index).css("display", "inline-block")
            $("#btn-remove" + index).css("display", "inline-block")
            $("#hide" + index).css("display", "none")
            var dataNew = {
                // "msv": `${index}`,
                "htsv": `${currentName}`,
                "ns": `${currentBirthday}`,
                "gt": `${currentSex}`,
                "email": `${currentEmail}`,
                "tuoi": `${n - now}`,
                "tt": `${currentStatus}`
            };
            if(data[index - 1])
                data[index - 1] = dataNew;
            else
                data.push(dataNew);

            localStorage.setItem('save', JSON.stringify(data))
            render();
        }
    });
    //remove
    $(document).on('click', '.btn-remove', function () {
        var index = $(this).attr("id");
        var indexNo = index.match(/[a-z\-]*(\d+)/)[1];
        var indexToRemove = parseInt(indexNo) - 1;
        if (indexToRemove > -1) {
            data.splice(indexToRemove, 1);
        }
        // var chuyendoi=Object.keys(data)
        localStorage.setItem('save', JSON.stringify(data))
        render();
    });
    // xóa dữ liệu
    //add
    $('#addItem').click(function () {
        var count = data.length + 1;
        var dataNew = {
            "htsv": ``,
            "ns": ``,
            "gt": ``,
            "email": ``,
            "tuoi": ``,
            "tt": ``
        };
        data.push(dataNew);
        render();
    });
});
