# Covert to bed
plink --vcf whole_bel.vcf.gz --make-bed --out proj_1
# Update sex, family, pheno

plink --bfile proj_1 --update-sex ./proj_update_files/sex.txt --make-bed --out proj_1
plink --bfile proj_1 --update-ids ./proj_update_files/family.txt --make-bed --out proj_1
plink --bfile proj_1 --update-parents ./proj_update_files/parents.txt --make-bed --out proj_1
plink --bfile proj_1 --pheno ./proj_update_files/pheno_nek.txt --make-bed --out proj_1

