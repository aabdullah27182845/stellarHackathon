# Soroban Project

## Project Structure

This repository uses the recommended structure for a Soroban project:
```text
.
├── contracts
│   └── hello_world
│       ├── src
│       │   ├── lib.rs
│       │   └── test.rs
│       └── Cargo.toml
├── Cargo.toml
└── README.md
```

- New Soroban contracts can be put in `contracts`, each in their own directory. There is already a `hello_world` contract in there to get you started.
- If you initialized this project with any other example contracts via `--with-example`, those contracts will be in the `contracts` directory as well.
- Contracts should have their own `Cargo.toml` files that rely on the top-level `Cargo.toml` workspace for their dependencies.
- Frontend libraries can be added to the top-level directory as well. If you initialized this project with a frontend template via `--frontend-template` you will have those files already included.


Here is how you can set up the contract and the project:

```
stellar contract build
```


Then, once you have built these, do the following:


```
stellar contract deploy --wasm target/wasm32-unknown-unknown/release/add_prisoner.wasm --network testnet
```


Check if you have a valid key prescriber with this:

```
stellar keys generate --global <name_of_key_prescriber> --network testnet
```


Once you ran the previous command, the one with deploying the contract, you should have gotten a key. After getting this key, run the following:

```
stellar contract invoke --id "CAKEUOVC4S6OOZOZIUUB2YXFUMSH4CR7I36GSDFK7V6UASHFDGUL47NK" --network testnet --source alice -- add_prisoner_record \
                                                                --current_block_id "hello" \
                                                                --current_cell_id "bye bye" \
                                                                --current_prison_id "lmaoo" \
                                                                --date_of_birth 2187828 \
                                                                --risk_status_id "never back down never what" \
                                                                --sentence_end_date 2197828 \
                                                                --background_info "was a crip ahh" \
                                                                --full_name "Joe Mama" \
                                                                --sentence_start_date 3010314 \
                                                                --prisoner_id "crip cuhh"
```

Wait until the get prisoner record ones are made properly too.