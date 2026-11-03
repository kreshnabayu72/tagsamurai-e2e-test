---
id: TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi
title: "Popup New Group: Nama Reserved All Groups, Emoji Diblok dan Ditolak Server, Auto-Trim Name/Code/Description, dan Name Hanya Spasi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-90
  - TC-FA-GRP-91
  - TC-FA-GRP-92
  - TC-FA-GRP-93
  - TC-FA-GRP-949
  - TC-FA-GRP-1055
coverage:
  web: automated
---

# Popup New Group: Nama Reserved All Groups, Emoji Diblok dan Ditolak Server, Auto-Trim Name/Code/Description, dan Name Hanya Spasi

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-90 dan TC-FA-GRP-92 ditolak server, TC-FA-GRP-93 dan TC-FA-GRP-949 menyimpan group).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client Plan Professional dengan jumlah group di bawah cap; Head Office punya child Floor 2.
- Data Dinamis bersuffix `{runId}-035` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script):
  - TC-FA-GRP-1055: Group Name tiga spasi. TC-FA-GRP-90: `  all groups  ` (dua spasi di depan dan belakang). TC-FA-GRP-91: `Gudang 🚀 Utama`. TC-FA-GRP-92: `Gudang 🚀`.
  - TC-FA-GRP-93: Name `  Trim Hall {runId}-035  ` dan Code `  TH1  ` (dua spasi di depan dan belakang); hasil `Trim Hall {runId}-035` dan `TH1`. Code `TH1` literal.
  - TC-FA-GRP-949: Name `Trim Test {runId}-035`, Description `  Lantai dua  `; langkah 5: Name `Trim Test 360 {runId}-035`, Description = 2 spasi + 360 karakter `a` + 2 spasi (364 karakter mentah).
- Kemampuan teknis: pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); pengetikan dan paste emoji; injeksi nilai langsung ke DOM field Group Name tanpa filter keystroke (TC-FA-GRP-92, disediakan tim FE).
- Pemulihan (hook `before` dan `after`): hapus lewat API seluruh group dengan suffix `{runId}-035` dan group ber-Code literal `TH1` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-1055: Group Name hanya spasi ditolak sebagai kosong

1. Klik [+] Group di sidebar
2. Isi Group Name dengan tiga spasi saja, lalu klik [Submit]
3. Verifikasi inline error `Group name must not be empty` di bawah Group Name
4. Verifikasi popup tetap terbuka
5. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-90: Nama reserved All Groups ditolak (case dan trim)

6. Ganti isi Group Name dengan `  all groups  `, lalu klik [Submit]
7. Verifikasi inline error `'All Groups' is a reserved name and cannot be used` setelah submit
8. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-91: Emoji diblok saat ketik/paste di Group Name

9. Kosongkan Group Name, lalu ketik dan paste `Gudang 🚀 Utama` ke Group Name
10. Verifikasi emoji tidak masuk ke value field dan karakter lain tetap (`Gudang` dan `Utama` tampil)
11. Verifikasi tidak ada pesan error pada Group Name

### TC-FA-GRP-92: Emoji yang lolos blok input ditolak server

12. Injeksi value `Gudang 🚀` langsung ke DOM field Group Name (bypass filter keystroke FE), lalu klik [Submit]
13. Verifikasi inline error `Group name contains invalid characters` dari server
14. Verifikasi popup tetap terbuka
15. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-93: Auto-trim spasi depan/belakang Group Name dan Code

16. Ganti isi Group Name dengan `  Trim Hall {runId}-035  `, isi Code `  TH1  `, lalu klik [Submit]
17. Verifikasi toast sukses `Success, group has been created.`
18. Ketik Search `Trim Hall {runId}-035`, tekan Enter
19. Verifikasi di tabel, Group Name `Trim Hall {runId}-035` dan Code `TH1` tersimpan tanpa spasi di depan dan belakang
20. Verifikasi di sidebar, node `Trim Hall {runId}-035` tampil tanpa spasi di depan dan belakang
21. Klik nama `Trim Hall {runId}-035` untuk membuka Popup Detail Group
22. Verifikasi di Detail, Group Name `Trim Hall {runId}-035` dan Code `TH1` tanpa spasi di depan dan belakang
23. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

### TC-FA-GRP-949: Auto-trim spasi depan/belakang Description

24. Klik [+] Group di sidebar
25. Isi Group Name `Trim Test {runId}-035` dan Description `  Lantai dua  `, lalu klik [Submit]
26. Verifikasi toast sukses `Success, group has been created.`
27. Ketik Search `Trim Test {runId}-035`, tekan Enter, lalu klik nama group untuk membuka Popup Detail Group
28. Verifikasi Description tersimpan dan tampil `Lantai dua` tanpa spasi di depan dan belakang
29. Tutup Popup Detail Group dan klik `(←)` pada kotak Search
30. Klik [+] Group di sidebar
31. Isi Group Name `Trim Test 360 {runId}-035` dan Description 2 spasi + 360 karakter `a` + 2 spasi (364 karakter mentah), lalu klik [Submit]
32. Verifikasi toast sukses `Success, group has been created.`
33. Verifikasi tidak ada error `Max. 360 characters` pada Description
34. Ketik Search `Trim Test 360 {runId}-035`, tekan Enter, lalu klik nama group untuk membuka Popup Detail Group
35. Verifikasi Description tersimpan 360 karakter `a` tanpa spasi di depan dan belakang
36. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-1055, 90, 91, 92), lalu aksi sukses (TC-FA-GRP-93, 949) sesuai S-10; berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 18 (Ketik Search `Trim Hall {runId}-035`, tekan Enter); langkah 21 (Klik nama `Trim Hall {runId}-035` untuk membuka Popup Detail Group); langkah 23 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search); langkah 27 (Ketik Search `Trim Test {runId}-035`, tekan Enter, lalu klik nama grou...); langkah 29 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search); langkah 30 dan 31 (membuat group Trim Test 360); langkah 34 (Ketik Search `Trim Test 360 {runId}-035`, tekan Enter, lalu klik nama group untuk membuka Popup Detail Group); langkah 36 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search).
- Langkah 18 dan langkah Search TC-FA-GRP-949 mencari baris target yang baru dibuat (R-16).
- Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (validasi dan auto-trim Popup New Group) dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah pertama TC-FA-GRP-90 dan seterusnya mengganti isi Group Name sehingga error TC sebelumnya hilang (R-12).
- Temuan untuk QA:
  - TC-FA-GRP-93 Expected b menyebut hasil "di tabel, sidebar, Detail" tanpa langkah membuka Detail; spec menambahkan langkah membuka Detail sebagai langkah penghubung.
  - TC-FA-GRP-91 tidak menyebut apakah teks tetap `Gudang  Utama` (dua spasi) atau dipadatkan; spec hanya mengasersi bahwa emoji tidak masuk dan karakter lain tetap.
  - Name TC-FA-GRP-93 dan TC-FA-GRP-949 memakai suffix `{runId}-035`; Code `TH1` literal sehingga dapat bentrok dengan data lain bila ada (dibersihkan di hook `before`).

