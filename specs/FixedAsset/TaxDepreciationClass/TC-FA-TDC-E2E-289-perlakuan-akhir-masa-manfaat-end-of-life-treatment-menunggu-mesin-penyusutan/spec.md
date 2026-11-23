---
id: TC-FA-TDC-E2E-289-perlakuan-akhir-masa-manfaat-end-of-life-treatment-menunggu-mesin-penyusutan
title: "Perlakuan Akhir Masa Manfaat Dieksekusi Mesin Penyusutan Menurut End-of-Life Treatment Class (Menunggu Mesin Penyusutan, OI-03 f)"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-961
sourceRules: ["FATDC-LOGIC-03g.2", "FATDC-LOGIC-03g.6", "FAAC-LOGIC-02i", "FAAC-LOGIC-02c"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-03g.2": [2, 4, 6]
  "FATDC-LOGIC-03g.6": [2, 4, 6]
  "FAAC-LOGIC-02i": [2, 4, 6]
  "FAAC-LOGIC-02c": 7
coverage:
  web: unsupported
---

# Perlakuan Akhir Masa Manfaat Dieksekusi Mesin Penyusutan Menurut End-of-Life Treatment Class (Menunggu Mesin Penyusutan, OI-03 f)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan teknis: mesin kalkulasi penyusutan fiskal atau Depreciation Run tersedia (Precondition b TC). Kemampuan ini disediakan tim FE/BE dan saat ini belum disusun (OI-03 f); selama belum tersedia, spec tidak dapat dijalankan sehingga `coverage.web` bernilai `unsupported`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; awalan `DBE-` tidak dipakai TC lain; kemampuan seeding, Asset Class pemakai, dan aset aktif disediakan tim FE/BE):

| Class Code | End-of-Life Treatment | Keadaan |
|---|---|---|
| `DBE-15` | `Charge in final period` | Non-building, Declining Balance, Useful Life 4, Declining Balance Rate 50; dipakai Asset Class dengan aset aktif |
| `DBE-16` | `Switch to straight-line` | Non-building, Declining Balance, Useful Life 4, Declining Balance Rate 50; dipakai Asset Class dengan aset aktif |
| `DBE-17` | `Keep depreciating` | Non-building, Declining Balance, Useful Life 4, Declining Balance Rate 50; dipakai Asset Class dengan aset aktif |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-961: Perlakuan akhir masa manfaat dieksekusi mesin penyusutan menurut End-of-Life Treatment class [DEFERRED]

1. Jalankan penyusutan fiskal sampai periode terakhir masa manfaat untuk aset pada class `DBE-15` (`Charge in final period`)
2. Verifikasi seluruh sisa nilai buku dibebankan sekaligus pada periode terakhir masa manfaat
3. Jalankan penyusutan fiskal sampai periode terakhir masa manfaat untuk aset pada class `DBE-16` (`Switch to straight-line`)
4. Verifikasi penyusutan beralih ke garis lurus atas sisa nilai buku dibagi sisa masa manfaat mulai dari periode ketika beban garis lurus lebih besar daripada beban saldo menurun, sehingga nilai buku habis tepat di akhir masa manfaat
5. Jalankan penyusutan fiskal sampai periode terakhir masa manfaat dan satu tahun pajak sesudah masa manfaat berakhir untuk aset pada class `DBE-17` (`Keep depreciating`)
6. Verifikasi saldo menurun berlanjut setelah masa manfaat berakhir sampai aset dilepas
7. Verifikasi batas Residual Value berlaku pada ketiga perlakuan (pemilik: `asset-class/` FAAC-LOGIC-02c)

## Notes

- TC-FA-TDC-961 berlabel [DEFERRED] (OI-03 f: mesin kalkulasi penyusutan fiskal atau Depreciation Run belum disusun) dan bertanda Manual Only pada kolom Automation. Spec memakai `coverage.web: unsupported` sampai mesin tersedia; konvensi bagian 2 mengatur bahwa TC yang tidak dapat dijalankan karena hambatan teknis tetap ditulis sebagai spec dan tidak dikeluarkan.
- Saat mesin tersedia: ganti `coverage.web` menjadi `automated`; ganti langkah 1, 3, dan 5 dengan langkah menjalankan penyusutan yang sebenarnya (cara menjalankan, periode, dan layar belum didefinisikan TC maupun PRD) dan langkah 2, 4, 6, dan 7 dengan asersi nilai pasti hasil mesin bila TC memuatnya; isi kondisi mesin pada Prerequisites dari kemampuan fixture BE yang tersedia.
- Langkah 2, 4, 6, dan 7 menyalin Expected a sampai d TC-FA-TDC-961 (tiap Expected berlabel [DEFERRED] di TC) sebagai satu `Verifikasi` per klausa (S-01); tidak ada angka karena TC belum menetapkannya.
- Tidak ada langkah penghubung (S-03) selain langkah 1, 3, dan 5 yang merupakan langkah TC.
- Temuan untuk QA:
  - TC-FA-TDC-961 tidak menyebut layar atau cara menjalankan penyusutan fiskal sampai periode terakhir; spec menulis kalimat TC apa adanya tanpa label tombol atau endpoint karangan (S-13).
  - TC-FA-TDC-961 tidak menyebut nilai Useful Life per periode, nilai perolehan aset, atau Residual Value; hanya Useful Life 4 dan Declining Balance Rate 50.
  - TC-FA-TDC-961 menyebut tiga class Non-building dengan Declining Balance dipakai Asset Class dengan aset aktif tanpa menyebut nama Asset Class atau aset; disediakan tim FE/BE.
  - TC-FA-TDC-961 Post Condition tidak ada (kolom "-"); tidak ada asersi tambahan.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
