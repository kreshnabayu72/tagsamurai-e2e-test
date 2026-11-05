---
id: TC-FA-FAAC-E2E-186-resilience-status-bulk-dan-delete
title: "Resilience: Delete, Toggle Active, dan Bulk Activate atau Deactivate Gagal karena Error Server 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-222
  - TC-FA-FAAC-250
  - TC-FA-FAAC-251
  - TC-FA-FAAC-302
  - TC-FA-FAAC-303
coverage:
  web: automated
---

# Resilience: Delete, Toggle Active, dan Bulk Activate atau Deactivate Gagal karena Error Server 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis: `Spectra.intercept` parsial yang memaksa respons HTTP 5xx pada permintaan Delete, Activate, dan Deactivate (satuan dan Bulk Action) di atas backend nyata, dilepas segera sesudah pemicu (S-09). Endpoint permintaan tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga dipilih tim FE saat script. Pembacaan status Active Asset Class dan jumlah entri Changelog Asset Class, System Log, dan Activity Log lewat kemampuan baca BE (disediakan tim FE/BE; audit trail permanen, asersi log memakai selisih terhadap baseline, bukan angka absolut).
- Data seed Pre-setup (kode literal TC, disediakan fixture BE): `B-DEL3` (tanpa Asset Name, belum pernah diposting); `B-IN5`, `B-IN6`, dan `B-IN9` Inactive; `B-FREE6`, `B-FREE7`, dan `B-FREE11` Active tanpa Asset Name. Semua aksi gagal sehingga data tidak berubah, kecuali kegagalan sebagian pada Bulk (TC-250 dan TC-251) yang dapat menyimpan sebagian Asset Class; fixture BE memulihkan status seed di hook `after`.
- Ukuran halaman tabel: spec mengubahnya menjadi 100 pada langkah 10 agar seluruh hasil Search `B-IN` dan `B-FREE` tampil (S-14).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-222: Delete gagal karena server error 5xx

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
2. Ketik Search `B-DEL3`, tekan Enter
3. Klik ikon `⋯` pada baris `B-DEL3`, lalu pilih `Delete`
4. Pasang intercept respons 5xx, lalu klik `Delete` pada dialog
5. Lepas intercept respons 5xx
6. Verifikasi toast error `Error, failed to delete asset class.`
7. Verifikasi baris `B-DEL3` tetap ada di tabel
8. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)

### TC-FA-FAAC-250: Bulk Activate gagal 5xx mempertahankan seleksi

9. Ganti isi kotak search dengan `B-IN`, tekan Enter
10. Ubah ukuran halaman tabel menjadi 100
11. Centang baris `B-IN5` dan `B-IN6` di tabel
12. Klik Bulk Action `Activate`
13. Pasang intercept respons 5xx, lalu klik `Activate` pada dialog
14. Lepas intercept respons 5xx
15. Verifikasi toast error `Error, failed to activate asset class.`
16. Verifikasi seleksi baris `B-IN5` dan `B-IN6` dipertahankan
17. Verifikasi daftar disegarkan: status `B-IN5` dan `B-IN6` di tabel sama dengan status di server (sebagian Asset Class mungkin sudah tersimpan)
18. Klik `Unselect All`

### TC-FA-FAAC-303: Activate gagal 5xx mengembalikan toggle ke nilai tersimpan

19. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
20. Klik toggle kolom Active pada baris `B-IN9` (Off)
21. Pasang intercept respons 5xx, lalu klik `Activate` pada dialog
22. Lepas intercept respons 5xx
23. Verifikasi toast error `Error, failed to activate asset class.`
24. Verifikasi toggle `B-IN9` kembali Off
25. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)

### TC-FA-FAAC-251: Bulk Deactivate gagal 5xx mempertahankan seleksi

26. Ganti isi kotak search dengan `B-FREE`, tekan Enter
27. Centang baris `B-FREE6` dan `B-FREE7` di tabel
28. Klik Bulk Action `Deactivate`
29. Pasang intercept respons 5xx, lalu klik `Deactivate` pada dialog
30. Lepas intercept respons 5xx
31. Verifikasi toast error `Error, failed to deactivate asset class.`
32. Verifikasi seleksi baris `B-FREE6` dan `B-FREE7` dipertahankan
33. Verifikasi daftar disegarkan: status `B-FREE6` dan `B-FREE7` di tabel sama dengan status di server (sebagian Asset Class mungkin sudah tersimpan)
34. Klik `Unselect All`

### TC-FA-FAAC-302: Deactivate gagal 5xx mengembalikan toggle ke nilai tersimpan

35. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class, System Log, dan Activity Log
36. Klik toggle kolom Active pada baris `B-FREE11` (On)
37. Pasang intercept respons 5xx, lalu klik `Deactivate` pada dialog
38. Lepas intercept respons 5xx
39. Verifikasi toast error `Error, failed to deactivate asset class.`
40. Verifikasi toggle `B-FREE11` kembali On
41. Verifikasi jumlah entri Changelog Asset Class, System Log, dan Activity Log sama dengan baseline (tidak ada log)
42. Klik `(←)` pada kotak Search

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan nomor TC supaya hasil Search `B-IN` (TC-250 dan TC-303) dan `B-FREE` (TC-251 dan TC-302) dipakai berturutan tanpa Search ulang (S-10).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 2, 9, dan 26 (Search untuk menemukan baris target, R-16); langkah 10 (mengubah ukuran halaman agar baris target tampil, S-14); langkah 18 dan 34 (membersihkan seleksi, S-09); langkah 42 (mengosongkan Search). Intercept dilepas segera sesudah pemicu (langkah 5, 14, 22, 30, dan 38; S-09).
3. Prinsip 13g dan S-12: klausa "tidak ada log" pada TC-222, TC-302, dan TC-303 adalah asersi jumlah pada TC fungsional (aksi UI dengan kegagalan server yang dipaksa, kelas b; bukan request langsung yang ditolak server) sehingga diasersi di spec ini dengan `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog Asset Class, System Log, Activity Log), sesudah toast error server sebagai anchor positif; baseline dicatat sebelum pemicu tiap TC.
4. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `B-DEL3`, `B-IN5`, `B-IN6`, `B-IN9`, `B-FREE6`, `B-FREE7`, dan `B-FREE11`; kode dipakai apa adanya tanpa suffix `{runId}`.
5. Alasan di atas sekitar 35 langkah: kelima blok satu kelas harness (b), berdiri sendiri dengan data dan baseline sendiri; konvensi bagian 3 prinsip 13 menetapkan kelas ringan cukup satu spec per kelas per modul, bukan per aksi. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
6. Temuan untuk QA: TC-250 dan TC-251 menulis "daftar disegarkan (sebagian Asset Class mungkin sudah tersimpan)" tanpa cara mengamatinya; spec mengasersi status baris sama dengan status di server (kemampuan baca BE). TC-250 dan TC-251 tidak menyebut cara menampilkan dua baris target sekaligus; spec memakai Search dan ukuran halaman 100. TC-222 tidak menyebut label tombol dialog selain `Delete`, dan TC-302 serta TC-303 tidak menyebut toast sukses sebagai anchor; spec memakai toast error server sebagai anchor.
