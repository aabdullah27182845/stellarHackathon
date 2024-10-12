#![no_std]
use soroban_sdk::{contract, contractimpl, Env, String, Symbol};
use soroban_sdk::serde::{Serialize, Deserialize};

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
impl PrisonerRecord {
    // Helper function to convert from Symbol to String
    pub fn from_symbol(symbol: &Symbol) -> String {
        let symbol_str: String = symbol.to_string();
        symbol_str
    }

    // Helper function to convert from String to Symbol
    pub fn to_symbol(env: &Env, string: &String) -> Symbol {
        Symbol::new(env, string)
    }
}

#[contract]
pub struct InmateContract;

#[contractimpl]
impl InmateContract {
    // Function to add a prisoner record to storage
    pub fn add_prisoner_record(
        env: Env,
        prisoner_id: Symbol,
        full_name: Symbol,
        date_of_birth: u64,
        sentence_start_date: u64,
        sentence_end_date: u64,
        background_info: Symbol,
        risk_status_id: Symbol,
        current_prison_id: Symbol,
        current_block_id: Symbol,
        current_cell_id: Symbol,
    ) {
        // Convert Symbols to Strings for serialization
        let record = PrisonerRecord {
            prisoner_id: PrisonerRecord::from_symbol(&prisoner_id),
            full_name: PrisonerRecord::from_symbol(&full_name),
            date_of_birth,
            sentence_start_date,
            sentence_end_date,
            background_info: PrisonerRecord::from_symbol(&background_info),
            risk_status_id: PrisonerRecord::from_symbol(&risk_status_id),
            current_prison_id: PrisonerRecord::from_symbol(&current_prison_id),
            current_block_id: PrisonerRecord::from_symbol(&current_block_id),
            current_cell_id: PrisonerRecord::from_symbol(&current_cell_id),
        };

        // Store the record using prisoner_id as the key
        env.storage().set(&prisoner_id, &record);
    }

    // Function to retrieve a prisoner record by prisoner_id
    pub fn get_prisoner_record(env: Env, prisoner_id: Symbol) -> Option<PrisonerRecord> {
        // Retrieve the record using the prisoner_id as the key
        env.storage().get(&prisoner_id)
    }
}
