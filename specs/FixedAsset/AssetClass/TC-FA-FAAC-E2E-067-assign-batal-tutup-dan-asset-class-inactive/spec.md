---
id: TC-FA-FAAC-E2E-067-assign-batal-tutup-dan-asset-class-inactive
title: "Batal dan Tutup Dialog Assign Asset Names serta Assign pada Asset Class Inactive"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-153
  - TC-FA-FAAC-154
  - TC-FA-FAAC-160
  - TC-FA-FAAC-712
coverage:
  web: automated
---

# Batal dan Tutup Dialog Assign Asset Names serta Assign pada Asset Class Inactive

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API, dihapus di hook `after`; kode literal, lihat Notes): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-067`, Class Name `Anchor Class {runId}-067` (disebut "anchor"); Asset Class Inactive Class Code `INACT-067`, Class Name `Inactive Class {runId}-067`.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Name tanpa Asset Class: Meeting Table (0 aset aktif; dipakai spec ini). Forklift 3T, Forklift 5T, Laptop Standard, dan Pallet Jack Electric adalah precondition TC, tidak diasersi. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk keanggotaan Asset Name.
- State global: tidak ada yang diubah (tidak ada Asset Name yang ter-assign oleh spec ini).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik link Class Code `ANCHOR-067`, lalu klik tab "Asset Names"

### TC-FA-FAAC-153: Batal Assign dengan tombol Cancel setelah memilih satu Asset Name

2. Klik tombol "+ Assign Asset Names"
3. Centang baris "Meeting Table"
4. Klik [Cancel]
5. Verifikasi dialog Assign menutup tanpa dialog konfirmasi apa pun
6. Verifikasi tidak ada toast
7. Verifikasi tabel tab Asset Names tidak berubah (tetap kosong) dan "Meeting Table" tidak ter-assign

### TC-FA-FAAC-154: Tutup dialog Assign dengan ikon ✕ setelah memilih satu Asset Name

8. Klik tombol "+ Assign Asset Names"
9. Centang baris "Meeting Table"
10. Klik ikon [✕] di header dialog
11. Verifikasi dialog menutup tanpa konfirmasi
12. Verifikasi tidak ada toast
13. Verifikasi "Meeting Table" tidak ter-assign (tabel tab Asset Names tetap kosong)

### TC-FA-FAAC-712: Tutup dialog Assign dengan tombol Esc setelah memilih satu Asset Name

14. Klik tombol "+ Assign Asset Names"
15. Centang baris "Meeting Table"
16. Tekan tombol Esc
17. Verifikasi dialog menutup tanpa dialog Unsaved Changes dan tanpa konfirmasi
18. Verifikasi tidak ada toast
19. Verifikasi tabel tab Asset Names tidak berubah dan "Meeting Table" tidak ter-assign

### TC-FA-FAAC-160: Klik + Assign Asset Names pada Asset Class Inactive menampilkan Dialog Blok

20. Buka Detail Asset Class `INACT-067`, lalu klik tab "Asset Names" (breadcrumb "Asset Class", klik link Class Code)
21. Verifikasi tombol "+ Assign Asset Names" tetap tampil dan Enabled
22. Klik tombol "+ Assign Asset Names"
23. Verifikasi Dialog Blok tampil: Title "Asset Class Unavailable", Body "• INACT-067 – Inactive Class {runId}-067" dan "This asset class is inactive. Activate it first.", tombol [OK]
24. Verifikasi dialog Assign tidak terbuka
25. Klik [OK]
26. Verifikasi dialog menutup
27. Verifikasi tidak ada toast

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 153, 154, 712 (blok batal/tutup pada anchor), lalu 160 (Asset Class Inactive).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name seed dipakai apa adanya; spec ini tidak meng-assign (hanya dibatalkan/ditutup).
- Class Code `ANCHOR-067` dan `INACT-067` ditulis literal tanpa suffix `{runId}-<NNN>` karena Class Code dibatasi 15 karakter sehingga suffix itu tidak muat (S-12, nama literal; pola spec 047 dan 048); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh).
- Langkah penghubung (S-03): langkah 1 dan 20 (navigasi ke Detail Asset Class).
- Precondition TC-160 "hasil TC anchor Deactivate" dipenuhi lewat seeding API (S-04) berupa Asset Class Inactive milik spec.
- Temuan untuk QA: tidak ada selisih lain.
