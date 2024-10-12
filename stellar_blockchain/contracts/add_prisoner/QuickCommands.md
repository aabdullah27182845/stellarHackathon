
# Quick References

Here is the command that allows you to fetch a user record from the stellar service.

`stellar contract invoke --id <contract-id> --secret <your-secret-key> --get_prisoner_record \
    prisoner_id="prisoner-001"`


Here is one that adds a record from the cli

`stellar contract invoke --id <contract-id> --secret <your-secret-key> --add_prisoner_record \
    prisoner_id="prisoner-001" first_name="John" last_name="Doe" date_of_birth=600000000 \
    gender="Male" sentence_start_date=1638316800 sentence_end_date=1702453325 \
    background_info="Non-violent offender" risk_status_id="medium" \
    current_prison_id="prison-001" current_block_id="block-001" current_cell_id="cell-001"`


