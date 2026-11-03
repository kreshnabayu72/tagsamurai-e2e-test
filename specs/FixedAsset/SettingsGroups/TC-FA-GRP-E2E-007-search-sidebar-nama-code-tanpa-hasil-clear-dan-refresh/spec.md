---
id: TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh
title: "Search Sidebar Group Tree: Nama, Code, Tanpa Hasil, Dikosongkan, dan Tidak Dipertahankan saat Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-15
  - TC-FA-GRP-16
  - TC-FA-GRP-17
  - TC-FA-GRP-18
  - TC-FA-GRP-19
coverage:
  web: automated
---

# Search Sidebar Group Tree: Nama, Code, Tanpa Hasil, Dikosongkan, dan Tidak Dipertahankan saat Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9): Head Office > Floor 2 > IT Department > Server Room; Warehouse A (Code `WH-A`). Spec ini tidak mengubah data.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-15: Search sidebar by nama

1. Ketik `server` di Search sidebar tanpa menekan Enter
2. Verifikasi tree belum berubah (Server Room belum tampil dan node level 1 lain masih tampil; pencarian tidak real-time)
3. Tekan Enter
4. Verifikasi tree hanya menampilkan Server Room beserta ancestor-nya (IT Department, Floor 2, Head Office)
5. Verifikasi ancestor IT Department, Floor 2, dan Head Office ter-expand otomatis
6. Verifikasi ancestor tampil normal (tidak di-highlight)
7. Verifikasi teks yang cocok `server` pada Server Room di-highlight
8. Verifikasi tabel dan node terpilih tidak berubah (`All Groups` tetap terpilih dan tabel tetap node level 1)
9. Klik `✕` pada Search sidebar, tekan Enter

### TC-FA-GRP-17: Search sidebar tanpa hasil

10. Ketik Search sidebar `zzzz`, tekan Enter
11. Verifikasi area tree menampilkan `No results found`
12. Klik `✕` pada Search sidebar, tekan Enter

### TC-FA-GRP-16: Search sidebar by Code, case-insensitive

13. Ketik Search sidebar `wh-a`, tekan Enter
14. Verifikasi node Warehouse A (Code `WH-A`) ditemukan
15. Klik `✕` pada Search sidebar, tekan Enter

### TC-FA-GRP-18: Search sidebar dikosongkan mengembalikan tree dan state expand

16. Klik toggle collapse-all pada sidebar
17. Klik chevron node Head Office untuk expand Head Office saja
18. Ketik Search sidebar `server`, tekan Enter
19. Klik `✕` pada Search sidebar, tekan Enter
20. Verifikasi tree penuh kembali (node level 1 selain Head Office, termasuk Warehouse A, tampil)
21. Verifikasi hanya Head Office yang ter-expand seperti sebelum search (Floor 2 tampil dan IT Department tidak tampil)

### TC-FA-GRP-19: Search sidebar tidak dipertahankan saat refresh

22. Ketik Search sidebar `server`, tekan Enter
23. Muat ulang halaman dengan F5
24. Verifikasi input Search sidebar kosong
25. Verifikasi tree penuh (node level 1 termasuk Warehouse A tampil)

## Notes

- Langkah penghubung (S-03): langkah 9, 12, 15 (mengosongkan Search sidebar agar TC berikutnya mulai dari tree penuh, S-09), langkah 16 dan 17 (menyiapkan state expand TC-FA-GRP-18). Pada langkah 1 dan 3 mengetik dan Enter dipisah karena TC-FA-GRP-15 menguji bahwa pencarian tidak real-time.
- Urutan TC dalam spec: 15, 17, 16, 18, 19 (TC-FA-GRP-19 terakhir karena muat ulang mereset state sidebar).
- Temuan untuk QA:
  - TC-FA-GRP-18 menyebut "hapus teks atau klik (✕)" sebagai dua alternatif; spec memakai `✕` lalu Enter (8b butir 9).
  - TC-FA-GRP-15 menyebut highlight tanpa warna atau gaya; spec mengasersi keberadaan highlight pada teks yang cocok.
