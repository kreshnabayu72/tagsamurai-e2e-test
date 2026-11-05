---
id: TC-FA-FAAC-E2E-188-volume-selection-limit-dan-5000-baris
title: "Volume Data: Selection Limit pada Seleksi Tabel dan Picker Assign serta Download Lebih dari 5.000 Baris"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-431
  - TC-FA-FAAC-632
  - TC-FA-FAAC-658
  - TC-FA-FAAC-673
coverage:
  web: automated
---

# Volume Data: Selection Limit pada Seleksi Tabel dan Picker Assign serta Download Lebih dari 5.000 Baris

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: Selection Limit (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits, nilai minimum 100), total Asset Class, dan jumlah Asset Name tanpa Asset Class. Pengaturan Selection Limit dan seed volume besar lewat fixture BE "disediakan tim FE/BE" (tanpa akun atau endpoint karangan; TC menulis nilai Selection Limit "dibaca dari Admin Console ... saat TC dijalankan" dan seed volume "disiapkan lewat seed data"). Nilai awal Selection Limit dicatat di hook `before`; hook `after` memulihkannya dan menghapus seed volume.
- Data volume: untuk TC-658 total Asset Class [n] = 101 dengan [Limit] = 100; untuk TC-632 dan TC-431 total Asset Class lebih dari 5.000 (5.001) dengan [Limit] = 100; untuk TC-673 sebanyak 101 Asset Name tanpa Asset Class dengan [Limit] = 100. Nilai [Limit] dan [n] pada TC-632 dibaca lewat kemampuan baca BE sebelum aksi (S-12).
- Data Dinamis milik spec: Asset Class anchor Class Code literal `B-VOL` dan Class Name `Volume Class {runId}-188` (Active, tanpa Asset Name ter-assign; "Asset Class anchor" TC-673), dibuat fixture BE di hook `before` (setelah menghapus sisa run sebelumnya) dan dihapus di hook `after`.
- Kemampuan teknis: pembacaan Selection Limit dan total Asset Class lewat kemampuan baca BE; hover pada checkbox dan membaca tooltip; pembaca berkas unduhan (hanya keberadaan berkas terunduh yang diasersi).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

1. Atur lewat fixture BE Selection Limit = `100` dan total Asset Class = `101`, lalu muat ulang halaman

### TC-FA-FAAC-658: Seleksi lewat checkbox header: checkbox baris berikutnya Disabled setelah Selection Limit tercapai

2. Ubah ukuran halaman tabel menjadi 100
3. Klik checkbox header di halaman 1 sehingga 100 baris tercentang
4. Pindah ke halaman 2
5. Arahkan kursor ke checkbox baris ke-101, lalu coba centang
6. Verifikasi checkbox baris ke-101 Disabled dengan tooltip `You've reached the maximum selection of 100 rows.`
7. Verifikasi checkbox baris ke-101 tidak dapat dicentang
8. Kembali ke halaman 1
9. Verifikasi 100 baris di halaman 1 tetap tercentang
10. Verifikasi Bulk Action Bar tetap tampil dan dapat dipakai untuk 100 baris yang terpilih
11. Klik `Unselect All`

### TC-FA-FAAC-632: Select All melebihi Selection Limit

12. Atur lewat fixture BE total Asset Class menjadi `5001` (lebih besar dari Selection Limit), baca [Limit] dan [n] lewat kemampuan baca BE, lalu muat ulang halaman
13. Klik `Select All` pada tabel Asset Class
14. Verifikasi toast error `Error, only the first [Limit] of [n] rows were selected. Narrow your filter to include the rest.` dengan [Limit] dan [n] berisi nilai yang dibaca
15. Verifikasi hanya [Limit] baris pertama yang terpilih (di-cap otomatis)
16. Verifikasi Bulk Action Bar tetap tampil dan dapat dipakai untuk baris yang terpilih
17. Klik `Unselect All`

### TC-FA-FAAC-431: Download lebih dari 5.000 baris memakai loading screen

18. Klik icon `Download`, lalu pilih `Download as CSV`
19. Verifikasi loading screen tampil sampai berkas siap
20. Verifikasi berkas terunduh langsung

### TC-FA-FAAC-673: Seleksi lewat checkbox header pada picker Assign: checkbox baris berikutnya Disabled setelah Selection Limit tercapai

21. Atur lewat fixture BE Selection Limit = `100` dan jumlah Asset Name tanpa Asset Class = `101`, lalu muat ulang halaman
22. Ketik Search `B-VOL`, tekan Enter
23. Klik link Class Code `B-VOL`, lalu klik tab `Asset Names`
24. Klik tombol `+ Assign Asset Names`
25. Ubah ukuran halaman picker ke 100
26. Klik checkbox header di halaman 1 sehingga 100 baris tercentang
27. Pindah ke halaman 2
28. Arahkan kursor ke checkbox baris ke-101, lalu coba centang
29. Verifikasi checkbox baris ke-101 Disabled dengan tooltip `You've reached the maximum selection of 100 rows.` dan tidak dapat dicentang
30. Kembali ke halaman 1
31. Verifikasi 100 baris di halaman 1 tetap tercentang
32. Klik `[×]` pada dialog Assign

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan nomor TC: volume 101 baris (TC-658) lebih dulu, lalu volume 5.001 baris (TC-632 dan TC-431), lalu picker Asset Name (TC-673), supaya seed volume besar hanya diatur tiga kali (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 12, dan 21 (mengatur Selection Limit dan seed volume); langkah 2 dan 25 (ukuran halaman 100, bagian dari precondition TC-658 dan langkah TC-673); langkah 30 (kembali ke halaman 1 sebelum asersi posisi, S-14; TC-673 tidak menulis langkah ini, TC-658 menulisnya sebagai langkah sendiri); langkah 11 dan 17 (membersihkan seleksi, S-09); langkah 22 (Search untuk menemukan baris target, R-16); langkah 32 (menutup dialog Assign tanpa konfirmasi, picker D-13 menurut TC-154 dan TC-712).
3. Pada TC-431 asersi "loading screen tampil" diletakkan segera setelah pemicu dan sebelum asersi artefak berkas terunduh (8b butir 5 dan 11); TC tidak menahan respons, sehingga ketepatan waktu bergantung pada volume 5.001 baris.
4. Pengecualian kode seed literal (S-06/S-12): TC-632 dan TC-431 membaca tabel Asset Class dengan seed volume; TC-673 memakai Asset Class anchor milik spec. Aksi pada spec ini hanya seleksi; tidak ada data yang diubah, selain state global yang dipulihkan hook `after`.
5. Temuan untuk QA: TC-632 menulis bahwa Selection Limit "bila perlu diturunkan lewat pengaturan itu" tanpa menyebut aktor perubahan; spec memakai fixture BE yang disediakan tim FE/BE. TC-658 mensyaratkan total Asset Class 101 pada client yang sama dengan TC-632 (lebih dari 5.000); spec mengatur total secara berurutan. TC-673 tidak menyebut kembali ke halaman 1 sebelum asersi baris halaman 1 dan tidak menyebut kode Asset Class anchor.
6. Class Code `B-VOL` ditulis literal dan `{runId}-188` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `B-VOL{runId}-188` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu.
