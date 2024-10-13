#![no_std]
use soroban_sdk::{contract, contracttype, contractimpl, symbol_short, Env, String};
// use serde::{Serialize, Deserialize};

#[contracttype]
#[derive(Clone, Debug)]
pub struct BlockRecord {
    pub block_id: String,
    pub block_name: String,
    pub prison_id: String,
    pub capacity: u64,
}

#[contract]
pub struct BlockContract;

#[contractimpl]
impl BlockContract {
    // Function to add a prisoner record to storage
    pub fn add_prisoner_record(
        env: Env,
        block_id: String,
        block_name: String,
        prison_id: String,
        capacity: u64
    ) {
        // Convert Symbols to Strings for serialization
        let record = BlockRecord {
            block_id,
            block_name,
            prison_id,
            capacity
        };

        // Use BytesN<32> for the storage key and store the record
        let key = symbol_short!("abcdefgh");
        env.storage().persistent().set(&key, &record);

    }

    // Function to remove a prisoner
    pub fn remove_block_record(env: Env, block_id: String) {
        env.storage().persistent().remove(&block_id);
    }

    // Function to retrieve a prisoner record by block_id
    pub fn get_prisoner_record(env: Env, block_id: String) -> Option<BlockRecord> {
        // Retrieve the record using the block_id as the key
        env.storage().persistent().get(&block_id)
    }
}