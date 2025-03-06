PLMC_DIR=$1

$PLMC_DIR/plmc/bin/plmc \
    -o plmc/adk_175_org.model_params \
    -c plmc/adk_175_org.EC \
    -le 16.2 -lh 0.01 -m 200 -t 0.2 -g \
    ../data/175_adk_org_aligned.fasta 