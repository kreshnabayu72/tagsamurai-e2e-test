---
id: TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi
title: "Popup Edit Group: Nama Reserved, Emoji, Auto-Trim Name/Code, dan Name Diganti Spasi Saja"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-196
  - TC-FA-GRP-197
  - TC-FA-GRP-198
  - TC-FA-GRP-199
  - TC-FA-GRP-1057
coverage:
  web: automated
---

# Popup Edit Group: Nama Reserved, Emoji, Auto-Trim Name/Code, dan Name Diganti Spasi Saja

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-196 dan TC-FA-GRP-198 ditolak server, TC-FA-GRP-199 menyimpan perubahan).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-062` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `Edit Target {runId}-062` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target"). TC-FA-GRP-1057: Group Name diganti tiga spasi. TC-FA-GRP-196: `  all groups  ` (dua spasi di depan dan belakang). TC-FA-GRP-197: `Gudang 🚀 Utama`. TC-FA-GRP-198: `Gudang 🚀`. TC-FA-GRP-199: Name `  Trim Hall {runId}-062  ` dan Code `  TH1  `; hasil `Trim Hall {runId}-062` dan `TH1` (Code `TH1` literal).
- Kemampuan teknis: pembacaan nilai Group Name node target lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); pengetikan dan paste emoji; injeksi nilai langsung ke DOM field Group Name tanpa filter keystroke (TC-FA-GRP-198, disediakan tim FE).
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-062` dan group ber-Code literal `ET` dan `TH1` (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-062`, tekan Enter

### TC-FA-GRP-1057: Group Name diganti spasi saja ditolak sebagai kosong

2. Buka elipsis (⋯) baris `Edit Target {runId}-062`, lalu klik Edit
3. Ganti Group Name dengan tiga spasi saja, lalu klik [Save]
4. Verifikasi inline error `Group name must not be empty` di bawah Group Name
5. Verifikasi popup tetap terbuka
6. Verifikasi Group Name tersimpan tetap `Edit Target {runId}-062` (dibaca lewat fixture BE)

### TC-FA-GRP-196: Nama reserved All Groups ditolak (case dan trim)

7. Ganti isi Group Name dengan `  all groups  `, lalu klik [Save]
8. Verifikasi inline error `'All Groups' is a reserved name and cannot be used` setelah submit
9. Verifikasi data tidak tersimpan: Group Name node target lewat fixture BE tetap `Edit Target {runId}-062`

### TC-FA-GRP-197: Emoji diblok saat ketik/paste di Group Name

10. Kosongkan Group Name, lalu ketik dan paste `Gudang 🚀 Utama` ke Group Name
11. Verifikasi emoji tidak masuk ke value field dan karakter lain tetap (`Gudang` dan `Utama` tampil)
12. Verifikasi tidak ada pesan error pada Group Name

### TC-FA-GRP-198: Emoji yang lolos blok input ditolak server

13. Injeksi value `Gudang 🚀` langsung ke DOM field Group Name (bypass filter keystroke FE), lalu klik [Save]
14. Verifikasi inline error `Group name contains invalid characters` dari server
15. Verifikasi popup tetap terbuka
16. Verifikasi data tidak tersimpan: Group Name node target lewat fixture BE tetap `Edit Target {runId}-062`

### TC-FA-GRP-199: Auto-trim spasi depan/belakang Group Name dan Code

17. Ganti isi Group Name dengan `  Trim Hall {runId}-062  `, isi Code `  TH1  `, lalu klik [Save]
18. Verifikasi toast sukses `Success, group has been updated.`
19. Ketik Search `Trim Hall {runId}-062`, tekan Enter
20. Verifikasi di tabel, Group Name `Trim Hall {runId}-062` dan Code `TH1` tersimpan tanpa spasi di depan dan belakang
21. Verifikasi di sidebar, node `Trim Hall {runId}-062` tampil tanpa spasi di depan dan belakang
22. Klik nama `Trim Hall {runId}-062` untuk membuka Popup Detail Group
23. Verifikasi di Detail, Group Name `Trim Hall {runId}-062` dan Code `TH1` tanpa spasi di depan dan belakang
24. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-1057, 196, 197, 198), lalu aksi sukses (TC-FA-GRP-199) sesuai S-10; berbeda dari urutan nomor TC sumber. Dalam satu popup, isi Group Name diganti sehingga error TC sebelumnya hilang (R-12).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-062`, tekan Enter); langkah 19 (Ketik Search `Trim Hall {runId}-062`, tekan Enter); langkah 22 (Klik nama `Trim Hall {runId}-062` untuk membuka Popup Detail Group); langkah 24 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search).
- Langkah Search mencari baris target (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-199 Expected b menyebut hasil "di tabel, sidebar, Detail" tanpa langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-197 tidak menyebut apakah teks tetap `Gudang  Utama` (dua spasi) atau dipadatkan; spec hanya mengasersi bahwa emoji tidak masuk dan karakter lain tetap.
  - TC-FA-GRP-1057 Expected b "Group Name tersimpan tetap Edit Target" tidak menyebut cara membaca nilai tersimpan; spec memakai pembacaan lewat fixture BE.
  - Code `TH1` literal dipakai oleh TC-FA-GRP-93 (spec 035), TC-FA-GRP-141 (spec 048), dan TC-FA-GRP-199; suite berjalan serial dan tiap spec membersihkan Code itu di hook `before` dan `after`.

