var arrTram=[];
function themForm(){
    document.getElementById('form').style.display='block';

}
document.getElementById('xac-nhan').onclick=function(){
    var tram = new TramThuGom();
    tram.id = document.getElementById('id').value;
    tram.ten = document.getElementById('ten').value;
    tram.viTri = document.getElementById('viTri').value;
    tram.trangThai = document.getElementById('trangThai').value;
    tram.thuGom = document.getElementById('thuGom').value;
    
    


    arrTram.push(tram);
    renderTram(arrTram);
}
function renderTram(arrTram){
    var contentHTML='';
    for (var index=0;index<arrTram.length;index++){
        var tramThuGom = arrTram[index];
        contentHTML+=`
        <tr>
        <td>${tramThuGom.id}</td>
        <td>${tramThuGom.ten}</td>
        <td>${tramThuGom.viTri}
        </td>
        <td>${tramThuGom.trangThai}</td>
        <td>${tramThuGom.thuGom}
        </td>

        <td>
          <div class="button">
            <button class="btn btn-danger" onclick="xoaTram('${tramThuGom.id}')">Xóa</button>
            <button class="btn btn-primary" onclick="suaTram('${tramThuGom.id}')">Sửa</button>
        </div>
        </td>
        </tr>
        
        
        `;
    }
    document.getElementById('tbody').innerHTML = contentHTML;
    document.getElementById('form').style.display='none';
}
function xoaTram(id){
    console.log(id);
    var indexDel=-1;
    for (var index=0;index<arrTram.length;i++){
        var tramTrongMang =  arrTram[index];
        if(tramTrongMang.id===id){
            indexDel=index;
            break;
        }
    }
    arrTram.splice(indexDel,1);
    renderTram(arrTram);
}
function xoaDefault(){
    document.getElementById('default').innerHTML='';
}
function suaTram(id){
    document.getElementById('form').style.display='block';
    var indexEdit=-1;
    for (var index=0;index<arrTram.length;i++){
        var tramTrongMang = arrTram[index];
        if(tramTrongMang.id===id){
            indexEdit=index;
            break;
        }
    }
    if(indexEdit!=-1){
        
        document.getElementById('id').value = arrTram[indexEdit].id;
        document.getElementById('ten').value = arrTram[indexEdit].ten;
        document.getElementById('viTri').value = arrTram[indexEdit].viTri;
        document.getElementById('trangThai').value = arrTram[indexEdit].trangThai;
        document.getElementById('thuGom').value = arrTram[indexEdit].thuGom;
        

        
        
    }
    renderTram(arrTram);
}
function closeForm(){
    var form = document.getElementById('form');
    form.style.display = 'none';
}