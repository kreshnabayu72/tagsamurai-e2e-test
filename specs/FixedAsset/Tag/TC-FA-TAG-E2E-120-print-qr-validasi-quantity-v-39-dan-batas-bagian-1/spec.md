---
id: TC-FA-TAG-E2E-120-print-qr-validasi-quantity-v-39-dan-batas-bagian-1
title: "Print QR: validasi Quantity V-39 untuk nilai kosong, 0, 101, desimal, dan negatif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-482
  - TC-FA-TAG-483
  - TC-FA-TAG-484
  - TC-FA-TAG-485
  - TC-FA-TAG-486
coverage:
  web: automated
---

# Print QR: validasi Quantity V-39 untuk nilai kosong, 0, 101, desimal, dan negatif

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data: tanpa data khusus. Semua nilai `Quantity` di spec ini ditolak sebelum permintaan cetak terkirim, jadi tidak ada kode QR yang dibuat.
- Kemampuan teknis (disediakan tim FE): pengamat jaringan atas permintaan cetak Start Print (`Spectra.intercept` dalam mode amati saja, tanpa mengubah respons) untuk asersi "tidak ada request cetak".

## Test Steps

1. Klik tombol `Print QR` di toolbar tab Paired.

### TC-482: Quantity kosong

2. Isi `Quantity` dengan nilai kosong (hapus nilai 1).
3. Verifikasi pesan inline "Quantity must be a whole number from 1 to 100" tampil sejak nilai diubah (sebelum Start Print).
4. Verifikasi Preview menampilkan empty state "Enter a quantity to see the preview."
5. Klik [Start Print].
6. Verifikasi tidak ada request cetak dan Toast sukses tidak tampil.
7. Verifikasi dialog tetap terbuka.
8. Isi `Quantity` dengan 1.

### TC-483: Quantity 0

9. Isi `Quantity` dengan nilai 0.
10. Verifikasi pesan inline "Quantity must be a whole number from 1 to 100" tampil sejak nilai diubah (sebelum Start Print).
11. Verifikasi Preview menampilkan empty state "Enter a quantity to see the preview."
12. Klik [Start Print].
13. Verifikasi tidak ada request cetak dan Toast sukses tidak tampil.
14. Verifikasi dialog tetap terbuka.
15. Isi `Quantity` dengan 1.

### TC-484: Quantity 101

16. Isi `Quantity` dengan nilai 101.
17. Verifikasi pesan inline "Quantity must be a whole number from 1 to 100" tampil sejak nilai diubah (sebelum Start Print).
18. Verifikasi Preview menampilkan empty state "Enter a quantity to see the preview."
19. Klik [Start Print].
20. Verifikasi tidak ada request cetak dan Toast sukses tidak tampil.
21. Verifikasi dialog tetap terbuka.
22. Isi `Quantity` dengan 1.

### TC-485: Quantity desimal 2.5

23. Isi `Quantity` dengan nilai 2.5.
24. Verifikasi pesan inline "Quantity must be a whole number from 1 to 100" tampil sejak nilai diubah (sebelum Start Print).
25. Verifikasi Preview menampilkan empty state "Enter a quantity to see the preview."
26. Klik [Start Print].
27. Verifikasi tidak ada request cetak dan Toast sukses tidak tampil.
28. Verifikasi dialog tetap terbuka.
29. Isi `Quantity` dengan 1.

### TC-486: Quantity negatif -1

30. Isi `Quantity` dengan nilai -1.
31. Verifikasi pesan inline "Quantity must be a whole number from 1 to 100" tampil sejak nilai diubah (sebelum Start Print).
32. Verifikasi Preview menampilkan empty state "Enter a quantity to see the preview."
33. Klik [Start Print].
34. Verifikasi tidak ada request cetak dan Toast sukses tidak tampil.
35. Verifikasi dialog tetap terbuka.
36. Klik [Cancel].

## Notes

- Langkah penghubung: langkah 1 membuka Dialog Print QR sekali untuk kelima kasus tanpa submit sukses. Langkah 8, 15, 22, dan 29 mengisi `Quantity` dengan 1 sebagai pembersih error inline yang identik antar kasus; langkah 36 menutup dialog.
- Alasan di atas sekitar 35 langkah (36 langkah): kelima blok memakai pola V-39 yang sama pada Dialog Print QR yang sama, dan kegagalan satu nilai tidak membuat nilai lain kehilangan makna.
- Pembagian TC lintas spec: TC-487 sampai TC-489 ada di spec 121.
- Temuan untuk QA:
  - Post Condition TC-482 sampai TC-486 ("Tidak ada kode QR yang dibuat") tidak punya langkah observasi di TC dan tidak diasersi.
  - Expected c TC-482 sampai TC-486 ("tidak ada request cetak") tidak menyebut cara pengamatannya; spec memakai pengamat jaringan (lihat Prerequisites).
