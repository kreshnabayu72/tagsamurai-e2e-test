---
id: TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan
title: "Delete Diblok: Aset Aktif di Node dan Descendant, Aset Draft/Waiting for Approval, dan Guard Pertama yang Terpenuhi Menentukan Dialog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-229
  - TC-FA-GRP-230
  - TC-FA-GRP-231
  - TC-FA-GRP-238
coverage:
  web: automated
---

# Delete Diblok: Aset Aktif di Node dan Descendant, Aset Draft/Waiting for Approval, dan Guard Pertama yang Terpenuhi Menentukan Dialog

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Pre-setup (Tabel A, No 9; hanya dibaca, dialog blokir tidak menghapus apa pun): `Warehouse A` (24 aset aktif) dan `Head Office` (aset aktif di cucu `IT Department`).
- Data Dinamis (di-seed lewat API di `before`): `Del Draft` dengan 1 aset Draft dan 1 aset Waiting for Approval; `Del Multi` dengan aset aktif dan sekaligus menjadi tujuan transfer yang belum tuntas (Waiting for Approval). Seeding aset dan transfer berat; aset dan transfer dibersihkan lewat fixture BE di `after` sebelum `Del Draft` dan `Del Multi` dihapus.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group sebelum dan sesudah aksi (audit trail permanen, tidak dapat diturunkan dari seeding; 8b butir 10) lewat fixture BE atau pembacaan UI.
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12). N1 dicatat pada langkah 16 (sebelum aksi TC-FA-GRP-230) dan N2 pada langkah 29 (sebelum aksi TC-FA-GRP-231), saat Modal Changelog: Group masih terbuka sesudah pembacaan blok sebelumnya (S-12).

## Test Steps

### Baseline Changelog

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group

### TC-FA-GRP-229: Aset aktif di node (Warehouse A)

5. Ketik Search `Warehouse A`, tekan Enter
6. Buka elipsis `⋯` baris `Warehouse A`, pilih `Delete`
7. Verifikasi dialog dengan title "Cannot Delete Group"
8. Verifikasi isi dialog "This group or its subgroups still hold assets. Transfer or dispose them first."
9. Verifikasi dialog hanya memuat tombol [OK]
10. Klik [OK]
11. Verifikasi dialog tertutup
12. Verifikasi `Warehouse A` tetap ada di tabel (tidak ada yang terhapus)
13. Verifikasi tidak ada toast yang tampil
14. Buka Modal Changelog: Group
15. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
16. Catat jumlah entri Modal Changelog: Group sebagai baseline N1 (jumlah total pada footer pagination)
17. Tutup Modal Changelog: Group

### TC-FA-GRP-230: Aset aktif di descendant (Head Office)

18. Ganti isi kotak Search dengan `Head Office`, tekan Enter
19. Buka elipsis `⋯` baris `Head Office`, pilih `Delete`
20. Verifikasi dialog dengan title "Cannot Delete Group"
21. Verifikasi isi dialog "This group or its subgroups still hold assets. Transfer or dispose them first."
22. Verifikasi dialog hanya memuat tombol [OK]
23. Klik [OK]
24. Verifikasi dialog tertutup
25. Verifikasi `Head Office` tetap ada di tabel (tidak ada yang terhapus)
26. Verifikasi tidak ada toast yang tampil
27. Buka Modal Changelog: Group
28. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N1
29. Catat jumlah entri Modal Changelog: Group sebagai baseline N2 (jumlah total pada footer pagination)
30. Tutup Modal Changelog: Group

### TC-FA-GRP-231: Aset Draft/Waiting for Approval dihitung aktif (Del Draft)

31. Ganti isi kotak Search dengan `Del Draft`, tekan Enter
32. Buka elipsis `⋯` baris `Del Draft`, pilih `Delete`
33. Verifikasi dialog dengan title "Cannot Delete Group"
34. Verifikasi isi dialog "This group or its subgroups still hold assets. Transfer or dispose them first."
35. Verifikasi dialog hanya memuat tombol [OK]
36. Klik [OK]
37. Verifikasi dialog tertutup
38. Verifikasi `Del Draft` tetap ada di tabel (tidak ada yang terhapus)
39. Verifikasi tidak ada toast yang tampil
40. Buka Modal Changelog: Group
41. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N2
42. Tutup Modal Changelog: Group

### TC-FA-GRP-238: Guard pertama yang terpenuhi menentukan dialog (Del Multi)

43. Ganti isi kotak Search dengan `Del Multi`, tekan Enter
44. Buka elipsis `⋯` baris `Del Multi`, pilih `Delete`
45. Verifikasi isi dialog "This group or its subgroups still hold assets. Transfer or dispose them first." (guard aset lebih dulu dari guard tujuan transfer)
46. Klik [OK]

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 14, 17, 27, 30, 40, 42, 46: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 5, 18, 31, 43 (Ketik atau ganti isi kotak Search dengan `Warehouse A`, `Head Office`, `Del Draft`, dan `Del Multi`, tekan Enter) menemukan baris yang dibuka elipsisnya; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: seluruh TC memblokir sehingga tidak ada aksi yang menghapus data; kondisi data berbeda per blok (prinsip 12). TC-238 terakhir karena tidak punya Expected log.
- Klausa "tanpa toast & log" tiap blok diasersi dengan baseline jumlah entri (langkah 13 dan 15 untuk TC-229, 23 dan 25 untuk TC-230, 34 dan 36 untuk TC-231); anchor positif: langkah 2 (entri lain tampil) dan node tetap ada (langkah 12, 25, 38). Butir `P-1`: seeding berat (aset dan transfer) membuat asersi log TC-231 tetap berada di spec ini dan memakai baseline.
- Spec berisi lebih dari 35 langkah (empat blok blokir). Alasan: seluruhnya satu kelas dan satu topik (Delete diblok kondisi data), tiap blok berdiri sendiri dan bergantung pada data berbeda, dan tiga blok baca-log berpola (buka Modal Changelog, Verifikasi jumlah, tutup) tidak dihitung menurut bagian 3 prinsip 13.
- Temuan untuk QA:
  - TC-229 sampai TC-231 menyebut "tanpa toast & log" tanpa menyebut surface log; spec memakai Modal Changelog: Group.
  - TC-238 tidak punya klausa tombol atau log pada Expected; spec hanya mengasersi isi dialog.
