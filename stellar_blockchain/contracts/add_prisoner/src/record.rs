#![no_std]
use soroban_sdk::{contract, contractimpl, Env, Symbol, Map, BytesN, Address};

#[derive(Clone)]
pub struct PrisonerRecord {
    pub prisoner_id: Symbol,
    pub first_name: Symbol,
    pub last_name: Symbol,
    pub date_of_birth: u64,           // Using u64 for date (timestamp)
    pub gender: Symbol,
    pub sentence_start_date: u64,     // Using u64 for date (timestamp)
    pub sentence_end_date: u64,       // Using u64 for date (timestamp)
    pub background_info: Symbol,
    pub risk_status_id: Symbol,       // Can later be linked externally
    pub current_prison_id: Symbol,
    pub current_block_id: Symbol,
    pub current_cell_id: Symbol,
}

#[contract]
pub struct InmateContract;