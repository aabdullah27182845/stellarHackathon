use pyo3::prelude::*;

fn main() -> PyResult<()> {
    Python::with_gil(|_py| {
        println!("Python interpreter initialized!");
        Ok(())
    })
}

// fn main() {
//     if cfg!(target_os = "linux") {
//         println!("cargo:rustc-link-lib=python3.8");
//         println!("cargo:rustc-link-search=native=/usr/lib");
//     } else if cfg!(target_os = "macos") {
//         println!("cargo:rustc-link-lib=python3.8");
//         println!("cargo:rustc-link-search=native=/usr/local/lib");
//     } else if cfg!(target_os = "windows") {
//         println!("cargo:rustc-link-lib=python38");
//         println!("cargo:rustc-link-search=native=C:\\path\\to\\python\\libs");
//     }
// }
