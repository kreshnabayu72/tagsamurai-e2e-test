---
id: TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click
title: "Bulk Delete Berhasil: Homogen, Campuran, Seleksi Lintas Search, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-115
  - TC-GS-UOM-116
  - TC-GS-UOM-118
  - TC-GS-UOM-280
  - TC-GS-UOM-281
coverage:
  web: automated
---

# Bulk Delete Berhasil: Homogen, Campuran, Seleksi Lintas Search, dan Klik Ganda

## Prerequisites

- Mode: FE+BE, dengan intercept parsial di atas backend nyata (TC-GS-UOM-281).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca): `Box` / `box` (in-use FAMS: 4 asset names) hanya ikut dicentang pada TC-GS-UOM-118 dan dilewati oleh server (tidak terhapus, tidak berubah; pengecualian S-06 untuk baris in-use yang dilewati).
- Data dinamis (seeding lewat API di hook `before`, semuanya bebas relasi; tidak menumpang spec lain; menggantikan `Centimeter`, `Millimeter`, `Liter`, `Pack` pada TC sumber agar baris Population dan Pre-setup tidak terhapus, S-06):
  - TC-GS-UOM-115: `Cent {runId}-034` / `cn34` dan `Mill {runId}-034` / `ml34`.
  - TC-GS-UOM-116 dan TC-GS-UOM-118: `Lit {runId}-034` / `lt34` dan `Pak {runId}-034` / `pk34`.
  - TC-GS-UOM-280 (D-21): `Cup {runId}-034` / `cup`, `Spoon {runId}-034` / `spn`, dan `Plate {runId}-034` / `plt`.
  - TC-GS-UOM-281 (D-22): `Bowl {runId}-034` / `bwl` dan `Dish {runId}-034` / `dsh`.
- Cleanup di hook `after` (tidak berasumsi seeding atau penghapusan berhasil penuh): hapus lewat API semua unit yang namanya memuat ` {runId}-034` bila masih ada.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request Delete Measurement (`DELETE /v2/enterprise-management/measurements`) selama 2 detik (TC-GS-UOM-281) lalu melepasnya; klik ganda cepat pada `[Delete]`; opsi page size 100 pada pagination.
- State global yang diubah: page size pagination (diubah ke 100 di langkah 1, dikembalikan ke 10 di langkah 43; hook `after` menjadi cadangan). Tidak ada state global lain yang diubah.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).

## Test Steps

### Persiapan

1. Ubah page size tabel menjadi 100

### TC-GS-UOM-115: Konfirmasi Bulk Delete homogen menghapus seluruh unit terpilih

2. Centang `Cent {runId}-034` dan `Mill {runId}-034`
3. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
4. Klik [Delete] pada dialog
5. Verifikasi toast `Success, unit has been deleted.`
6. Tutup toast
7. Verifikasi `Cent {runId}-034` dan `Mill {runId}-034` hilang dari tabel
8. Verifikasi Bulk Action Bar hilang

### TC-GS-UOM-116 dan TC-GS-UOM-118: Bulk Delete campuran, dialog dua kelompok, dan Continue

9. Centang `Lit {runId}-034`, `Pak {runId}-034`, dan `Box`
10. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
11. Verifikasi dialog Title `Delete Units` (warning)
12. Verifikasi kelompok `The following will be deleted:` berisi `Lit {runId}-034` dan `Pak {runId}-034`
13. Verifikasi kelompok `The following are still in use and will be skipped:` berisi `Box` dengan sub-bullet `FAMS (4 asset names)`
14. Verifikasi kalimat `Are you sure you want to continue? This action cannot be undone.`
15. Verifikasi tombol `[Cancel]` dan `[Continue]` (danger)
16. Klik [Continue]
17. Verifikasi toast `Success, unit has been deleted. Some items were skipped.`
18. Tutup toast
19. Verifikasi `Lit {runId}-034` dan `Pak {runId}-034` hilang dari tabel
20. Verifikasi `Box` tetap ada di tabel
21. Verifikasi Bulk Action Bar hilang
22. Verifikasi seleksi di-reset ke 0
23. Verifikasi checkbox `Box` tidak lagi tercentang

### TC-GS-UOM-280: Bulk Delete berlaku untuk seluruh seleksi termasuk baris yang tidak tampil karena Search

24. Centang `Cup {runId}-034`, `Spoon {runId}-034`, dan `Plate {runId}-034`
25. Ketik Search `Cup {runId}-034`, tekan Enter
26. Verifikasi hanya baris `Cup {runId}-034` tampil di tabel
27. Verifikasi counter `3 units selected`
28. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
29. Verifikasi dialog `Delete Units` memuat bullet `Cup {runId}-034`, `Plate {runId}-034`, dan `Spoon {runId}-034`
30. Klik [Delete] pada dialog
31. Verifikasi toast `Success, unit has been deleted.`
32. Tutup toast
33. Klik `(←)` pada kotak Search
34. Verifikasi `Cup {runId}-034`, `Spoon {runId}-034`, dan `Plate {runId}-034` tidak ada di tabel

### TC-GS-UOM-281: Klik ganda konfirmasi Bulk Delete hanya memproses satu penghapusan

35. Pasang intercept yang menahan respons Delete Measurement selama 2 detik
36. Centang `Bowl {runId}-034` dan `Dish {runId}-034`
37. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
38. Klik [Delete] pada dialog dua kali cepat
39. Verifikasi tepat satu toast `Success, unit has been deleted.`
40. Verifikasi tidak ada toast error dari klik kedua
41. Verifikasi `Bowl {runId}-034` dan `Dish {runId}-034` hilang dari tabel
42. Lepas intercept respons Delete Measurement
43. Ubah page size tabel kembali ke 10

## Notes

- Mode: FE+BE (intercept parsial untuk TC-GS-UOM-281). Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 43.
- Urutan TC dalam spec: 115, 116/118, 280, 281 (urutan sumber 115, 116, 118, 280, 281). Aksi menghapus data adalah inti spec ini; tiap blok memakai unit milik sendiri sehingga urutan tidak saling bergantung, dan blok klik ganda (TC-281) di akhir. TC-GS-UOM-116 (screening dialog campuran) dan TC-GS-UOM-118 (`[Continue]`) berbagi satu pembukaan dialog, jadi digabung. Dependensi `TC-GS-UOM-36` dan TC-GS-UOM-116 dipenuhi oleh seeding spec sendiri (S-04).
- Page size 100 (langkah 1) membuat seluruh baris tabel (20 baris baseline + unit milik spec) tampil di satu halaman sehingga unit target dan `Box` dicentang tanpa pindah halaman; Search hanya dipakai pada TC-GS-UOM-280, yang memang menguji seleksi lintas Search.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 43 (page size), semua langkah "Tutup toast" (S-09: toast sukses identik berulang di-dismiss sebelum diasersi lagi), langkah 33 (mengosongkan Search lewat `(←)`, sebelum asersi hilangnya unit di tabel penuh), dan langkah 42 (melepas intercept, S-09). Langkah 35 adalah langkah 1 TC-281.
- Asersi hitungan toast pada langkah 39 didahului "Tutup toast" pada langkah 32 sehingga toast lama tidak terhitung (butir 8b).
- Asersi absence pada langkah 7, 19, 34, dan 41 memakai toast sukses langkah 5, 17, 31, dan 39 sebagai anchor (butir 2 bagian 8b); langkah 34 juga didahului pengosongan Search sehingga tabel penuh tampil.
- `Box` pada TC-118 adalah baris Pre-setup in-use yang dilewati server; tidak diubah (S-06).
- Spec ini di atas batas 35 langkah (43): seluruhnya satu kelas (Bulk Delete sukses, destruktif, di akhir) dengan data milik spec per blok; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-GS-UOM-116 menyebut `Liter` dan `Pack` bebas relasi serta `Box` in-use pada baseline Pre-setup; spec memakai unit milik sendiri sebagai pengganti `Liter` dan `Pack` karena TC-GS-UOM-118 menghapusnya secara permanen. Nama pada Expected TC diganti nama bersuffix.
