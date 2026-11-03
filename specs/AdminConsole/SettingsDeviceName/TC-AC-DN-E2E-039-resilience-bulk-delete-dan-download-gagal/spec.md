---
id: TC-AC-DN-E2E-039-resilience-bulk-delete-dan-download-gagal
title: "Resilience: Bulk Delete Gagal/Tanpa Respons dan Download List/Changelog Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-235
  - TC-AC-DN-236
  - TC-AC-DN-368
  - TC-AC-DN-487
coverage:
  web: automated
---

# Resilience: Bulk Delete Gagal/Tanpa Respons dan Download List/Changelog Gagal

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-235, 236, 368, 487 |

- Env var password: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (dibaca saja): Device Name inti dan seed 120 baris (#16, #17) untuk TC-AC-DN-368; Riwayat Changelog Uji (#19) dan General Settings entitas uji (#20) untuk TC-AC-DN-487.
- Data milik spec (S-06, S-12): `Cable Tester {runId}-039` (Category `Accessory`, Measurement `Unit`) dan `Door Antenna {runId}-039` (Category `Antenna`, Measurement `Unit`), tanpa SKU dan tanpa unit BYO, dibuat fixture backend di hook `before` (disediakan tim FE/BE) sebagai target Bulk Delete yang gagal (record tidak terhapus). Hook `after` menghapus keduanya.
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menjawab request dengan status 500, menahan respons sampai batas waktu, dan menunda respons; intercept dilepas segera setelah pemicunya selesai (S-09). Jeda nyata 10 detik pada langkah "Tunggu 10 detik" dipilih spec untuk mengamati toast yang tidak hilang sendiri (di bawah batas ±30 detik, bagian 6).
- Kemampuan teknis lain: pemicu kegagalan download lewat intercept; pembaca berkas unduhan untuk asersi tidak ada berkas terunduh (disediakan tim FE/BE).

## Test Steps

1. Ketik Search `{runId}-039`, tekan Enter

### TC-AC-DN-235: Bulk Delete gagal karena error server mempertahankan seleksi

2. Centang checkbox baris `Cable Tester {runId}-039`
3. Centang checkbox baris `Door Antenna {runId}-039`
4. Klik tombol `Bulk Action` pada Bulk Action Bar
5. Klik `Delete`
6. Paksa respons server 500 pada request hapus massal dengan intercept jaringan
7. Klik `[Delete]` pada dialog
8. Verifikasi toast error: "Error, failed to delete device name."
9. Tunggu 10 detik tanpa menutup toast
10. Verifikasi toast tidak hilang otomatis sampai di-dismiss
11. Verifikasi Bulk Action Bar tetap tampil dengan counter `2 Device Names selected`
12. Verifikasi List di-refresh dan baris `Cable Tester {runId}-039` dan `Door Antenna {runId}-039` tampil sesuai keadaan terbaru
13. Lepas intercept jaringan
14. Tutup toast error
15. Hilangkan centang pada baris `Cable Tester {runId}-039` dan `Door Antenna {runId}-039`

### TC-AC-DN-236: Bulk Delete tanpa respons menampilkan toast koneksi dan mempertahankan seleksi

16. Centang checkbox baris `Cable Tester {runId}-039`
17. Centang checkbox baris `Door Antenna {runId}-039`
18. Klik tombol `Bulk Action` pada Bulk Action Bar
19. Klik `Delete`
20. Tunda respons request hapus massal melewati batas timeout dengan intercept jaringan
21. Klik `[Delete]` pada dialog
22. Verifikasi toast error: "Connection problem. Please try again." tanpa tombol aksi
23. Verifikasi Bulk Action Bar tetap tampil dengan counter `2 Device Names selected`
24. Verifikasi List di-refresh
25. Lepas intercept jaringan
26. Tutup toast error
27. Hilangkan centang pada baris `Cable Tester {runId}-039` dan `Door Antenna {runId}-039`
28. Klik `(←)` pada kotak Search

### TC-AC-DN-368: Download gagal menampilkan toast error tanpa ekstensi

29. Atur intercept jaringan agar permintaan download mengembalikan kegagalan server
30. Klik ikon Download lalu klik `Download as CSV`
31. Verifikasi toast error: "Error, failed to download Device-Name."
32. Tunggu 10 detik tanpa menutup toast
33. Verifikasi toast persist sampai di-dismiss
34. Verifikasi tidak ada file terunduh
35. Lepas intercept jaringan
36. Tutup toast error

### TC-AC-DN-487: Download Changelog gagal karena server error menampilkan toast error

37. Klik ikon Changelog di toolbar
38. Klik ikon Download di toolbar popup
39. Aktifkan intercept yang membuat request download gagal dengan respons server error
40. Klik "Download as CSV"
41. Verifikasi toast error persisten: "Error, failed to download Changelog-Device-Name."
42. Verifikasi toast tidak menyebut ekstensi file
43. Tunggu 10 detik tanpa menutup toast
44. Verifikasi toast tidak hilang otomatis sampai di-dismiss
45. Lepas intercept jaringan
46. Tutup toast error
47. Tutup popup "Changelog: Device Name"

## Notes

- Spec resilience (kelas b): kegagalan Bulk Delete, Bulk Delete tanpa respons, dan kegagalan Download yang dipaksa lewat intercept di atas backend nyata (bagian 6, `FE+BE`). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan data (S-06): target Bulk Delete `Cable Tester` dan `Door Antenna` (Pre-setup #16) diganti record milik spec bersuffix; daftar dipersempit lewat Search `{runId}-039` (langkah 1, R-16) agar kedua baris tampil.
- Langkah penghubung (S-03): melepas intercept dan menutup toast error sebelum diasersi lagi (R-12); menghilangkan centang (S-09); mengosongkan Search lewat `(←)`; menutup popup Changelog.
- Ukuran spec (47 langkah, di atas 35 langkah; alasan R3): satu kelas harness (b) yang memakai intercept dan satu akun; blok Bulk Delete dan Download berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-DN-235 Expected c ("tampil sesuai keadaan terbaru") tidak menyatakan keadaan terbaru yang diharapkan; spec memverifikasi kedua baris tampil karena penghapusan gagal.
  - TC-AC-DN-235 dan 236 tidak menyatakan apakah dialog Delete tertutup setelah gagal; spec membuka kembali dialog untuk TC-AC-DN-236 sesuai langkah TC.
  - Pesan toast download TC-AC-DN-368 menyebut `Device-Name` sedangkan judul TC menyebut "tanpa ekstensi"; teks toast mengikuti Expected.
