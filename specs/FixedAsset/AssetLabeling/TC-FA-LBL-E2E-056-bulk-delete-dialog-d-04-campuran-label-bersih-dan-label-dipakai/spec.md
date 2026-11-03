---
id: TC-FA-LBL-E2E-056-bulk-delete-dialog-d-04-campuran-label-bersih-dan-label-dipakai
title: "Bulk Delete: Dialog D-04 Campuran (Label Bersih dan Label Dipakai)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-191
  - TC-FA-LBL-192
  - TC-FA-LBL-193
  - TC-FA-LBL-194
coverage:
  web: automated
---

# Bulk Delete: Dialog D-04 Campuran (Label Bersih dan Label Dipakai)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Alpha; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.assetLabeling.totalControl.email`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Seeding label di hook `before` spec ini lewat fixture BE; cleanup di hook `after` menghapus label sisa milik spec dan tidak mengasumsikan setup berhasil penuh.
- Data Pre-setup: katalog Company Alpha 9 label (#12); `High Priority` (Total Asset 3, label dipakai) dan `Warehouse Priority` (Total Asset 0, Default Label Asset Name `Warehouse Item`, #12 dan #14) hanya dipilih dan tidak dihapus: dialog `Cancel` atau `[Continue]` melewatinya sehingga Last Updated keduanya tidak berubah (S-06).
- Data Dinamis (label bersih = Total Asset 0, bukan Default Label; nama dasar dari `Fixture.assetLabeling.labels.<kunci>`, suffix `{runId}-056`):
  - TC-FA-LBL-191: `Bulk Clean A 191 {runId}-056` (`bulkCleanA191`)
  - TC-FA-LBL-191: `Bulk Clean B 191 {runId}-056` (`bulkCleanB191`)
  - TC-FA-LBL-192: `Bulk Clean A 192 {runId}-056` (`bulkCleanA192`)
  - TC-FA-LBL-192: `Bulk Clean B 192 {runId}-056` (`bulkCleanB192`)
  - TC-FA-LBL-193: `Bulk Clean A 193 {runId}-056` (`bulkCleanA193`)
  - TC-FA-LBL-194: `Bulk Clean A 194 {runId}-056` (`bulkCleanA194`)
- Katalog Company Alpha berisi 9 label Pre-setup #12 ditambah label seed spec ini; spec lain membersihkan datanya sendiri sehingga total di bawah 25 baris dan page size 25 cukup menampilkan seluruhnya tanpa Search.
- Kemampuan teknis: seeding label lewat fixture BE.
- State global: tidak ada yang diubah. Label TC-FA-LBL-191, 193, dan 194 tetap ada sampai `after`; label TC-FA-LBL-192 dihapus oleh spec.
- Suite berjalan serial (`parallel: false`); spec ini menghapus data sehingga dijalankan sesudah spec non-destruktif.

## Test Steps

1. Atur page size 25

### TC-FA-LBL-191: Screening dialog Bulk Delete campuran (D-04)

2. Centang `Bulk Clean B 191 {runId}-056`, `High Priority`, dan `Bulk Clean A 191 {runId}-056` (urutan klik B, High Priority, A)
3. Klik `Bulk Action` lalu klik `Delete`
4. Verifikasi dialog Title `Delete Labels`
5. Verifikasi teks `The following will be deleted:` diikuti bullet `• Bulk Clean A 191 {runId}-056` dan `• Bulk Clean B 191 {runId}-056` terurut abjad A sampai Z
6. Verifikasi teks `The following are in use and will be skipped:` diikuti bullet `• High Priority`
7. Verifikasi teks penutup `Are you sure you want to continue? This action cannot be undone.`
8. Verifikasi tombol `[Cancel]` dan `[Continue]` (danger/merah) tampil
9. Klik `[Cancel]`
10. Klik ikon `×`

### TC-FA-LBL-193: Cancel pada D-04 tidak menghapus dan mempertahankan seleksi

11. Centang `Bulk Clean A 193 {runId}-056` dan `High Priority`
12. Klik `Bulk Action` lalu klik `Delete`
13. Klik `[Cancel]`
14. Verifikasi dialog tertutup
15. Verifikasi baris `Bulk Clean A 193 {runId}-056` dan `High Priority` tetap ada
16. Verifikasi seleksi dan Bulk Action Bar dipertahankan dengan counter `2 Labels selected`
17. Klik ikon `×`

### TC-FA-LBL-194: Label yang hanya menjadi Default Label dihitung dipakai pada D-04

18. Centang `Bulk Clean A 194 {runId}-056` dan `Warehouse Priority`
19. Klik `Bulk Action` lalu klik `Delete`
20. Verifikasi dialog Title `Delete Labels`
21. Verifikasi teks `The following will be deleted:` dengan bullet `• Bulk Clean A 194 {runId}-056`
22. Verifikasi teks `The following are in use and will be skipped:` dengan bullet `• Warehouse Priority`
23. Klik `[Cancel]`
24. Klik ikon `×`

### TC-FA-LBL-192: Continue pada D-04 menghapus yang bersih dan melewati yang dipakai

25. Centang `Bulk Clean A 192 {runId}-056`, `Bulk Clean B 192 {runId}-056`, dan `High Priority`
26. Klik `Bulk Action` lalu klik `Delete`
27. Klik `[Continue]`
28. Verifikasi toast `Success, label has been deleted. Some items were skipped.`
29. Verifikasi baris `Bulk Clean A 192 {runId}-056` dan `Bulk Clean B 192 {runId}-056` hilang dari tabel
30. Verifikasi baris `High Priority` tetap ada dengan Total Asset `3`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: TC-FA-LBL-192 (aksi yang menghapus data) di akhir; TC-FA-LBL-191, TC-FA-LBL-193, dan TC-FA-LBL-194 yang tidak mengubah data mendahuluinya (S-10).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (page size 25 supaya seluruh label spec tampil tanpa Search); klik `[Cancel]` dan klik ikon `×` di akhir TC-FA-LBL-191, TC-FA-LBL-193, dan TC-FA-LBL-194 menutup dialog dan membersihkan seleksi sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-186 dan TC-FA-LBL-195 (dialog Bulk Delete yang semuanya dipakai) ada di spec 052.
- Pencatatan log: Post Condition TC-FA-LBL-192 (seleksi 0 termasuk label yang dilewati; entri Delete hanya untuk dua label yang terhapus) tidak punya langkah observasi di TC dan tidak diasersi di spec ini.
- Temuan untuk QA:
  - Post Condition TC-FA-LBL-192 a dan b (bar hilang dan seleksi 0 termasuk label yang dilewati; tidak ada entri untuk `High Priority`) tidak diasersi karena TC tidak memberi langkah observasi.
  - TC-FA-LBL-193 Precondition menyebut `Bulk Clean B 193` tetapi Langkah Uji hanya memakai `Bulk Clean A 193` dan `High Priority`; TC-FA-LBL-194 memakai `Warehouse Priority` dengan Total Asset 0 yang konsisten dengan Pre-setup #12.
