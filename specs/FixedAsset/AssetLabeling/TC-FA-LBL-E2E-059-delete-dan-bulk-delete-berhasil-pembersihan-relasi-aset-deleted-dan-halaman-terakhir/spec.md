---
id: TC-FA-LBL-E2E-059-delete-dan-bulk-delete-berhasil-pembersihan-relasi-aset-deleted-dan-halaman-terakhir
title: "Delete dan Bulk Delete Berhasil: Pembersihan Relasi Aset Deleted dan Halaman Terakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-160
  - TC-FA-LBL-161
  - TC-FA-LBL-281
  - TC-FA-LBL-499
coverage:
  web: automated
---

# Delete dan Bulk Delete Berhasil: Pembersihan Relasi Aset Deleted dan Halaman Terakhir

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup: katalog Company Alpha 9 label (#12); aset berstatus Deleted `Laptop Dell - 7` (#13) sebagai pemegang relasi sisa label `Residue Target 161` dan `Residue Bulk A 499`. Relasi sisa dibuat seeding dan dibersihkan oleh aksi Delete yang diuji; aset `Laptop Dell - 7` tidak berubah status (S-06).
- Data Dinamis (label bersih = Total Asset 0, bukan Default Label; nama dasar dari `Fixture.assetLabeling.labels.<kunci>`, suffix `{runId}-059`):
  - TC-FA-LBL-160: `Delete Target 160 {runId}-059` (`deleteTarget160`)
  - TC-FA-LBL-161: `Residue Target 161 {runId}-059` (`residueTarget161`)
  - TC-FA-LBL-499: `Residue Bulk A 499 {runId}-059` (`residueBulkA499`)
  - TC-FA-LBL-499: `Residue Bulk B 499 {runId}-059` (`residueBulkB499`)
  - TC-FA-LBL-281: `Zz Last Row 281 {runId}-059` (`lastRow281`; awalan `Zz` membuatnya terurut terakhir pada default sort Label A-Z)
  - TC-FA-LBL-281: `Zy Last Row Filler 281 {runId}-059` (`lastRowFiller281`; awalan `Zy` membuatnya terurut tepat sebelum `Zz Last Row 281`)
  - `Residue Target 161` dan `Residue Bulk A 499` hanya terpasang pada `Laptop Dell - 7` (Deleted), sehingga Total Asset keduanya `0`.
  - `Zy Last Row Filler 281 {runId}-059` dipakai sebagai precondition TC-FA-LBL-281, tidak diasersi: bersama 9 label Pre-setup (semua bernama terurut sebelum `Zy`) dan `Zz Last Row 281 {runId}-059` membuat katalog tepat 11 label sesudah TC lain menghapus labelnya, dengan `Zz Last Row 281 {runId}-059` sendirian di halaman 2 pada page size 10.
- Katalog Company Alpha berisi 9 label Pre-setup #12 ditambah label seed spec ini; spec lain membersihkan datanya sendiri. Sebelum TC-FA-LBL-281 label seed TC-FA-LBL-160, 161, dan 499 sudah terhapus sehingga katalog tepat 11 label.
- Kemampuan teknis: seeding label lewat fixture BE, termasuk memasang label pada aset berstatus Deleted `Laptop Dell - 7` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE/BE); Kemampuan baca jumlah entri log per surface (Changelog: Labels, System Log aktor, dan Activity Log) untuk label bernama tertentu: disediakan tim FE/BE (mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga tidak ada endpoint yang ditulis). Kemampuan baca status aset lewat fixture BE (disediakan tim FE/BE).
- State global: tidak ada yang diubah. Cleanup di `after`: hapus `Zz Last Row 281 {runId}-059` dan `Zy Last Row Filler 281 {runId}-059` serta label seed yang tersisa.
- Suite berjalan serial (`parallel: false`); spec ini menghapus data sehingga dijalankan sesudah spec non-destruktif.

## Test Steps

1. Atur page size 25

### TC-FA-LBL-160: Delete label bersih berhasil dengan toast dan baris hilang

2. Klik `⋯` pada baris `Delete Target 160 {runId}-059` lalu klik `Delete`
3. Klik `[Delete]`
4. Verifikasi toast `Success, label has been deleted.`
5. Verifikasi dialog tertutup
6. Verifikasi baris `Delete Target 160 {runId}-059` hilang dari tabel seketika

### TC-FA-LBL-161: Delete label bersih ikut membersihkan sisa relasi pada aset berstatus Deleted tanpa menghapus aset

7. Klik `⋯` pada baris `Residue Target 161 {runId}-059` lalu klik `Delete`
8. Verifikasi dialog konfirmasi D-01 `Delete Label` tampil (bukan dialog D-02) karena Total Asset `0` dan aset Deleted tidak dihitung
9. Klik `[Delete]`
10. Verifikasi toast `Success, label has been deleted.`

### TC-FA-LBL-499: Bulk Delete label bersih ikut membersihkan sisa relasi pada aset berstatus Deleted tanpa menghapus aset

11. Centang `Residue Bulk A 499 {runId}-059` dan `Residue Bulk B 499 {runId}-059`
12. Klik `Bulk Action` lalu klik `Delete`
13. Verifikasi dialog `Delete Labels` (D-03) tampil karena Total Asset kedua label `0` dan aset Deleted tidak dihitung
14. Klik `[Delete]` pada dialog `Delete Labels`
15. Verifikasi toast `Success, label has been deleted.`
16. Verifikasi baris `Residue Bulk A 499 {runId}-059` dan `Residue Bulk B 499 {runId}-059` hilang dari tabel
17. Verifikasi aset `Laptop Dell - 7` tetap berstatus Deleted dan tidak terhapus
18. Verifikasi hanya dua entri Delete label yang tercatat: satu untuk `Residue Bulk A 499 {runId}-059` dan satu untuk `Residue Bulk B 499 {runId}-059` pada Changelog: Labels, System Log aktor, dan Activity Log (baseline nol karena nama bersuffix unik)

### TC-FA-LBL-281: Menghapus baris terakhir di halaman terakhir memindahkan ke halaman terakhir yang masih ada

19. Atur page size 10
20. Pindah ke halaman 2
21. Verifikasi halaman 2 memuat tepat satu baris `Zz Last Row 281 {runId}-059`
22. Klik `⋯` pada baris `Zz Last Row 281 {runId}-059` lalu klik `Delete`
23. Klik `[Delete]`
24. Verifikasi tabel pindah ke halaman 1 yang berisi 10 label

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: TC-FA-LBL-281 terakhir karena precondition-nya (katalog tepat 11 label) hanya terpenuhi sesudah label seed TC-FA-LBL-160, 161, dan 499 terhapus; aksi yang menghapus data berada di akhir (S-10).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (page size 25 supaya seluruh label spec tampil tanpa Search) dan langkah 19 (mengembalikan page size 10 agar halaman 2 berisi satu label); pindah ke halaman 2 pada TC-FA-LBL-281.
- Langkah 21 memastikan precondition TC-FA-LBL-281 (label `Zz Last Row 281 {runId}-059` sendirian di halaman 2) sebelum Delete; asersi ini tidak ada di Expected TC dan ditambahkan supaya hasil halaman 1 bermakna (S-14).
- Pencatatan log: Post Condition TC-FA-LBL-160 (satu entri Delete di tiga surface) dan TC-FA-LBL-161 b (tidak ada entri log tambahan di log aset; hanya satu entri Delete label) tidak punya langkah observasi di TC dan tidak diasersi; asersi log itu ada di TC Section 5. Asersi absence log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-FA-LBL-160 a (label tidak muncul di dropdown penugasan `asset/`, filter `reports/`, dan Default Label `settings-asset-name/`) dan c (tidak ada aset yang ikut terhapus) tidak punya langkah observasi di TC dan tidak diasersi; Post Condition TC-FA-LBL-161 a tidak diasersi tetapi Expected c TC-FA-LBL-499 yang sama untuk Bulk Delete diasersi.
  - Cara membuat relasi sisa label pada aset berstatus Deleted `Laptop Dell - 7` tidak didefinisikan di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan seeding yang disediakan tim FE/BE (S-13).
  - TC-FA-LBL-281 mensyaratkan katalog tepat 11 label; label `Zy Last Row Filler 281` dan keadaan 9 label Pre-setup yang tidak bertambah dari spec lain adalah asumsi spec ini.
  - Expected c TC-FA-LBL-499 ("hanya dua entri Delete label tercatat") tidak menyebut surface log; spec memakai tiga surface pencatatan (Changelog: Labels, System Log aktor, dan Activity Log) mengikuti Post Condition TC-FA-LBL-160.
