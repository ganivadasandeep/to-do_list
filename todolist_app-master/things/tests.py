var code = ` 
                    <div style="order:${data.id}" id="${data.id}" class="list">
                        <div style="flex: 2;"  class="fas fa-check"></div>
                        <div style="flex: 8;" id="${data.id}_title">${data.title}</div>                
                        <input type="hidden" style="flex: 6;" id="${data.id}_text" placeholder="Add task" id="taskadd" name="tasknew">
                        <div style="flex: 1;" id="${data.id}_edit" onclick="edit_task('${data.id}')" class="btn btn-sm btn-outline-primary edit mr-3">Edit</div>
                        <div style="flex: 1;" id="${data.id}_update" onclick="update_task('${data.id}')" class="btn btn-sm btn-outline-danger ml-3 mr-3 update">Done</div>
                        <div style="flex: 2;" id="${data.id}_delete" class="far fa-trash-alt delete"></div>
                    </div>`

                    $('.showtasks').append(code);