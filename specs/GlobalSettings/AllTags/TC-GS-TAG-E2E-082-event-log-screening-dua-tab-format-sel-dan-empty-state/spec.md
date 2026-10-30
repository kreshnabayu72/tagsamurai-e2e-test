---
id: TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state
title: "Modal Event Log: Screening Tab Activate TAG dan Audit TAG, Format Sel, Tombol Hidden di Tab Paired, dan Empty State S-04"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-247
  - TC-GS-TAG-248
  - TC-GS-TAG-249
  - TC-GS-TAG-250
  - TC-GS-TAG-251
  - TC-GS-TAG-252
coverage:
  web: automated
---

# Modal Event Log: Screening Tab Activate TAG dan Audit TAG, Format Sel, Tombol Hidden di Tab Paired, dan Empty State S-04

## Prerequisites

- Mode: FE+BE.
- Akun aktor utama: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` mengembalikan sesi ke akun ini.
- Akun kedua (langkah 42 sampai 44, TC-252): Total Control Client Empty Budi Santoso `totalControl_automated_qaEmpty@qwertysystem.net`; kredensial `Spectra.env.GS_TC_EMPTY_PASSWORD` (terdaftar di `.env.example`). Client Empty tanpa tag dan tanpa riwayat sesi.
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client A (dibaca saja, tidak ada aksi tulis): Seed Event Log, yaitu 14 baris Tab Activate TAG `E-01` sampai `E-14` dan 12 baris Tab Audit TAG `A-01` sampai `A-12` (Tabel Data Uji Dinamis TC). Nilai literal sesuai tabel karena asersi isi sel dan urutan bergantung padanya (pengecualian setara S-12: seeding idempotent lewat fixture BE, dilewati bila sudah ada, suite serial). Mekanisme dan endpoint seeding tidak didefinisikan di TC dan disediakan tim FE/BE (lihat Temuan untuk QA). Seed Registri A dipakai untuk tombol Event Log di Tab Paired (TC-251).
- Event Log menumpuk antar spec (spec lain menambah baris dan tidak ada pembersihan), sehingga hitungan footer tidak diasersi sebagai total absolut tanpa batas: tabel dibatasi Filter Date `07/08/26` sampai `16/09/26` (Tab Activate TAG; 14 baris: `E-13` 07/08/26 sampai `E-01` 16/09/26) dan `08/08/26` sampai `16/09/26` (Tab Audit TAG; 12 baris: `A-12` 08/08/26 sampai `A-01` 16/09/26), format tanggal General Settings Client A default `dd/MM/yy` 24-hour.
- Asumsi tanggal: tanggal sistem lingkungan run lebih besar dari 16/09/26; rentang Filter Date seed `07/08/26` sampai `16/09/26` (Tab Activate TAG) dan `08/08/26` sampai `16/09/26` (Tab Audit TAG) berlaku.
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel Event Log; mengarahkan kursor ke tombol toolbar dan ikon TAG Type untuk membaca tooltip; mengganti akun (Logout lalu login) di tengah spec.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-TAG-247: Screening modal Event Log, tab Activate TAG aktif default

1. Arahkan kursor ke tombol `Event Log` di toolbar
2. Verifikasi tooltip `Event Log`
3. Verifikasi tombol `Event Log` hanya berikon (tanpa teks)
4. Klik tombol `Event Log`
5. Verifikasi judul modal `Event Log`
6. Verifikasi tab `Activate TAG` (aktif) dan `Audit TAG` pada header modal
7. Verifikasi Toolbar modal `Search | Filter | Download`
8. Verifikasi kolom berurutan `Date (sortable) | TAG Type (sortable) | Activity (sortable) | Success (sortable) | Waiting for Approval (sortable) | Failed (sortable) | Hardware (sortable) | PIC (sortable) | Column Visibility (⋯) (unsortable)`
9. Klik Filter di toolbar modal, pilih Date `07/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
10. Verifikasi sedikitnya satu baris tampil dan sel Actions setiap baris memuat `Detail`
11. Verifikasi baris diurutkan Date terbaru dahulu: baris pertama `E-01` (16/09/26 14:30), baris kedua `E-02` (15/09/26 09:10)
12. Verifikasi Footer pagination `Showing 1 - 10 of 14 logs`

### TC-GS-TAG-248: Screening Tab Audit TAG pada modal Event Log

13. Klik tab `Audit TAG`
14. Verifikasi kolom berurutan `Date (sortable) | TAG Type (sortable) | Found (sortable) | Not Found (sortable) | Not Found Action (sortable) | Hardware (sortable) | PIC (sortable) | Column Visibility (⋯) (unsortable)`
15. Klik Filter, pilih Date `08/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
16. Verifikasi sedikitnya satu baris tampil dan sel Actions setiap baris memuat `Detail`
17. Verifikasi kolom `Not Found Action` dan kolom lain pada baris `A-01` tampil sebagai plain text (bukan badge)
18. Verifikasi urutan awal Date terbaru dahulu: baris pertama `A-01` (16/09/26 10:00), baris kedua `A-02` (13/09/26 13:20)
19. Verifikasi Footer pagination `Showing 1 - 10 of 12 logs`
20. Klik header `Not Found Action` sekali
21. Verifikasi baris pertama berurutan menurut `Not Found Action` (sort aktif): baris `A-03` (`Kept previous status`) berada sebelum baris `A-01` (`Marked as Damaged/Missing`)
22. Ketik Search `marked`, tekan Enter
23. Verifikasi sedikitnya satu baris tampil dan setiap baris yang tampil memuat Not Found Action `Marked as Damaged/Missing`
24. Klik `(←)` pada kotak Search
25. Klik Filter, buka dropdown field `Not Found Action`
26. Verifikasi field `Not Found Action` berupa multi-select dengan kotak pencarian opsi (searchable)
27. Tutup Filter Panel dengan klik Filter, lalu klik header `Not Found Action` dua kali lagi (urutan kembali ke Date terbaru dahulu)

### TC-GS-TAG-249: Format isi sel Event Log, Mixed, Waiting for Approval untuk Delete, dan Hardware kosong

28. Klik tab `Activate TAG`, klik Filter, pilih Date `07/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
29. Verifikasi baris `E-03` (14/09/26 16:45): Activity `Delete`, Success `3`, Waiting for Approval `—`, Failed `0`, Hardware `Zebra RFD40 (SN-2201)`
30. Verifikasi TAG Type baris `E-05` (13/09/26 10:00) `Mixed`
31. Verifikasi Hardware baris `E-02` (15/09/26 09:10) `—`
32. Verifikasi nilai count 0 tampil `0`, bukan `—`: Failed baris `E-03` `0` dan Waiting for Approval baris `E-02` `0`
33. Arahkan kursor ke ikon TAG Type baris `E-01` (16/09/26 14:30)
34. Verifikasi label tooltip `RFID`

### TC-GS-TAG-250: Format sel Tab Audit, Not Found Action sesuai pilihan checkbox

35. Klik tab `Audit TAG`, klik Filter, pilih Date `08/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
36. Verifikasi Not Found Action baris `A-01` (16/09/26 10:00) `Marked as Damaged/Missing`
37. Verifikasi Not Found Action baris `A-02` (13/09/26 13:20) `—`
38. Verifikasi Not Found Action baris `A-03` (12/09/26 08:30) `Kept previous status`

### TC-GS-TAG-251: Tombol Event Log Hidden di Tab Paired

39. Tutup modal Event Log lewat `✕`, lalu klik Tab `Paired`
40. Verifikasi toolbar Tab Paired tampil (Table Tools `Search` dan `Filter` tampil)
41. Verifikasi tombol `Event Log` tidak tampil di toolbar Tab Paired

### TC-GS-TAG-252: Empty state S-04 saat belum ada riwayat

42. Klik avatar akun, pilih `Logout`
43. Login sebagai Total Control Client Empty Budi Santoso (`Spectra.env.GS_TC_EMPTY_PASSWORD`)
44. Buka Global Settings > TAG, Tab All
45. Klik tombol `Event Log` di toolbar
46. Verifikasi Tab Activate TAG menampilkan empty state `No logs found` dengan deskripsi `History records will appear after activation or audit sessions are completed.`
47. Klik tab `Audit TAG`
48. Verifikasi Tab Audit TAG menampilkan empty state `No logs found` dengan deskripsi `History records will appear after activation or audit sessions are completed.`
49. Tutup modal Event Log lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data dan tidak menghapus apa pun.
- Urutan TC dalam spec: 247, 248, 249, 250, 251, 252. Screening di awal; TC-252 di akhir karena butuh ganti akun eksplisit (langkah 42 sampai 44) dan bagian itu tetap bermakna bila bagian sebelumnya gagal; TC-251 (Tab Paired) mendahului ganti akun.
- Alasan spec di atas sekitar 35 langkah (49 langkah): seluruh blok berkelas sama (baca modal Event Log, read-only), memakai dataset Seed Event Log yang sama, dan berurutan dari modal yang sama; kegagalan membuka modal Event Log membuat blok TC-247 sampai TC-250 kehilangan makna. Tidak ada langkah berulang dengan ekspansi.
- Urutan langkah 1 sampai 4 berbeda dari TC-247 (hover lalu klik): tombol tertutup oleh modal setelah dibuka, sehingga tooltip diasersi sebelum klik (bagian 8b butir 5).
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 9, 15, 28, 35 (Filter Date membatasi tabel pada populasi Seed Event Log karena Event Log menumpuk, S-12; tanpa pembatas, baris baru spec lain mengisi halaman 1 dan hitungan footer berubah), langkah 20 dan 22 sampai 27 (aksi sort, Search, dan Filter Panel untuk Expected c TC-248), langkah 24 dan 27 (mengosongkan Search dan mengembalikan sort ke urutan awal, S-09), langkah 39 (menutup modal), langkah 42 sampai 44 (ganti akun), langkah 49 (menutup modal).
- Retensi Filter Date antar tab dan antar pembukaan modal tidak ditetapkan TC; Filter Date diterapkan ulang pada tiap tab sebelum membaca baris sehingga tidak bergantung pada retensi itu.
- Langkah 10 dan 16 (Detail pada setiap baris) memakai baris sebagai pembanding sebelum asersi universal; langkah 23 memakai pembanding sedikitnya satu baris.
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Seed Event Log (E-01..E-14, A-01..A-12) dan reset antar spec tidak didefinisikan di TC (Q-4).
  - TC-247 Expected f dan TC-248 Expected e menyatakan hitungan absolut ("of 14 logs", "of 12 logs"); Event Log menumpuk antar spec sehingga hitungan hanya valid pada populasi yang dibatasi Filter Date. Pemilik TC perlu menulis ulang Data Uji sebagai Filter Date rentang seed atau hitungan relatif (S-12).
  - TC-248 Expected b menyebut kolom `Activity` pada Tab Audit TAG, sedangkan daftar kolom Expected a tidak memuat `Activity`; spec mengasersi kolom `Not Found Action` dan kolom lain sebagai plain text pada baris `A-01` dan tidak mengasersi kolom `Activity` yang tidak ada.
  - TC-248 Expected c ("`Not Found Action` dapat di-sort dan dicari") tidak menyebut nilai urutan; spec hanya mengasersi urutan relatif `A-03` terhadap `A-01` (alfabetis `Kept previous status` sebelum `Marked as Damaged/Missing`).
  - TC-251 tidak menyebut kontrol Table Tools lain di toolbar Tab Paired; spec memakai `Search` dan `Filter` sebagai anchor permukaan (bagian 8b butir 2).
