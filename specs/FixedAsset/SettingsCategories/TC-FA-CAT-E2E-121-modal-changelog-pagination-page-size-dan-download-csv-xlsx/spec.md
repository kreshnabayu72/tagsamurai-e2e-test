---
id: TC-FA-CAT-E2E-121-modal-changelog-pagination-page-size-dan-download-csv-xlsx
title: "Modal Changelog: Pagination dan Page Size, Navigasi Halaman, serta Download CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-412
  - TC-FA-CAT-588
  - TC-FA-CAT-587
coverage:
  web: automated
---

# Modal Changelog: Pagination dan Page Size, Navigasi Halaman, serta Download CSV dan XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Changelog CatMain bertambah oleh spec lain dan tidak pernah dikosongkan. Hitungan baris pada blok TC-FA-CAT-412 dan TC-FA-CAT-588 hanya atas baris seed Pre-setup #23, dibatasi Filter Date 20 Jun 2026 sampai 1 Jul 2026 (rentang tanggal Example Data PRD §4.1, S-14); Filter dipasang lewat langkah penghubung. Pada blok TC-FA-CAT-587 jumlah total baris Changelog (N) tidak dapat diturunkan dari seeding; N dibaca lewat kemampuan baca sebelum aksi (disediakan tim FE/BE, 8b butir 10) dan asersi isi berkas memakai N itu (S-12).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.
- Parameter nomor halaman tidak valid (dipakai pada langkah perulangan):

| Baris | Input nomor halaman |
|---|---|
| 1 | `0` |
| 2 | `99` |
| 3 | `abc` |
- Berkas hasil Download dibaca dari buffer unduhan browser (isi baris, kolom, dan urutan Sort); kemampuan membaca berkas unduhan disediakan tim FE.

## Test Steps

### TC-FA-CAT-412: Pagination Changelog default 10 dan opsi page size

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal, pilih rentang tanggal 20 Jun 2026 sampai 1 Jul 2026 pada field Date, lalu klik `[Apply]`
3. Verifikasi pagination default menampilkan 10 baris
4. Verifikasi opsi page size 10, 25, 50, 100
5. Ubah page size ke 25
6. Verifikasi page size 25 menampilkan 12 baris contoh pada satu halaman
7. Ubah page size kembali ke 10

### TC-FA-CAT-588: Navigasi paginasi Modal Changelog

8. Klik kontrol halaman berikutnya
9. Verifikasi halaman 2 memuat 2 baris sisa dari 12 baris
10. Klik kontrol halaman sebelumnya
11. Verifikasi kembali ke halaman 1 dengan 10 baris
12. Ketik halaman `2` pada input nomor halaman lalu tekan `Enter`
13. Verifikasi halaman 2 terbuka
Untuk setiap baris pada tabel "Parameter nomor halaman tidak valid" (langkah 14 sampai 15):

14. Ketik input nomor halaman baris tabel lalu tekan `Enter`
15. Verifikasi input diabaikan dan tabel tetap di halaman 2
16. Ganti sort kolom Action
17. Verifikasi ganti sort tetap di halaman 2
18. Ubah page size ke 25
19. Verifikasi ganti page size ke 25 kembali ke halaman 1 dan menampilkan 12 baris pada satu halaman
20. Ubah page size kembali ke 10
21. Pindah ke halaman 2 lalu klik icon Search, ketik `e`, dan tekan `Enter`
22. Verifikasi Search `e` mereset tabel ke halaman 1
23. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong, kemudian pindah ke halaman 2
24. Klik icon Filter, pilih rentang Date yang mencakup seluruh 12 baris, lalu klik `[Apply]`
25. Verifikasi Apply Filter mereset tabel ke halaman 1
26. Klik Clear Filter lalu klik icon Close (✕) pada modal Changelog

### TC-FA-CAT-587: Download Modal Changelog

27. Klik icon Changelog di Table Tools
28. Catat N jumlah total baris Changelog CatMain tanpa Search dan Filter (kemampuan baca)
29. Klik Download > `Download as CSV` tanpa Search/Filter (pagination 10)
30. Verifikasi berkas pertama bernama `Changelog-Category.csv`
31. Verifikasi berkas memuat seluruh N baris Changelog yang dicatat sebelum unduh (bukan hanya 10 baris halaman aktif)
32. Klik icon Search, ketik `Electronics`, tekan `Enter`, lalu klik Download > `Download as CSV`
33. Verifikasi berkas kedua hanya memuat baris yang cocok dengan `Electronics`
34. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong
35. Klik header Actions (⋯) > `Setup Column...`, hilangkan centang kolom `Field`, klik `[Save]`, lalu klik Download > `Download as CSV`
36. Verifikasi tidak ada toast atau peringatan
37. Verifikasi berkas tidak memuat kolom `Field`
38. Klik header Actions (⋯) > `Setup Column...`, centang kolom `Field`, klik `[Save]`, lalu klik Download > `Download as CSV`
39. Verifikasi kolom `Field` kembali ikut ter-export
40. Klik icon Search, ketik `tidak-ada-xyz`, dan tekan `Enter`
41. Verifikasi tombol Download tetap aktif pada hasil nol baris
42. Klik Download > `Download as CSV`
43. Verifikasi tidak ada toast
44. Verifikasi berkas hanya berisi baris header kolom yang visible
45. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong
46. Klik header kolom Date sampai Sort menjadi Oldest First, lalu klik Download > `Download as XLSX`
47. Verifikasi berkas `Changelog-Category.xlsx` berurut Date dari yang terlama mengikuti Sort aktif
48. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Alasan di atas sekitar 35 langkah: langkah 14 sampai 15 diulang pada tiga input tidak valid (ekspansi 6 langkah menggantikan 2) sehingga total ekspansi 52 langkah (48 langkah bernomor) (melampaui 35). Ketiga TC memakai modal Changelog yang sama dengan 12 baris seed Pre-setup #23 dan state halaman, page size, Search, dan Sort dikembalikan sebelum TC berikutnya (S-09); memecahnya akan mengulang pembukaan modal dan pemulihan Setup Column tanpa manfaat (8b butir 7).
- Urutan (8b butir 11): pada TC-FA-CAT-587, absence toast diasersi tepat sesudah klik Download (langkah 36 setelah langkah 35 dan langkah 43 setelah langkah 42) sebelum asersi isi berkas.
- Langkah penghubung (S-03, S-14): langkah 2 membatasi Changelog ke rentang Date baris seed Pre-setup #23; langkah 7 dan 20 mengembalikan page size ke 10; langkah pencatatan N; langkah pembersih Search dan Filter di antara TC (R-12); dan langkah penutup modal.
- TC-FA-CAT-587 berHINT `f` (buffer biner): berkas unduhan dibaca lewat kemampuan tim FE (lihat Prerequisites); sisa TC tidak membutuhkan buffer.
- Expected TC-FA-CAT-588 butir a dipecah menjadi dua Verifikasi (halaman 2 dan kembali ke halaman 1), butir b menjadi satu Verifikasi per input (langkah 15 per iterasi), butir e menjadi dua Verifikasi (Search dan Apply Filter).
- Temuan untuk QA:
  - TC-FA-CAT-412 langkah 2 menggabungkan pengamatan default dan pengubahan page size; spec memisahkannya agar tiap klausa Expected diasersi.
  - TC-FA-CAT-588 langkah 7 dan 8 memindahkan ke halaman 2 tanpa menyebut cara mengosongkan Search sebelumnya; spec menambahkan langkah pembersih Search.
  - TC-FA-CAT-587 butir c ("tanpa toast atau peringatan") tidak memberi cara mengamati absence toast; spec memakai asersi pada UI tanpa observasi lanjutan.
