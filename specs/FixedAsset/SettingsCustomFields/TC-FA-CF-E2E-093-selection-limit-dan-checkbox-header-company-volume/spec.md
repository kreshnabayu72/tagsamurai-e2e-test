---
id: TC-FA-CF-E2E-093-selection-limit-dan-checkbox-header-company-volume
title: "Selection Limit dan Checkbox Header pada Company Volume"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-345
  - TC-FA-CF-346
  - TC-FA-CF-631
  - TC-FA-CF-632
coverage:
  web: automated
---

# Selection Limit dan Checkbox Header pada Company Volume

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah Selection Limit Company Volume (state global) dan memakai dataset volume 120 field.
- Akun aktor: Total Control Company Volume (Pre-setup #20), kredensial `Spectra.env.FA_TC_VOLUME_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Company Volume (Pre-setup #20; kelas volume data): 120 field Inactive pada tab General, `Volume Field 001` sampai `Volume Field 120` (Scope General), ukuran halaman default 10 sehingga 12 halaman. Dataset diseed oleh hook `before` lewat seed reset Company (disediakan tim FE/BE; fixture baru `Fixture.faCustomFields.volume`); semua field Inactive dan tidak diubah spec ini sehingga spec ini tidak menulis log.
- State global (Pre-setup #34): Selection Limit Company Volume diturunkan ke 100 (minimum) di Lifecycle Settings > System Limits oleh hook `before` (kemampuan disediakan tim FE/BE); hook `after` memulihkan nilai awalnya.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: mencentang baris tabel satu per satu (100 klik pada langkah 21); memindahkan halaman Pagination; hover untuk membaca tooltip; jeda pendek 10 detik pada langkah 34 untuk mengamati toast persisten (dinyatakan eksplisit; di bawah 30 detik).

## Test Steps

### TC-FA-CF-631: Checkbox header hanya memilih dan membatalkan baris halaman aktif

1. Klik checkbox header pada halaman 1
2. Verifikasi sepuluh baris halaman 1 tercentang
3. Verifikasi Bulk Action Bar menampilkan `10 custom fields selected`
4. Pindah ke halaman 2
5. Verifikasi tidak ada baris tercentang pada halaman 2
6. Verifikasi checkbox header unchecked
7. Kembali ke halaman 1
8. Klik checkbox header lagi
9. Verifikasi sepuluh centang pada halaman 1 dibatalkan
10. Verifikasi Bulk Action Bar hilang

### TC-FA-CF-632: Checkbox header berstatus indeterminate

11. Centang satu baris pada halaman 1
12. Verifikasi checkbox header berstatus indeterminate (ikon strip minus)
13. Verifikasi counter Bulk Action Bar `1 custom field selected`
14. Centang sembilan baris lainnya pada halaman 1
15. Verifikasi checkbox header berstatus checked
16. Hapus centang satu baris
17. Verifikasi checkbox header kembali berstatus indeterminate
18. Verifikasi counter Bulk Action Bar `9 custom fields selected`
19. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-345: Seleksi manual ke-101 diblok live

20. Pilih ukuran halaman 100 pada Pagination
21. Centang baris satu per satu dari baris ke-1 sampai baris ke-100 pada halaman 1
22. Pindah ke halaman 2
23. Coba centang baris pertama pada halaman 2 (baris ke-101)
24. Arahkan kursor ke checkbox baris ke-101
25. Verifikasi checkbox baris ke-101 disabled dengan tooltip `You've reached the maximum selection of 100 rows.`
26. Verifikasi seleksi 100 baris yang sudah dicentang tetap terpilih (Bulk Action Bar menampilkan `100 custom fields selected`)
27. Verifikasi Bulk Action Bar tetap aktif
28. Klik icon `[✕]` pada Bulk Action Bar

### TC-FA-CF-346: Select All melebihi Selection Limit di-cap ke 100 baris

29. Centang satu baris
30. Klik `Select All (120 records)`
31. Verifikasi hanya 100 baris pertama terpilih
32. Verifikasi Bulk Action Bar tetap muncul
33. Verifikasi toast error `Error, only the first 100 of 120 rows were selected. Narrow your filter to include the rest.` tampil
34. Tunggu 10 detik tanpa menyentuh toast
35. Verifikasi toast error dari langkah 33 masih tampil (bertahan sampai di-dismiss)
36. Dismiss toast error dari langkah 33

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec berada di sekitar 35 langkah (36 langkah). Seluruhnya satu kelas (volume data) dan satu dataset Company Volume dengan Selection Limit 100; empat blok berdiri sendiri dan tidak menulis data.
- Urutan TC dalam spec: 631 dan 632 (ukuran halaman default 10), lalu 345 dan 346 (ukuran halaman 100). Urutan menyimpang dari urutan TC sumber (345, 346, 631, 632) karena TC-FA-CF-631 dan TC-FA-CF-632 mensyaratkan ukuran halaman 10 ("120 field, page size 10") sedangkan TC-FA-CF-345 membutuhkan 100 baris dalam satu halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 dan 7 (pindah halaman, aksi TC-FA-CF-631), langkah 19 dan 28 (membersihkan seleksi; S-09), langkah 20 (ukuran halaman 100 agar 100 baris pertama terpilih dalam satu halaman; TC tidak menyebut ukuran halaman), langkah 22 (pindah ke halaman 2 untuk mencapai baris ke-101), langkah 24 (hover untuk menampilkan tooltip, diasersi tepat setelahnya pada langkah 25), langkah 34 (jeda untuk mengamati toast persisten), dan langkah 36 (dismiss toast).
- Asersi tambahan di luar Expected TC (S-03): langkah 26 menyebut counter `100 custom fields selected` sebagai cara mengamati "seleksi 1 sampai 100 tetap tercentang" dari halaman 2 (format counter dari TC-FA-CF-631 dan TC-FA-CF-632).
- Temuan untuk QA:
  - TC-FA-CF-345 langkah 1 ("Centang baris satu per satu sampai 100") tidak menyebut ukuran halaman; spec memakai ukuran halaman 100 (opsi Pagination) agar 100 baris berada dalam satu halaman, dan baris ke-101 berada di halaman 2.
  - TC-FA-CF-346 Expected butir b "bertahan sampai di-dismiss" tidak menyebut durasi pengamatan; spec memakai jeda 10 detik (pilihan spec) sebelum mengasersi toast masih tampil.
  - TC-FA-CF-632 langkah 2 ("sembilan baris lainnya") tidak menyebut halaman; spec memakai halaman 1.
  - Email akun Total Control Company Volume tidak ada di Pre-setup TC.
