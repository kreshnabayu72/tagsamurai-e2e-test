---
id: TC-AC-ACTS-E2E-035-role-matrix-positif-delete-dan-approval-manage-delete-distributor-dan-additional-approver
title: "Role Matrix Positif: Delete oleh Read+Delete dan Distributor serta Approve oleh Additional Approver"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-131
  - TC-AC-ACTS-132
  - TC-AC-ACTS-135
coverage:
  web: automated
---

# Role Matrix Positif: Delete oleh Read+Delete dan Distributor serta Approve oleh Additional Approver

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Additional Approver tanpa capability Manage TAG stock`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Additional Approver tanpa capability Manage TAG stock (#4) | `additionalApprover_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_AA_PASSWORD` |
| 2 | Distributor Toggle ON (#9) | `distributorOn_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_ON_PASSWORD` |
| 3 | Manage TAG stock Read+Delete (#7) | `manageTagStockDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_DELETE_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_AA_PASSWORD`, `AC_DIST_ON_PASSWORD`, `AC_TS_DELETE_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12).
- Data seed milik spec (unit dan Subject bersuffix `{runId}-035`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): untuk TC-AC-ACTS-132 satu Subject Register Duplicate pending dari requester lain; untuk TC-AC-ACTS-135 satu unit Available milik Distributor Toggle ON pada SKU RFID; untuk TC-AC-ACTS-131 satu unit Available pada SKU RFID.
- Pembacaan TAG Code Subject yang di-approve (`[TAG Code]`) memakai kode seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-132: Additional Approver tanpa capability menyetujui Subject

1. Klik menu sidebar Approvals > TAG Stock, lalu buka Tab Active
2. Klik `Review` pada Subject pending, pilih Approve, klik `[Submit]`
3. Verifikasi Toast sukses `Success, duplicate TAG has been approved and registered as [TAG Code].`
4. Verifikasi Subject pindah ke Tab History

### TC-AC-ACTS-135: Distributor Toggle ON mengeksekusi Delete atas stok sendiri (aksi hapus di akhir)

5. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock, buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
6. Catat jumlah unit entitas lain pada SKU `Fixture.tagStock.skuRfid` lewat fixture BE
7. Klik (⋯) > `Delete` pada unit milik sendiri
8. Klik `[Delete]` di dialog `Delete Unit`
9. Verifikasi Toast `Success, unit has been deleted.`
10. Verifikasi Baris unit hilang dari Tab Available
11. Verifikasi Unit milik entitas lain tidak berubah (jumlah sama dengan yang dicatat pada langkah 6)

### TC-AC-ACTS-131: Eksekusi Delete oleh Read+Delete

12. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Delete (email dan password dari tabel «Role yang diuji»), lalu buka TAG > Stock
13. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
14. Klik row action `Delete` pada unit
15. Klik `[Delete]` di dialog `Delete Unit`
16. Verifikasi Toast sukses `Success, unit has been deleted.`
17. Verifikasi Baris hilang dari Tab Available

## Notes

- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30).
- Penggabungan Role Matrix (§3a, keputusan 2026-11-02): spec memuat tiga role dan dua aksi (Delete dan Approve) dalam satu spec karena polaritasnya seragam positif, tabel «Role yang diuji» dan pola langkah per blok sama (ganti akun, buka halaman, aksi, `Verifikasi` toast dan hasil), dan seeding unit dan Subject milik spec di hook `before` dipakai bersama.
- TC-AC-ACTS-136 (menu Approvals > TAG Stock Hidden untuk Distributor, negatif) ada di spec 033.
- Langkah penghubung (S-03): Ganti akun lewat Logout dan login; TC-AC-ACTS-135 dan 131 (Delete) di akhir spec (S-10).
- Temuan untuk QA (S-15): TC-AC-ACTS-132 Expected butir a memakai `[TAG Code]` sebagai placeholder; spec mengasersi pola pesan dengan kode seed. TC-AC-ACTS-131 dan 135 tidak menyebut baseline unit entitas lain; spec membandingkan jumlah sebelum dan sesudah lewat fixture BE (tanpa endpoint karangan).
