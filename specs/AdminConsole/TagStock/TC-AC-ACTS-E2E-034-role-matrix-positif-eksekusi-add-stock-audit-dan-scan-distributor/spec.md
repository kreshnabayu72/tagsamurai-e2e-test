---
id: TC-AC-ACTS-E2E-034-role-matrix-positif-eksekusi-add-stock-audit-dan-scan-distributor
title: "Role Matrix Positif: Eksekusi Add Stock oleh Read+Create, Audit oleh Read+Update, serta Add Stock dan Audit oleh Distributor Toggle ON dan OFF, dan Item Sidebar TAG > Stock untuk Aktor Read"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-128
  - TC-AC-ACTS-129
  - TC-AC-ACTS-130
  - TC-AC-ACTS-133
  - TC-AC-ACTS-134
  - TC-AC-ACTS-724
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Add Stock oleh Read+Create, Audit oleh Read+Update, serta Add Stock dan Audit oleh Distributor Toggle ON dan OFF, dan Item Sidebar TAG > Stock untuk Aktor Read

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Manage TAG stock Read+Create`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Manage TAG stock Read+Create (#5) | `manageTagStockCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_CREATE_PASSWORD` |
| 2 | Manage TAG stock Read+Update (#6) | `manageTagStockUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_UPDATE_PASSWORD` |
| 3 | Distributor Toggle ON (#9) | `distributorOn_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_ON_PASSWORD` |
| 4 | Distributor Toggle OFF (#10) | `distributorOff_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_OFF_PASSWORD` |
| 5 | Manage TAG stock Read (#8) | `manageTagStockRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_READ_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_TS_CREATE_PASSWORD`, `AC_TS_UPDATE_PASSWORD`, `AC_DIST_ON_PASSWORD`, `AC_DIST_OFF_PASSWORD`, `AC_TS_READ_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12).
- Data seed milik spec (unit bersuffix `{runId}-034`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): untuk TC-AC-ACTS-130 satu unit Damaged/Missing SKU RFID; untuk TC-AC-ACTS-134 satu unit Damaged/Missing milik Distributor Toggle ON; untuk TC-AC-ACTS-724 dua unit milik Distributor Toggle OFF (unit A Damaged/Missing, unit B Available). Tepat dua unit milik Distributor Toggle OFF pada SKU RFID.
- Pemulihan (S-06): hook `after` menghapus lewat fixture BE unit yang didaftarkan spec ini pada SKU Pre-setup `Fixture.tagStock.skuRfid` (dua TAG TC-AC-ACTS-129 dan satu TAG TC-AC-ACTS-133) agar SKU bersama tidak menyimpan unit tambahan; unit Damaged/Missing seed spec dihapus di hook yang sama.
- Kemampuan teknis (kelas d): simulator pemindai RFID (scan TAG satu per satu, sesi scan) disediakan tim FE; TAG RFID baru yang belum terdaftar (dua TAG untuk TC-AC-ACTS-129, satu TAG untuk TC-AC-ACTS-133) disediakan lewat simulator itu. Kemampuan membaca jumlah unit entitas lain lewat fixture BE (untuk asersi "unit milik entitas lain tidak berubah") disediakan tim FE/BE tanpa endpoint karangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-129: Eksekusi Add Stock oleh Read+Create

1. Klik (⋯) > `Add Stock` pada SKU `Fixture.tagStock.skuRfid`
2. Klik `[Add by Scan]`, pindai 2 TAG RFID baru lewat simulator, klik `[Stop]`
3. Klik `[Submit]`
4. Verifikasi Toast sukses `Success, TAG has been registered.`
5. Verifikasi Dua unit terdaftar dengan TAG Code baru

### TC-AC-ACTS-130: Eksekusi Audit oleh Read+Update

6. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Update (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
7. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available, klik `[Audit TAG]`
8. Klik `[Start Scan]`, pindai unit Damaged/Missing lewat simulator, klik `[Stop]`
9. Klik `[Submit]`
10. Verifikasi Unit pulih menjadi Available
11. Verifikasi Toast sukses `Success, TAG has been verified. 1 TAG recovered to Available.`

### TC-AC-ACTS-133: Distributor Toggle ON mengeksekusi Add Stock atas stok sendiri

12. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
13. Catat jumlah unit entitas lain pada SKU `Fixture.tagStock.skuRfid` lewat fixture BE
14. Klik (⋯) > `Add Stock` pada SKU `Fixture.tagStock.skuRfid`
15. Klik `[Add by Scan]`, pindai 1 TAG RFID baru lewat simulator, klik `[Stop]`
16. Klik `[Submit]`
17. Verifikasi Toast `Success, TAG has been registered.`
18. Verifikasi Unit baru berstatus Available muncul di Tab Available Distributor itu dengan TAG Code baru
19. Verifikasi Unit milik entitas lain tidak berubah (jumlah sama dengan yang dicatat)

### TC-AC-ACTS-134: Distributor Toggle ON mengeksekusi Audit TAG atas stok sendiri

20. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available, klik `[Audit TAG]`
21. Klik `[Start Scan]`, pindai unit Damaged/Missing milik Distributor lewat simulator, klik `[Stop]`
22. Klik `[Submit]`
23. Verifikasi Toast `Success, TAG has been verified. 1 TAG recovered to Available.`
24. Verifikasi Unit menjadi Available dan hanya unit batch Distributor itu yang berubah

### TC-AC-ACTS-724: Distributor Toggle OFF tetap dapat Audit dan Delete atas stok sendiri (aksi hapus di akhir spec)

25. Ganti akun: Logout, lalu login sebagai Distributor Toggle OFF (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
26. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available, klik `[Audit TAG]`, klik `[Start Scan]`
27. Pindai unit A dan unit B lewat simulator, klik `[Stop]`, klik `[Submit]`
28. Verifikasi Audit berhasil tanpa dialog Konfirmasi: unit A pulih menjadi Available
29. Verifikasi Toast `Success, TAG has been verified. 1 TAG recovered to Available.`
30. Di Tab Available klik (⋯) > `Delete` pada unit B, klik `[Delete]` di dialog
31. Verifikasi Toast `Success, unit has been deleted.`
32. Verifikasi Unit B hilang dari Tab Available
33. Verifikasi Tidak ada penolakan server akibat toggle OFF

### TC-AC-ACTS-128: Item sidebar TAG > Stock tampil untuk aktor dengan minimal satu capability

34. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read (email dan password dari tabel «Role yang diuji»), lalu buka dashboard Admin Console
35. Perhatikan sidebar
36. Verifikasi Item sidebar TAG > Stock tampil

## Notes

- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30).
- Penggabungan Role Matrix (§3a, keputusan 2026-11-02): spec memuat lima role dan beberapa aksi (Add Stock, Audit, Delete, serta pengecekan item sidebar) dalam satu spec karena polaritasnya seragam positif (aksi atau elemen berhasil tersedia), tabel «Role yang diuji» dan pola langkah per blok sama (ganti akun, buka halaman, aksi, `Verifikasi` hasil), dan seeding unit milik spec di hook `before` serta simulator pemindai RFID dipakai bersama. Pemisahan per aksi menghasilkan spec dengan satu atau dua blok yang mengulang login hook, seeding, dan pemulihan yang sama. Spec ini melewati sekitar 35 langkah (36 langkah); alasan: semua blok satu pola Role Matrix positif, satu blok per role, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- TC-AC-ACTS-136 dan TC-AC-ACTS-128 mengikuti polaritas §3a: TC-AC-ACTS-136 (menu Hidden, negatif) ada di spec 033, TC-AC-ACTS-128 (item sidebar tampil, positif) di spec ini.
- Langkah penghubung (S-03): Ganti akun lewat Logout dan login; TC-AC-ACTS-724 ditaruh sesudah semua blok yang membutuhkan unit seed dan sebelum TC-AC-ACTS-128 karena menghapus unit B (S-10); TC-AC-ACTS-128 hanya membaca sidebar.
- Temuan untuk QA (S-15): TC-AC-ACTS-129 dan 130 memiliki kolom tambahan (Post Condition "Dua unit Available di Tab Available") yang tidak punya langkah observasi di TC; tidak diasersi di luar Expected butir b. TC-AC-ACTS-133 butir b ("unit milik entitas lain tidak berubah") membutuhkan pembacaan state BE; disediakan tim FE/BE tanpa endpoint karangan. Cara memindai unit dan TAG baru lewat simulator tidak didefinisikan TC. Pemulihan SKU Pre-setup bersama dan pemindaian TAG baru bergantung pada fixture BE dan simulator yang belum ada (disediakan tim FE/BE).
