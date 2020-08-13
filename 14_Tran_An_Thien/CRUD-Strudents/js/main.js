// Load data from localStorage or IndexedDB

var data = [
    {
        "msv": "LPYTHON2006E-01",
        "htsv": "Nguyen Van A",
        "ns": "22/2/1999",
        "gt": "nam",
        "email": "someone@email.com",
        "tuoi": 21,
        "tt": "danghoc"
    },
    {
        "msv": "LPYTHON2006E-02",
        "htsv": "Nguyen Van B",
        "ns": "22/2/1999",
        "gt": "nu",
        "email": "someoneelse@email.com",
        "tuoi": 21,
        "tt": "danghoc"
    }
];
$(document).ready(function () {
    let tableBody = $('#tableBody');
    $.each(data, function (index, item) {
        let currentIndex = index + 1;
        tableBody.append(`<tr>
                <th id="msv-${currentIndex}" scope="row">${item.msv}</th>
                <td id="htsv-${currentIndex}">${item.htsv}</td>
                <td id="ns-${currentIndex}">${item.ns}</td>
                <td id="gt-${currentIndex}">${item.gt}</td>
                <td id="email-${currentIndex}">${item.email}</td>
                <td id="tuoi-${currentIndex}">${item.tuoi}</td>
                <td id="tt-${currentIndex}">${item.tt}</td>
                <td name="bstable-actions">
                    <div class="btn-group pull-right">
                        <button row-id="1" id="bEdit-1" type="button" class="btn btn-sm btn-default edit-btn">
                            <span class="fa fa-edit"> </span>
                        </button>
                        <button row-id="1" id="bDel-1" type="button" class="btn btn-sm btn-default">
                            <span class="fa fa-trash"> </span>
                        </button>
                        <button row-id="1" id="bAcep-1" type="button" class="btn btn-sm btn-default  accept-btn" 
                        style="display:none;">
                            <span class="fa fa-check-circle"> </span>
                        </button>
                        <button row-id="1" id="bCanc-1" type="button" class="btn btn-sm btn-default" 
                        style="display:none;">
                            <span class="fa fa-times-circle"> </span>
                        </button>
                    </div>
                </td>
            </tr>`)
    })


    $(".edit-btn").click(function () {
        console.log("button click" + $(this).attr("row-id"));
        let rowId = $(this).attr("row-id");
        $(this).toggle();


        let htsvID = "#htsv-" + rowId;
        let hotensv = $(htsvID).text();
        $(htsvID).html("<input type = 'text' value= '" + hotensv + "'>");

        let nsID = "#ns-" + rowId;
        let nsinh = $(nsID).text();
        $(nsID).html("<input type = 'text' id='datepicker' value= '" + nsinh + "'>");
        $("#datepicker").datepicker();

        let gtID = "#gt-" + rowId;
        let gioitinh = $(gtID).text();
        $(gtID).html(`<select id="gioitinh">
                    <option value="nam">Nam</option>
                    <option value="nu">Nữ</option>
                    </select>`);

        let emailid = "#email-" + rowId;
        let emailsv = $(emailid).text();
        $(emailid).html("<input type = 'text' value= '" + emailsv + "'>");

        let ttid = "#tt-" + rowId;
        let trangthaisv = $(ttid).text();
        console.log(trangthaisv);
        $(ttid).html(`<select id="gioitinh">
                    <option value="danghoc">Đang học</option>
                    <option value="dilam">Đi làm</option>
                    </select>`);

        let btnAcceptId = "#bAcep-" + rowId;
        $(btnAcceptId).toggle();
    });
    $(".accept-btn").click(function () {
        let rowId = $(this).attr("row-id");
        let btnAcceptId = "#bAcep-" + rowId;
        $(btnAcceptId).toggle();

        let btnEditId = "#bEdit-" + rowId;
        $(btnEditId).toggle();
    });

});