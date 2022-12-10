var arrPhuongTien=[];
function themForm(){
    document.getElementById('form').style.display='block';

}
document.getElementById('xac-nhan').onclick=function(){
    var xe = new PhuongTien();
    xe.id = document.getElementById('id').value;
    xe.ten = document.getElementById('ten').value;
    xe.bienSo = document.getElementById('bienSo').value;
    xe.truongLuong = document.getElementById('trongLuong').value;
    xe.xangTieuThu = document.getElementById('xangTieuThu').value;
    xe.trangThai = document.getElementById('trangThai').value;
    


    arrPhuongTien.push(xe);
    renderPhuongTien(arrPhuongTien);
}
function renderPhuongTien(arrPhuongTien){
    var contentHTML='';
    for (var index=0;index<arrPhuongTien.length;index++){
        var phuongTien = arrPhuongTien[index];
        contentHTML+=`
        <tr>
        <td>${phuongTien.id}</td>
        <td>${phuongTien.ten}</td>
        <td>${phuongTien.bienSo}
        </td>
        <td>${phuongTien.truongLuong}</td>
        <td>${phuongTien.xangTieuThu}
        </td>
        <td>${phuongTien.trangThai}
        </td>
        <td>
          <div class="button">
            <button class="btn btn-danger" onclick="xoaPhuongTien('${phuongTien.id}')">Xóa</button>
            <button class="btn btn-primary" onclick="suaPhuongTien('${phuongTien.id}')">Sửa</button>
        </div>
        </td>
        </tr>
        
        
        `;
    }
    document.getElementById('tbody').innerHTML = contentHTML;
    document.getElementById('form').style.display='none';
}
function xoaPhuongTien(id){
    console.log(id);
    var indexDel=-1;
    for (var index=0;index<arrPhuongTien.length;i++){
        var xeTrongMang =  arrPhuongTien[index];
        if(xeTrongMang.id===id){
            indexDel=index;
            break;
        }
    }
    arrPhuongTien.splice(indexDel,1);
    renderPhuongTien(arrPhuongTien);
}
function xoaDefault(){
    document.getElementById('default').innerHTML='';
}
function suaPhuongTien(id){
    document.getElementById('form').style.display='block';
    var indexEdit=-1;
    for (var index=0;index<arrPhuongTien.length;i++){
        var xeTrongMang = arrPhuongTien[index];
        if(xeTrongMang.id===id){
            indexEdit=index;
            break;
        }
    }
    if(indexEdit!=-1){
        
        document.getElementById('id').value = arrPhuongTien[indexEdit].id;
        document.getElementById('ten').value = arrPhuongTien[indexEdit].ten;
        document.getElementById('bienSo').value = arrPhuongTien[indexEdit].bienSo;
        document.getElementById('trongLuong').value = arrPhuongTien[indexEdit].truongLuong;
        document.getElementById('xangTieuThu').value = arrPhuongTien[indexEdit].xangTieuThu;
        document.getElementById('trangThai').value = arrPhuongTien[indexEdit].trangThai;

        
        
    }
    renderPhuongTien(arrPhuongTien);
}
function closeForm(){
    var form = document.getElementById('form');
    form.style.display = 'none';
}