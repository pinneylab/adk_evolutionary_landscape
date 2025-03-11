PLMC_DIR=$1

$PLMC_DIR/plmc/bin/plmc \
    -o plmc/big_adk.model_params \
    -c plmc/big_adk.EC \
    -le 16.2 -lh 0.01 -m 200 -t 0.2 \
    ../data/all_adk_representative_seqs_bacdive_aligned.fasta 