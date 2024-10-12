fn main() {
    // Link with the Python 3.12 library
    println!("cargo:rustc-link-lib=python3.12");

    // Adjust the path to where libpython3.12.so is located
    println!("cargo:rustc-link-search=native=/usr/lib");
}

