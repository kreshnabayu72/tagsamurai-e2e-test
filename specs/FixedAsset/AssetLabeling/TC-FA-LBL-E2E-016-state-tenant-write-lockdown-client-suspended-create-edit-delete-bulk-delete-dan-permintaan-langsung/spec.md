---
id: TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung
title: "State Tenant: Write Lockdown Client Suspended (Create, Edit, Delete, Bulk Delete, dan Permintaan Langsung)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-107
  - TC-FA-LBL-154
  - TC-FA-LBL-175
  - TC-FA-LBL-206
  - TC-FA-LBL-459
coverage:
  web: automated
---

# State Tenant: Write Lockdown Client Suspended (Create, Edit, Delete, Bulk Delete, dan Permintaan Langsung)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control `Client Suspended` (Pre-setup #15, entitas Suspended), `Fixture.assetLabeling.akun.totalControlSuspended`, `Spectra.env.FA_TC_SUSPENDED_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Environment variable: `FA_TC_SUSPENDED_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Dinamis (workspace `Client Suspended`, di-seed di hook `before` sebelum baseline log pada langkah 1, bersuffix `{runId}-016`; dibersihkan di hook `after`; kemampuan seeding pada workspace Suspended disediakan tim FE/BE, lihat Temuan untuk QA):

| Label | Dipakai di | Kondisi |
|---|---|---|
| `Suspended Target {runId}-016` | TC-FA-LBL-154, TC-FA-LBL-459 | bersih, tidak berubah selama spec |
| `Suspended Delete {runId}-016` | TC-FA-LBL-175 | bersih, tidak terhapus selama spec |
| `Suspended Bulk A {runId}-016` | TC-FA-LBL-206 | bersih, tidak terhapus selama spec |
| `Suspended Bulk B {runId}-016` | TC-FA-LBL-206 | bersih, tidak terhapus selama spec |

- Kemampuan teknis: (a) sesi API aktor Total Control `Client Suspended` untuk permintaan langsung ke server pada langkah 33 sampai 40 (klien HTTP); (b) kemampuan membaca jumlah entri log label pada tiga surface (Changelog, System Log, Activity Log) workspace `Client Suspended` untuk baseline langkah 1 (disediakan tim FE/BE, tanpa mengarang endpoint); (c) fixture BE untuk seeding dan pembersihan.
- State global: tidak ada yang diubah (status Suspended adalah keadaan awal Pre-setup #15). Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Persiapan baseline

1. Catat jumlah entri log label pada Changelog, System Log, dan Activity Log workspace `Client Suspended` sebagai baseline
2. Ketik Search `Suspended`, tekan Enter

### TC-FA-LBL-107: Create ditolak saat client Suspended atau Expired

3. Klik `[+ Label]`
4. Isi Label Name dengan `Suspended 107 {runId}-016`
5. Klik `[Submit]`
6. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
7. Tutup toast error
8. Verifikasi modal ditutup dan tabel di-refresh
9. Verifikasi tabel hasil Search tidak memuat baris `Suspended 107 {runId}-016` (tidak ada label dibuat)
10. Verifikasi jumlah entri log label pada tiga surface sama dengan baseline langkah 1 (tidak ada entri log)

### TC-FA-LBL-154: Edit ditolak saat client Suspended

11. Klik `⋯` pada baris `Suspended Target {runId}-016` lalu `Edit`
12. Ganti Label Name dengan `Suspended Edit 154 {runId}-016`
13. Klik `[Save]`
14. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
15. Tutup toast error
16. Verifikasi modal ditutup dan tabel di-refresh
17. Verifikasi baris `Suspended Target {runId}-016` tampil dengan nama yang tidak berubah
18. Verifikasi jumlah entri log label pada tiga surface sama dengan baseline langkah 1 (tidak ada entri log)

### TC-FA-LBL-175: Delete ditolak saat client Suspended

19. Klik `⋯` pada baris `Suspended Delete {runId}-016` lalu `Delete`
20. Klik `[Delete]`
21. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
22. Tutup toast error
23. Verifikasi dialog ditutup dan tabel di-refresh
24. Verifikasi baris `Suspended Delete {runId}-016` masih tampil (label tidak terhapus)
25. Verifikasi jumlah entri log label pada tiga surface sama dengan baseline langkah 1 (tidak ada entri log)

### TC-FA-LBL-206: Bulk Delete ditolak saat client Suspended

26. Centang baris `Suspended Bulk A {runId}-016` dan `Suspended Bulk B {runId}-016`
27. Klik `Bulk Action` lalu klik `Delete`
28. Klik `[Delete]` pada dialog
29. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
30. Verifikasi dialog ditutup dan tabel di-refresh
31. Verifikasi baris `Suspended Bulk A {runId}-016` dan `Suspended Bulk B {runId}-016` masih tampil (tidak ada label terhapus)
32. Verifikasi jumlah entri log label pada tiga surface sama dengan baseline langkah 1 (tidak ada entri log)

### TC-FA-LBL-459: Aksi tulis lewat permintaan langsung ditolak saat client Suspended atau Expired

33. Kirim permintaan langsung ke server (sesi API Total Control `Client Suspended`): membuat label
34. Verifikasi respons ditolak `403 Forbidden`
35. Kirim permintaan langsung ke server: mengubah label seed `Suspended Target {runId}-016`
36. Verifikasi respons ditolak `403 Forbidden`
37. Kirim permintaan langsung ke server: menghapus label seed `Suspended Target {runId}-016`
38. Verifikasi respons ditolak `403 Forbidden`
39. Kirim permintaan langsung ke server: membaca daftar label
40. Verifikasi permintaan baca daftar label berhasil

## Notes

- Langkah penghubung (S-03): langkah 1 (baseline log, S-12), langkah 2 (Search `Suspended` untuk menampilkan label seed; hasilnya memuat empat label seed sehingga menjadi pembanding absence, R-16).
- P-1: asersi "tidak ada entri log" pada langkah 10, 18, 25, dan 32 (TC-FA-LBL-107, 154, 175, 206) ditulis di spec ini dengan baseline, bukan dirujuk ke spec absence, karena tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05); state tenant `Client Suspended` adalah keadaan berat (status entitas di Pre-setup #15) yang dipakai bersama ke empat TC. Asersi log permintaan langsung (TC-FA-LBL-459) tidak ada di Expected TC dan tidak diasersi.
- Toast error identik berulang antar TC: toast ditutup (langkah 7, 15, 22) sebelum asersi toast TC berikutnya (R-12).
- Permintaan langsung (langkah 33 sampai 40) tidak melewati browser: asersi hanya status respons (bagian 8b butir 1).
- Absence (langkah 9, 17, 24, 31): toast error langkah sebelumnya dan baris seed lain pada Search `Suspended` menjadi anchor positif (bagian 8b butir 2).
- Alasan di atas sekitar 35 langkah (40 langkah): seluruh blok adalah lockdown tulis client Suspended (kelas h) dengan akun dan dataset seed yang sama; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LBL-107 sampai 206 menyebut "tidak ada entri log" tanpa menyebut surface; spec memeriksa tiga surface (Changelog, System Log, Activity Log) lewat kemampuan baca yang disediakan tim FE/BE.
  - TC-FA-LBL-459 Judul menyebut Suspended atau Expired tetapi Precondition hanya Client Suspended (Pre-setup #15); permintaan langsung pada Client Expired (Pre-setup #16) tidak diuji di spec ini. "Tanpa memandang capability" tidak teramati karena hanya satu akun (Total Control) yang mengirim permintaan.
  - TC-FA-LBL-206 Precondition "Dua label bersih tersedia" tanpa nama; spec memakai `Suspended Bulk A` dan `Suspended Bulk B`.
  - Seeding label pada workspace berstatus Suspended membutuhkan kemampuan khusus (aksi tulis ditolak untuk akun biasa); mekanisme tidak ditulis TC, PRD, atau LLD.
  - TC-FA-LBL-107 Judul menyebut Expired sedangkan Precondition hanya Suspended; Expired diuji di TC-FA-LBL-108 (spec 157).
