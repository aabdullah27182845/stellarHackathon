#![no_std]
use soroban_sdk::{contract, contracttype, contractimpl, symbol_short, Env, String};
// use serde::{Serialize, Deserialize};

#[contracttype]
#[derive(Clone, Debug)]
pub struct PrisonerRecord {
    pub prisoner_id: String,          // Use String instead of Symbol for serialization
    pub full_name: String,            // Use String instead of Symbol for serialization
    pub date_of_birth: u64,           // Dates as Unix timestamps
    pub sentence_start_date: u64,     
    pub sentence_end_date: u64,       
    pub background_info: String,      // Use String instead of Symbol for serialization
    pub risk_status_id: String,       // Use String instead of Symbol for serialization
    pub current_prison_id: String,    
    pub current_block_id: String,     
    pub current_cell_id: String,      
}

// Manual implementation of Serialize and Deserialize
// impl PrisonerRecord {
//     // Helper function to convert from Symbol to String
//     pub fn from_symbol(symbol: &Symbol) -> String {
//         let symbol_str: String = symbol.to_string();
//         symbol_str
//     }

//     // Helper function to convert from String to Symbol
//     pub fn to_symbol(env: &Env, string: &String) -> Symbol {
//         Symbol::new(env, string)
//     }
// }

#[contract]
pub struct InmateContract;

#[contractimpl]
impl InmateContract {
    // Function to add a prisoner record to storage
    pub fn add_prisoner_record(
        env: Env,
        prisoner_id: String,
        full_name: String,
        date_of_birth: u64,
        sentence_start_date: u64,
        sentence_end_date: u64,
        background_info: String,
        risk_status_id: String,
        current_prison_id: String,
        current_block_id: String,
        current_cell_id: String,
    ) {
        // Convert Symbols to Strings for serialization
        let record = PrisonerRecord {
            prisoner_id,
            full_name,
            date_of_birth,
            sentence_start_date,
            sentence_end_date,
            background_info,
            risk_status_id,
            current_prison_id,
            current_block_id,
            current_cell_id,
        };

        // Use BytesN<32> for the storage key and store the record
        let key = symbol_short!("abcdefgh");
        env.storage().persistent().set(&key, &record);

    }

    // Function to remove a prisoner
    pub fn remove_prisoner_record(env: Env, prisoner_id: String) {
        env.storage().persistent().remove(&prisoner_id);
    }

    // Function to retrieve a prisoner record by prisoner_id
    pub fn get_prisoner_record(env: Env, prisoner_id: String) -> Option<PrisonerRecord> {
        // Retrieve the record using the prisoner_id as the key
        env.storage().persistent().get(&prisoner_id)
    }
}