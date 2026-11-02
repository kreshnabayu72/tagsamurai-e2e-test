---
id: TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali
title: "Fallback T-0: Group Terlama Tetap Usable, Tie-Break Nama A-Z, Seleksi Kosong karena Group Dihapus, Fallback Tidak Jalan Setelah Submit, dan Plan Naik Auto-Reset Excess"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-310
  - TC-FA-GRP-311
  - TC-FA-GRP-318
  - TC-FA-GRP-319
  - TC-FA-GRP-964
coverage:
  web: automated
---

# Fallback T-0: Group Terlama Tetap Usable, Tie-Break Nama A-Z, Seleksi Kosong karena Group Dihapus, Fallback Tidak Jalan Setelah Submit, dan Plan Naik Auto-Reset Excess

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Data Dinamis (di-seed ulang per blok lewat fixture BE, kosong tanpa aset): blok TC-310 dan TC-318: enam group `G1` (terlama) sampai `G6` dibuat berurutan; blok TC-311: empat group `delta`, `Alpha`, `charlie`, `Bravo` dibuat pada timestamp sama, cap 2; blok TC-319: tiga group berstatus Excess; blok TC-964: enam group termasuk `Sel Del A` dan `Sel Del B` (tanpa aset aktif) dengan seleksi tersimpan berisi keduanya. Seleksi Wizard tersimpan dikosongkan di `before` (fixture BE, disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group, Activity Log, dan System Log aktor sebelum dan sesudah aksi (audit trail permanen; 8b butir 10).
- Jam server dan jam browser sinkron; Date entri log dibandingkan dengan waktu yang dicatat sesudah transaksi T-0 commit dengan toleransi satu menit (S-12).
- Baseline log: S0 = jumlah entri System Log akun aktor yang dicatat pada langkah 22, sebelum aksi pemicu pertama yang diasersi TC-964 (S-12). Pemicu T-0 (perubahan cap langsung, T-0 = saat disimpan, atau hook uji) dan perubahan plan di Admin Console disediakan tim FE/BE tanpa endpoint karangan.

## Test Steps

### TC-FA-GRP-310: Client belum pernah submit, group terlama tetap usable

1. Seed: enam group `G1` sampai `G6` dibuat berurutan, downgrade ke cap 3, belum submit Wizard
2. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
3. Buka Fixed Asset > Settings > Groups
4. Verifikasi `G1`, `G2`, dan `G3` usable (tidak di-dim)
5. Verifikasi `G4`, `G5`, dan `G6` (terbaru) berstatus Excess (di-dim)

### TC-FA-GRP-311: Waktu pembuatan sama, tie-break Group Name A-Z case-insensitive

6. Seed ulang: empat group `delta`, `Alpha`, `charlie`, `Bravo` pada timestamp sama, cap 2, belum submit
7. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
8. Buka Fixed Asset > Settings > Groups
9. Verifikasi `Alpha` dan `Bravo` usable
10. Verifikasi `charlie` dan `delta` berstatus Excess

### TC-FA-GRP-318: Fallback tidak berjalan bila client sudah submit Wizard

11. Seed ulang: enam group `G1` sampai `G6`, seleksi tersimpan `G4`, `G5`, `G6` (bukan terlama)
12. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
13. Buka Fixed Asset > Settings > Groups
14. Verifikasi `G4`, `G5`, dan `G6` usable sesuai seleksi
15. Verifikasi `G1`, `G2`, dan `G3` berstatus Excess (bukan urutan waktu pembuatan)

### TC-FA-GRP-319: Plan naik lagi, auto-reset seluruh Excess

16. Seed ulang: tiga group berstatus Excess
17. Simpan perubahan plan (upgrade ke Professional) di Admin Console
18. Buka Fixed Asset > Settings > Groups
19. Verifikasi seluruh node kembali usable (tidak di-dim)
20. Verifikasi aksi `Edit` dan `Add Subgroup` tampil pada node

### TC-FA-GRP-964: Seleksi tersimpan kosong karena group tercentang dihapus sebelum T-0

21. Seed ulang: enam group termasuk `Sel Del A` dan `Sel Del B`, seleksi tersimpan berisi keduanya
22. Catat jumlah entri System Log akun aktor sebagai baseline S0 (kemampuan baca disediakan tim FE/BE)
23. Buka elipsis `⋯` baris `Sel Del A`, pilih `Delete`
24. Klik [Delete]
25. Tunggu aksi selesai
26. Buka elipsis `⋯` baris `Sel Del B`, pilih `Delete`
27. Klik [Delete]
28. Tunggu aksi selesai
29. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
30. Catat waktu sesudah transaksi T-0 commit
31. Buka Fixed Asset > Settings > Groups
32. Verifikasi seleksi tersimpan dibuang (kosong) sehingga diperlakukan belum pernah submit (dibaca lewat fixture BE)
33. Verifikasi tiga group terlama usable
34. Verifikasi satu group terbaru berstatus Excess
35. Buka Modal Changelog: Group, lalu ketik Search nama group terbaru, tekan Enter
36. Verifikasi entri Action `Marked as Excess (Group Consolidation)` untuk group terbaru dengan Modified By = System
37. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group
38. Verifikasi entri Activity Log `Marked as Excess (Group Consolidation)` untuk group terbaru dengan Modified By = System (dibaca lewat kemampuan baca)
39. Verifikasi jumlah entri System Log akun aktor sama dengan baseline S0 (tanpa System Log)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 sampai 3, 6 sampai 8, 11 sampai 13, 16 sampai 18, 21 dan 22, 25, 28 sampai 31, 35, 37: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Seeding ulang antar blok memulihkan state tiap TC (S-09). Seluruh blok kelas h dengan pemicu T-0 yang sama; pemicu bukan objek uji.
- P-1 (state berat): TC-964 membangun seleksi tersimpan dan menghapus dua group sebelum T-0; asersi "tanpa System Log" (S-05) memakai baseline S0 dan anchor positif: entri Changelog dan Activity Log milik group terbaru tampil (langkah sebelum asersi System Log, 8b butir 2).
- Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (h, penerapan T-0 dan fallback) dan berdiri sendiri dengan state seed berbeda; sekitar 16 langkah adalah penghubung seeding, pemicu T-0, dan pembacaan log berpola, bukan asersi baru.
- Temuan untuk QA:
  - TC-310 dan TC-319 Post Condition (Changelog Marked/Restored, Modified By System, tanpa System Log) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-311 dan TC-318 Precondition tidak menyebut cara men-seed timestamp sama dan seleksi tersimpan; kemampuan fixture BE disediakan tim FE/BE (R-19).
  - TC-964 Expected c menyebut Activity Log tanpa menyebut cara membukanya; spec memakai kemampuan baca disediakan tim FE/BE.
