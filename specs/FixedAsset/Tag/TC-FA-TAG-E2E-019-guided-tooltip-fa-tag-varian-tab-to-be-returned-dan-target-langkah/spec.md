---
id: TC-FA-TAG-E2E-019-guided-tooltip-fa-tag-varian-tab-to-be-returned-dan-target-langkah
title: "Guided Tooltip fa-tag: Teks Langkah 3 dan 4 Varian Tab To Be Returned serta Target Sorotan Tiap Langkah"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-73
  - TC-FA-TAG-75
coverage:
  web: automated
---

# Guided Tooltip fa-tag: Teks Langkah 3 dan 4 Varian Tab To Be Returned serta Target Sorotan Tiap Langkah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-tag` sendiri sehingga mengecualikan pernyataan hook suite. Hook `before` spec ini menyetel flag itu belum ada untuk akun Total Control sesudah hook suite, dan hook `after` memulihkannya ke true (nilai awal akun dicatat di hook `before`). Langkah 1 dan 13 menghapus flag lewat kemampuan teknis di bawah.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak didefinisikan di TC maupun PRD yang dibaca, S-13): menghapus dan menyetel flag `guided_tooltip_seen_fa-tag` untuk akun Total Control.
- Data Pre-setup (dipakai sebagai latar; hanya dibaca, tidak diubah): dataset tab Paired (Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A) dan tab To Be Returned dengan 3 Tag `RF-00071`, `RF-00088`, `NF-00092`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena data Pre-setup yang sama dipakai spec lain (suite.md).
- State global yang diubah: flag Guided Tooltip akun Total Control (dipulihkan di hook `after`); suite berjalan serial.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Data Pre-setup hanya dibaca; satu-satunya perubahan adalah flag Guided Tooltip `guided_tooltip_seen_fa-tag` akun Total Control lewat fixture (hapus flag: langkah 1, 13; disetel kembali oleh walkthrough: langkah 3, 12, 23), dipulihkan di hook `after`; tidak ada entri Changelog, Event Log, TAG Log, atau batch QR.

## Test Steps

### TC-FA-TAG-73: Guided Tooltip langkah 3 dan 4 pada tab To Be Returned memakai teks varian tab

1. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
2. Buka menu Fixed Asset > TAG lewat sidebar
3. Klik `[Skip]`
4. Klik Tab `To Be Returned`
5. Klik tombol `[?]`
6. Klik `[Next]` dua kali
7. Verifikasi Step 3 of 4 dengan judul `To be returned` dan deskripsi `Scan a TAG or return it manually to send it back to Global Settings.`
8. Verifikasi spotlight pada tabel To Be Returned
9. Klik `[Next]` sekali lagi
10. Verifikasi Step 4 of 4 dengan judul `Event Log` dan deskripsi `Review the TAGs returned to Global Settings.`
11. Verifikasi spotlight pada tombol Event Log
12. Klik `[Skip]`

### TC-FA-TAG-75: Setiap langkah Guided Tooltip menyorot elemen permanen halaman

13. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
14. Buka menu Fixed Asset > TAG lewat sidebar
15. Verifikasi langkah 1 menyorot Tabs
16. Klik `[Next]`
17. Verifikasi langkah 2 menyorot kartu filter
18. Klik `[Next]`
19. Verifikasi langkah 3 menyorot tabel grup
20. Klik `[Next]`
21. Verifikasi langkah 4 menyorot tombol `Changelog`
22. Verifikasi tidak ada langkah yang menyorot row action, bulk action bar, atau konten modal
23. Klik `[Done]`

## Notes

- Langkah 1, 12, 13, dan 23 adalah langkah penghubung (menghapus flag; menutup walkthrough), tanpa asersi (S-03). Flag diatur belum ada oleh hook `before` untuk langkah 2.
- Langkah 22 adalah asersi absence atas target sorotan; anchor positif adalah Verifikasi target langkah 1 sampai 4 pada langkah 15, 17, 19, dan 21 (bagian 8b butir 2).
- TC-FA-TAG-62 sampai 68 ada di spec 013, TC-FA-TAG-69, 70, dan 74 ada di spec 014, dan TC-FA-TAG-71 dan 72 ada di spec 015.
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut data yang sama dengan spec lain; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Data Pre-setup hanya dibaca; satu-satunya perubahan adalah flag Guided Tooltip `guided_tooltip_seen_fa-tag` akun Total Control lewat fixture (hapus flag: langkah 1, 13; disetel kembali oleh walkthrough: langkah 3, 12, 23), dipulihkan di hook `after`; tidak ada entri Changelog, Event Log, TAG Log, atau batch QR.
- Temuan untuk QA:
  - TC-FA-TAG-73 langkah 6 ("Klik `[Next]` dua kali" lalu "sekali lagi") dimulai dari Step 1 setelah `[?]`; Expected a dan b diasersi pada Step 3 dan Step 4, sehingga `[Next]` ketiga ke Step 4 dihitung dari Step 3.
  - TC-FA-TAG-75 Expected b ("tidak ada langkah yang menyorot row action, bulk action bar, atau konten modal") disimpulkan dari target langkah 1 sampai 4; tidak ada pengamatan terpisah selain keempat target itu.
