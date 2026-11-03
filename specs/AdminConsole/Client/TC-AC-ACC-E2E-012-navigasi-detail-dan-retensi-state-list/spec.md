---
id: TC-AC-ACC-E2E-012-navigasi-detail-dan-retensi-state-list
title: "Navigasi ke Detail dari Row Action dan Retensi State List (Back dan F5)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-796
  - TC-AC-ACC-40
  - TC-AC-ACC-41
coverage:
  web: automated
---

# Navigasi ke Detail dari Row Action dan Retensi State List (Back dan F5)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pilihan jumlah baris per halaman (25) dipulihkan ke 10 dalam spec; Search, Sort, dan sub-tab direset lewat klik item `Client` pada sidebar.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-796: Row action Detail membuka Detail Client dari sub-tab Active, Suspended, dan Archived

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik `⋯` pada baris `PT Sejahtera Abadi`, lalu klik `Detail`
3. Verifikasi halaman Admin Console > Client > Detail `PT Sejahtera Abadi` terbuka
4. Verifikasi Breadcrumb `Client > Detail`
5. Verifikasi badge status `Active`
6. Kembali ke List dengan tombol Back browser
7. Klik sub-tab `Suspended`
8. Ketik Search `PT Wahana Nusantara`, tekan Enter
9. Klik `⋯` pada baris `PT Wahana Nusantara`, lalu klik `Detail`
10. Verifikasi halaman Detail `PT Wahana Nusantara` terbuka
11. Verifikasi Breadcrumb `Client > Detail`
12. Verifikasi badge status `Suspended`
13. Kembali ke List dengan tombol Back browser
14. Klik sub-tab `Archived`
15. Ketik Search `PT Karya Abadi`, tekan Enter
16. Klik `⋯` pada baris `PT Karya Abadi`, lalu klik `Detail`
17. Verifikasi halaman Detail `PT Karya Abadi` terbuka
18. Verifikasi Breadcrumb `Client > Detail`
19. Verifikasi badge status `Archived`

### TC-AC-ACC-40: Kembali dari Detail Page mempertahankan state List

20. Klik item `Client` pada sidebar untuk mereset state List
21. Klik sub-tab `Suspended`, ketik Search `Wahana`, tekan Enter, lalu klik header kolom `Client Code` dua kali hingga urutan descending
22. Klik Company Name `PT Wahana Nusantara`
23. Klik Back pada browser
24. Verifikasi kotak Search berisi `Wahana`
25. Verifikasi sort `Client Code` descending tetap aktif

### TC-AC-ACC-41: Refresh halaman (F5) List mempertahankan Search, Sort, jumlah baris per halaman, dan halaman aktif

26. Klik item `Client` pada sidebar untuk mereset state List
27. Pada sub-tab `Active`, ketik Search `Uji`, tekan Enter
28. Klik header kolom `Client Code` dua kali hingga urutan descending
29. Ubah jumlah baris per halaman menjadi 25
30. Pindah ke halaman 2
31. Tekan F5
32. Verifikasi kotak Search masih berisi `Uji`
33. Verifikasi kolom `Client Code` masih terurut descending (`↓`)
34. Verifikasi jumlah baris per halaman masih 25
35. Verifikasi halaman 2 masih aktif (bukan kembali ke halaman 1)
36. Ubah jumlah baris per halaman menjadi 10 dan klik item `Client` pada sidebar untuk mereset state List

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 8, 15, 20, 26, 36. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): tidak ada; urutan TC sumber 796, 40, 41 dipertahankan.
- Klik header `Client Code` dua kali dipakai sesuai TC-AC-ACC-41 langkah 2 untuk mencapai urutan descending (klik pertama ascending, klik kedua descending); pola yang sama dipakai TC-AC-ACC-40 untuk "sort Client Code descending".
- Ukuran spec (36 langkah, melewati sekitar 35 langkah): satu dataset (List dan Detail) tanpa aksi tulis; tiap blok TC memulai dari state bersih (klik sidebar mereset Search, Sort, dan Filter) sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-AC-ACC-40: Expected hanya menyebut Search dan Sort yang dipertahankan, padahal langkah 1 juga memilih sub-tab `Suspended`; spec tidak mengasersi sub-tab terpilih sesudah Back karena TC tidak memintanya.
