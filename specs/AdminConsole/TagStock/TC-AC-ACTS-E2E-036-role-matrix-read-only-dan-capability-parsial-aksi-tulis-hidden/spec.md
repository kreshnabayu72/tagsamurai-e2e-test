---
id: TC-AC-ACTS-E2E-036-role-matrix-read-only-dan-capability-parsial-aksi-tulis-hidden
title: "Role Matrix: Aksi Tulis Hidden untuk Read Only dan Capability Parsial (Toolbar Tab Available, Delete by Scan, Checkbox, Bulk Bar, Review Approvals, TAG Log)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-296
  - TC-AC-ACTS-387
  - TC-AC-ACTS-816
  - TC-AC-ACTS-983
coverage:
  web: automated
---

# Role Matrix: Aksi Tulis Hidden untuk Read Only dan Capability Parsial (Toolbar Tab Available, Delete by Scan, Checkbox, Bulk Bar, Review Approvals, TAG Log)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Read Only`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Read Only (#3) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |
| 2 | Manage TAG stock Read+Create (#5) | `manageTagStockCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_CREATE_PASSWORD` |
| 3 | Manage TAG stock Read+Update (#6) | `manageTagStockUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_UPDATE_PASSWORD` |
| 4 | Manage TAG stock Read+Delete (#7) | `manageTagStockDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TS_DELETE_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_TS_CREATE_PASSWORD`, `AC_TS_UPDATE_PASSWORD`, `AC_TS_DELETE_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; SKU RFID `Fixture.tagStock.skuRfid` (#12) dengan unit Available, dan Subject pending di Approvals.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-296: Read Only membuka Review

1. Klik menu sidebar Approvals > TAG Stock, buka Tab Active, lalu klik `Review` pada Subject pending
2. Verifikasi Radio Approve/Reject tidak terpilih dan disabled
3. Verifikasi Approval Note kosong dan disabled
4. Verifikasi Footer hanya `[Close]`, tanpa `[Submit]`
5. Klik `[Close]`

### TC-AC-ACTS-387: Toolbar Tab Available untuk Read Only

6. Buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
7. Verifikasi Toolbar memuat `[Event Log]`
8. Verifikasi `[Add Stock]` dan `[Audit TAG]` Hidden

### TC-AC-ACTS-816 (Read Only): Delete by Scan, Checkbox, dan Bulk Action Bar

9. Amati toolbar Tab Available, lalu amati kolom paling kiri tabel
10. Verifikasi `[Delete by Scan]` Hidden
11. Verifikasi Kolom Checkbox Hidden
12. Klik satu baris
13. Verifikasi Bulk Action Bar tidak muncul

### TC-AC-ACTS-983: Read Only dapat membuka TAG Log

14. Klik (⋯) pada baris Available
15. Verifikasi Menu memuat `TAG Log` (tanpa `Delete`)
16. Klik `TAG Log`
17. Verifikasi Popup terbuka read-only
18. Tutup popup TAG Log

### TC-AC-ACTS-816 (Manage TAG stock Read+Create)

19. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Create (email dan password dari tabel «Role yang diuji»), lalu buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
20. Verifikasi `[Delete by Scan]` Hidden
21. Verifikasi Kolom Checkbox Hidden
22. Klik satu baris
23. Verifikasi Bulk Action Bar tidak muncul

### TC-AC-ACTS-816 (Manage TAG stock Read+Update)

24. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Update (email dan password dari tabel «Role yang diuji»), lalu buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
25. Verifikasi `[Delete by Scan]` Hidden
26. Verifikasi Kolom Checkbox Hidden
27. Klik satu baris
28. Verifikasi Bulk Action Bar tidak muncul

### TC-AC-ACTS-816 (Manage TAG stock Read+Delete)

29. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Delete (email dan password dari tabel «Role yang diuji»), lalu buka Detail SKU `Fixture.tagStock.skuRfid` > Tab Available
30. Verifikasi `[Delete by Scan]` tampil
31. Verifikasi Kolom Checkbox tampil
32. Centang satu baris
33. Verifikasi Bulk Action Bar muncul setelah satu baris dicentang
34. Hilangkan centang baris

## Notes

- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30).
- Langkah penghubung (S-03): menutup dialog Review dan popup TAG Log; Ganti akun lewat Logout dan login; mencentang lalu menghilangkan centang baris pada blok Read+Delete mengembalikan seleksi (S-09).
- Rujukan lintas spec: aksi tulis role terkait diuji di spec 034 (Add Stock dan Audit), spec 035 (Delete dan Approve), dan spec 028 sampai 032 (visibilitas elemen).
- Temuan untuk QA (S-15): TC-AC-ACTS-816 menulis "Read Only (ulangi untuk Manage TAG stock Read+Create, Read+Update, Read+Delete)"; spec mengulangnya per blok role. TC-AC-ACTS-296 tidak menyebut bahwa `[Close]` menutup dialog; spec menutup dialog sebagai langkah penghubung.
