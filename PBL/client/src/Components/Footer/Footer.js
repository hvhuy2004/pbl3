import React from "react";

function Footer() {
  return (
    <>
      <footer className="footer text-center">
        <div className="container">
          <div className="row d-flex justify-content-center">
            <div className="col-lg-4 mb-5 mb-lg-0">
              <h4 className="text-uppercase mb-3">Đại học Bách Khoa - Đại học Đà Nẵng</h4>
              <p className="lead mb-0">
                54, Nguyễn Lương Bằng,
                <br />
                Quận Liên Chiểu, Thành phố Đà Nẵng
              </p>
            </div>
            <div className="col-lg-4 mb-5 mb-lg-0">
              <h4 className="text-uppercase mb-4">liên quan</h4>
              <a className="btn btn-outline-light btn-social mx-1" href="#!">
                <i className="fab fa-fw fa-facebook-f" />
              </a>
              <a className="btn btn-outline-light btn-social mx-1" href="#!">
                <i className="far fa-chart-bar"></i>
              </a>
              <a className="btn btn-outline-light btn-social mx-1" href="#!">
                <i className="fab fa-fw fa-internet-explorer" />
              </a>
            </div>
            <div className="col-lg-4">
              <h4 className="text-uppercase mb-4">đồ án chuyên ngành</h4>
              <p className="lead mb-0">
                Giảng viên hướng dẫn: Nguyễn Tấn Khôi
                <br />
                Nhóm thực hiện: Vũ Huy, Phước Thành
              </p>
            </div>
          </div>
        </div>
      </footer>
      <div className="copyright py-4 text-center text-white">
        <div className="container">
          <small>Copyright © Vieclam24h.vn</small>
        </div>
      </div>
    </>
  );
}

export default Footer;
