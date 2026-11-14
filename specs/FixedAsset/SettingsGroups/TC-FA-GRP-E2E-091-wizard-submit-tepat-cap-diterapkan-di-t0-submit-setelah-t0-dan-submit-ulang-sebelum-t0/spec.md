---
id: TC-FA-GRP-E2E-091-wizard-submit-tepat-cap-diterapkan-di-t0-submit-setelah-t0-dan-submit-ulang-sebelum-t0
title: "Wizard: Submit Tepat Cap Diterapkan di T-0, Submit Setelah T-0 Langsung Diterapkan, dan Submit Ulang Sebelum T-0"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-303
  - TC-FA-GRP-305
  - TC-FA-GRP-306
coverage:
  web: automated
---

# Wizard: Submit Tepat Cap Diterapkan di T-0, Submit Setelah T-0 Langsung Diterapkan, dan Submit Ulang Sebelum T-0

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group, Activity Log, dan System Log aktor sebelum dan sesudah aksi (audit trail permanen; 8b butir 10).
- Jam server dan jam browser sinkron; Date entri log dibandingkan dengan waktu yang dicatat sesudah transaksi T-0 commit dengan toleransi satu menit (S-12).
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12). N1 dan A1 = jumlah entri Modal Changelog: Group dan Activity Log yang dicatat pada langkah 39, sebelum pemicu T-0 TC-FA-GRP-306 (S-12).
- Pembacaan dropdown tujuan Register Asset (Expected c TC-303): dropdown assignment baru diwakili dropdown tujuan Register Asset; TC tidak menyebut dropdown mana (lihat Temuan untuk QA).

## Test Steps

### Baseline Changelog

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group

### TC-FA-GRP-303: Submit tepat cap, diterapkan di T-0

5. Buka Wizard Reconciliation > Step Group Consolidation
6. Centang `Head Office`, `Warehouse A`, dan `Branch Office`
7. Klik [Save Selection]
8. Verifikasi toast "Success, group consolidation has been updated."
9. Buka Fixed Asset > Settings > Groups
10. Verifikasi `Warehouse B`, `Disposal Yard`, dan `Global HQ` belum berstatus Excess (tidak di-dim)
11. Buka Modal Changelog: Group
12. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
13. Tutup Modal Changelog: Group
14. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
15. Muat ulang Fixed Asset > Settings > Groups
16. Verifikasi `Warehouse B`, `Disposal Yard`, dan `Global HQ` berstatus Excess (nama di-dim)
17. Untuk setiap group Excess `Warehouse B`, `Disposal Yard`, dan `Global HQ` (langkah 17 sampai 20): buka elipsis (⋯) baris group itu
18. Verifikasi menu elipsis baris group itu terbuka
19. Verifikasi aksi `Edit` dan `Add Subgroup` Hidden pada menu baris group itu
20. Tutup menu elipsis (Esc)
21. Buka Fixed Asset > Register Asset
22. Buka dropdown tujuan Register Asset
23. Verifikasi ketiga group Excess tetap tampil di dropdown tetapi tidak dapat dipilih
24. Tutup dropdown
25. Buka Fixed Asset > Settings > Groups
26. Verifikasi `Head Office`, `Warehouse A`, dan `Branch Office` usable (tidak di-dim)

### TC-FA-GRP-305: Submit setelah T-0 langsung diterapkan dan bisa memilih ulang

27. Verifikasi Alert Group Consolidation tampil di Settings > Groups
28. Klik [Choose Groups] pada Alert
29. Centang `Warehouse B`, `Disposal Yard`, dan `Global HQ` (group yang tadinya Excess)
30. Klik [Save Selection]
31. Verifikasi toast "Success, group consolidation has been updated."
32. Verifikasi `Warehouse B`, `Disposal Yard`, dan `Global HQ` kembali usable seketika
33. Verifikasi `Head Office`, `Warehouse A`, dan `Branch Office` berstatus Excess sesuai seleksi baru

### TC-FA-GRP-306: Submit ulang sebelum T-0, submit terakhir yang berlaku

34. Pulihkan state: plan dijadwalkan downgrade, seleksi tersimpan kosong, seluruh group usable (fixture BE)
35. Buka Wizard Reconciliation > Step Group Consolidation
36. Centang `Head Office`, `Warehouse A`, dan `Branch Office` (seleksi A)
37. Klik [Save Selection]
38. Tunggu aksi selesai, lalu buka ulang Wizard Reconciliation > Step Group Consolidation
39. Atur centang sehingga hanya `Warehouse B`, `Disposal Yard`, dan `Global HQ` tercentang (seleksi B)
40. Klik [Save Selection]
41. Tunggu aksi selesai
42. Catat jumlah entri Modal Changelog: Group sebagai baseline N1 dan jumlah entri Activity Log sebagai baseline A1 (dibaca lewat fixture BE)
43. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
44. Catat waktu sesudah transaksi T-0 commit
45. Buka Fixed Asset > Settings > Groups
46. Verifikasi `Warehouse B`, `Disposal Yard`, dan `Global HQ` usable sesuai seleksi B
47. Verifikasi `Head Office`, `Warehouse A`, dan `Branch Office` berstatus Excess
48. Buka Modal Changelog: Group, lalu ketik Search `{runId}-091`, tekan Enter
49. Verifikasi entri Action `Marked as Excess (Group Consolidation)` untuk `Head Office`, `Warehouse A`, dan `Branch Office` (dicari lewat nama group) bertanggal sesuai waktu yang dicatat pada langkah 44
50. Verifikasi Modified By entri tersebut = user yang melakukan submit seleksi B (aktor, format [First Name] [Last Initial])
51. Verifikasi jumlah entri Modal Changelog: Group (dibaca lewat fixture BE) bertambah tepat 3 terhadap baseline N1: satu entri per group yang menjadi Excess
52. Verifikasi jumlah entri Activity Log (dibaca lewat fixture BE) bertambah tepat 3 terhadap baseline A1
53. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 sampai 5, 9, 11, 13 sampai 15, 21 dan 22, 24 dan 25, 34 dan 35, 38, 41 sampai 45, 48, 53: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Langkah 17 sampai 20 berulang untuk tiga group Excess (ekspansi 3 x 4 = 12 langkah): 17 membuka elipsis, 18 menjadi anchor menu terbuka sebelum asersi Hidden (8b butir 2), dan 20 menutup menu (S-03). Ketiga group ada di client Wizard yang hanya punya enam group (satu halaman).
- P-1 (state berat): TC-305 memakai keadaan pasca-T-0 (cap baru berlaku, tiga group Excess) yang baru dibangun TC-303 pada spec ini, sehingga TC-305 berada di spec yang sama tanpa membangun ulang; TC-306 membangun ulang plan terjadwal pada langkah penghubung sendiri (S-09). Kelas h.
- Klausa "belum ada baris log" sebelum T-0 (TC-303 Expected b) diasersi pada langkah 12 dengan baseline N0; anchor positif: langkah 2 (entri lain tampil). Asersi tambahan: tidak ada. Search untuk menemukan entri target (langkah di TC-306) adalah langkah penghubung (R-16).
- Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (h, penerapan seleksi Wizard) pada satu dataset dan satu alur state; langkah penghubung seeding, pemicu T-0, dan baca-log berpola bukan asersi baru (bagian 3 prinsip 13, P-1).
- Temuan untuk QA:
  - TC-303 Expected c menyebut dropdown assignment baru tanpa menyebut dropdown mana; spec memakai dropdown tujuan Register Asset (rujukan TC-1051).
  - TC-303 dan TC-306 Post Condition/Expected tentang log di T-0 mengasersi Modified By = submit terakhir; pada TC-306 hanya satu aktor yang submit sehingga Modified By = aktor yang sama; perlu konfirmasi QA bila seharusnya dua user berbeda.
  - TC-305 Post Condition (Changelog dan Activity Log Marked/Restored seketika, System Log ditempel ke user submit) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-306 tidak menyebut isi checkbox pada pembukaan ulang Wizard sesudah submit; spec mengatur centang sampai hanya seleksi B tercentang.
