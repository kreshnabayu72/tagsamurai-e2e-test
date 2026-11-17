---
id: TC-FA-FAAC-E2E-192-state-tenant-write-lockdown-asset-name-suspended-expired
title: "State Tenant: Assign, Unassign, dan Move Asset Name Ditolak saat Client Suspended atau Expired"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-622
  - TC-FA-FAAC-623
  - TC-FA-FAAC-624
sourceRules: ["T-13", "E-FAAC-73"]
smoke: []
dependsOn: []
trace:
  "T-13": [10, 20, 30]
  "E-FAAC-73": [12, 13, 21, 22, 32, 33]
coverage:
  web: automated
---

# State Tenant: Assign, Unassign, dan Move Asset Name Ditolak saat Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: status client (`Active`, `Suspended`, `Expired`). Pelaku perubahan status tidak disebut TC, PRD, atau LLD; fixture BE untuk mengubah status entitas "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Status awal `Active` dicatat di hook `before`; hook `after` memulihkan status ke `Active` walau spec gagal di tengah.
- Data seed (kode dan nama literal TC, disediakan fixture BE, milik spec ini): Asset Class `B-ANCHOR` (Active, tanpa Asset Name ter-assign) sebagai "Asset Class anchor" TC-622; Asset Name tanpa Asset Class `Hand Truck`; Asset Class `HEAVY-EQ` (Active, Heavy Equipment) dengan tiga Asset Name ter-assign: `Excavator PC200` (8 aset aktif), `Wheel Loader` (4 aset aktif), `Crane Rental Unit` (0 aset aktif; Machinery > Rented); Asset Class `MACHINERY` (Active) sebagai tujuan Move. Permintaan yang ditolak tidak mengubah data; fixture BE memulihkan keanggotaan Asset Name di hook `after` bila berubah.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` menurut precondition TC-623 dan TC-624; fixture BE menyetelnya pada langkah 1, sebelum status client diubah, dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Kemampuan teknis: pembacaan keanggotaan Asset Name dan jumlah entri Changelog Asset Class, System Log, dan Activity Log lewat kemampuan baca BE (disediakan tim FE/BE; audit trail permanen, asersi log memakai selisih terhadap baseline, bukan angka absolut).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-623 dan TC-624)
2. Atur lewat fixture BE status client menjadi `Suspended`, lalu muat ulang halaman

### TC-FA-FAAC-622: Assign saat entitas Suspended ditolak dengan toast baku

3. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
4. Ketik Search `B-ANCHOR`, tekan Enter
5. Klik link Class Code `B-ANCHOR` di tabel
6. Klik tab `Asset Names`
7. Klik tombol `+ Assign Asset Names`
8. Centang `Hand Truck`
9. Klik `[Assign]`
10. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
11. Tutup dialog Assign lewat `[×]`
12. Verifikasi `Hand Truck` tidak tampil di tab `Asset Names`
13. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
14. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-624: Unassign saat entitas Suspended ditolak dengan toast baku

15. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
16. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
17. Klik link Class Code `HEAVY-EQ` di tabel, lalu klik tab `Asset Names`
18. Klik ikon `⋯` pada baris `Crane Rental Unit`, lalu pilih `Unassign`
19. Klik `[Unassign]`
20. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
21. Verifikasi `Crane Rental Unit` tetap ter-assign (baris tetap tampil di tab `Asset Names`)
22. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
23. Atur lewat fixture BE status client menjadi `Expired`, lalu muat ulang halaman

### TC-FA-FAAC-623: Move saat entitas Expired ditolak dengan toast baku

24. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
25. Ketik Search `HEAVY-EQ`, tekan Enter
26. Klik link Class Code `HEAVY-EQ` di tabel, lalu klik tab `Asset Names`
27. Klik ikon `⋯` pada baris `Crane Rental Unit`, lalu pilih `Move`
28. Pilih `Destination Asset Class` = `MACHINERY – Machinery`
29. Klik `[Move]`
30. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.`
31. Klik `[Cancel]` pada dialog Move
32. Verifikasi `Crane Rental Unit` tetap di `Heavy Equipment` (baris tetap tampil di tab `Asset Names`)
33. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
34. Atur lewat fixture BE status client kembali menjadi `Active`, lalu muat ulang halaman

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor (622, 624 lalu 623) supaya status client hanya berganti `Suspended` ke `Expired` satu kali (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (fixture BE menyetel keadaan awal dinamis TC-623 dan TC-624, S-14, bukan bagian TC); langkah 2, 23, dan 34 (mengganti status client); langkah 4, 16, dan 25 (Search untuk menemukan baris target, R-16; langkah 25 diperlukan karena muat ulang di langkah 23 menutup Detail `HEAVY-EQ`); langkah 26 (membuka kembali Detail `HEAVY-EQ` dan tab `Asset Names`); langkah 11 (menutup dialog Assign, picker D-13 menutup tanpa konfirmasi menurut TC-154 dan TC-712); langkah 14 (kembali ke tabel); langkah 31 (menutup dialog Move dengan `[Cancel]`, yang tidak memunculkan dialog `Unsaved Changes` menurut Catatan Cakupan TC-698 dan TC-699).
3. S-05 dan prinsip 13g (pengecualian kelas h): klausa "tidak ada log" pada ketiga TC diasersi di spec ini dengan selisih jumlah entri terhadap baseline per surface log (Changelog Asset Class, System Log, Activity Log); baseline dicatat sebelum pemicu tiap TC (S-12).
4. Pengecualian kode dan nama seed literal (S-06/S-12): TC mewajibkan `B-ANCHOR`, `HEAVY-EQ`, `MACHINERY`, `Hand Truck`, `Crane Rental Unit`; nilai dipakai apa adanya tanpa suffix `{runId}`. Aksi tulis ditolak server sehingga data tidak berubah.
5. Temuan untuk QA: TC-622 menyebut "Asset Class anchor (hasil TC anchor Create Asset Class valid)" tanpa kode; spec memakai seed `B-ANCHOR` tanpa Asset Name. TC-622 dan TC-623 tidak menyebut apakah dialog Assign dan Move tetap terbuka sesudah penolakan; spec berasumsi tetap terbuka seperti pada kegagalan 5xx (TC-165, TC-211) dan menutup dialog Assign dengan `[×]` serta dialog Move dengan `[Cancel]`. TC-624 tidak menyebut keadaan dialog Unassign sesudah penolakan; spec berasumsi dialog menutup setelah toast error. TC-623 memakai ikon `⋯` dan `Move` seperti TC sumber dan tidak menyebut Effective From untuk Asset Name tanpa aset aktif (`Crane Rental Unit` 0 aset aktif).
