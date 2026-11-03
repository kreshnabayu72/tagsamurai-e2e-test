---
id: TC-AC-PF-E2E-136-kombinasi-search-filter-sort-dan-clear-tab-default-active
title: Kombinasi Search, Filter, Sort, dan Clear Tab Default Active
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-329
  - TC-AC-PF-331
  - TC-AC-PF-332
  - TC-AC-PF-333
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Clear Tab Default Active

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter` (FAMS, Free, v2, Clients 12), `Growth` (FAMS, Paid, v5, 47), `Professional` (FAMS, Paid, v3, 23), `Enterprise` (FAMS, Paid, v1, 8), `SIEM` (SIEM, Paid, v1, 5).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-329 Pindah kolom sort tidak mereset Search dan Filter

1. Ketik Search `r`, tekan Enter.
2. Buka Filter Panel, pilih Product `FAMS`, klik `[Apply]`.
3. Klik header `Clients` satu kali.
4. Klik header `Version` satu kali.
5. Verifikasi panah sort kolom `Clients` netral.
6. Verifikasi kolom `Version` ascending.
7. Verifikasi Search `r` tetap aktif.
8. Verifikasi Filter Product `FAMS` tetap aktif.

### TC-AC-PF-331 Kombinasi empat kontrol

9. Klik header `Clients` dua kali (descending).
10. Ubah Rows per page ke `25`.
11. Verifikasi tabel menampilkan `Growth` (47), `Professional` (23), `Starter` (12), `Enterprise` (8) berurutan.
12. Verifikasi semua kontrol tetap aktif: Search `r`, Filter Product `FAMS`, sort Clients descending, dan Rows per page `25`.

### TC-AC-PF-332 Clear Search saat Filter dan Sort aktif

13. Klik ikon `x` pada Search, tekan Enter.
14. Verifikasi Filter Product `FAMS` dan sort Clients descending tetap aktif.
15. Verifikasi tabel menampilkan empat baris FAMS berurutan Clients turun.

### TC-AC-PF-333 Clear Field Filter saat Search dan Sort aktif

16. Ketik Search `r`, tekan Enter.
17. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`.
18. Verifikasi Search `r` dan sort Clients descending tetap aktif.
19. Verifikasi tabel menampilkan semua baris yang mengandung `r` berurutan Clients turun.
20. Klik ikon `x` pada Search, tekan Enter.
21. Klik header `Clients` satu kali untuk mengembalikan sort ke netral.
22. Ubah Rows per page ke `10`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 16 menyetel ulang Search `r` sebagai kondisi awal TC-AC-PF-333 (Search `r`, Filter `FAMS`, sort Clients descending); langkah 20 sampai 22 memulihkan Search, sort, dan ukuran halaman.
- TC-AC-PF-329 ditempatkan di spec ini karena memakai kombinasi kontrol Search, Filter, dan Sort yang sama; langkah 9 mengubah sort dari `Version` ascending ke `Clients` descending.
