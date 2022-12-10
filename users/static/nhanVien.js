var arrTask=[];
function themForm(){
    document.getElementById('form').style.display='block';

}
document.getElementById('xac-nhan').onclick=function(){
    var task = new Task();
    task.tenTask = document.getElementById('tenTask').value;
    task.desc = document.getElementById('desc').value;
    task.MCP = document.getElementById('lst_MCP_options').value;
    task.phuongTien = document.getElementById('lst_vehicle_options').value;
    task.tuyenDuong = document.getElementById('tuyenDuong').value;
    arrTask.push(task);
    renderTask(arrTask);
}
function renderTask(arrTask){
    var contentHTML='';
    for (var index=0;index<arrTask.length;index++){
        var congViec = arrTask[index];
        contentHTML+=`
        <tr>
        <td>${congViec.tenTask}</td>
        <td>${congViec.desc}</td>
        <td>${congViec.MCP}
        </td>
        <td>${congViec.phuongTien}</td>
        <td>${congViec.tuyenDuong}
        </td>
        <td>
          <div class="button">
            <button class="btn btn-danger" onclick="xoaTask('${congViec.tenTask}')">Xóa</button>
            <button class="btn btn-primary" onclick="suaTask('${congViec.tenTask}')">Sửa</button>
        </div>
        </td>
        </tr>
        
        
        `;
    }
    document.getElementById('tbody').innerHTML = contentHTML;
    document.getElementById('form').style.display='none';
}
function xoaTask(tenTask){
    var indexDel=-1;
    for (var index=0;index<arrTask.length;i++){
        var taskTrongMang =  arrTask[index];
        if(taskTrongMang.tenTask===tenTask){
            indexDel=index;
            break;
        }
    }
    arrTask.splice(indexDel,1);
    renderTask(arrTask);
}
function suaTask(tenTask){
    document.getElementById('form-sua').style.display='block'
    var indexEdit=-1;
    for (var index=0;index<arrTask.length;i++){
        var taskTrongMang = arrTask[index];
        if(taskTrongMang.tenTask===tenTask){
            indexEdit=index;
            break;
        }
    }
    if(indexEdit!=-1){
        
        document.getElementById('tenTask').value = arrTask[indexEdit].tenTask;
        document.getElementById('desc').value = arrTask[indexEdit].desc;
        document.getElementById('lst_MCP_options').value = arrTask[indexEdit].MCP;
        document.getElementById('lst_vehicle_options').value = arrTask[indexEdit].phuongTien;
        document.getElementById('tuyenDuong').value = arrTask[indexEdit].tuyenDuong;
        
        
        
    }
    renderTask(arrTask);
}
document.getElementById('btnCapNhat').onclick = function(){
    //lấy thông tin người dùng thay đổi để update lại mảng
    document.getElementById('form-sua').style.display='block';
    var taskUpdate = new Task();
    taskUpdate.tenTask = document.getElementById('tenTask').value;
    taskUpdate.desc = document.getElementById('desc').value;
    taskUpdate.MCP = document.getElementById('lst_MCP_options').value;
    taskUpdate.phuongTien = document.getElementById('lst_vehicle_options').value;
    taskUpdate.tuyenDuong = document.getElementById('tuyenDuong').value;
   
    

    for (var index=0;index<arrTask.length;index++){
        var taskTrongMang = arrTask[index];
        if (taskTrongMang.tenSinhVien==taskUpdate.tenTask){
            //tiến hành cập nhật
            taskTrongMang.tenTask = taskUpdate.tenTask;
            taskTrongMang.desc = taskUpdate.desc;
            taskTrongMang.MCP = taskUpdate.MCP;
            taskTrongMang.phuongTien = taskUpdate.phuongTien;
            taskTrongMang.tuyenDuong = taskUpdate.tuyenDuong;
           


            break;
        }
    }
    //render lại giao diện
    renderTask(arrTask);
}
function closeForm(){
    var form = document.getElementById('form');
    form.style.display = 'none';
}
function closeFormSua(){
    var form = document.getElementById('form-sua');
    form.style.display = 'none';
}