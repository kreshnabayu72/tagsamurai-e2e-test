---
id: TC-FA-TAG-E2E-119-print-qr-screening-tombol-dialog-dan-preview-quantity-start-bagian-2
title: "Print QR: Preview berubah langsung saat Quantity atau Start position diubah dan batas 100"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-479
  - TC-FA-TAG-480
  - TC-FA-TAG-481
coverage:
  web: automated
---

# Print QR: Preview berubah langsung saat Quantity atau Start position diubah dan batas 100

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data: tanpa data khusus. Spec ini tidak menekan [Start Print], jadi tidak ada kode QR yang dibuat.

## Test Steps

### TC-479: Preview berubah langsung saat Quantity diubah

1. Klik tombol `Print QR` di toolbar tab Paired.
2. Isi `Quantity` dengan 3.
3. Verifikasi Preview memuat sel `1` sampai `3`.
4. Ubah `Quantity` menjadi 2.
5. Verifikasi Preview memuat sel `1` dan `2` tanpa menekan tombol apa pun.

### TC-480: Preview berubah langsung saat Start position diubah

6. Isi `Quantity` dengan 2.
7. Pilih `Right` pada `Start position`.
8. Verifikasi sel kiri baris pertama kosong.
9. Verifikasi sel `1` berada di kanan baris pertama.
10. Verifikasi sel `2` berada di kiri baris 2.
11. Pilih `Left` pada `Start position`.
12. Verifikasi sel `1` berada di kiri baris pertama.
13. Verifikasi sel `2` berada di kanan baris pertama.

### TC-481: Preview Quantity 100 Left

14. Isi `Quantity` dengan 100.
15. Verifikasi Preview memuat sel `1` sampai `100` dalam 50 baris.
16. Verifikasi sel terakhir bernomor `100` berada di kolom kanan baris ke-50.
17. Verifikasi tidak ada pesan "Quantity must be a whole number from 1 to 100".
18. Klik [Cancel].

## Notes

- Langkah penghubung: Dialog Print QR dibuka sekali di langkah 1 dan dipakai TC-479 sampai TC-481; langkah 18 menutup dialog. Pada TC-480 `Quantity` sudah 2 dari TC-479, langkah 6 tetap ditulis sesuai TC.
- Pembagian TC lintas spec: TC-473 sampai TC-478 ada di spec 118.
- Temuan untuk QA:
  - TC-481 mengasersi absence pesan V-39 tanpa anchor di Expected; Verifikasi Preview 100 sel (langkah 15 dan 16) menjadi anchor positif pada surface yang sama.
