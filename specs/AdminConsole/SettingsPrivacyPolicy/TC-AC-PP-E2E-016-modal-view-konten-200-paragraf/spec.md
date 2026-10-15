---
id: TC-AC-PP-E2E-016-modal-view-konten-200-paragraf
title: "Modal View: Konten 200 Paragraf Dirender Penuh dengan Scroll"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-33
coverage:
  web: automated
---

# Modal View: Konten 200 Paragraf Dirender Penuh dengan Scroll

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, Andi Wijaya, env `Spectra.env.AC_TC_PASSWORD`), login di hook `before`; hook `after` mengembalikan sesi ke akun default suite yang sama.
- Dataset Riwayat A varian isi (Pre-setup 9): Version 3 Active berisi 200 paragraf, Version 2 dan Version 1 seperti Riwayat A standar. Hook `before` men-seed varian ini lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat dengan isi konten kustom; riwayat versi append-only) dan hook `after` mengembalikan dataset ke Riwayat A standar.
- Spec tidak membuat atau mengubah versi. Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `jumlahParagrafKontenPanjang` | `200` (jumlah paragraf pada Version 3 varian) | TC-AC-PP-33 (Data Uji) |

## Test Steps

### TC-AC-PP-33: Konten panjang di Modal View dirender penuh dengan scroll tanpa dipotong

1. Buka Settings > Privacy Policy
2. Klik teks tautan `Version 3`
3. Gulir area konten sampai paragraf terakhir
4. Verifikasi seluruh paragraf (`jumlahParagrafKontenPanjang`, yaitu 200) dapat dijangkau lewat scroll di dalam modal
5. Verifikasi tidak ada pemotongan teks
6. Verifikasi tidak ada tombol untuk memperluas konten
7. Verifikasi info bar tetap terlihat
8. Verifikasi footer tetap terlihat

## Notes

- Mode: FE+BE. Kelas e (volume data khusus): konten 200 paragraf dipisah dari spec screening Modal View (`TC-AC-PP-E2E-015`). Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Tidak ada langkah penghubung.
- Temuan untuk QA: TC-AC-PP-33 tidak menyebut isi tiap paragraf sehingga paragraf pertama dan terakhir tidak dapat diidentifikasi; tim FE perlu menyeeding paragraf berpenanda urutan (mis. nomor 1 sampai 200) agar "paragraf terakhir dapat dijangkau" bisa diasersi. Post Condition TC ("Tidak ada perubahan data") tidak punya langkah observasi sehingga tidak diasersi.
