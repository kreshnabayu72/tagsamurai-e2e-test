---
id: TC-FA-TAG-E2E-122-print-qr-start-print-data-tersimpan-dialog-cetak-browser-dan-bagian-1
title: "Print QR: Start Print menyimpan data, membuka dialog cetak browser, dan menampilkan toast"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-490
  - TC-FA-TAG-491
  - TC-FA-TAG-492
  - TC-FA-TAG-493
coverage:
  web: automated
---

# Print QR: Start Print menyimpan data, membuka dialog cetak browser, dan menampilkan toast

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data: tanpa data khusus. Tiap Start Print membuat kode QR di backend (3, 1, 100, dan 1 kode).
- Kemampuan teknis (disediakan tim FE/BE):
  - Dialog cetak browser (tingkat OS) teramati: isi dokumen cetak (jumlah label dan posisi label) dibaca dan dialognya ditutup oleh harness.
  - `Spectra.intercept` menunda respons permintaan Start Print beberapa detik selama spec (nilai tepat dipilih tahap script) supaya state loading teramati; penundaan dipasang di hook `before` dan dilepas di hook `after`. Penundaan hanya untuk mengamati state UI, bukan kegagalan yang dipaksakan.
  - Pengamat jaringan atas permintaan cetak untuk menghitung jumlah permintaan.
  - Pembersihan kode QR hasil cetak dari registri Global lewat fixture backend.
- State global yang dipulihkan: kode QR yang dibuat spec ini dihapus dari registri Global di hook `after`.

## Test Steps

### TC-490: Start Print Quantity 3 Left

1. Klik tombol `Print QR` di toolbar tab Paired.
2. Isi `Quantity` dengan 3.
3. Klik [Start Print].
4. Verifikasi state loading tampil pada [Start Print] selama proses.
5. Verifikasi dialog cetak browser terbuka dengan 3 label.
6. Verifikasi label pertama berada di kolom kiri baris pertama.
7. Tutup dialog cetak browser.
8. Verifikasi Dialog Print QR menutup.
9. Verifikasi Toast "Success, QR labels have been sent to print."

### TC-491: Start position Right

10. Klik tombol `Print QR` di toolbar tab Paired.
11. Isi `Quantity` dengan 1.
12. Pilih `Right` pada `Start position`.
13. Klik [Start Print].
14. Verifikasi dokumen cetak menempatkan label di kolom kanan baris pertama.
15. Verifikasi sel kiri baris pertama pada dokumen cetak kosong.
16. Tutup dialog cetak browser.
17. Verifikasi Toast "Success, QR labels have been sent to print."

### TC-492: Quantity 100 (batas atas)

18. Klik tombol `Print QR` di toolbar tab Paired.
19. Isi `Quantity` dengan 100.
20. Verifikasi field `Quantity` berisi 100.
21. Verifikasi tidak ada pesan "Quantity must be a whole number from 1 to 100".
22. Klik [Start Print].
23. Verifikasi Toast "Success, QR labels have been sent to print."
24. Tutup dialog cetak browser.

### TC-493: Tombol Start Print saat proses

25. Klik tombol `Print QR` di toolbar tab Paired.
26. Klik [Start Print].
27. Verifikasi tombol [Start Print] menampilkan state loading.
28. Verifikasi tombol [Start Print] tetap tampil selama loading.
29. Verifikasi tombol [Start Print] berstatus Disabled selama loading.
30. Coba klik [Start Print] sekali lagi.
31. Verifikasi jumlah permintaan cetak tetap satu (penekanan ulang tidak mengirim permintaan kedua).
32. Tutup dialog cetak browser.

## Notes

- Langkah penghubung: langkah 7, 16, 24, dan 32 menutup dialog cetak browser yang terbuka setelah Start Print; langkah 30 adalah aksi penekanan ulang yang dibutuhkan Expected b TC-493 (TC tidak menuliskannya sebagai langkah).
- Anchor positif (S-03): langkah 20 (field `Quantity` berisi 100) menjadi anchor absence di langkah 21 TC-492, karena dialog menutup setelah Start Print sehingga absence harus diasersi sebelum klik. Anchor itu tidak ada di Expected TC.
- Penundaan respons di Prerequisites hanya untuk mengamati state loading (bagian 3 prinsip 13b); spec ini bukan kelas b.
- Pembagian TC lintas spec: TC-498 ada di spec 123.
- Temuan untuk QA:
  - Post Condition TC-490 ("Backend menyimpan data cetak dan 3 kode QR berstatus Available" dan "Tidak ada entri Changelog, Activity Log, maupun System Log"), TC-491, dan TC-492 tidak punya langkah observasi di TC dan tidak diasersi; absence entri log mengikuti NC-03 dan tidak diklaim teruji di spec ini (S-05).
  - TC-490 sampai TC-492 diberi label Manual Only karena dialog cetak browser tingkat OS; spec tetap memuatnya dengan kemampuan di Prerequisites.
  - TC-493 menuliskan "penekanan ulang tidak mengirim permintaan kedua" di Expected tanpa langkah penekanan ulang.
