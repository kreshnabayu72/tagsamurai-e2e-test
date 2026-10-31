---
id: TC-GS-UOM-E2E-028-delete-row-action-dialog-screening-dan-cancel
title: "Screening Row Action dan Dialog Delete Unit serta Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-93
  - TC-GS-UOM-94
  - TC-GS-UOM-95
  - TC-GS-UOM-333
coverage:
  web: automated
---

# Screening Row Action dan Dialog Delete Unit serta Cancel

## Prerequisites

- Mode: FE+BE. Dialog `Delete Unit` muncul sesudah cek referensi ke backend nyata (Check References); tidak ada data dibuat, diubah, atau dihapus.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca): unit `Meter` / `m` (bebas relasi). Baris ini hanya dibuka dialognya dan dibatalkan (`[Cancel]`, Esc); tidak pernah dihapus, dan Last Updated tidak berubah (pengecualian S-06: aksi dibatalkan). Fixture belum ada; tim FE menyiapkan `fixtures/measurement.json` dengan kunci `preSetupClientA`.
- Data dinamis: tidak ada; tidak ada cleanup.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-UOM-333: Screening Overlay Row Action pada baris Measurement

1. Ketik Search `Meter`, tekan Enter
2. Verifikasi baris `Meter` tampil di tabel
3. Klik `⋯` pada baris `Meter`
4. Verifikasi Overlay Row Action muncul menempel pada `⋯`
5. Verifikasi Overlay Row Action muncul tanpa backdrop
6. Verifikasi opsi berurutan: `Detail`, `Edit`, `Delete`
7. Verifikasi opsi `Detail` memakai icon FileInfoLine dan severity dark
8. Verifikasi opsi `Edit` memakai icon Edit2Line dan severity dark
9. Verifikasi opsi `Delete` memakai icon DeleteBin6Line dan severity danger

### TC-GS-UOM-93: Screening dialog Delete Unit untuk unit bebas relasi

10. Klik `Delete` pada overlay baris `Meter`
11. Verifikasi dialog Title `Delete Unit` (severity danger)
12. Verifikasi Body: bullet `Meter`
13. Verifikasi Body: kalimat `Are you sure you want to delete it? This action cannot be undone.`
14. Verifikasi tombol `[Cancel]` (text, contrast) dan `[Delete]` (filled, danger)

### TC-GS-UOM-95: Esc tidak menutup dialog Delete

15. Tekan Esc
16. Verifikasi dialog tetap terbuka

### TC-GS-UOM-94: Cancel pada dialog Delete tidak menghapus unit

17. Klik [Cancel]
18. Verifikasi dialog tertutup
19. Verifikasi baris `Meter` tetap ada di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 19.
- Urutan TC dalam spec: 333, 93, 95, 94 (urutan sumber 93, 94, 95, 333). Alasan: TC-333 adalah screening overlay (screening di awal, prinsip 2); TC-93, 95, dan 94 berbagi satu pembukaan dialog `Delete Unit` pada `Meter`: Esc diuji dulu karena tidak menutup dialog, lalu `[Cancel]` menutupnya.
- Langkah penghubung: langkah 1 (Search `Meter` untuk menemukan baris; hasil Search juga memuat `Centimeter` dan `Millimeter` yang namanya memuat `meter`, baris `Meter` tetap diverifikasi di langkah 2) dan langkah 10 (klik `Delete` pada overlay yang sudah dibuka di langkah 3, sama dengan langkah "Klik `⋯` baris Meter > Delete" TC-93).
- Tidak ada pembagian TC lintas spec; seluruh TC sumber spec ini dikerjakan di sini.
- Temuan untuk QA: tidak ada.
