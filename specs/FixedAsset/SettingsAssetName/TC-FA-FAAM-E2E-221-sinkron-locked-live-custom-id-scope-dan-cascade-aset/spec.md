---
id: TC-FA-FAAM-E2E-221-sinkron-locked-live-custom-id-scope-dan-cascade-aset
title: "Sinkron Lintas Modul: Code ke Custom Asset ID, Rename ke Detail Aset, dan Delete Melepas Scope Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-600
  - TC-FA-FAAM-601
  - TC-FA-FAAM-603
coverage:
  web: automated
---

# Sinkron Lintas Modul: Code ke Custom Asset ID, Rename ke Detail Aset, dan Delete Melepas Scope Custom Field

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup: No. 10 (`Dell Latitude`, Code `DLAT`, Total Asset 42) dan No. 10p (konfigurasi Custom Asset ID client memakai segmen `[Asset Name Code]`). `Dell Latitude` tidak dapat digandakan dan menjadi target Edit Code TC-FA-FAAM-600 beserta registrasi satu aset baru. Hook `before` dan hook `after` menyediakannya ulang ke Code `DLAT` dan menghapus aset baru lewat seed API (kemampuan disediakan tim BE/FE); antar blok dipulihkan oleh langkah 14. Efek: Last Updated `Dell Latitude` dan audit trail Changelog berubah; suite berjalan serial. Pernyataan ini belum ada di `suite.md` (lihat Temuan untuk QA).
- Data Dinamis, di-seed lewat API di hook `before`:
  - `Warehouse Pallet 603 {runId}-221` (Code `PLT-WH603`; Tabel Data Uji Dinamis No. 63): salinan fixture 13 dengan satu aset terdaftar (Total Asset 1); diubah nama menjadi `Warehouse Pallet 603 {runId}-221 Baru` oleh TC-FA-FAAM-603.
  - `Scope Only Item 601 {runId}-221` (Total Asset 0; Tabel Dinamis No. 80) satu-satunya anggota scope custom field `Scope Only Field 601 {runId}-221` (Text, General, status Active; fixture No. 27c).
- Kemampuan teknis: pembukaan Fixed Asset > Assets (tabel aset dan detail aset), Registrasi Aset, Settings > Custom Fields, dan FAMS > Settings > Asset Transactional Policy; seed API per TC.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini lewat API dan pulihkan `Dell Latitude`.
- State global yang diubah: Code `Dell Latitude` (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-600, 601, 603: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-600: Perubahan Code dipakai segmen Asset Name Code di Custom Asset ID

1. Buka Fixed Asset > Assets lalu catat nomor aset yang sudah terbit untuk Asset Name `Dell Latitude`
2. Buka Fixed Asset > Settings > Asset Master > Asset Name
3. Ketik Search `Dell Latitude`, tekan Enter
4. Klik `⋯` baris `Dell Latitude` lalu `Edit`
5. Ubah Code `Dell Latitude` dari `DLAT` menjadi `DLX`
6. Klik `[Save]`
7. Buka Registrasi Aset
8. Registrasikan aset baru dari Asset Name `Dell Latitude` (field wajib lain sesuai form)
9. Verifikasi nomor aset yang digenerate memakai `DLX`
10. Buka Fixed Asset > Assets
11. Verifikasi nomor aset yang sudah terbit (langkah 1) tidak berubah
12. Sediakan ulang `Dell Latitude` ke Code `DLAT` dan hapus aset baru lewat seed API
13. Buka Fixed Asset > Settings > Asset Master > Asset Name

### TC-FA-FAAM-603: Perubahan Asset Name terlihat di detail dan tabel aset dan kolom Asset Name Asset Transactional Policy

14. Ketik Search `Warehouse Pallet 603 {runId}-221`, tekan Enter
15. Klik `⋯` baris `Warehouse Pallet 603 {runId}-221` lalu `Edit`
16. Ubah Asset Name menjadi `Warehouse Pallet 603 {runId}-221 Baru`
17. Klik `[Save]`
18. Buka detail aset yang merujuk `Warehouse Pallet 603 {runId}-221 Baru` dan tabel aset di `asset/`
19. Verifikasi detail aset menampilkan `Warehouse Pallet 603 {runId}-221 Baru`
20. Verifikasi tabel aset di `asset/` menampilkan `Warehouse Pallet 603 {runId}-221 Baru`
21. Buka kolom Asset Name di settings-asset-transactional-policy
22. Ketik Search `Warehouse Pallet 603 {runId}-221 Baru`, tekan Enter
23. Verifikasi kolom Asset Name di settings-asset-transactional-policy menampilkan `Warehouse Pallet 603 {runId}-221 Baru`

### TC-FA-FAAM-601: Delete Asset Name melepas scope custom field di modul Custom Fields

24. Buka custom field `Scope Only Field 601 {runId}-221` dan catat Scope serta status field
25. Buka Fixed Asset > Settings > Asset Master > Asset Name
26. Ketik Search `Scope Only Item 601 {runId}-221`, tekan Enter
27. Klik `⋯` baris `Scope Only Item 601 {runId}-221` lalu `Delete`
28. Klik `[Delete]`
29. Tunggu aksi selesai
30. Buka custom field `Scope Only Field 601 {runId}-221`
31. Verifikasi Scope `Scope Only Field 601 {runId}-221` kosong (kolom Scope tampil `—`)
32. Verifikasi status field tidak berubah (sama dengan catatan langkah 24)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 dan 24 (mencatat data baseline), langkah 2, 10, 13, 25 (navigasi), langkah 3, 14, 22, 26 (Search untuk menemukan baris target), langkah 12 (pemulihan `Dell Latitude`), dan langkah 29 (menunggu penghapusan selesai sebelum pindah surface).
- Urutan TC: TC-FA-FAAM-600, TC-FA-FAAM-603, TC-FA-FAAM-601 (aksi menghapus data di akhir; S-10).
- Pembagian TC lintas spec: TC-FA-FAAM-597 ada di spec 241; TC-FA-FAAM-602 dan 609 ada di spec 242.
- Temuan untuk QA:
  - TC-FA-FAAM-600 menyebut registrasi aset tanpa daftar field wajib; spec menulis "field wajib lain sesuai form" (kebutuhan teknis dipenuhi tim FE).
  - TC-FA-FAAM-600 mengubah `Dell Latitude` (Pre-setup No. 10) dan mendaftarkan aset sehingga Total Asset menjadi 43 sampai dipulihkan; S-06 mensyaratkan fixture pemulihan dinyatakan di `suite.md` (belum ada).
  - TC-FA-FAAM-603 mencantumkan `Dell Latitude` Total Asset 42 pada precondition tetapi langkahnya tidak memakainya; spec tidak memakai data itu.
  - TC-FA-FAAM-601 butir "status field tidak berubah" tidak menyebut nilai status; spec membandingkan dengan status yang dicatat sebelum Delete.
