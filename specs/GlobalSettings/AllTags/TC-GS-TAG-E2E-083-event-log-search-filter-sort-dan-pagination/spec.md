---
id: TC-GS-TAG-E2E-083-event-log-search-filter-sort-dan-pagination
title: "Event Log: Search Kolom Searchable, Filter per Tab, Sort 3-State per Kelas Kolom, dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-253
  - TC-GS-TAG-254
  - TC-GS-TAG-255
  - TC-GS-TAG-256
coverage:
  web: automated
---

# Event Log: Search Kolom Searchable, Filter per Tab, Sort 3-State per Kelas Kolom, dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` tidak mengganti sesi.
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client A (dibaca saja, tidak ada aksi tulis): Seed Event Log, yaitu 14 baris Tab Activate TAG `E-01` sampai `E-14` dan 12 baris Tab Audit TAG `A-01` sampai `A-12` (Tabel Data Uji Dinamis TC; PIC `Budi S` dan `Siti A`; Hardware `Zebra RFD40 (SN-2201)` pada `E-01`, `E-03`, `A-01`). Nilai literal sesuai tabel karena asersi Search, Filter, Sort, dan hitungan bergantung padanya (pengecualian setara S-12: seeding idempotent lewat fixture BE, suite serial; mekanisme seeding disediakan tim FE/BE, lihat Temuan untuk QA).
- Event Log menumpuk antar spec (spec lain menambah baris dan tidak ada pembersihan), sehingga setiap asersi hasil Search, Filter, Sort, dan hitungan dibatasi Filter Date `07/08/26` sampai `16/09/26` (Tab Activate TAG; 14 baris) dan `08/08/26` sampai `16/09/26` (Tab Audit TAG; 12 baris). Format tanggal General Settings Client A default `dd/MM/yy`.
- Kolom tabel Event Log dibaca dengan nilai yang berbeda pada kolom yang disort/dicari/difilter: `Activity` (`Activate`, `Delete`), `PIC` (`Budi S`, `Siti A`), `Success` (22, 10, 5, 4, 3, 1, 0), `Not Found Action` (`Marked as Damaged/Missing`, `Kept previous status`, `—`) sehingga asersi memakai sedikitnya dua nilai distinct (S-11).
- Asumsi tanggal: tanggal sistem lingkungan run lebih besar dari 16/09/26; rentang Filter Date seed `07/08/26` sampai `16/09/26` (Tab Activate TAG) dan `08/08/26` sampai `16/09/26` (Tab Audit TAG) berlaku.
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel Event Log.
- State global yang diubah: tidak ada (Search, Filter, dan Sort modal Event Log tidak dipertahankan antar pembukaan modal); Rows per page modal diubah pada langkah 45 dan dipulihkan pada langkah 48.

## Test Steps

### TC-GS-TAG-253: Search Event Log pada kolom searchable

1. Klik tombol `Event Log` di toolbar
2. Klik Filter, pilih Date `07/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
3. Klik icon Search di toolbar modal
4. Verifikasi placeholder kotak search `Search PIC, hardware...`
5. Ketik Search `delete`, tekan Enter
6. Verifikasi sedikitnya satu baris tampil dan hanya baris Activity `Delete` yang tampil: `E-03`, `E-04`, `E-05`, `E-14`
7. Ganti isi kotak search dengan `zebra`, tekan Enter
8. Verifikasi hanya baris Hardware `Zebra RFD40 (SN-2201)` yang tampil: `E-01`, `E-03`
9. Ganti isi kotak search dengan `siti`, tekan Enter
10. Verifikasi hanya baris PIC `Siti A` yang tampil: `E-02`, `E-04`, `E-06` sampai `E-13`
11. Ganti isi kotak search dengan `rfid`, tekan Enter
12. Verifikasi hanya baris TAG Type RFID yang tampil: `E-01`, `E-03`, `E-14`
13. Ganti isi kotak search dengan `16/09/26`, tekan Enter
14. Verifikasi empty state `No results found` tampil (kolom Date tidak searchable)
15. Klik `(←)` pada kotak Search
16. Klik tab `Audit TAG`, klik Filter, pilih Date `08/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
17. Ketik Search `47`, tekan Enter
18. Verifikasi empty state `No results found` tampil (kolom angka tidak searchable; `47` = nilai `Found` `A-01`)
19. Ganti isi kotak search dengan `marked`, tekan Enter
20. Verifikasi hanya baris Not Found Action `Marked as Damaged/Missing` yang tampil: `A-01`, `A-04` sampai `A-12`
21. Klik `(←)` pada kotak Search

### TC-GS-TAG-254: Filter Event Log per tab, opsi populate, dan AND antar field

22. Klik tab `Activate TAG` lalu klik Filter
23. Verifikasi field Filter Panel `Date | TAG Type | Activity | Hardware | PIC`
24. Verifikasi tidak ada field `Success`, `Waiting for Approval`, dan `Failed` (kolom angka tidak memiliki field filter)
25. Verifikasi opsi `Activity` hanya `Activate` dan `Delete`
26. Verifikasi opsi `PIC` memuat `Budi S` dan `Siti A`
27. Pilih Date `07/08/26` sampai `16/09/26` dan `Activity` = `Delete`, klik `[Apply]`
28. Verifikasi hanya baris Activity `Delete` yang tampil: `E-03`, `E-04`, `E-05`, `E-14`
29. Klik Filter, tambah `PIC` = `Budi S`, klik `[Apply]`
30. Verifikasi hanya baris yang memenuhi Activity `Delete` dan PIC `Budi S` yang tampil: `E-03`, `E-05`, `E-14`
31. Hapus chip filter `Activity` dan `PIC` lewat `✕` pada tiap chip
32. Klik tab `Audit TAG`, klik Filter
33. Verifikasi field Filter Panel `Date | TAG Type | Not Found Action | Hardware | PIC`
34. Verifikasi tidak ada field `Found` dan `Not Found` (kolom angka tidak memiliki field filter)
35. Verifikasi opsi `TAG Type` hanya `RFID` dan `NFC`
36. Tutup Filter Panel dengan klik Filter

### TC-GS-TAG-255: Sort Event Log, default Date terbaru dahulu, siklus 3-state per kelas kolom

37. Klik tab `Activate TAG`, klik Filter, pilih Date `07/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
38. Verifikasi urutan awal `Date` descending: baris pertama `E-01`, baris kedua `E-02`
39. Klik header `Date` sekali
40. Verifikasi `Date` ascending (Oldest First): baris pertama `E-13` (07/08/26 09:00), baris kedua `E-12` (08/08/26 09:00)
41. Klik header `Success` dua kali
42. Verifikasi `Success` descending dari nilai terbesar: baris pertama Success `22` (`E-01`), baris kedua Success `10` (`E-02`)
43. Klik header `PIC` sekali
44. Verifikasi `PIC` berurutan berdasarkan nama lengkap A-Z: baris PIC `Budi S` (`E-01`, `E-03`, `E-05`, `E-14`) berada sebelum baris PIC `Siti A`
45. Ubah Rows per page menjadi 25 (seluruh 14 baris tampil pada satu halaman)
46. Klik header `Activity` sekali
47. Verifikasi `Activity` alfabetis: baris Activity `Activate` berada sebelum baris Activity `Delete`
48. Ubah Rows per page kembali menjadi 10
49. Klik tab `Audit TAG`, klik Filter, pilih Date `08/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
50. Klik header `Not Found Action` sekali
51. Verifikasi `Not Found Action` alfabetis: baris `A-03` (`Kept previous status`) berada sebelum baris `A-01` (`Marked as Damaged/Missing`)

### TC-GS-TAG-256: Pagination Event Log mengikuti §5

52. Tutup modal Event Log lewat `✕`, klik tombol `Event Log` di toolbar, klik Filter, pilih Date `07/08/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
53. Verifikasi Footer pagination default `Showing 1 - 10 of 14 logs`
54. Buka dropdown rows per page
55. Verifikasi pilihan `10`, `25`, `50`, `100`
56. Pindah ke halaman 2
57. Verifikasi halaman 2 memuat sisa 4 baris dari 14 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data.
- Urutan TC dalam spec sama dengan sumber (253, 254, 255, 256). Setiap blok mengosongkan Search dan menghapus chip sebelum blok berikutnya (S-09).
- Alasan spec di atas sekitar 35 langkah (57 langkah): empat TC memakai dataset Seed Event Log yang sama dan modal Event Log yang sama (prinsip 1 bagian 3, topik satu dataset), seluruhnya read-only dan satu kelas harness; pemisahan menambah login, pembukaan modal, dan penerapan Filter Date berulang. Tidak ada langkah berulang dengan ekspansi.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 2, 16, 37, 49 (Filter Date membatasi tabel pada populasi Seed Event Log karena Event Log menumpuk, S-12), langkah 3 (membuka input Search; placeholder diasersi tepat saat kotak masih kosong, S-14), langkah 15, 21 (mengosongkan Search), langkah 27 (rentang Date ikut dalam Apply pertama), langkah 31 (menghapus chip), langkah 36 (menutup panel), langkah 45 dan 48 (Rows per page 25 supaya 10 baris `Activate` dan 4 baris `Delete` tampil pada satu halaman dan urutan `Activity` teramati, lalu dipulihkan ke 10), langkah 52 (menutup dan membuka kembali modal sehingga sort kembali ke default, lalu menerapkan ulang Filter Date sebelum membaca pagination).
- Langkah 6, 8, 10, 12, 20, 28, 30 adalah asersi universal ("hanya baris ...") dan memakai baris-baris yang disebut sebagai pembanding positif; baris `No results found` pada langkah 14 dan 18 adalah anchor positif absence hasil Search.
- Expected e TC-253 menyatakan tab Activate TAG memakai `16/09/26`; pencarian Date dibuktikan lewat empty state `No results found`.
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Seed Event Log dan reset antar spec tidak didefinisikan di TC (Q-4).
  - Hitungan absolut (TC-256 "14 baris"; TC-253/254/255 daftar baris) valid hanya pada populasi yang dibatasi Filter Date; Event Log menumpuk antar spec (S-12). Pemilik TC perlu menulis ulang Data Uji sebagai Filter Date rentang seed.
  - TC-254 Expected a ("opsi `PIC` hanya admin yang tercatat"): opsi dibangun dari riwayat yang terus bertambah (admin lain dari spec lain ikut tercatat), sehingga klausa "hanya" tidak dapat diasersi utuh; spec mengasersi bahwa `Budi S` dan `Siti A` ada pada opsi.
  - TC-255 Expected d ("`PIC` berdasarkan nama lengkap A-Z, bukan format tampilan `Budi S`") tidak dapat dibedakan dari urutan format tampilan pada data seed (`Budi S` mendahului `Siti A` pada kedua cara); TC perlu data PIC yang membedakan nama lengkap dan singkatan.
  - TC-255 Expected f tidak menyebut posisi baris Not Found Action `—` (A-02); spec tidak mengasersi posisinya.
  - TC-255 Expected e (urutan `Activity`) tidak dapat diasersi pada halaman 1 berukuran 10: Filter Date `07/08/26` sampai `16/09/26` memuat 10 baris `Activate` dan 4 baris `Delete`, sehingga ascending hanya menampilkan `Activate`. Spec menaikkan Rows per page menjadi 25 (langkah 45); TC perlu menyebut ukuran halaman atau cara menjangkau baris `Delete`.
  - TC-256 Expected menyebut "halaman 2 memuat sisa baris" tanpa teks footer halaman 2; spec mengasersi 4 baris sisa saja.
