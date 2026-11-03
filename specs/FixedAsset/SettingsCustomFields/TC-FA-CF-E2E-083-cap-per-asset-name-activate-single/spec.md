---
id: TC-FA-CF-E2E-083-cap-per-asset-name-activate-single
title: "Cap Per Asset Name: Activate Single Ditolak di Atas Batas, Diterima di Batas, Scope Kosong, dan Kuota Dibebaskan Deactivate"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-309
  - TC-FA-CF-310
  - TC-FA-CF-311
  - TC-FA-CF-626
coverage:
  web: automated
---

# Cap Per Asset Name: Activate Single Ditolak di Atas Batas, Diterima di Batas, Scope Kosong, dan Kuota Dibebaskan Deactivate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah status field Company Cap dan membaca log permanen yang dibagi suite.
- Akun aktor: Total Control Company Cap (Pre-setup #16; pengguna Sarah Johnson, Modified By `Sarah J`), kredensial `Spectra.env.FA_TC_CAP_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Company Cap (Pre-setup #16; Max custom fields per asset name 2), tab General tujuh baris dalam satu halaman. Asset Name `Compressor`, `Generator`, `Pump`, `Turbine`. Active: `Cap General` (General), `Cap Pump` ({Pump}), `Cap Compressor` ({Compressor}). Inactive: `Cap Pump Inactive` ({Pump}), `Cap Gen Inactive` ({Generator}), `Cap Both Inactive` ({Compressor, Generator}), `Cap Orphan` (Scope kosong). Hitungan Active awal: `Pump` 2, `Compressor` 2, `Generator` 1, `Turbine` 1. Hook `before` memulihkan baseline lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.cap`).
- Data Dinamis (dibuat spec ini lewat UI pada langkah 28 sampai 32): field `Cap Pump Free {runId}-083` (Text, Scope `Specific Asset Name` dengan `Pump`). Cleanup: hook `after` menghapus field bersuffix `{runId}-083` yang masih ada lewat API tanpa mengandalkan langkah 32 berhasil; seed reset Company membersihkan sisanya.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membaca jumlah entri Modal Changelog, System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log), dan Activity Log (Reports & Logs > Activity Log > Tab User Action) sebagai baseline (disediakan tim FE/BE; hanya selisih terhadap baseline yang diasersi); membaca hitungan field Active per Asset Name dan Scope sebuah field (disediakan tim FE/BE; TC tidak memberi cara cek, lihat Temuan untuk QA).
- State global: Max custom fields per asset name 2 pada Company Cap (nilai baseline Company; tidak diubah spec ini) dan flag Guided Tooltip (dipulihkan hook `after`).

## Test Steps

### Baseline log

1. Catat jumlah entri awal pada Modal Changelog, System Log aktor, dan Activity Log sebagai baseline (aksi baca tanpa `Verifikasi`)

### TC-FA-CF-309: Activate single yang membuat Asset Name melebihi cap ditolak

2. Geser switch Active baris `Cap Pump Inactive` ke ON
3. Klik `[Activate]`
4. Verifikasi dialog blok 🔒 `Limit Reached` dengan teks `You've reached the limit of 2 custom fields for Pump. Deactivate or delete another field, or contact support if you need a higher limit.` tampil
5. Klik `[OK]`
6. Verifikasi switch Active baris `Cap Pump Inactive` kembali ke posisi OFF sehingga status tidak berubah
7. Klik icon Changelog
8. Verifikasi jumlah entri Modal Changelog sama dengan baseline langkah 1 (tidak ada entri dari langkah 3)
9. Tutup modal Changelog dengan `✕`
10. Buka System Log aktor (Settings > User > Detail pengguna aktor > Tab System Log)
11. Verifikasi jumlah entri System Log aktor sama dengan baseline langkah 1 (tidak ada entri dari langkah 3)
12. Buka Activity Log (Reports & Logs > Activity Log > Tab User Action)
13. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 1 (tidak ada entri dari langkah 3)
14. Buka Fixed Asset > Settings > Custom Fields (tab General)

### TC-FA-CF-310: Activate single tepat di batas cap diterima

15. Geser switch Active baris `Cap Gen Inactive` ke ON
16. Klik `[Activate]`
17. Verifikasi toast sukses `Success, custom field has been activated.` tampil
18. Verifikasi `Generator` memiliki 2 field Active dari cap 2

### TC-FA-CF-311: Activate field ber-Scope kosong tidak dihitung ke cap

19. Tunggu toast dari langkah 17 hilang otomatis
20. Geser switch Active baris `Cap Orphan` ke ON
21. Klik `[Activate]` pada dialog
22. Verifikasi toast sukses `Success, custom field has been activated.` tampil
23. Verifikasi dialog `Limit Reached` tidak tampil
24. Verifikasi Scope field `Cap Orphan` yang Active tetap `—`

### TC-FA-CF-626: Deactivate membebaskan kuota cap per Asset Name

25. Geser switch Active baris `Cap Pump` ke OFF
26. Klik `[Deactivate]`
27. Verifikasi `Pump` memiliki 1 field Active
28. Klik `[+ Custom Field]`
29. Isi Field Name `Cap Pump Free {runId}-083`
30. Pilih Data Type `Text`
31. Pilih Scope `Specific Asset Name` dengan `Pump`
32. Klik `[Submit]`
33. Verifikasi toast sukses `Success, custom field has been created.` tampil
34. Verifikasi dialog `Limit Reached` tidak tampil

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 309 (penolakan tanpa perubahan data) lebih dulu, lalu 310, 311, 626 (aksi yang mengubah data); sama dengan urutan TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline log), langkah 7, 10, dan 12 (membuka surface log), langkah 9 (menutup modal Changelog), langkah 14 (kembali ke layar Custom Fields), dan langkah 19 (menunggu toast sukses lama hilang otomatis supaya toast pada langkah 22 adalah toast hasil langkah 21). Tabel Company Cap tujuh baris berada di satu halaman sehingga Search tidak diperlukan.
- P-1: asersi "tidak ada entri log" TC-FA-CF-309 (langkah 8, 11, dan 13) berada di spec ini karena bergantung pada state cap penuh Company Cap yang dipakai langkah 2 sampai 5; dipenuhi dengan baseline jumlah entri (langkah 1; S-12).
- Asersi tambahan di luar Expected TC (S-03): langkah 6 menulis "switch kembali ke OFF" dan "status tidak berubah" TC-FA-CF-309 butir b sebagai satu `Verifikasi` karena status Inactive hanya teramati lewat switch; langkah 34 memecah "tanpa dialog `Limit Reached`" TC-FA-CF-626 butir b menjadi `Verifikasi` sendiri (anchor toast sukses di langkah 33).
- Nama field Dinamis `Cap Pump Free` (Pre-setup Dinamis #8) memakai suffix `{runId}-083` (S-12).
- Temuan untuk QA:
  - TC-FA-CF-310, 311, dan 626 mengasersi hitungan field Active per Asset Name dan Scope field tanpa menyebut cara memeriksanya di UI; spec memakai kemampuan baca "disediakan tim FE/BE" tanpa endpoint karangan (S-11).
  - TC-FA-CF-626 tidak menyebut kondisi Required lain pada modal Create (hanya Field Name dan Data Type); spec mengikuti TC.
  - TC-FA-CF-311 langkah 2 "Klik `[Activate]` pada dialog" tidak punya Expected untuk dialog konfirmasi; dialog tidak diasersi.
  - Email akun Total Control Company Cap tidak ada di Pre-setup TC.
  - TC-FA-CF-309 dan 310 dijalankan pada field Inactive seed `Cap Pump Inactive` dan `Cap Gen Inactive`; TC-FA-CF-310 mensyaratkan `Generator` hanya memiliki 1 field Active sebelum aksi (benar pada baseline Pre-setup #16 dan tidak berubah oleh TC-FA-CF-309).
