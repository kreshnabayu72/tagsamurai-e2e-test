---
id: TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx
title: "Modal Changelog User: Download CSV dan XLSX (Isi Berkas Seluruh Data, Cakupan Search, Kolom Hidden, dan Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-503
  - TC-GS-USER-504
  - TC-GS-USER-505
  - TC-GS-USER-506
  - TC-GS-USER-507
coverage:
  web: automated
---

# Modal Changelog User: Download CSV dan XLSX (Isi Berkas Seluruh Data, Cakupan Search, Kolom Hidden, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role, Full CRUD (Fajar Nugroho), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4); kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`. Dipakai hanya untuk memicu entri Changelog dengan Modified By kedua `Fajar N` (nama singkat dibentuk seperti `Siti N`; TC tidak menyebutnya), sehingga kolom Modified By punya sedikitnya dua nilai distinct (S-11). Tidak ada sesi UI kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`, berurutan; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-083@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Hanya data yang dipakai `Verifikasi` yang di-seed):
  - U-1: Create `Alfa {runId}-083` oleh Siti Nurhaliza (Action Create, Old Value `—`, Modified By `Siti N`), lalu Edit Position `Staff` menjadi `Supervisor` oleh Siti Nurhaliza (Action Edit). Search `Alfa {runId}-083` hanya mengembalikan kedua entri ini (TC-GS-USER-505).
  - U-2: Create `Beta {runId}-083` oleh Fajar Nugroho (Action Create, Modified By `Fajar N`), lalu Deactivate oleh Siti Nurhaliza (Action Deactivate); memberi entri di luar hasil Search `Alfa`.
  - U-3 sampai U-10: Create `Unduh 01 {runId}-083` sampai `Unduh 08 {runId}-083` oleh Siti Nurhaliza. Bersama U-1 dan U-2, spec ini menghasilkan 12 entri (lebih dari 10), sehingga berkas ekspor melebihi satu halaman tampilan (TC-GS-USER-503).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1 sampai U-10 bila masih ada; hapus berkas unduhan; kembalikan sesi ke akun default suite; hapus konfigurasi kolom Modal Changelog User di `localStorage` bila tersisa. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f; isi berkas dipisah dari kegagalan ekspor): menangkap tiap berkas unduhan browser ke direktori bersih terpisah; membaca isi berkas CSV dan XLSX (nama berkas, baris header, jumlah baris data, nilai sel); membaca total entri Changelog Client sebagai pembanding jumlah baris CSV (disediakan tim FE/BE; TC tidak menyebut cara).
- Precondition TC-GS-USER-503 sampai 507: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); riwayat Changelog terisi.
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-083`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: konfigurasi kolom Modal Changelog User (TC-GS-USER-506 menyembunyikan lalu menampilkan lagi `Modified By`, dipulihkan di langkah 26).

## Test Steps

### TC-GS-USER-503: Download CSV seluruh data tanpa toast sukses
1. Klik icon Changelog di Table Tools
2. Klik icon Download di modal
3. Verifikasi overlay memuat opsi `Download as CSV` dan `Download as XLSX`
4. Klik `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Changelog-User.csv` terunduh
7. Verifikasi berkas memuat semua baris (jumlah baris data sama dengan total entri Changelog Client)
8. Verifikasi jumlah baris data berkas lebih dari 10 (tidak dibatasi halaman)
### TC-GS-USER-507: Nilai kosong ditulis `-` di berkas ekspor
9. Buka berkas `Changelog-User.csv` yang terunduh
10. Verifikasi berkas memuat baris Create `Alfa {runId}-083`
11. Verifikasi sel Old Value pada baris Create `Alfa {runId}-083` ditulis `-`
### TC-GS-USER-504: Download XLSX
12. Klik icon Download di modal, klik `Download as XLSX`
13. Verifikasi berkas `Changelog-User.xlsx` terunduh
### TC-GS-USER-505: Download mengikuti Search aktif
14. Klik icon Search, ketik `Alfa {runId}-083`, tekan Enter
15. Verifikasi tabel memuat baris Create dan Edit `Alfa {runId}-083`
16. Klik icon Download di modal, klik `Download as CSV`
17. Verifikasi berkas `Changelog-User.csv` terunduh
18. Verifikasi berkas hanya berisi baris hasil Search (tepat dua baris data: Create dan Edit `Alfa {runId}-083`)
### TC-GS-USER-506: Download mengecualikan kolom hidden lalu menyertakannya setelah unhide
19. Klik icon `(✕)`, tekan Enter pada input kosong
20. Klik header Column Visibility (⋯), hilangkan centang `Modified By` pada overlay
21. Tutup overlay Column Visibility
22. Klik icon Download di modal, klik `Download as CSV`
23. Verifikasi tidak ada toast peringatan
24. Verifikasi berkas pertama memuat kolom `Date`, `Action`, `User Name`, `Field`, `Old Value`, dan `New Value`
25. Verifikasi berkas pertama tidak memuat kolom `Modified By`
26. Klik header Column Visibility (⋯), centang kembali `Modified By` pada overlay
27. Tutup overlay Column Visibility
28. Klik icon Download di modal, klik `Download as CSV`
29. Verifikasi berkas kedua memuat kolom `Modified By`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-503, 507, 504, 505, 506. Alasan: TC-GS-USER-507 diverifikasi pada berkas CSV yang sama dengan TC-GS-USER-503 (langkah "Download CSV" identik), sehingga tidak ada unduhan CSV kedua; TC-GS-USER-506 terakhir karena menyembunyikan kolom (mengubah konfigurasi kolom) dan memulihkannya sendiri. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): `Klik icon (✕), tekan Enter pada input kosong` sebelum TC-GS-USER-506 (melepas Search TC-GS-USER-505), menutup overlay Column Visibility, dan membuka berkas hasil unduhan pada TC-GS-USER-507 (aksi TC "Buka file").
- Langkah tambahan atas TC (S-03): `Verifikasi` berkas memuat baris Create `Alfa` pada TC-GS-USER-507 adalah anchor positif untuk asersi sel `-`; `Verifikasi` berkas pertama memuat enam kolom lain pada TC-GS-USER-506 adalah pembanding untuk asersi ketiadaan kolom `Modified By`; `Verifikasi` jumlah baris lebih dari 10 pada TC-GS-USER-503 membuktikan berkas tidak dibatasi halaman.
- Urutan asersi absence toast (bagian 8b butir 11): `Verifikasi tidak ada toast sukses` (langkah 5) dan `Verifikasi tidak ada toast peringatan` (langkah 23) ditaruh segera setelah klik `Download as CSV` dan sebelum `Verifikasi` berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh.
- Isi berkas dipisah dari spec kegagalan ekspor (kelas binary buffer, prinsip 13f). Asersi berkas memakai pola baris bersuffix `{runId}-083`; satu-satunya asersi jumlah terhadap seluruh entri adalah langkah 7 (pembanding total entri Changelog Client yang dibaca tim FE/BE) dan jumlah dua baris hasil Search pada TC-GS-USER-505.
- Pembagian TC Modal Changelog User: screening dan Search ada di spec 078, Filter Panel ada di spec 079, kombinasi Search+Filter ada di spec 080, Sort dan Pagination ada di spec 081, Setup Column ada di spec 082.
- Temuan untuk QA: (1) TC-GS-USER-503 Expected b "semua baris" tidak menyebut cara mengetahui total entri; spec membandingkan jumlah baris data berkas dengan total entri Changelog yang dibaca tim FE/BE. (2) TC-GS-USER-504 hanya mengharapkan nama berkas; isi XLSX tidak diasersi. (3) TC-GS-USER-505 tidak menyebut keyword; spec memakai `Alfa {runId}-083`. (4) TC-GS-USER-506 tidak menyebut kolom yang di-hide; spec memakai `Modified By`. (5) TC-GS-USER-507 tidak menyebut kolom tempat sel kosong; spec memakai Old Value baris Create (UI menampilkan `—`, berkas menulis `-`, prd-conventions.md §9.9). (6) PRD prd-conventions.md §9.17 menyebut CSV berencoding UTF-8 dengan BOM dan XLSX satu sheet `Sheet1`; TC tidak memuatnya sehingga tidak diasersi.
