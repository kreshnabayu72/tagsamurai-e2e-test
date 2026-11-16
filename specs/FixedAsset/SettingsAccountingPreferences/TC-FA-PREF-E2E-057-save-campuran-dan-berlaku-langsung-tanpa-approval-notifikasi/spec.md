---
id: TC-FA-PREF-E2E-057-save-campuran-dan-berlaku-langsung-tanpa-approval-notifikasi
title: "Save Campuran Setting Berdampak dan Tidak Berdampak; Save Berlaku Langsung Tanpa Approval dan Notifikasi"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-583
  - TC-FA-PREF-593
sourceRules: ["D-01", "PV-01", "FAPREF-LOGIC-10k", "T-01", "F-FAPREF-01.k11", "F-FAPREF-01.k13", "FAPREF-LOGIC-09c", "FAPREF-LOGIC-10d"]
smoke: []
dependsOn: []
trace:
  "D-01": [5, 7, 8, 20, 22, 23]
  "PV-01": [6, 21]
  "FAPREF-LOGIC-10k": 9
  "T-01": [11, 25]
  "F-FAPREF-01.k11": 13
  "F-FAPREF-01.k13": 14
  "FAPREF-LOGIC-09c": 15
  "FAPREF-LOGIC-10d": [26, 27]
anchor: [29, 31, 33, 34]
coverage:
  web: automated
---

# Save Campuran Setting Berdampak dan Tidak Berdampak; Save Berlaku Langsung Tanpa Approval dan Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PC-1 (Preferences nilai awal, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Journal Grouping Group; bulan berjalan Oktober 2026), PC-6 (Asset Class IT Equipment threshold sendiri 2.000.000; Vehicles dan Furniture tanpa threshold sendiri) dan PC-8 (akun pengguna).
- Akun kedua untuk TC-593: Manage accounting - Read + Update (Budi Santoso, tampil "Budi S"): hanya jumlah notifikasinya yang dibaca, lewat kemampuan baca BE tanpa login sebagai Budi Santoso. Kesamaan akun ini dengan Budi Santoso dan kesamaan akun Total Control suite dengan Rina Anggraini perlu dikonfirmasi tim FE (email keduanya tidak tertulis di Pre-setup TC).
- Jumlah notifikasi in-app awal Rina Anggraini (Total Control, tampil "Rina A") dan Budi Santoso (Manage accounting - Read + Update, tampil "Budi S") dibaca lewat kemampuan baca BE sebelum aksi dan sesudahnya, sehingga baseline dan hasil dibaca dari sumber yang sama (8b butir 10; disediakan tim FE/BE).
- Jendela amat notifikasi in-app: Tunggu 5 detik tanpa memuat ulang halaman sebelum membaca jumlah notifikasi sesudah Save (pilihan spec, bukan nilai TC/PRD); toast sukses langkah 25 menjadi anchor.
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
8. Verifikasi footer dialog memuat tombol [Cancel] dan [Save]
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
23. Verifikasi footer dialog memuat tombol [Cancel] dan [Save]
24. Klik [Save] pada dialog D-01
25. Verifikasi toast "Success, accounting preferences have been saved." tampil
26. Verifikasi Save langsung berlaku tanpa langkah approval
27. Verifikasi tidak ada status menunggu persetujuan
28. Buka Settings > Accounting > Asset Class
29. Verifikasi kolom Capitalization Threshold kelas Vehicles pada tabel Asset Class menampilkan "Default"
30. Buka Edit kelas Vehicles (halaman Detail Asset Class) dan pilih tab Depreciation
31. Verifikasi field Capitalization Threshold pada bagian Capitalization kosong (tidak ada salinan 10.000.000 tersimpan pada kelas)
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi jumlah notifikasi in-app milik Rina Anggraini (kemampuan baca BE) sama dengan jumlah awal
34. Verifikasi jumlah notifikasi in-app milik Budi Santoso (kemampuan baca BE) sama dengan jumlah awal
35. Pulihkan Preferences ke PC-1 lewat seed API

## Notes

- Langkah penghubung (S-03): pemulihan Preferences lewat seed API, catat baseline notifikasi (langkah 17), pindah ke Asset Class, Tunggu 5 detik tanpa memuat ulang halaman (langkah 32, jendela amat notifikasi in-app).
- Sumber baca notifikasi (8b butir 10): TC-593 Precondition d tidak menetapkan cara mencatat baseline dan Langkah 5 membuka daftar notifikasi; spec membaca baseline dan hasil kedua akun lewat kemampuan baca BE (sumber sama, tanpa login ganti akun). Spec berakhir di sesi Total Control; hook `after` mengembalikan sesi ke akun default suite (S-07).
- Asersi tidak adanya approval dan notifikasi bukan asersi absence log (kelas g): diasersi lewat toast sukses sebagai anchor, status approval tidak tampil, dan jumlah notifikasi sama dengan baseline.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-593 Precondition d menyebut jumlah notifikasi awal "telah dicatat penguji" tanpa cara mencatat dan tanpa menyebut cara membuka notifikasi akun Budi Santoso; spec menambah langkah Catat baseline. Email Rina Anggraini dan Budi Santoso tidak tertulis di Pre-setup (PC-8).
  - TC-583 Precondition tidak menyatakan Chart of Accounts; tidak dibutuhkan langkahnya.
  - TC-593 Precondition d dan Langkah 5 tidak menetapkan sumber baca jumlah notifikasi (spec memakai kemampuan baca BE; lihat catatan sumber baca di atas). Mohon tim QA/TC menetapkan sumber baca dan penerima notifikasi.
