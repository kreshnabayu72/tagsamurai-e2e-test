---
id: TC-FA-LBL-E2E-157-state-tenant-write-lockdown-client-expired-create-dan-seluruh-aksi-tulis-dengan-baca-tetap-diizinkan
title: "State Tenant: Write Lockdown Client Expired (Create dan Seluruh Aksi Tulis dengan Baca Tetap Diizinkan)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-108
  - TC-FA-LBL-475
coverage:
  web: automated
---

# State Tenant: Write Lockdown Client Expired (Create dan Seluruh Aksi Tulis dengan Baca Tetap Diizinkan)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control `Client Expired` (Pre-setup #16, entitas Expired), `Fixture.assetLabeling.akun.totalControlExpired`, `Spectra.env.FA_TC_EXPIRED_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Environment variable: `FA_TC_EXPIRED_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Dinamis (workspace `Client Expired`, di-seed di hook `before` sebelum baseline log pada langkah 1, bersuffix `{runId}-157`; dibersihkan di hook `after`; kemampuan seeding pada workspace Expired disediakan tim FE/BE, lihat Temuan untuk QA):

| Label | Dipakai di | Kondisi |
|---|---|---|
| `Expired Edit 475 {runId}-157` | TC-FA-LBL-475 | bersih, tidak berubah selama spec; chip dibuka di Drawer (langkah 10) |
| `Expired Delete 475 {runId}-157` | TC-FA-LBL-475 | bersih, tidak terhapus selama spec |
| `Expired Bulk A 475 {runId}-157` | TC-FA-LBL-475 | bersih, tidak terhapus selama spec |
| `Expired Bulk B 475 {runId}-157` | TC-FA-LBL-475 | bersih, tidak terhapus selama spec |

- Kemampuan teknis: (a) kemampuan membaca jumlah entri log label pada tiga surface (Changelog, System Log, Activity Log) workspace `Client Expired` untuk baseline langkah 1 (disediakan tim FE/BE, tanpa mengarang endpoint); (b) fixture BE untuk seeding dan pembersihan (lihat `suite.md`).
- State global: tidak ada yang diubah (status Expired adalah keadaan awal Pre-setup #16). Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Persiapan baseline

1. Catat jumlah entri log label pada Changelog, System Log, dan Activity Log workspace `Client Expired` sebagai baseline
2. Ketik Search `Expired`, tekan Enter

### TC-FA-LBL-108: Create ditolak saat client Expired dengan copy yang sama

3. Klik `[+ Label]`
4. Isi Label Name dengan `Expired 108 {runId}-157`
5. Klik `[Submit]`
6. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
7. Tutup toast error
8. Verifikasi tabel hasil Search tidak memuat baris `Expired 108 {runId}-157` (tidak ada label dibuat)

### TC-FA-LBL-475: Client Expired menolak Create, Edit, Delete, dan Bulk Delete dengan copy yang sama sementara baca tetap diizinkan

9. Verifikasi Labels List menampilkan label seed `Expired Edit 475 {runId}-157`, `Expired Delete 475 {runId}-157`, `Expired Bulk A 475 {runId}-157`, dan `Expired Bulk B 475 {runId}-157` (baca daftar berhasil)
10. Klik chip `Expired Edit 475 {runId}-157`
11. Verifikasi Drawer Tagged Asset terbuka (baca Drawer berhasil)
12. Tutup Drawer Tagged Asset
13. Klik icon Changelog
14. Verifikasi Modal Changelog terbuka (baca Changelog berhasil)
15. Tutup Modal Changelog
16. Klik `[+ Label]`
17. Isi Label Name dengan `Expired Create 475 {runId}-157`
18. Klik `[Submit]`
19. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` untuk Create
20. Tutup toast error
21. Klik `⋯` pada baris `Expired Edit 475 {runId}-157` lalu `Edit`
22. Ganti Label Name dengan `Expired Edit 475 Renamed {runId}-157`
23. Klik `[Save]`
24. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` untuk Edit
25. Tutup toast error
26. Klik `⋯` pada baris `Expired Delete 475 {runId}-157` lalu `Delete`
27. Klik `[Delete]` pada dialog
28. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` untuk Delete
29. Tutup toast error
30. Centang baris `Expired Bulk A 475 {runId}-157` dan `Expired Bulk B 475 {runId}-157`
31. Klik `Bulk Action` lalu klik `Delete`
32. Klik `[Delete]` pada dialog
33. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` untuk Bulk Delete
34. Verifikasi keempat label seed tampil dengan nama semula (tidak ada perubahan data)
35. Verifikasi tabel hasil Search tidak memuat baris `Expired Create 475 {runId}-157` dan `Expired Edit 475 Renamed {runId}-157`
36. Verifikasi jumlah entri log label pada tiga surface sama dengan baseline langkah 1 (tidak ada entri log)

## Notes

- Langkah penghubung (S-03): langkah 1 (baseline log, S-12), langkah 2 (Search `Expired` untuk menampilkan label seed; hasilnya memuat empat label seed sehingga menjadi pembanding absence, R-16), langkah 12 dan 15 (menutup Drawer dan modal), langkah 7, 20, 25, dan 29 (menutup toast error identik yang berulang sebelum asersi toast berikutnya, R-12).
- P-1: asersi "tidak ada entri log" pada langkah 36 (TC-FA-LBL-475) ditulis di spec ini dengan baseline, bukan dirujuk ke spec absence, karena tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05); state tenant `Client Expired` adalah keadaan berat (status entitas di Pre-setup #16).
- Absence (langkah 8, 35): toast error langkah sebelumnya dan label seed lain pada Search `Expired` menjadi anchor positif (bagian 8b butir 2).
- Alasan di atas sekitar 35 langkah (36 langkah): seluruh blok adalah lockdown tulis client Expired (kelas h) dengan akun dan dataset seed yang sama; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-LBL-108 tidak menyebut keadaan modal sesudah toast error; TC-FA-LBL-107 menyebut modal ditutup otomatis untuk copy yang sama. Langkah 16 mengandaikan modal Create sudah tertutup (seperti TC-FA-LBL-107).
  - TC-FA-LBL-475 menyebut "tidak ada entri log" tanpa menyebut surface; spec memeriksa tiga surface lewat kemampuan baca yang disediakan tim FE/BE.
  - TC-FA-LBL-475 Precondition "Label seed tersedia" tanpa nama; spec memakai empat label seed (`Expired Edit 475`, `Expired Delete 475`, `Expired Bulk A 475`, `Expired Bulk B 475`).
  - Seeding label pada workspace berstatus Expired membutuhkan kemampuan khusus (aksi tulis ditolak untuk akun biasa); mekanisme tidak ditulis TC, PRD, atau LLD.
