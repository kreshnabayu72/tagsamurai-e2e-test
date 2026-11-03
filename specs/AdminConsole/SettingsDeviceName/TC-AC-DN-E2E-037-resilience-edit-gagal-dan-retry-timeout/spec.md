---
id: TC-AC-DN-E2E-037-resilience-edit-gagal-dan-retry-timeout
title: "Resilience: Edit Gagal, Timeout, dan Retry Create Setelah Timeout Tidak Membuat Ganda"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-167
  - TC-AC-DN-168
  - TC-AC-DN-578
coverage:
  web: automated
---

# Resilience: Edit Gagal, Timeout, dan Retry Create Setelah Timeout Tidak Membuat Ganda

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-167, 168, 578 |

- Env var password: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Measurement `Unit` (#13) dan Pohon Uji Kategori dengan leaf `Antenna` (#14) dibaca saja.
- Data milik spec (S-06, S-12): `Door Antenna {runId}-037` (Category `Antenna`, Measurement `Unit`) dibuat fixture backend di hook `before` sebagai target Edit TC-AC-DN-167 dan 168 (record tidak berubah karena Save gagal); `Retry Device {runId}-037` dibuat langkah Create TC-AC-DN-578. Hook `after` menghapus keduanya lewat fixture backend (disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menjawab request dengan status 500, menahan respons sampai batas waktu, dan menunda respons; intercept dilepas segera setelah pemicunya selesai (S-09). Jeda nyata 10 detik pada langkah "Tunggu 10 detik" dipilih spec untuk mengamati toast yang tidak hilang sendiri (di bawah batas ±30 detik, bagian 6).
- Kemampuan intersepsi tambahan (disediakan tim FE/BE): membuang respons request Create setelah request mencapai server (TC-AC-DN-578).

## Test Steps

### TC-AC-DN-167: Kegagalan server saat Save Edit menampilkan toast error dan mempertahankan popup

1. Ketik Search `Door Antenna {runId}-037`, tekan Enter
2. Buka menu aksi pada baris `Door Antenna {runId}-037` lalu klik `Edit`
3. Kosongkan field Device Name lalu ketik `Door Gagal {runId}-037`
4. Atur intercept jaringan agar request penyimpanan dijawab status 500
5. Klik `[Save]`
6. Verifikasi toast error: "Error, failed to update device name."
7. Verifikasi toast tampil di kanan bawah
8. Tunggu 10 detik tanpa menutup toast
9. Verifikasi toast error masih tampil dan tidak hilang sendiri
10. Verifikasi popup form tetap terbuka dengan Device Name `Door Gagal {runId}-037` dipertahankan
11. Verifikasi tombol `[Save]` kembali enabled
12. Lepas intercept jaringan
13. Tutup toast error

### TC-AC-DN-168: Timeout saat Save Edit menampilkan toast koneksi dan mempertahankan popup

14. Kosongkan field Device Name lalu ketik `Door Timeout {runId}-037`
15. Atur intercept jaringan agar request penyimpanan tidak mendapat respons sampai batas waktu
16. Klik `[Save]`
17. Verifikasi toast error: "Connection problem. Please try again." tampil tanpa tombol aksi
18. Verifikasi popup form tetap terbuka dengan input dipertahankan
19. Verifikasi tombol `[Save]` kembali enabled
20. Lepas intercept jaringan
21. Tutup toast error
22. Kembalikan field Device Name ke nilai tersimpan `Door Antenna {runId}-037`
23. Tutup form lewat icon close `✕`
24. Klik `(←)` pada kotak Search

### TC-AC-DN-578: Retry Submit setelah timeout tidak membuat Device Name ganda

25. Klik `+ Device Name`
26. Ketik `Retry Device {runId}-037` pada field Device Name
27. Pilih Measurement "Unit"
28. Pilih Category "Antenna"
29. Atur intersepsi jaringan agar respons request Create dibuang setelah request mencapai server
30. Klik `[Submit]`
31. Verifikasi toast error "Connection problem. Please try again." tampil
32. Verifikasi form tetap terbuka dengan input dipertahankan
33. Hapus intersepsi jaringan
34. Tutup toast error
35. Klik `[Submit]` lagi
36. Verifikasi inline error "Device name already exists" tampil di bawah field Device Name
37. Tutup form lewat icon close `(✕)`
38. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
39. Klik `[Leave]`
40. Ketik Search `Retry Device {runId}-037`, tekan Enter
41. Verifikasi hasil Search memuat tepat satu baris `Retry Device {runId}-037`
42. Klik `(←)` pada kotak Search

## Notes

- Spec resilience (kelas b): kegagalan server, timeout, dan retry setelah timeout yang dipaksa lewat intercept di atas backend nyata (bagian 6, `FE+BE`). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan data (S-06): target Edit `Door Antenna` (Pre-setup #16) diganti record milik spec bersuffix.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); melepas intercept dan menutup toast error sebelum diasersi lagi (R-12); TC-AC-DN-168 memakai form Edit yang tetap terbuka dari TC-AC-DN-167 (form yang sama dipakai berulang; langkah buka form tidak diulang); langkah 22 mengembalikan field ke nilai tersimpan sebelum form ditutup (S-09); menutup form TC-AC-DN-578 yang dirty (S-08).
- Ukuran spec (42 langkah, di atas 35 langkah; alasan R3): satu kelas harness (b) pada Edit dan Create; tiga TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-DN-578 langkah 5 menyebut form ditutup lewat `(✕)` tanpa menyebut dialog `Unsaved Changes`; spec menambahkannya sesuai S-08.
  - Post Condition TC-AC-DN-167 ("record tidak berubah") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.
