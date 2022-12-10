var btnThongBao = document.getElementById('btn-thong-bao');
btnThongBao.onclick = function(){
    //input: taiKhoan: string, matKhau:string
    var taiKhoan =document.getElementById('taikhoan').value;
    var matKhau=document.getElementById('matkhau').value; 




    //output: ketQua:string
    //process:xử lý
    if (taiKhoan==='admin'&& matKhau==='123'){
        window.location="index";
    }
    else{
        btnThongBao.innerHTML = 'Login unsuccessful';
        btnThongBao.className = 'btn btn-danger';
    }
}