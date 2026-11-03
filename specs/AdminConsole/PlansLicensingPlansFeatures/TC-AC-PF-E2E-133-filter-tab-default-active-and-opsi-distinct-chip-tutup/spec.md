---
id: TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup
title: Filter Tab Default Active Logika AND, Opsi Distinct, Chip, dan Tutup Panel
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-315
  - TC-AC-PF-316
  - TC-AC-PF-317
  - TC-AC-PF-318
  - TC-AC-PF-319
coverage:
  web: automated
---

# Filter Tab Default Active Logika AND, Opsi Distinct, Chip, dan Tutup Panel

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter` (FAMS, Free, v2, Clients 12), `Growth` (FAMS, Paid, v5, 47), `Professional` (FAMS, Paid, v3, 23), `Enterprise` (FAMS, Paid, v1, 8), `SIEM` (SIEM, Paid, v1, 5); tidak ada baris SAMS.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-315 Kombinasi dua field memakai AND

1. Buka Filter Panel, pilih Product `FAMS`, Pricing Type `Paid`, Min Clients `20`, klik `[Apply]`.
2. Verifikasi tabel menampilkan `Growth` (47) dan `Professional` (23).
3. Verifikasi `Enterprise` (8) dan `Starter` (Free) tidak tampil.
4. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-316 Opsi dropdown berasal dari data tabel

5. Buka Filter Panel dan buka dropdown Product.
6. Verifikasi opsi Product hanya `FAMS` dan `SIEM` (tidak ada `SAMS` karena tidak ada baris SAMS).
7. Buka dropdown Pricing Type.
8. Verifikasi opsi Pricing Type adalah `Free` dan `Paid`.
9. Klik ikon Filter untuk menutup panel.

### TC-AC-PF-318 Hapus chip lewat (x)

10. Buka Filter Panel, pilih Product `FAMS` dan `SIEM`, klik `[Apply]`.
11. Buka Filter Panel, klik (x) pada chip `SIEM`, buka dropdown Product.
12. Verifikasi chip `SIEM` hilang.
13. Verifikasi checkbox `SIEM` ter-uncheck.
14. Verifikasi chip `FAMS` tetap tampil.
15. Klik `[Apply]`.
16. Verifikasi tabel menampilkan empat baris FAMS.
17. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.

### TC-AC-PF-319 Tutup panel tanpa Apply

18. Buka Filter Panel dan pilih Product `FAMS` tanpa klik `[Apply]`.
19. Klik ikon Filter lagi untuk menutup panel.
20. Verifikasi tabel tetap menampilkan lima baris.
21. Buka Filter Panel lagi.
22. Verifikasi panel menampilkan nilai ter-Apply terakhir (tidak ada pilihan Product).

### TC-AC-PF-317 Interaksi internal dropdown dan chip

23. Buka dropdown Product dan ketik `si` pada kotak pencarian di dalam dropdown.
24. Verifikasi kotak pencarian di dalam dropdown tersedia.
25. Verifikasi ketik `si` menyisakan opsi `SIEM`.
26. Hapus teks pada kotak pencarian di dalam dropdown, lalu centang opsi `FAMS` dan `SIEM`.
27. Tutup dropdown.
28. Verifikasi opsi terpilih tampil sebagai chip di field Product.
29. Verifikasi `All products` tidak tampil lagi.
30. Klik ikon Filter untuk menutup panel tanpa Apply.

## Notes

- Urutan blok: TC-AC-PF-317 ditempatkan paling akhir karena berakhir dengan pilihan yang belum di-Apply (bagian 3: kasus menutup form di akhir); TC-AC-PF-318 mendahului TC-AC-PF-319 supaya TC-AC-PF-319 dimulai dari tabel penuh.
- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 4, 17 mengosongkan Filter; langkah 9 dan 30 menutup Filter Panel; langkah 26 menghapus teks pencarian dropdown sebelum mencentang kedua opsi (TC memberi urutan ketik `si` lalu centang `FAMS` dan `SIEM`).
- Anchor absence: langkah 3 didahului langkah 2 (baris yang lolos filter tampil di tabel yang sama).
