---
id: TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara
title: "Resolusi Group, Managed By, dan Badge Produk pada List Client untuk Distributor PT Distribusi Nusantara"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-36
  - TC-AC-ACC-15
  - TC-AC-ACC-927
  - TC-AC-ACC-569
  - TC-AC-ACC-570
  - TC-AC-ACC-572
  - TC-AC-ACC-559
coverage:
  web: automated
---

# Resolusi Group, Managed By, dan Badge Produk pada List Client untuk Distributor PT Distribusi Nusantara

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-13 | Distributor Total Control (PT Distribusi Nusantara) | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` |

- Login di hook `before` spec ini (Distributor Total Control, A-13); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen: `C-ROL-1` `PT Jalur Distributor Dulu` (Distributor-langsung PT Distribusi Nusantara ditetapkan 2026-01-05, Partner CV Mitra Sejati 2026-02-10), `C-ROL-2` `PT Jalur Partner Dulu` (Partner CV Mitra Sejati 2026-01-05, Distributor-langsung 2026-02-10), `C-ROL-13` `PT Direct Jakarta` (Direct, Group Client `Area Jakarta`), `C-W3LST-3` `PT Tiga Mitra Uji`, dan Pre-setup `C-10` `PT Lintas Jaringan` (SAMS dan SIEM plan owner CV Mitra Timur, di luar jaringan) hanya dibaca.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-36: Distributor: Group Client dengan Partner mengikuti Group Partner parent, relasi langsung ke Group Distributor sendiri

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Lihat kolom Group baris `PT Sejahtera Abadi`
3. Verifikasi Group `PT Sejahtera Abadi` adalah Group Partner CV Mitra Sejati `Cabang Menteng`
4. Ganti isi kotak Search dengan `PT Sinar Distributor`, tekan Enter
5. Lihat kolom Group baris `PT Sinar Distributor`
6. Verifikasi Group `PT Sinar Distributor` adalah Group Distributor sendiri `Area Jakarta`

### TC-AC-ACC-15: Sel produk menampilkan "—" bila plan owner produk di luar jaringan viewer

7. Ganti isi kotak Search dengan `PT Lintas Jaringan`, tekan Enter
8. Lihat baris `PT Lintas Jaringan` di sub-tab `Active`
9. Verifikasi sel FAMS `PT Lintas Jaringan` adalah badge `Active`
10. Verifikasi sel SAMS dan SIEM `PT Lintas Jaringan` berupa teks `—` (bukan `No Subscription` dan bukan badge)

### TC-AC-ACC-927: Managed By per viewer: Distributor menghitung +N more dan daftar hover hanya dari manager dalam jaringannya

11. Ganti isi kotak Search dengan `PT Tiga Mitra Uji`, tekan Enter, lihat sel Managed By, lalu arahkan kursor ke sel Managed By tersebut
12. Verifikasi sel Managed By `PT Tiga Mitra Uji` adalah `CV Mitra Sejati` diikuti `+1 more`
13. Verifikasi hover menampilkan daftar manager berurutan: `CV Mitra Sejati` (Anchor), lalu `CV Mitra Lestari`
14. Verifikasi teks `CV Mitra Mandiri` tidak tampil di daftar hover
15. Ganti isi kotak Search dengan `PT Lintas Jaringan`, tekan Enter, lihat sel Managed By baris `PT Lintas Jaringan`, lalu arahkan kursor ke sel tersebut
16. Verifikasi sel Managed By `PT Lintas Jaringan` adalah `CV Mitra Sejati` tanpa teks `+N more`
17. Verifikasi hover tidak menampilkan daftar manager (hanya satu manager dalam jaringan viewer)

### TC-AC-ACC-569: Anchor lintas jenis relasi: relasi Distributor-langsung lebih awal dari Partner menjadi Anchor di view Distributor

18. Ganti isi kotak Search dengan `PT Jalur Distributor Dulu`, tekan Enter
19. Lihat sel Managed By dan Group baris `PT Jalur Distributor Dulu`
20. Verifikasi Managed By `PT Jalur Distributor Dulu` diawali `PT Distribusi Nusantara`
21. Verifikasi Group `PT Jalur Distributor Dulu` adalah `Area Jakarta` (Group Distributor sendiri)

### TC-AC-ACC-570: Anchor lintas jenis relasi: Partner lebih awal dari relasi Distributor-langsung menjadi Anchor di view Distributor

22. Ganti isi kotak Search dengan `PT Jalur Partner Dulu`, tekan Enter
23. Lihat sel Managed By dan Group baris `PT Jalur Partner Dulu`
24. Verifikasi Managed By `PT Jalur Partner Dulu` diawali `CV Mitra Sejati`
25. Verifikasi Group `PT Jalur Partner Dulu` adalah `Cabang Menteng` (Group Partner CV Mitra Sejati)

### TC-AC-ACC-572: Distributor melihat Client Direct yang Group-nya tepat node Group milik Distributor itu

26. Ganti isi kotak Search dengan `PT Direct Jakarta`, tekan Enter
27. Lihat sel Managed By dan Group baris `PT Direct Jakarta`
28. Verifikasi baris `PT Direct Jakarta` tampil di sub-tab `Active`
29. Verifikasi Managed By `PT Direct Jakarta` adalah `Direct`
30. Verifikasi Group `PT Direct Jakarta` adalah `Area Jakarta`
31. Klik `(←)` pada kotak Search

### TC-AC-ACC-559: Klik node Group Partner memfilter Client menurut Group Partner parent oleh Distributor

32. Klik node `Cabang Menteng` pada Sidebar Group Tree
33. Verifikasi node `Cabang Menteng` aktif
34. Verifikasi `[All Groups]` tidak aktif
35. Ketik Search `PT Sejahtera Abadi`, tekan Enter
36. Verifikasi baris `PT Sejahtera Abadi` tampil dengan Group `Cabang Menteng`
37. Ganti isi kotak Search dengan `PT Sinar Distributor`, tekan Enter
38. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Sinar Distributor` memiliki Group Distributor sendiri `Area Jakarta`)
39. Klik `(←)` pada kotak Search, lalu klik `[All Groups]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 4, 7, 18, 22, 26, 31, 39. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-36, 15, 927, 569, 570, 572, 559 (semula 15, 36, 559, 569, 570, 572, 927); TC-AC-ACC-559 di akhir karena mengubah pilihan node Group yang dipulihkan sesudahnya.
- Asersi TC-AC-ACC-927 "teks `CV Mitra Mandiri` tidak tampil di daftar" memakai daftar hover yang tampil pada `Verifikasi` tepat sebelumnya sebagai anchor positif.
- Pembagian TC lintas spec: cakupan Client yang terlihat Distributor ini (TC-AC-ACC-58, 574, 575, 576, 950, 451) ada di spec 016; viewer Principal di spec 013, Distributor Timur di spec 017.
- Ukuran spec (39 langkah, melewati sekitar 35 langkah): satu akun, satu dataset (kolom Group, Managed By, dan badge produk), tanpa aksi tulis, dan tiap blok TC memulai dari Search eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-AC-ACC-570: Expected Group `Cabang Menteng` (Group Partner CV Mitra Sejati) konsisten dengan TC-AC-ACC-36; tidak ada selisih, dicatat hanya sebagai konfirmasi silang.
  - TC-AC-ACC-559: Expected butir c menyebut empty state sesudah klik node, tanpa menjelaskan apakah Search terkait ikut direset; spec mempertahankan node `Cabang Menteng` sampai blok berakhir.
