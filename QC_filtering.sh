
#QC

plink --bfile proj_1 --missing
Rscript --no-save hist_miss.R
plink --bfile proj_1 --geno 0.2 --make-bed --out proj_2
plink --bfile proj_2 --mind 0.2 --make-bed --out proj_3
plink --bfile proj_3 --geno 0.02 --make-bed --out proj_4
plink --bfile proj_4 --mind 0.02 --make-bed --out proj_5
Rscript --no-save gender_check.R
grep "PROBLEM" plink.sexcheck| awk '{print$1,$2}'> sex_discrepancy.txt
plink --bfile proj_5 --remove sex_discrepancy.txt --make-bed --out proj_6
plink --bfile proj_5 --impute-sex --make-bed --out proj_6
awk '{ if ($1 >= 1 && $1 <= 22) print $2 }' proj_6.bim > snp_1_22.txt
plink --bfile proj_6 --extract snp_1_22.txt --make-bed --out proj_7
plink --bfile proj_7 --freq --out MAF_check
plink --bfile proj_7 --maf 0.05 --make-bed --out proj_8
plink --bfile HapMap_hwe_filter_step1 --hwe 1e-10 --hwe-all --make-bed --out proj_9
plink --bfile proj_9 --exclude inversion.txt --range --indep-pairwise 50 5 0.2 --out indepSNP
plink --bfile proj_9 --extract indepSNP.prune.in --het --out R_check
Rscript --no-save check_heterozygosity_rate.R
Rscript --no-save heterozygosity_outliers_list.R
sed 's/"// g' fail-het-qc.txt | awk '{print$1, $2}'> het_fail_ind.txt
plink --bfile proj_9 --remove het_fail_ind.txt --make-bed --out proj_10
plink --bfile proj_10 --extract indepSNP.prune.in --genome --min 0.2 --out pihat_min0.2
awk '{ if ($8 >0.9) print $0 }' pihat_min0.2.genome>zoom_pihat.genome
Rscript --no-save Relatedness.R
plink --bfile proj_10 --filter-founders --make-bed --out proj_11
plink --bfile proj_11 --extract indepSNP.prune.in --genome --min 0.2 --out pihat_min0.2_in_founders
plink --bfile proj_11 --missing

