---
id: TC-FA-CF-E2E-084-cap-per-asset-name-bulk-activate-dan-delete
title: "Cap Per Asset Name: Bulk Activate Ditolak Tanpa Perubahan Sebagian, Hitungan Kumulatif, dan Delete Membebaskan Kuota"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-343
  - TC-FA-CF-344
  - TC-FA-CF-323
coverage:
  web: automated
---

# Cap Per Asset Name: Bulk Activate Ditolak Tanpa Perubahan Sebagian, Hitungan Kumulatif, dan Delete Membebaskan Kuota

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah data field Company Cap dan membaca log permanen yang dibagi suite.
- Akun aktor: Total Control Company Cap (Pre-setup #16; pengguna Sarah Johnson, Modified By `Sarah J`), kredensial `Spectra.env.FA_TC_CAP_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Company Cap (Pre-setup #16; Max custom fields per asset name 2), tab General tujuh baris dalam satu halaman. Active: `Cap General` (General), `Cap Pump` ({Pump}), `Cap Compressor` ({Compressor}). Inactive: `Cap Pump Inactive` ({Pump}), `Cap Gen Inactive` ({Generator}), `Cap Both Inactive` ({Compressor, Generator}), `Cap Orphan` (Scope kosong). Hitungan Active awal: `Pump` 2, `Compressor` 2, `Generator` 1, `Turbine` 1. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.cap`). Spec ini menghapus `Cap Pump` (langkah 28) sehingga dipulihkan hook `after`.
- Data Dinamis (dibuat spec ini lewat UI pada langkah 29 sampai 33): field `Cap Pump Free {runId}-084` (Text, Scope `Specific Asset Name` dengan `Pump`). Cleanup: hook `after` menghapus field bersuffix `{runId}-084` yang masih ada lewat API tanpa mengandalkan langkah 33 berhasil.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membaca jumlah entri Modal Changelog, System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log), dan Activity Log (Reports & Logs > Activity Log > Tab User Action) sebagai baseline (disediakan tim FE/BE; hanya selisih terhadap baseline yang diasersi).
- State global: Max custom fields per asset name 2 pada Company Cap (nilai baseline Company; tidak diubah spec ini) dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### Baseline log

1. Catat jumlah entri awal pada Modal Changelog, System Log aktor, dan Activity Log sebagai baseline (aksi baca tanpa `Verifikasi`)

### TC-FA-CF-343: Bulk Activate yang membuat Asset Name melebihi cap dibatalkan seluruhnya

2. Centang baris `Cap Pump Inactive` dan `Cap Gen Inactive`
3. Klik `[Activate]` pada Bulk Action Bar
4. Klik `[Activate]` pada dialog
5. Verifikasi dialog `Limit Reached` varian Activate tampil dengan nama `Pump`
6. Klik `[OK]`
7. Verifikasi dialog konfirmasi tertutup
8. Verifikasi seleksi `Cap Pump Inactive` dan `Cap Gen Inactive` dipertahankan
9. Verifikasi Bulk Action Bar dipertahankan
10. Verifikasi tidak ada field yang berubah: switch `Cap Pump Inactive` dan `Cap Gen Inactive` tetap OFF
11. Klik icon Changelog
12. Verifikasi jumlah entri Modal Changelog sama dengan baseline langkah 1 (tidak ada entri dari langkah 4)
13. Tutup modal Changelog dengan `✕`
14. Buka System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log)
15. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 1 (tidak ada entri dari langkah 4)
16. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
17. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 1 (tidak ada entri dari langkah 4)
18. Buka Fixed Asset > Settings > Custom Fields (tab General)

### TC-FA-CF-344: Field Inactive terpilih dihitung kumulatif per Asset Name

19. Centang baris `Cap Gen Inactive` dan `Cap Both Inactive`
20. Klik `[Activate]` pada Bulk Action Bar
21. Klik `[Activate]` pada dialog
22. Verifikasi dialog `Limit Reached` varian Activate tampil dengan teks `You've reached the limit of 2 custom fields for Compressor and Generator. Deactivate or delete another field, or contact support if you need a higher limit.`
23. Verifikasi `Generator` disebut pada teks dialog bersama `Compressor` karena dihitung kumulatif (1 Active ditambah 2 field terpilih melebihi cap 2)
24. Klik `[OK]`
25. Verifikasi tidak ada field yang berubah: switch `Cap Gen Inactive` dan `Cap Both Inactive` tetap OFF

### TC-FA-CF-323: Delete field membebaskan kuota cap per Asset Name

26. Klik icon `[✕]` pada Bulk Action Bar
27. Klik row action `⋯` > `Delete` pada baris `Cap Pump`
28. Klik `[Delete]` pada dialog
29. Klik `[+ Custom Field]`
30. Isi Field Name `Cap Pump Free {runId}-084`
31. Pilih Data Type `Text`
32. Pilih Scope `Specific Asset Name` dengan `Pump`
33. Klik `[Submit]`
34. Verifikasi toast sukses `Success, custom field has been created.` tampil
35. Verifikasi dialog `Limit Reached` tidak tampil

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 343 dan 344 (penolakan tanpa perubahan data), lalu 323 (aksi Delete, paling akhir; S-10). Urutan menyimpang dari urutan TC sumber (323, 343, 344) supaya baseline log (langkah 1) dan state cap penuh `Pump` belum berubah oleh Delete.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline log), langkah 11, 14, dan 16 (membuka surface log), langkah 13 (menutup modal Changelog), langkah 18 (kembali ke layar Custom Fields, yang juga membersihkan seleksi), dan langkah 26 (membersihkan seleksi TC-FA-CF-344). Tabel Company Cap tujuh baris berada di satu halaman sehingga Search tidak diperlukan.
- P-1: asersi "tidak ada entri log" TC-FA-CF-343 (langkah 12, 15, dan 17) berada di spec ini karena bergantung pada state cap penuh dan seleksi dua baris yang dibangun langkah 2 sampai 6; dipenuhi dengan baseline jumlah entri (langkah 1; S-12).
- Asersi tambahan di luar Expected TC (S-03): langkah 24 (`[OK]`) menutup dialog `Limit Reached` TC-FA-CF-344 agar langkah 25 dapat membaca switch; TC tidak menyebut cara menutup dialog itu. Langkah 23 menuliskan butir b TC-FA-CF-344 (alasan hitungan kumulatif) sebagai `Verifikasi` atas teks dialog langkah 22.
- Spec berada di sekitar 35 langkah (35 langkah). Seluruhnya satu topik (cap per Asset Name pada aksi bulk dan Delete) dan satu dataset Company Cap; tujuh langkah pembacaan log (langkah 11 sampai 17) hanya diperlukan satu kali untuk TC-FA-CF-343.
- Temuan untuk QA:
  - TC-FA-CF-343 Expected butir a tidak menyebut teks dialog `Limit Reached` selain "dengan nama `Pump`"; spec mengasersi varian dan nama sesuai TC.
  - TC-FA-CF-323 tidak menyebut Field Name, Data Type, maupun kriteria sukses Create selain "sukses"; spec memakai `Cap Pump Free {runId}-084` bertipe `Text` dan toast `Success, custom field has been created.` (teks dari TC-FA-CF-626).
  - TC-FA-CF-344 Expected butir b adalah penjelasan alasan; teramati hanya lewat teks dialog.
  - Email akun Total Control Company Cap tidak ada di Pre-setup TC.
