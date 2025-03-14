PLMC_DIR=$1

$PLMC_DIR/plmc/bin/plmc \
    -o plmc/adk_175_org_bs_focus.model_params \
    -c plmc/adk_175_org_bs_focus.EC \
    -le 16.2 -lh 0.01 -m 200 -t 0.2 \
    -f bacillus_subtilis \
    ../data/175_adk_org_aligned.fasta 