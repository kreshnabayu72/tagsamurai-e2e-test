---
id: TC-GS-UOM-E2E-067-sync-device-name-admin-console
title: "Sinkronisasi Unit ke Device Name Admin Console: Opsi Dropdown, Rename, Stale Reference, dan Breakdown Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-227
  - TC-GS-UOM-232
  - TC-GS-UOM-233
  - TC-GS-UOM-268
coverage:
  web: automated
---

# Sinkronisasi Unit ke Device Name Admin Console: Opsi Dropdown, Rename, Stale Reference, dan Breakdown Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control (Principal), Hendra Wijaya (`Hendra W`), `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login di hook `before` spec ini pada Global Settings instance Principal; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Master Reference > Measurement. Akun yang sama membuka Admin Console > Settings > Device Name (lintas modul); akses Principal ke Admin Console diasumsikan (lihat Temuan untuk QA).
- Pelaku pemicu (hanya lewat sesi API, tanpa login UI): akun Principal yang sama dengan aktor UI (sesi API terpisah) untuk Delete Measurement, serta penghapusan dan pembuatan Device Name Admin Console.
- Environment variable: `GS_PRINCIPAL_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis instance Principal (suffix per run dan nomor spec, bagian 5 konvensi), milik spec ini:
  - `Lux {runId}-067` / `lx` (D-17): dibuat spec lewat UI pada TC-GS-UOM-227; dihapus lewat sesi API pada TC-GS-UOM-232.
  - `Watt {runId}-067` / `W`: di-seed lewat API; dipakai Device Name Admin Console `BLE Gateway {runId}-067` dan `Handheld Reader {runId}-067` (pengganti Watt Pre-setup Principal). Delete Watt diblokir guard (dialog `Cannot Delete Data`) dan unit tidak terhapus.
  - `Ampere {runId}-067` / `A`: di-seed lewat API; dipakai Device Name `Fixed Reader {runId}-067`; di-rename spec menjadi `Amperage {runId}-067` pada TC-GS-UOM-268.
  - Device Name `Lux Reader {runId}-067` (tidak jadi tersimpan pada TC-GS-UOM-232).
- Nilai field wajib lain Device Name Admin Console yang dibuat lewat form UI atau API: disediakan tim FE (`admin-console/settings-device-name/PRD/settings-device-name.md`). Fixture `fixtures/measurement.json` belum ada; tim FE menyediakannya:

  | Kunci fixture | Field | Nilai |
  |---|---|---|
  | `deviceName.*` | field wajib Device Name selain Measurement | disediakan tim FE |

- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Device Name `BLE Gateway`, `Handheld Reader`, `Fixed Reader`, dan `Lux Reader` bersuffix `{runId}-067` bila ada, lalu unit `Lux`, `Watt`, `Ampere` atau `Amperage` bersuffix `{runId}-067` bila masih ada (Device Name dihapus sebelum unitnya).
- Kemampuan teknis: sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk Principal (Delete Measurement dan Device Name); akses ke form Create Device Name dan field dropdown Measurement di Admin Console.
- Tidak ada state global yang diubah.
- TC-GS-UOM-227, 232, 233, 268: login sebagai Total Control (Principal) dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-227: Unit baru muncul di dropdown Measurement form Device Name Admin Console

1. Klik [+ Unit], isi Unit Name `Lux {runId}-067` dan Symbol `lx`, klik [Submit]
2. Tunggu aksi selesai (form tertutup)
3. Buka Admin Console > Settings > Device Name > Create
4. Buka dropdown Measurement
5. Verifikasi opsi `Lux {runId}-067` tersedia

### TC-GS-UOM-232: Form Device Name dengan unit terpilih yang dihapus admin lain menampilkan error field

6. Pilih opsi `Lux {runId}-067` pada field Measurement, isi Device Name `Lux Reader {runId}-067` dan field wajib lain dari fixture
7. [Sesi API Principal] Hapus `Lux {runId}-067` hingga tersimpan
8. Klik [Submit] pada form Create Device Name
9. Verifikasi error field Measurement: `This measurement no longer exists. Please select another.`
10. Verifikasi field Measurement dikosongkan (auto-clear)
11. Klik `✕` pada form Create Device Name
12. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Leave]`

### TC-GS-UOM-268: Rename unit tercermin di Admin Console Device Name tanpa mengubah relasi

14. Buka Global Settings > Master Reference > Measurement, ketik Search `Ampere {runId}-067`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Unit Name menjadi `Amperage {runId}-067`, klik [Save]
15. Tunggu aksi selesai (modal tertutup)
16. Buka Admin Console > Settings > Device Name > Detail `Fixed Reader {runId}-067`
17. Verifikasi Measurement Fixed Reader tampil `Amperage {runId}-067`
18. Buka Global Settings > Master Reference > Measurement, ketik Search `Amperage {runId}-067`, tekan Enter, klik teks `Amperage {runId}-067`
19. Verifikasi Detail Amperage memuat Device Name `Fixed Reader {runId}-067` (relasi tidak berubah)
20. Tutup Unit Detail

### TC-GS-UOM-233: Perubahan Device Name di Admin Console mengubah breakdown delete guard

21. [Sesi API Principal] Hapus Device Name `Handheld Reader {runId}-067` hingga tersimpan
22. Ketik Search `Watt {runId}-067`, tekan Enter, klik `⋯` pada baris tersebut > Delete
23. Verifikasi dialog `Cannot Delete Data` tampil dengan sub-bullet `Admin Console (1 device name)`
24. Klik [OK]
25. Klik teks `Watt {runId}-067`
26. Verifikasi Accordion Device Name List Watt memuat `BLE Gateway {runId}-067`
27. Verifikasi Accordion Device Name List Watt tidak memuat `Handheld Reader {runId}-067`
28. Tutup Unit Detail

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: lintas modul (Admin Console Device Name sebagai konsumen); pelaku kedua hanya memicu perubahan state lewat sesi API.
- Urutan TC di spec berbeda dari urutan sumber: 227 (pembuatan unit dan opsi dropdown), 232 (memakai unit yang sama, lalu dihapus), 268 (rename), lalu 233 (Delete Watt diblokir guard, tidak menghabisi data). Form Create Device Name dibuka sekali (langkah 3) dan ditutup sekali lewat `✕` dan `[Leave]` (langkah 11 sampai 13).
- Dependensi TC-GS-UOM-227 (pembuatan Lux) dijalankan sebagai langkah 1 sampai 5; TC-GS-UOM-232 memakai Lux yang sama.
- Sumber memakai nama literal (Lux, Watt, Ampere, Handheld Reader, Fixed Reader); spec memakai nama bersuffix `{runId}-067` (S-12) dan unit milik spec sebagai pengganti baris Pre-setup Principal (S-06).
- Langkah penghubung: langkah 2 dan 15 (menunggu aksi selesai sebelum pindah ke Admin Console), langkah 11 sampai 13 (menutup form Create Device Name dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`; S-08), langkah 14, 18, dan 22 (Search baris target pada tabel Measurement), langkah 20, 24, dan 28 (menutup Unit Detail dan dialog).
- Langkah 26 menjadi anchor positif bagi absence `Handheld Reader` pada langkah 27 (bagian 8b butir 2).
- Temuan untuk QA:
  - Aktor Principal membuka Admin Console > Settings > Device Name dari Global Settings; TC tidak menyatakan apakah akun Total Control Principal memiliki akses Admin Console Device Name. Spec mengasumsikannya.
  - Nilai field wajib Device Name selain Measurement tidak disebut TC (S-13); disediakan tim FE.
  - TC-GS-UOM-233 tidak menyebut cara menghapus Device Name `Handheld Reader` (UI atau API); spec memakai sesi API sebagai pemicu.
  - TC-GS-UOM-233 Pre-setup Principal: Watt dipakai Device Name BLE Gateway dan Handheld Reader; "Delete Watt di modul ini" tidak menyebut Post Condition, tidak diasersi.
