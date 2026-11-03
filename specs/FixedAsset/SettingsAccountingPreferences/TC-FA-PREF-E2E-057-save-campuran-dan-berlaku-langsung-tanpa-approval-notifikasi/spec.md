---
id: TC-FA-PREF-E2E-057-save-campuran-dan-berlaku-langsung-tanpa-approval-notifikasi
title: "Save Campuran Setting Berdampak dan Tidak Berdampak; Save Berlaku Langsung Tanpa Approval dan Notifikasi"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-583
  - TC-FA-PREF-593
coverage:
  web: automated
---

# Save Campuran Setting Berdampak dan Tidak Berdampak; Save Berlaku Langsung Tanpa Approval dan Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PC-1 (Preferences nilai awal, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Journal Grouping Group; bulan berjalan Oktober 2026), PC-6 (Asset Class IT Equipment threshold sendiri 2.000.000; Vehicles dan Furniture tanpa threshold sendiri), PC-5 (akun Chart of Accounts) dan PC-8 (akun pengguna).
- Akun kedua untuk TC-593: Manage accounting - Read + Update (Budi Santoso): `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MARU_PASSWORD` (env var belum terdaftar; didaftarkan tim FE). Kesamaan akun ini dengan Budi Santoso dan kesamaan akun Total Control suite dengan Rina Anggraini perlu dikonfirmasi tim FE (email keduanya tidak tertulis di Pre-setup TC).
- Jumlah notifikasi in-app awal Rina Anggraini (Total Control, tampil "Rina A") dan Budi Santoso (Manage accounting - Read + Update, tampil "Budi S") dibaca lewat kemampuan baca BE sebelum aksi (disediakan tim FE/BE).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-583: Save campuran setting berdampak dan tidak berdampak

1. Ubah Default Capitalization Threshold menjadi "10000000"
2. Pilih "Manual by Accounting" pada Select In-service Date Source
3. Tambahkan opsi "Category" pada Journal Grouping
4. Klik [Save changes]
5. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
6. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default threshold."
7. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
8. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
9. Verifikasi In-service Date Source dan Journal Grouping tidak memiliki baris dampak pada dialog
10. Klik [Save] pada dialog D-01
11. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
12. Muat ulang tab Preferences dengan F5
13. Verifikasi Default Capitalization Threshold menampilkan Rp 10.000.000,00
14. Verifikasi Select In-service Date Source menampilkan Manual by Accounting
15. Verifikasi Journal Grouping menampilkan Group, Category
16. Pulihkan Preferences ke PC-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-593: Save Preferences berlaku langsung tanpa approval dan tanpa notifikasi

17. Catat jumlah notifikasi in-app milik Rina Anggraini dan Budi Santoso (kemampuan baca BE)
18. Ubah Default Capitalization Threshold menjadi "10000000"
19. Klik [Save changes]
20. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
21. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default threshold."
22. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
23. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
24. Klik [Save] pada dialog D-01
25. Verifikasi toast "Success, accounting preferences have been saved." tampil tanpa langkah approval maupun status menunggu persetujuan
26. Buka Settings > Accounting > Asset Class
27. Verifikasi kolom Capitalization Threshold kelas Vehicles pada tabel Asset Class menampilkan "Default"
28. Buka Edit kelas Vehicles (halaman Detail Asset Class) dan pilih tab Depreciation
29. Verifikasi field Capitalization Threshold pada bagian Capitalization kosong (tidak ada salinan 10.000.000 tersimpan pada kelas)
30. Buka daftar notifikasi in-app milik Rina Anggraini
31. Verifikasi jumlah notifikasi in-app milik Rina Anggraini sama dengan jumlah awal
32. Logout dari akun Total Control
33. Login sebagai Manage accounting - Read + Update (`manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MARU_PASSWORD`)
34. Buka daftar notifikasi in-app milik Budi Santoso
35. Verifikasi jumlah notifikasi in-app milik Budi Santoso sama dengan jumlah awal
36. Pulihkan Preferences ke PC-1 lewat seed API

## Notes

- Langkah penghubung (S-03): pemulihan Preferences lewat seed API, catat baseline notifikasi, pindah ke Asset Class, ganti akun dengan logout dan login eksplisit.
- Spec berakhir di akun Manage accounting - Read + Update; hook `after` mengembalikan sesi ke akun default suite (S-07). Spec ini di atas 35 langkah (36) dengan alasan: TC-593 harus memeriksa notifikasi dua akun berbeda sesudah satu Save (baseline, ganti akun, dua pembacaan) dan tidak dapat dipisah tanpa mengulang Save dan seed; TC-583 berdiri sendiri di blok pertama.
- Asersi tidak adanya approval dan notifikasi bukan asersi absence log (kelas g): diasersi lewat toast sukses sebagai anchor, status approval tidak tampil, dan jumlah notifikasi sama dengan baseline.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-593 Precondition d menyebut jumlah notifikasi awal "telah dicatat penguji" tanpa cara mencatat dan tanpa menyebut cara membuka notifikasi akun Budi Santoso; spec menambah langkah Catat dan ganti akun eksplisit. Email Rina Anggraini dan Budi Santoso tidak tertulis di Pre-setup (PC-8).
  - TC-583 Precondition tidak menyatakan Chart of Accounts; tidak dibutuhkan langkahnya.
