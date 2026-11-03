---
id: TC-FA-TAG-E2E-124-print-qr-cancel-ikon-close-backdrop-dan-nilai-bawaan
title: "Print QR: Cancel, ikon close, backdrop, dan nilai bawaan saat dibuka ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-499
  - TC-FA-TAG-500
  - TC-FA-TAG-501
  - TC-FA-TAG-502
coverage:
  web: automated
---

# Print QR: Cancel, ikon close, backdrop, dan nilai bawaan saat dibuka ulang

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data: tanpa data khusus. Tidak ada kasus yang menekan [Start Print], jadi tidak ada kode QR yang dibuat.
- Kemampuan teknis (disediakan tim FE): pengamat jaringan atas permintaan cetak Start Print (`Spectra.intercept` mode amati saja) untuk asersi "tidak ada request cetak".

## Test Steps

### TC-499: Cancel menutup tanpa konfirmasi

1. Klik tombol `Print QR` di toolbar tab Paired.
2. Isi `Quantity` dengan 5.
3. Klik [Cancel].
4. Verifikasi dialog menutup tanpa dialog konfirmasi apa pun.
5. Verifikasi tidak ada request cetak.

### TC-500: Ikon close menutup tanpa konfirmasi

6. Klik tombol `Print QR` di toolbar tab Paired.
7. Isi `Quantity` dengan 5.
8. Klik ikon close dialog.
9. Verifikasi dialog menutup tanpa dialog konfirmasi apa pun.

### TC-501: Klik backdrop tidak menutup dialog

10. Klik tombol `Print QR` di toolbar tab Paired.
11. Klik area backdrop di luar dialog.
12. Verifikasi Dialog Print QR tetap terbuka.

### TC-502: Nilai bawaan saat dibuka ulang

13. Isi `Quantity` dengan 5.
14. Pilih `Right` pada `Start position`.
15. Klik [Cancel].
16. Klik tombol `Print QR` di toolbar tab Paired.
17. Verifikasi `Quantity` berisi `1`.
18. Verifikasi `Start position` terpilih `Left`.
19. Klik [Cancel].

## Notes

- Langkah penghubung: Dialog Print QR dari langkah 10 tetap terbuka dan dipakai TC-502 (langkah 13 sampai 15); langkah 19 menutup dialog.
- Langkah 4 menjadi anchor langkah 5 (absence request cetak); langkah 5 tidak punya anchor terpisah di TC.
- Temuan untuk QA:
  - Post Condition "Tidak ada kode QR yang dibuat" pada TC-499 dan TC-500 tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-499 menutup dialog yang sudah terisi tanpa `Unsaved Changes`; spec mengikuti TC (Dialog Print QR tidak memakai guard form dirty) sehingga langkah 3 dan langkah 8 tidak memakai pola S-08.
