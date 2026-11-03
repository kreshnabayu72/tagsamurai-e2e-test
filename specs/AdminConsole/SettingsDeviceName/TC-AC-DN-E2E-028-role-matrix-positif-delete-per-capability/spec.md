---
id: TC-AC-DN-E2E-028-role-matrix-positif-delete-per-capability
title: "Role Matrix Positif: Delete dan Bulk Delete Berhasil oleh Delete-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-72
  - TC-AC-DN-201
  - TC-AC-DN-238
coverage:
  web: automated
---

# Role Matrix Positif: Delete dan Bulk Delete Berhasil oleh Delete-Only

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Delete-Only (Manage device master data: Delete + Read) (Pre-setup #6); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #6 | Delete-Only (Manage device master data: Delete + Read) | (tanpa nama di TC) | `manageDeviceD_automated_{namaCompany}@qwertysystem.net` | `akunDeleteOnly` | `Spectra.env.AC_DN_DELETE_PASSWORD` | TC-AC-DN-72, TC-AC-DN-201, TC-AC-DN-238 |

- Env var password: `Spectra.env.AC_DN_DELETE_PASSWORD`. `AC_DN_DELETE_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Device Name inti (#16) hanya dibaca; tidak dijadikan target hapus.
- Data milik spec (S-06, S-12), dibuat fixture backend di hook `before` (disediakan tim FE/BE): `Cable Tester A {runId}-028`, `Cable Tester B {runId}-028`, dan `Cable Tester C {runId}-028` (Category `Accessory`, Measurement `Unit`, tanpa SKU dan tanpa unit BYO) serta `Door Antenna {runId}-028` (Category `Antenna`, Measurement `Unit`, tanpa SKU dan tanpa unit BYO). Hook `after` menghapus sisa record milik spec bila ada.

## Test Steps

### TC-AC-DN-72: Delete-Only menghapus Device Name tanpa relasi sampai berhasil

1. Ketik Search `Cable Tester A {runId}-028`, tekan Enter
2. Klik ikon `⋯` pada baris `Cable Tester A {runId}-028` lalu pilih `Delete`
3. Klik `[Delete]` pada dialog konfirmasi `Delete Device Name`
4. Verifikasi toast sukses: "Success, device name has been deleted."
5. Verifikasi dialog konfirmasi tertutup
6. Verifikasi baris `Cable Tester A {runId}-028` tidak lagi tampil pada List
7. Klik `(←)` pada kotak Search

### TC-AC-DN-201: Aktor Delete-Only menyelesaikan Delete Device Name sampai sukses

8. Ketik Search `Cable Tester B {runId}-028`, tekan Enter
9. Klik ikon aksi pada kolom Actions baris `Cable Tester B {runId}-028` lalu klik `Delete`
10. Klik `[Delete]` pada dialog konfirmasi
11. Verifikasi toast sukses: "Success, device name has been deleted."
12. Verifikasi baris `Cable Tester B {runId}-028` tidak lagi ada pada List
13. Klik `(←)` pada kotak Search

### TC-AC-DN-238: Aktor Delete-Only menyelesaikan Bulk Delete sampai sukses

14. Ketik Search `{runId}-028`, tekan Enter
15. Centang checkbox baris `Cable Tester C {runId}-028`
16. Centang checkbox baris `Door Antenna {runId}-028`
17. Klik tombol `Bulk Action` pada Bulk Action Bar
18. Klik `Delete`
19. Klik `[Delete]` pada dialog
20. Verifikasi toast sukses: "Success, device name has been deleted."
21. Verifikasi baris `Cable Tester C {runId}-028` dan `Door Antenna {runId}-028` tidak lagi ada pada List
22. Klik `(←)` pada kotak Search

## Notes

- Spec Role Matrix positif (bagian 3a konvensi): aksi Delete dan Bulk Delete berhasil oleh Delete-Only. Subjudul `###` memetakan langkah ke id TC granular. Aksi menghapus data berada di spec ini seluruhnya (S-10).
- Penyimpangan data (S-06): target hapus `Cable Tester` dan `Door Antenna` (Pre-setup #16 di TC) diganti record milik spec bersuffix.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16) pada langkah 1, 8, dan 14, serta mengosongkan Search lewat `(←)`; daftar pada TC-AC-DN-238 dipersempit lewat Search suffix agar kedua baris tampil.
- Temuan untuk QA:
  - TC-AC-DN-72 dan TC-AC-DN-201 (Delete-Only menghapus `Cable Tester`) berbeda hanya pada langkah Search; Expected identik. Tiap TC tetap satu spec.
  - Post Condition TC-AC-DN-72 ("terhapus permanen") tidak punya langkah observasi di luar Expected b dan tidak diasersi tambahan.
