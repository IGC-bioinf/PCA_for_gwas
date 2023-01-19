#!/bin/bash
prefix=$(echo $1| sed "s/.vcf//g")
bcftools norm -m-any ${prefix}.vcf > ${prefix}_splitted.vcf
bgzip ${prefix}_splitted.vcf
tabix ${prefix}_splitted.vcf.gz
bcftools annotate ${prefix}_splitted.vcf.gz --threads 8 -x ID -I +'%CHROM:%POS:%REF:%ALT'   > ${prefix}_annotated.vcf
bcftools view -m2 -M2 -i  'QUAL>30' ${prefix}_annotated.vcf -Ou | bcftools annotate -x FORMAT,INFO  > ${prefix}_cleaned.vcf
plink --vcf  ${prefix}_cleaned.vcf --make-bed --out ${prefix} --double-id
plink --bfile ${prefix} --pca
