---
id: TC-FA-TAG-E2E-118-print-qr-screening-tombol-dialog-dan-preview-quantity-start-bagian-1
title: "Print QR: screening tombol toolbar, Dialog, dan Preview Quantity serta Start position (bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-473
  - TC-FA-TAG-474
  - TC-FA-TAG-475
  - TC-FA-TAG-476
  - TC-FA-TAG-477
  - TC-FA-TAG-478
coverage:
  web: automated
---

# Print QR: screening tombol toolbar, Dialog, dan Preview Quantity serta Start position (bagian 1)

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data: tanpa data khusus. Spec ini tidak menekan [Start Print], jadi tidak ada kode QR yang dibuat.

## Test Steps

### TC-473: Screening tombol toolbar Print QR

1. Amati urutan tombol di toolbar tab Paired.
2. Verifikasi tombol `Print QR` bergaya Button Outline.
3. Verifikasi tombol `Print QR` berikon PrinterLine.
4. Verifikasi tombol `Print QR` berada di sebelah kiri tombol scan `Replace TAG`.
5. Verifikasi tombol `Print QR` berada setelah tombol `Changelog`.
6. Klik tombol `Print QR`.
7. Verifikasi Dialog Print QR terbuka.

### TC-474: Screening Dialog Print QR

8. Verifikasi dialog (Size MD) berjudul `Print QR`.
9. Verifikasi field `Quantity` (NumberInput) berisi `1`.
10. Verifikasi field `Start position` (RadioGroup) berpilihan `Left` dan `Right`.
11. Verifikasi pilihan `Left` terpilih pada `Start position`.
12. Verifikasi bagian `Preview` menampilkan lembar label dua kolom.
13. Verifikasi footer memuat tombol [Cancel] dan [Start Print].
14. Verifikasi tombol [Start Print] Enabled.

### TC-475: Preview default Quantity 1 Left

15. Verifikasi Preview menampilkan satu sel bernomor `1` di kolom kiri baris pertama.
16. Verifikasi kolom kanan baris pertama kosong.
17. Verifikasi Preview tidak menampilkan kode QR sebenarnya.

### TC-476: Preview Quantity 5 Left

18. Isi `Quantity` dengan 5.
19. Verifikasi baris 1 Preview memuat sel `1` (kiri) dan `2` (kanan).
20. Verifikasi baris 2 Preview memuat sel `3` dan `4`.
21. Verifikasi baris 3 Preview memuat sel `5` di kiri dan kolom kanan kosong.

### TC-477: Preview Quantity 1 Right

22. Isi `Quantity` dengan 1.
23. Pilih `Right` pada `Start position`.
24. Verifikasi sel kiri baris pertama kosong.
25. Verifikasi sel bernomor `1` berada di kolom kanan baris pertama.

### TC-478: Preview Quantity 4 Right

26. Isi `Quantity` dengan 4.
27. Pilih `Right` pada `Start position`.
28. Verifikasi baris 1 Preview memuat sel kiri kosong dan sel `1` di kanan.
29. Verifikasi baris 2 Preview memuat sel `2` dan `3`.
30. Verifikasi baris 3 Preview memuat sel `4` di kiri dan kolom kanan kosong.
31. Klik [Cancel].

## Notes

- Langkah penghubung: Dialog Print QR dibuka sekali di TC-473 dan dipakai TC-474 sampai TC-478 (kasus tanpa submit memakai satu pembukaan). Langkah 22 mengembalikan `Quantity` ke 1 sebagai kondisi awal TC-477, dan langkah 31 menutup dialog.
- Pembagian TC lintas spec: TC-479 sampai TC-481 ada di spec 119.
- Temuan untuk QA:
  - TC-475 mengasersi absence ("tidak menampilkan kode QR sebenarnya") tanpa anchor di Expected; urutan Verifikasi di spec menaruh Verifikasi sel `1` lebih dulu sebagai anchor positif.
