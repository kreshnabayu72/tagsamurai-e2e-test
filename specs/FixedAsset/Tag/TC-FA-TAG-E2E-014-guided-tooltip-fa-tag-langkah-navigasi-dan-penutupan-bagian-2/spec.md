---
id: TC-FA-TAG-E2E-014-guided-tooltip-fa-tag-langkah-navigasi-dan-penutupan-bagian-2
title: "Guided Tooltip fa-tag: Tombol Back, Navigasi Keyboard, dan Resize Viewport Menutup Tanpa Menandai Seen"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-69
  - TC-FA-TAG-70
  - TC-FA-TAG-74
coverage:
  web: automated
---

# Guided Tooltip fa-tag: Tombol Back, Navigasi Keyboard, dan Resize Viewport Menutup Tanpa Menandai Seen

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-tag` sendiri sehingga mengecualikan pernyataan hook suite. Hook `before` spec ini menyetel flag itu belum ada untuk akun Total Control sesudah hook suite, dan hook `after` memulihkannya ke true (nilai awal akun dicatat di hook `before`). Langkah 1, 7, dan 19 menghapus flag dan langkah 18 serta 23 membaca flag lewat kemampuan teknis di bawah.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak didefinisikan di TC maupun PRD yang dibaca, S-13): menghapus dan menyetel flag `guided_tooltip_seen_fa-tag` untuk akun Total Control, membaca nilainya; pengaturan ukuran viewport browser (diubah pada langkah 21 dan dipulihkan pada langkah 26, juga di hook `after`).
- Data Pre-setup tab Paired (dipakai sebagai latar; hanya dibaca, tidak diubah): grup Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena data Pre-setup yang sama dipakai spec lain (suite.md).
- State global yang diubah: flag Guided Tooltip akun Total Control dan ukuran viewport (dipulihkan di hook `after`); suite berjalan serial.
- Nilai literal Pre-setup dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Data Pre-setup hanya dibaca; satu-satunya perubahan adalah flag Guided Tooltip `guided_tooltip_seen_fa-tag` akun Total Control dan ukuran viewport browser (diubah di langkah 21, dipulihkan di langkah 26) lewat fixture (hapus flag: langkah 1, 7, 19; disetel kembali oleh walkthrough: langkah 16, 26), dipulihkan di hook `after`; tidak ada entri Changelog, Event Log, TAG Log, atau batch QR.

## Test Steps

### TC-FA-TAG-69: Tombol Back kembali ke langkah sebelumnya

1. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
2. Buka menu Fixed Asset > TAG lewat sidebar
3. Klik `[Next]`
4. Klik `[Back]`
5. Verifikasi walkthrough kembali ke Step 1 of 4 dengan judul `Tabs`
6. Verifikasi tombol `[Back]` Hidden kembali

### TC-FA-TAG-70: Navigasi keyboard Guided Tooltip

7. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
8. Buka menu Fixed Asset > TAG lewat sidebar
9. Verifikasi Tooltip box menerima fokus keyboard
10. Tekan Enter
11. Verifikasi walkthrough pindah ke Step 2
12. Tekan panah kiri
13. Verifikasi walkthrough kembali ke Step 1
14. Tekan panah kanan
15. Verifikasi walkthrough ke Step 2
16. Tekan Esc
17. Verifikasi walkthrough tertutup sebagai Skip
18. Verifikasi flag `guided_tooltip_seen_fa-tag` bernilai true

### TC-FA-TAG-74: Mengubah ukuran viewport menutup walkthrough tanpa menandai seen

19. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
20. Buka menu Fixed Asset > TAG lewat sidebar
21. Ubah ukuran viewport browser
22. Verifikasi walkthrough tertutup saat resize
23. Verifikasi flag `guided_tooltip_seen_fa-tag` belum ditetapkan
24. Muat ulang halaman
25. Verifikasi walkthrough muncul lagi dari Step 1
26. Pulihkan ukuran viewport browser dan klik `[Skip]`

## Notes

- Langkah 1, 7, 19 (menghapus flag) dan 26 (memulihkan viewport dan menutup walkthrough) adalah langkah penghubung, tanpa asersi (S-03). Flag diatur belum ada oleh hook `before` untuk langkah 2.
- Langkah 9 diletakkan sebelum Enter karena Tooltip box harus sudah menerima fokus saat walkthrough terbuka; Expected TC-FA-TAG-70 butir e disusun mengikuti urutan state (bagian 8b butir 5).
- TC-FA-TAG-62 sampai 68 ada di spec 013, TC-FA-TAG-71 dan 72 ada di spec 015, TC-FA-TAG-73 dan 75 ada di spec 019.
- A-15: nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena TC menuntut data tab Paired yang sama dengan spec lain; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Data Pre-setup hanya dibaca; satu-satunya perubahan adalah flag Guided Tooltip `guided_tooltip_seen_fa-tag` akun Total Control dan ukuran viewport browser (diubah di langkah 21, dipulihkan di langkah 26) lewat fixture (hapus flag: langkah 1, 7, 19; disetel kembali oleh walkthrough: langkah 16, 26), dipulihkan di hook `after`; tidak ada entri Changelog, Event Log, TAG Log, atau batch QR.
- Temuan untuk QA:
  - TC-FA-TAG-70 Expected e ("Tooltip box menerima fokus keyboard") tidak menyebut kapan fokus diamati; spec mengasersinya saat walkthrough baru terbuka.
  - TC-FA-TAG-70 Post Condition ("Flag seen tersimpan pada akun") diasersi lewat langkah 18 karena sudah ada pada Expected d; mekanisme pembacaan flag tidak didefinisikan di TC, PRD, atau LLD.
  - TC-FA-TAG-74 Expected a ("tanpa menetapkan flag seen") membutuhkan pembacaan flag; langkah 23 memakai kemampuan baca flag yang disediakan tim FE/BE, dan muat ulang pada langkah 24 menjadi bukti tak langsung (Expected b).
  - TC-FA-TAG-74 tidak menyebut ukuran viewport target saat diubah; spec menyerahkannya ke tahap script.
