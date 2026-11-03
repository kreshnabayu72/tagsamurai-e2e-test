---
id: TC-AC-DN-E2E-036-resilience-create-gagal
title: "Resilience: Create Gagal karena Error Server, Retry, dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-112
  - TC-AC-DN-113
  - TC-AC-DN-114
coverage:
  web: automated
---

# Resilience: Create Gagal karena Error Server, Retry, dan Timeout

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-112, 113, 114 |

- Env var password: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Measurement `Unit` (#13) dan Pohon Uji Kategori dengan leaf `Antenna` (#14) dibaca saja.
- Data Dinamis (S-12): `Gagal Server Gateway {runId}-036`, `Retry Gateway {runId}-036`, dan `Timeout Gateway {runId}-036` (Category `Antenna`, Measurement `Unit`); hanya `Retry Gateway {runId}-036` yang tersimpan (retry sukses). Hook `after` menghapusnya lewat fixture backend (disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menjawab request dengan status 500, menahan respons sampai batas waktu, dan menunda respons; intercept dilepas segera setelah pemicunya selesai (S-09). Jeda nyata 10 detik pada langkah "Tunggu 10 detik" dipilih spec untuk mengamati toast yang tidak hilang sendiri (di bawah batas ±30 detik, bagian 6).

## Test Steps

### TC-AC-DN-112: Kegagalan server saat Submit Create menampilkan toast error dan mempertahankan popup

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `Gagal Server Gateway {runId}-036` pada field Device Name
3. Klik field Measurement lalu pilih `Unit`
4. Klik field `Category`, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
5. Atur intercept jaringan agar request penyimpanan dijawab status 500
6. Klik `[Submit]`
7. Verifikasi toast error: "Error, failed to create device name."
8. Verifikasi toast tampil di kanan bawah
9. Tunggu 10 detik tanpa menutup toast
10. Verifikasi toast error masih tampil dan tidak hilang sendiri
11. Verifikasi popup form tetap terbuka dengan Device Name, Measurement, dan Category dipertahankan
12. Verifikasi tombol `[Submit]` kembali enabled
13. Lepas intercept jaringan
14. Tutup toast error

### TC-AC-DN-113: Retry Submit Create setelah kegagalan server berhasil tanpa mengisi ulang form

15. Klik `[Clear Field]`
16. Ketik `Retry Gateway {runId}-036` pada field Device Name
17. Klik field Measurement lalu pilih `Unit`
18. Klik field `Category`, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
19. Atur intercept jaringan agar request penyimpanan dijawab status 500
20. Klik `[Submit]`
21. Hapus intercept jaringan
22. Tutup toast error
23. Klik `[Submit]` kembali tanpa mengubah isian
24. Verifikasi toast sukses: "Success, device name has been created."
25. Verifikasi popup form tertutup
26. Ketik Search `Retry Gateway {runId}-036`, tekan Enter
27. Verifikasi List memuat baris `Retry Gateway {runId}-036`
28. Klik `(←)` pada kotak Search

### TC-AC-DN-114: Timeout saat Submit Create menampilkan toast koneksi dan mempertahankan popup

29. Klik tombol `+ Device Name` pada toolbar
30. Ketik `Timeout Gateway {runId}-036` pada field Device Name
31. Klik field Measurement lalu pilih `Unit`
32. Klik field `Category`, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
33. Atur intercept jaringan agar request penyimpanan tidak mendapat respons sampai batas waktu
34. Klik `[Submit]`
35. Verifikasi toast error: "Connection problem. Please try again." tampil tanpa tombol aksi
36. Verifikasi popup form tetap terbuka dengan input dipertahankan
37. Verifikasi tombol `[Submit]` kembali enabled
38. Lepas intercept jaringan
39. Tutup toast error
40. Tutup form lewat icon close `✕`
41. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
42. Klik `[Leave]`

## Notes

- Spec resilience (kelas b): kegagalan server dan timeout pada Submit Create yang dipaksa lewat intercept di atas backend nyata (bagian 6, `FE+BE`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): melepas intercept dan menutup toast error sebelum diasersi lagi (R-12); `[Clear Field]` (langkah 15) mengosongkan form TC-AC-DN-112 yang tetap terbuka sebagai awal TC-AC-DN-113 (form yang sama dipakai berulang, langkah buka form tidak diulang); Search untuk menemukan baris `Retry Gateway {runId}-036` (R-16); langkah 40 sampai 42 menutup form yang dirty (S-08, S-09).
- Ukuran spec (42 langkah, di atas 35 langkah; alasan R3): satu topik (Create gagal), satu kelas harness (b), satu form; tiga variasi kegagalan (500, retry, timeout) berdiri sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition TC-AC-DN-112 ("tidak ada record baru tersimpan") dan TC-AC-DN-113 ("hanya satu record tersimpan") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan (S-01).
  - TC-AC-DN-113 langkah 7 menyebut toast error tampil tanpa menaruhnya di Expected; hasil antara itu tidak diasersi.
