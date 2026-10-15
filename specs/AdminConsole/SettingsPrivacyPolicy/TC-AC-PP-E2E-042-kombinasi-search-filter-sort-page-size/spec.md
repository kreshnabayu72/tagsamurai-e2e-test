---
id: TC-AC-PP-E2E-042-kombinasi-search-filter-sort-page-size
title: "Kombinasi Search, Filter, Sort, dan Page Size pada Version History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-115
  - TC-AC-PP-199
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Page Size pada Version History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat B (Version 1 pada 01 Jan 2026 dan tiap versi berikutnya satu hari lebih akhir sampai Version 120 pada 30 Apr 2026; Published By ganjil `John Doe` dan genap `Jane Smith`; Version 120 Active). Hook `before` men-seed Riwayat B lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI). Hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini tidak membuat atau mengubah versi.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-115: Search dan Filter menghasilkan irisan yang sama pada urutan Search dulu maupun Filter dulu

1. Buka Settings > Privacy Policy lewat sidebar
2. Klik icon Search, ketik "doe", lalu tekan Enter
3. Klik icon Filter di toolbar
4. Pada field `Published By` centang `John Doe`
5. Klik `[Apply]`
6. Verifikasi footer menampilkan `1–10 of 60` (urutan Search lalu Filter)
7. Verifikasi seluruh baris Published By `John D`
8. Catat sepuluh baris pertama sebagai baseline urutan Search lalu Filter
9. Klik icon `(←)` pada search bar untuk menutup dan mereset Search
10. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
11. Buka panel Filter, centang `John Doe` pada field `Published By`, lalu klik `[Apply]`
12. Klik icon Search, ketik "doe", lalu tekan Enter
13. Verifikasi footer menampilkan `1–10 of 60` (urutan Filter lalu Search)
14. Verifikasi sepuluh baris pertama sama persis dengan baseline langkah 8
15. Verifikasi jumlah total sama dengan urutan Search lalu Filter (60 baris)

### TC-AC-PP-199: Search, Filter, Sort, dan page size aktif bersamaan menghasilkan irisan yang benar tanpa saling mereset

16. Klik icon `(←)` pada search bar untuk menutup dan mereset Search
17. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`
18. Ubah page size menjadi 25
19. Klik icon Search, ketik "doe", lalu tekan Enter
20. Buka panel Filter, pilih rentang `Published At` 01 Mar 26 sampai 31 Mar 26, lalu klik `[Apply]`
21. Verifikasi footer menampilkan `1–15 of 15`
22. Verifikasi seluruh baris adalah Version ganjil `Version 61` sampai `Version 89`
23. Verifikasi Published By seluruh baris `John D`
24. Klik header `Version` satu kali
25. Verifikasi urutan menaik `Version 61`, `Version 63`, sampai `Version 89`
26. Verifikasi input Search tetap `doe`
27. Verifikasi filter tetap aktif
28. Verifikasi page size tetap 25

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 9 dan 10 (bersihkan Search dan Filter sebelum urutan Filter dulu pada TC-115, sesuai langkah 2 TC sumber), langkah 16 dan 17 (bersihkan Search dan Filter sebelum TC-199), langkah 18 (page size 25 sebagai precondition TC-199). Pemulihan akhir (Search, Filter, sort, page size) dilakukan hook `after` bersama pemulihan dataset.
- Langkah 8 mencatat baseline sepuluh baris pertama (S-12) agar perbandingan di langkah 14 deterministik.
- Spec tidak membuat data dan tidak mengubah Pre-setup.
- Temuan untuk QA: tidak ada.
