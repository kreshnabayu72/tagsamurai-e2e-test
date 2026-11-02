---
id: TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi
title: "Popup New Subgroup: Nama Reserved All Groups, Emoji, Auto-Trim Name/Code, dan Name Hanya Spasi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-138
  - TC-FA-GRP-139
  - TC-FA-GRP-140
  - TC-FA-GRP-141
  - TC-FA-GRP-1056
coverage:
  web: automated
---

# Popup New Subgroup: Nama Reserved All Groups, Emoji, Auto-Trim Name/Code, dan Name Hanya Spasi

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-138 dan TC-FA-GRP-140 ditolak server, TC-FA-GRP-141 menyimpan subgroup).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-048` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-1056: Group Name tiga spasi. TC-FA-GRP-138: `  all groups  ` (dua spasi di depan dan belakang). TC-FA-GRP-139: `Gudang 🚀 Utama`. TC-FA-GRP-140: `Gudang 🚀`. TC-FA-GRP-141: Name `  Trim Hall {runId}-048  ` dan Code `  TH1  `; hasil `Trim Hall {runId}-048` dan `TH1` (Code `TH1` literal).
- Kemampuan teknis: pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); pengetikan dan paste emoji; injeksi nilai langsung ke DOM field Group Name tanpa filter keystroke (TC-FA-GRP-140, disediakan tim FE).
- Pemulihan (hook `before` dan `after`): hapus lewat API seluruh group dengan suffix `{runId}-048` dan group ber-Code literal `TH1` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-1056: Group Name hanya spasi ditolak sebagai kosong

1. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
2. Isi Group Name dengan tiga spasi saja, lalu klik [Submit]
3. Verifikasi inline error `Group name must not be empty` di bawah Group Name
4. Verifikasi popup tetap terbuka
5. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-138: Nama reserved All Groups ditolak (case dan trim)

6. Ganti isi Group Name dengan `  all groups  `, lalu klik [Submit]
7. Verifikasi inline error `'All Groups' is a reserved name and cannot be used` setelah submit
8. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-139: Emoji diblok saat ketik/paste di Group Name

9. Kosongkan Group Name, lalu ketik dan paste `Gudang 🚀 Utama` ke Group Name
10. Verifikasi emoji tidak masuk ke value field dan karakter lain tetap (`Gudang` dan `Utama` tampil)
11. Verifikasi tidak ada pesan error pada Group Name

### TC-FA-GRP-140: Emoji yang lolos blok input ditolak server

12. Injeksi value `Gudang 🚀` langsung ke DOM field Group Name (bypass filter keystroke FE), lalu klik [Submit]
13. Verifikasi inline error `Group name contains invalid characters` dari server
14. Verifikasi popup tetap terbuka
15. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-141: Auto-trim spasi depan/belakang Group Name dan Code

16. Ganti isi Group Name dengan `  Trim Hall {runId}-048  `, isi Code `  TH1  `, lalu klik [Submit]
17. Verifikasi toast sukses `Success, group has been created.`
18. Klik Head Office di sidebar, lalu ketik Search `Trim Hall {runId}-048`, tekan Enter
19. Verifikasi di tabel, Group Name `Trim Hall {runId}-048` dan Code `TH1` tersimpan tanpa spasi di depan dan belakang
20. Verifikasi di sidebar, node `Trim Hall {runId}-048` tampil tanpa spasi di depan dan belakang
21. Klik nama `Trim Hall {runId}-048` untuk membuka Popup Detail Group
22. Verifikasi di Detail, Group Name `Trim Hall {runId}-048` dan Code `TH1` tanpa spasi di depan dan belakang
23. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-1056, 138, 139, 140), lalu aksi sukses (TC-FA-GRP-141) sesuai S-10; berbeda dari urutan nomor TC sumber. Dalam satu popup, isi Group Name diganti sehingga error TC sebelumnya hilang (R-12).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 18 (Klik Head Office di sidebar, lalu ketik Search `Trim Hall {runId}-048`...); langkah 21 (Klik nama `Trim Hall {runId}-048` untuk membuka Popup Detail Group); langkah 23 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search).
- Langkah 18 mencari baris target yang baru dibuat (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-141 Expected b menyebut hasil "di tabel, sidebar, Detail" tanpa langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-139 tidak menyebut apakah teks tetap `Gudang  Utama` (dua spasi) atau dipadatkan; spec hanya mengasersi bahwa emoji tidak masuk dan karakter lain tetap.
  - Code `TH1` literal dipakai oleh TC-FA-GRP-93 (spec 035), TC-FA-GRP-141, dan TC-FA-GRP-199 (spec 062); suite berjalan serial dan tiap spec membersihkan Code itu di hook `before` dan `after`.

