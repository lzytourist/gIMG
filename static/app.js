$('#form').submit(function (e) {
    e.preventDefault();
    $('input:submit').val('Loading...');
    $('#images').hide(200)
    $('#image-links').html('');

    $.ajax($(this)[0].action, {
        type: 'POST',
        data: {
            website: $('input[name=website]').val()
        }
    }).done(function (res) {
        if (res.status) {
            // showMessage(res.message);
            res.images.map(image => {
                let link = `<div class="col-md-4 col-lg-3">
                                <div class="card mb-4 shadow">
                                  <img class="card-img-top" src="${image}" alt="Image" style="height: 230px">
                                  <div class="card-body">
                                  <div class="card-link">
                                  <a href="${image}" target="_blank" class="btn btn-outline-primary">Download</a>
                                </div>
                                  </div>
                                </div>
                             </div>`;
                $('#image-links').append(link);
            });
            $('#images').show(200)
        } else {
            showMessage(res.message, 'error');
        }
        $('input:submit').val('Get');
    }).catch(function (err) {
        showMessage(err.response.message, 'error');
        $('input:submit').val('Get');
    });
});

function showMessage(msg, icon = 'success') {
    Swal.fire({
        icon: icon,
        title: icon === 'success' ? 'Boo yah!' : 'Oops..',
        text: msg,
    });
}