# Fasta parser and converts to genbank format.
## Computing in Molecular Biology 1 Assignment.

## Run setup.sh to start converting.
```
git clone https://github.com/jsphu/muscle-proteins
cd muscle-proteins
./setup.sh
```

## You'll get this output on your terminal when it is done.
```
LOCUS       NP_001258970.1           377 aa                     UNK 01-JAN-1980
DEFINITION  NP_001258970.1 actin, alpha skeletal muscle [Mus musculus].
ACCESSION   NP_001258970
VERSION     NP_001258970.1
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     region          1..377
ORIGIN
        1 mcdedettal vcdngsglvk agfagddapr avfpsivgrp rhqgvmvgmg qkdsyvgdea
       61 qskrgiltlk ypiehgiitn wddmekiwhh tfynelrvap eehptlltea plnpkanrek
      121 mtqimfetfn vpamyvaiqa vlslyasgrt tgivldsgdg vthnvpiyeg yalphaimrl
      181 dlagrdltdy lmkiltergy sfvttaerei vrdikeklcy valdfenema taasssslek
      241 syelpdgqvi tignerfrcp etlfqpsfig mesagihett ynsimkcdid irkdlyannv
      301 msggttmypg iadrmqkeit alapstmkik iiapperkys vwiggsilas lstfqqmwit
      361 kqeydeagps ivhrkcf
//
LOCUS       KAA0193717.1             367 aa                     UNK 01-JAN-1980
DEFINITION  KAA0193717.1 Actin alpha skeletal muscle [Fasciolopsis buskii].
ACCESSION   KAA0193717
VERSION     KAA0193717.1
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     region          1..367
ORIGIN
        1 mtleempivl dngagylkag yagesapril vpmyttrtfs ywgpsewfvg eharalrref
       61 plscpisqgq vtdfdelaiv wqyvyakelr tnpaerpilv teypllprch reriaemafe
      121 kfsipaiyfa cqsvlslyav glstglsvdi gtaitnvtpv vesyvltest krhtiggmdv
      181 tnflqrllvs anpkvarfin advtryfkeq lcyltldstt etplysqsqp vryqtpdgql
      241 vsigqerpma peilfnpkqa gleangiqhs vlsairecre elqpylfgni vlsggttmtr
      301 gfperlkqel tnltgdcvln vyapphrkys vwiggsilgs lstfqdslis kkefeeigsa
      361 ivhqkcp
//
LOCUS       NP_001091.1              377 aa                     UNK 01-JAN-1980
DEFINITION  NP_001091.1 actin, alpha skeletal muscle [Homo sapiens].
ACCESSION   NP_001091
VERSION     NP_001091.1
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     region          1..377
ORIGIN
        1 mcdedettal vcdngsglvk agfagddapr avfpsivgrp rhqgvmvgmg qkdsyvgdea
       61 qskrgiltlk ypiehgiitn wddmekiwhh tfynelrvap eehptlltea plnpkanrek
      121 mtqimfetfn vpamyvaiqa vlslyasgrt tgivldsgdg vthnvpiyeg yalphaimrl
      181 dlagrdltdy lmkiltergy sfvttaerei vrdikeklcy valdfenema taasssslek
      241 syelpdgqvi tignerfrcp etlfqpsfig mesagihett ynsimkcdid irkdlyannv
      301 msggttmypg iadrmqkeit alapstmkik iiapperkys vwiggsilas lstfqqmwit
      361 kqeydeagps ivhrkcf
//
Converted to ./output/muscle-proteins.gb
```

## Credits.
Y. Unal 2024
