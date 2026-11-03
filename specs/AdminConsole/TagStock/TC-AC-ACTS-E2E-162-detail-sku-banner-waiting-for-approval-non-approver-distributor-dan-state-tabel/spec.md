---
id: TC-AC-ACTS-E2E-162-detail-sku-banner-waiting-for-approval-non-approver-distributor-dan-state-tabel
title: "Detail SKU Banner: Non-Approver (Teks Tanpa Link), Distributor Hanya Batch Sendiri, Tidak Terpengaruh Search/Filter/Sort, Tidak Tampil di Tab In Use, Loading, Error, dan Tidak Dapat Ditutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-989
  - TC-AC-ACTS-990
  - TC-AC-ACTS-992
  - TC-AC-ACTS-993
  - TC-AC-ACTS-994
coverage:
  web: automated
---

# Detail SKU Banner: Non-Approver (Teks Tanpa Link), Distributor Hanya Batch Sendiri, Tidak Terpengaruh Search/Filter/Sort, Tidak Tampil di Tab In Use, Loading, Error, dan Tidak Dapat Ditutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Manage TAG stock Read+Create (Pre-setup #5) `manageTagStockCreate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TS_CREATE_PASSWORD`.
- Akun aktor ketiga (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12). Data per blok TC (di-reset fixture BE): 2 Subject Register Duplicate pending dan lebih dari 10 unit Available (TC-AC-ACTS-992); 2 Subject pending (TC-AC-ACTS-993); 1 Subject pending (TC-AC-ACTS-994); 2 Subject pending dari Add Stock aktor #5 (TC-AC-ACTS-989); Distributor A memiliki 1 Subject pending sementara Principal dan Distributor B memiliki Subject pending pada SKU yang sama (TC-AC-ACTS-990).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk menahan request tab (Loading) dan untuk respons `5xx` (Error) pada TC-AC-ACTS-993; intercept dilepas segera sesudah dipakai.

## Test Steps

### TC-AC-ACTS-992: Banner tidak terpengaruh Search, Filter, Sort, dan paginasi serta tidak mengubah isi tabel atau Summary bar

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Catat Total Registered dan kartu Summary bar
3. Verifikasi banner `2 TAGs are waiting for approval.` tampil
4. Ketik Search dengan keyword yang tidak ada hasilnya, tekan Enter
5. Verifikasi banner tetap tampil dengan hitungan sama setelah Search
6. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
7. Terapkan Filter Status
8. Verifikasi banner tetap tampil dengan hitungan sama setelah Filter
9. Kosongkan Filter Status
10. Urutkan kolom dan pindah halaman
11. Verifikasi banner tetap tampil dengan hitungan sama setelah Sort dan paginasi
12. Bandingkan Summary bar sebelum dan sesudah
13. Verifikasi Total Registered dan kartu Summary bar tidak berubah akibat unit Waiting

### TC-AC-ACTS-993: Banner tidak tampil di Tab In Use, saat Loading, dan saat Error

14. Klik menu sidebar TAG > Stock, lalu buka lagi Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
15. Verifikasi banner tampil di Tab Available (pembanding)
16. Buka Tab In Use
17. Verifikasi Tab In Use tanpa banner
18. Tahan request Tab Available (Loading), lalu kembali ke Tab Available
19. Verifikasi saat Loading tab tidak menampilkan banner (hanya komponen Loading)
20. Lepas tahanan request
21. Intercept request tab dengan respons `5xx`, lalu pindah ke Tab In Use dan kembali ke Tab Available
22. Verifikasi saat Error tab tidak menampilkan banner (hanya komponen error `S-04`)
23. Lepas intercept

### TC-AC-ACTS-994: Banner tidak dapat ditutup

24. Reset dataset: 1 Subject pending lewat fixture BE, lalu muat ulang halaman
25. Amati banner dan cari kontrol close
26. Verifikasi banner `1 TAG is waiting for approval.` tampil
27. Verifikasi tidak ada tombol close pada banner
28. Muat ulang halaman
29. Verifikasi banner tampil lagi setelah reload selama unit masih menunggu

### TC-AC-ACTS-989: Aktor non-approver melihat banner berupa teks tanpa link

30. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Create (`Spectra.env.AC_TS_CREATE_PASSWORD`)
31. Reset dataset: 2 Subject pending dari Add Stock aktor #5 lewat fixture BE
32. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
33. Verifikasi banner `2 TAGs are waiting for approval.` tampil
34. Verifikasi banner tanpa link `Review in Approvals`

### TC-AC-ACTS-990: Distributor hanya menghitung unit Waiting dari batch registrasi miliknya

35. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
36. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
37. Amati banner sebagai Distributor A
38. Verifikasi banner `1 TAG is waiting for approval.`
39. Verifikasi Subject entitas lain (Principal dan Distributor B) tidak dihitung

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (Detail SKU, satu SKU dan satu dataset); tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah pembukaan Detail SKU dan pemulihan state diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", navigasi sidebar yang mereset state, `(←)` pada kotak Search, pemulihan Filter Status, pelepasan intercept, dan penahanan request. Urutan TC: 992, 993, 994, 989, 990; TC-AC-ACTS-989 dan 990 sesudah Ganti akun.
- P-5 butir b: TC-AC-ACTS-993 menahan request dan menginjeksi satu respons 5xx hanya untuk mengamati tidak adanya banner pada keadaan Loading dan Error (objek uji ringan kelas b) di spec fungsional banner; satu-satunya TC kelas b di spec ini.
- Temuan untuk QA:
  - Langkah Uji TC-AC-ACTS-992 nomor 4 membandingkan Summary bar sebelum dan sesudah; TC tidak menyebut kartu mana yang dicatat, sehingga spec mencatat Total Registered dan semua kartu Summary bar.
  - TC-AC-ACTS-993 menyebut hanya "komponen Loading / error `S-04`"; teks error tidak disebut, sehingga spec mengasersi tidak adanya banner pada kedua keadaan tanpa menyalin teks.
  - TC-AC-ACTS-990 tidak menyebut apakah Search/Filter Tab Available diubah; spec tidak mengubahnya.
  - TC-AC-ACTS-989 mengasersi aktor non-approver tanpa teks pembeda status approver; Pre-setup #5 dipakai sesuai TC.
