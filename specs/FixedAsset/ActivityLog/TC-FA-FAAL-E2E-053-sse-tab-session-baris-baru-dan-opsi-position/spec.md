---
id: TC-FA-FAAL-E2E-053-sse-tab-session-baris-baru-dan-opsi-position
title: "SSE Tab Session: Sesi Baru, Filter Aktif, dan Opsi Position Real-Time"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-79
  - TC-FA-FAAL-265
  - TC-FA-FAAL-282
  - TC-FA-FAAL-283
coverage:
  web: automated
---

# SSE Tab Session: Sesi Baru, Filter Aktif, dan Opsi Position Real-Time

## Prerequisites

- Mode: FE+BE (backend nyata; pembaruan real-time lewat SSE tanpa intercept).
- Akun aktor observer sesi A: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka).
- Pemicu sesi baru (konteks browser B): user lain yang login dan membuka produk Fixed Asset sehingga tercatat baris `Session started`. Konteks B dibuka per blok TC, bukan konteks yang diasersi, dan ditutup di akhir blok dengan menghapus sesi login browser terkait (S-09). Pemicu memakai browser nyata karena baris Tab Session hanya tercatat dari sesi web; sesi API aktor tidak dihitung sebagai sesi web (`suite.md`).
- User pemicu: John Doe (Division `Marketing`, TC-FA-FAAL-265 dan 282), Siti Nurbaya (Division `Finance`, TC-FA-FAAL-283), keduanya dengan App Access Fixed Asset dan seat subscription tersedia (Pre-setup #16); user dengan Position `Director` yang belum pernah membuka FAMS (TC-FA-FAAL-79). Email dan password ketiga user tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup: Data Log Tab Session SS-01 sampai SS-11 (#11). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Uji dari TC sumber: Filter Division `Finance`; Position baru `Director`.
- Total entri (Z): dibaca dari teks `Showing X–Y of Z entries` sesi A sebelum aksi pemicu. Log bersifat permanen dan spec lain menambah baris, sehingga asersi memakai selisih terhadap Z yang dicatat, bukan angka absolut (S-12, bagian 8b butir 10).
- State yang diubah dan pemulihannya: baris Tab Session hasil sesi baru bersifat permanen dan tidak dihapus; opsi Position `Director` tetap ada sesudah dicatat. User dengan Position `Director` yang belum pernah membuka FAMS disediakan tim FE/BE untuk setiap run (kemampuan seed). Hook `after` menutup konteks B bila masih terbuka.
- Jendela asersi absence SSE: lima detik tanpa memuat ulang halaman, pilihan spec ini (bagian 6).
- Suite berjalan serial (`parallel: false`).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### TC-FA-FAAL-79: Opsi Position bertambah real-time

1. Di sesi A buka Filter Panel, lalu buka dropdown Position
2. Verifikasi opsi lain pada dropdown Position tampil (mis. `Manager`)
3. Verifikasi opsi `Director` tidak ada
4. Tutup dropdown Position
5. Di konteks B login sebagai user dengan Position `Director`, lalu buka produk Fixed Asset
6. Di sesi A buka kembali dropdown Position tanpa memuat ulang halaman
7. Verifikasi opsi `Director` muncul di dropdown Position tanpa muat ulang halaman
8. Tutup dropdown Position dan Filter Panel tanpa Apply
9. Tutup konteks B dan hapus sesi login browser terkait

### TC-FA-FAAL-265: Baris baru muncul otomatis tanpa reset scroll

10. Di sesi A catat Z dari teks `Showing X–Y of Z entries`
11. Di konteks B login sebagai John Doe, lalu buka produk Fixed Asset
12. Verifikasi baris `John D` dengan Note `Session started` muncul otomatis di baris paling atas tanpa muat ulang, dan Z bertambah satu dari nilai yang dicatat
13. Verifikasi tidak ada dialog maupun toast
14. Tutup konteks B dan hapus sesi login browser terkait

### TC-FA-FAAL-282: Sesi baru yang tidak cocok dengan Filter aktif diabaikan

15. Di sesi A terapkan Filter Division `Finance`
16. Catat teks `Showing 1–Y0 of Z0 entries` hasil filter sebagai baseline
17. Verifikasi hasil filter memuat baris SS-03, SS-05, SS-09, dan SS-11
18. Di konteks B login sebagai John Doe (Division `Marketing`), lalu buka produk Fixed Asset
19. Tunggu 5 detik tanpa memuat ulang halaman
20. Verifikasi sedikitnya satu baris Division `Finance` tetap tampil di sesi A
21. Verifikasi baris `John D` dengan Note `Session started` tidak disisipkan
22. Verifikasi teks pagination tetap `Showing 1–Y0 of Z0 entries`, sama dengan baseline langkah 16
23. Tutup konteks B dan hapus sesi login browser terkait

### TC-FA-FAAL-283: Sesi baru yang cocok dengan Filter aktif disisipkan

24. Di sesi A pastikan Filter Division `Finance` tetap aktif dan catat teks `Showing 1–Y0 of Z0 entries` sebagai baseline
25. Verifikasi teks pagination `Showing 1–Y0 of Z0 entries` sama dengan baseline TC-FA-FAAL-282
26. Di konteks B login sebagai Siti Nurbaya (Division `Finance`), lalu buka produk Fixed Asset
27. Verifikasi baris `Siti N` dengan Note `Session started` disisipkan in-place di baris pertama tanpa muat ulang
28. Verifikasi tidak ada dialog maupun toast
29. Verifikasi teks pagination menjadi `Showing 1–Y1 of Z1 entries` dengan Z1 = Z0 + 1 dan Y1 = Y0 + 1
30. Tutup konteks B dan hapus sesi login browser terkait
31. Bersihkan Filter lewat Clear Field

## Notes

- Mode: FE+BE, kelas c (multi-konteks): sesi A mengamati pembaruan SSE akibat sesi web user lain. Konteks B hanya pemicu state tanpa asersi (login dan buka produk), bukan konteks kedua yang diasersi.
- Asersi tambahan atas TC (S-03): selisih Z (+1) pada langkah 12, 29 dan baseline langkah 16, 22, 24 adalah baseline S-12 agar baris dari run sebelumnya tidak dianggap baris baru. Langkah 17 dan 20 menjadi anchor positif baris pembanding sebelum asersi absence langkah 21.
- Urutan TC dalam spec berbeda dari nomor TC sumber (S-10): TC-FA-FAAL-79 di awal dan TC-FA-FAAL-283 sesudah TC-FA-FAAL-282 agar Filter Division `Finance` tetap aktif dan tidak diterapkan ulang.
- Urutan asersi absence (langkah 19 sampai 22): jendela lima detik ditulis sebagai langkah penghubung tanpa `Verifikasi` (bagian 6).
- Langkah penghubung (S-03, S-09): langkah 4 dan 8 (menutup dropdown dan panel), 9, 14, 23, 30 (menutup konteks B dan menghapus sesi login browser terkait), 31 (membersihkan Filter).
- Temuan untuk QA:
  - TC-FA-FAAL-79 butir d, TC-FA-FAAL-265, 282, dan 283 menyebut user pemicu (`Director`, John Doe, Siti Nurbaya) tanpa email dan password di tabel Pre-setup; akun disediakan tim FE. User `Director` harus belum pernah membuka FAMS sehingga hanya berlaku sekali per user; tim FE/BE perlu user baru atau pemulihan setiap run.
  - TC-FA-FAAL-79 Expected butir a tidak menyebut opsi pembanding; spec memakai opsi lain (`Manager`, Position seed SS-03) sebagai anchor positif dropdown (langkah 2).
  - TC-FA-FAAL-265 tidak menyebut user pemicu; spec memakai John Doe sesuai Expected (`John D`).
