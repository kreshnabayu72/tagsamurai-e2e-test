---
id: TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi
title: "T-0 dan Seleksi Tersimpan: Count <= Cap Dibuang, Group Baru Tidak Tercentang, Group Tercentang Dihapus, Downgrade Dibatalkan, Cap Baru Berubah, dan Penerapan Sync Satu Transaksi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-312
  - TC-FA-GRP-313
  - TC-FA-GRP-314
  - TC-FA-GRP-315
  - TC-FA-GRP-316
  - TC-FA-GRP-317
  - TC-FA-GRP-1051
coverage:
  web: automated
---

# T-0 dan Seleksi Tersimpan: Count <= Cap Dibuang, Group Baru Tidak Tercentang, Group Tercentang Dihapus, Downgrade Dibatalkan, Cap Baru Berubah, dan Penerapan Sync Satu Transaksi

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Data Dinamis (di-seed ulang per blok lewat fixture BE, kosong tanpa aset): blok TC-312 dan TC-1051 memakai group `G1` sampai `G6` dan `Warehouse B`; blok TC-313: seleksi tersimpan 3 group lalu `New After` dibuat sebelum T-0; blok TC-314: seleksi `G1`, `G2`, `G3`, lalu `G3` dihapus sebelum T-0 (count masih di atas cap); blok TC-315 sampai TC-317: seleksi dan cap sesuai blok. Seleksi Wizard tersimpan dan perubahan cap dilakukan fixture BE (disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group, Activity Log, dan System Log aktor sebelum dan sesudah aksi (audit trail permanen; 8b butir 10).
- Jam server dan jam browser sinkron; Date entri log dibandingkan dengan waktu yang dicatat sesudah transaksi T-0 commit dengan toleransi satu menit (S-12).
- Pemicu T-0 (perubahan cap langsung, T-0 = saat disimpan, atau hook uji) dan pembatalan downgrade di Admin Console disediakan tim FE/BE tanpa endpoint karangan. Sesi A (TC-1051) adalah akun hook `before`.

## Test Steps

### TC-FA-GRP-312: Count sudah <= cap, seleksi tersimpan dibuang

1. Seed: seleksi tersimpan tiga group; sebelum T-0 group dihapus sampai count sama dengan cap
2. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
3. Buka Fixed Asset > Settings > Groups
4. Verifikasi sedikitnya satu group tampil di tabel
5. Verifikasi tidak ada group berstatus Excess

### TC-FA-GRP-313: Group dibuat setelah submit diperlakukan tidak dicentang

6. Seed ulang: seleksi tersimpan tiga group, lalu `New After` dibuat sebelum T-0
7. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
8. Buka Fixed Asset > Settings > Groups
9. Verifikasi `New After` berstatus Excess (di-dim)

### TC-FA-GRP-314: Group tercentang yang dihapus sebelum T-0 tidak diisi otomatis

10. Seed ulang: seleksi `G1`, `G2`, `G3`; `G3` dihapus sebelum T-0; count masih di atas cap
11. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
12. Buka Fixed Asset > Settings > Groups
13. Verifikasi hanya `G1` dan `G2` usable
14. Verifikasi slot `G3` tidak diisi group lain (group lain berstatus Excess)

### TC-FA-GRP-315: Downgrade terjadwal dibatalkan, seleksi dibuang

15. Seed ulang: seleksi tersimpan; downgrade dibatalkan di Admin Console
16. Picu hook uji handler plan-efektif pada tanggal T-0 semula (downgrade sudah dibatalkan), tunggu transaksi commit
17. Buka Fixed Asset > Settings > Groups
18. Verifikasi sedikitnya satu group tampil di tabel
19. Verifikasi tidak ada group yang jadi Excess

### TC-FA-GRP-316: Cap baru berubah sebelum T-0, seleksi tetap dipakai bila <= cap baru

20. Seed ulang: seleksi dua group; cap baru berubah dari 3 menjadi 2
21. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
22. Buka Fixed Asset > Settings > Groups
23. Verifikasi seleksi dua group diterapkan (usable)
24. Verifikasi group lain berstatus Excess

### TC-FA-GRP-317: Cap baru berubah sebelum T-0, seleksi di atas cap baru dibuang, fallback berlaku

25. Seed ulang: seleksi tiga group; cap baru berubah dari 3 menjadi 2; tidak submit ulang
26. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
27. Buka Fixed Asset > Settings > Groups
28. Verifikasi dua group terlama usable (fallback; seleksi dibuang)

### TC-FA-GRP-1051: T-0 diterapkan Sync dalam satu transaksi

29. Seed ulang: client di atas cap plan baru; seleksi Wizard tersimpan; `Warehouse B` tidak dicentang
30. Muat ulang Fixed Asset > Settings > Groups di sesi A
31. Verifikasi `Warehouse B` usable di tabel, Group Context Header, dan sidebar sebelum T-0
32. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
33. Muat ulang Fixed Asset > Settings > Groups di sesi A
34. Verifikasi `Warehouse B` berstatus Excess di tabel (nama di-dim)
35. Klik `Warehouse B` di sidebar
36. Verifikasi Group Context Header `Warehouse B` berstatus Excess pada pemuatan yang sama
37. Verifikasi `Warehouse B` berstatus Excess di sidebar pada pemuatan yang sama
38. Buka dropdown tujuan Register Asset
39. Verifikasi `Warehouse B` tetap tampil di dropdown tetapi tidak dapat dipilih
40. Tutup dropdown
41. Verifikasi tidak ada keadaan sebagian: seluruh group tidak tercentang berstatus Excess dan seluruh group tercentang usable di tabel, header, dan sidebar
42. Buka Modal Changelog: Group, lalu ketik Search `{runId}-093`, tekan Enter
43. Verifikasi Modal Changelog memuat entri `Marked as Excess (Group Consolidation)` untuk setiap group yang berubah
44. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group
45. Verifikasi Activity Log memuat entri untuk setiap group yang berubah (dibaca lewat kemampuan baca)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 sampai 3, 6 sampai 8, 10 sampai 12, 15 sampai 17, 20 sampai 22, 25 sampai 27, 29 dan 30, 32 dan 33, 35, 38, 40, 42, 44: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Seeding ulang antar blok memulihkan state tiap TC (S-09). Seluruh blok kelas h dengan pemicu T-0 yang sama; pemicu bukan objek uji. Asersi absence Excess (TC-312, TC-315) didahului verifikasi group lain tampil (anchor, 8b butir 2).
- Spec berisi lebih dari 35 langkah. Alasan: tujuh blok satu kelas (h, penerapan T-0 atas seleksi tersimpan) dan berdiri sendiri dengan state seed berbeda; sebagian besar langkah adalah penghubung seeding dan pemicu T-0, bukan asersi baru.
- Langkah 31 dan 34 membandingkan tampilan sebelum dan sesudah T-0 pada sesi A (TC-1051 langkah 1 sampai 3).
- Temuan untuk QA:
  - TC-312 sampai TC-317 tidak menyebut cara men-seed seleksi tersimpan, penghapusan group, dan perubahan cap sebelum T-0 selain di Precondition; kemampuan fixture BE disediakan tim FE/BE (R-19).
  - TC-1051 Expected d menyebut Modal Changelog dan Activity Log "untuk setiap node yang berubah" tanpa jumlah; spec mengasersi entri per group yang berubah.
  - TC-1051 tidak menyebut sesi A selain Langkah 1; spec memakai satu sesi A.
