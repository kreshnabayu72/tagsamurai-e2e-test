---
id: TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan
title: "Template Self-Purchased: Brand Baru/Case-Insensitive, Batas 120 Karakter, Emoji, Terisi Sebagian, Clear Field, dan Edit Susulan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-53
  - TC-GS-TAG-54
  - TC-GS-TAG-55
  - TC-GS-TAG-56
  - TC-GS-TAG-57
  - TC-GS-TAG-58
coverage:
  web: automated
---

# Template Self-Purchased: Brand Baru/Case-Insensitive, Batas 120 Karakter, Emoji, Terisi Sebagian, Clear Field, dan Edit Susulan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Data: opsi mandiri (BYO) aktif; opsi Brand existing `Zebra` (Global Settings > Brand Client A, dibaca saja); katalog Device Name `Queclink GV300` (Admin Console Client A, dibaca saja; disediakan tim FE). Identifier uji `356938035643101` (DD-N1) dan `356938035643102` (DD-N2) tidak ada di stok resmi dan tidak ada di registri Client A; Template kosong pada awal tiap sesi.
- Brand `NovaTrack` dan `Queclink` diketik bebas; spec tidak membuat record Brand di Global Settings > Brand. Langkah akhir (TC-53 lanjutan) membaca Global Settings > Brand Client A sebagai pengamat.
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE sesuai plan bagian 6) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-55: Emoji pada Brand dan Model/Type diblok (sesi 1)

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Buka section `Self-Purchased Template`
3. Ketik `Zebra😀` pada Brand
4. Verifikasi karakter emoji tidak masuk ke field Brand
5. Ketik `ZT😀` pada Model/Type
6. Verifikasi karakter emoji tidak masuk ke field Model/Type
7. Kosongkan field Brand dan Model/Type

### TC-GS-TAG-53: Brand baru dan pencocokan case-insensitive

8. Ketik `zebra` pada Brand lalu tekan Enter
9. Verifikasi input `zebra` menjadi nilai opsi existing `Zebra` (pencocokan tidak peka huruf besar-kecil)
10. Ketik `NovaTrack` pada Brand lalu tekan Enter
11. Verifikasi input `NovaTrack` tersimpan sebagai teks pada Template

### TC-GS-TAG-54: Batas 120 karakter Brand dan Model/Type

12. Isi Brand dengan 121 karakter `A`
13. Verifikasi Brand menampilkan error inline `Max. 120 characters` langsung tanpa menunggu `Save`
14. Isi Model/Type dengan 121 karakter `B`
15. Verifikasi Model/Type menampilkan error inline `Max. 120 characters` langsung tanpa menunggu `Save`
16. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
17. Verifikasi baris `356938035643101` berstatus `Needs Info` karena field yang melebihi batas tidak dianggap terisi
18. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### TC-GS-TAG-56: Template terisi sebagian tidak menampilkan error

19. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
20. Buka section `Self-Purchased Template`
21. Isi hanya Brand `Queclink`
22. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
23. Verifikasi tidak ada error inline pada Template
24. Verifikasi baris `356938035643101` berstatus `Needs Info` dengan Device Name, SKU, Brand, dan Model/Type `—`
25. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### TC-GS-TAG-57: Clear Field mengosongkan empat field Template

26. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
27. Isi Template dengan Device Name `Queclink GV300`, Brand `Queclink`, Model/Type `GV300`
28. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
29. Klik `Clear Field`
30. Verifikasi empat field Template (Device Name, SKU, Brand, Model/Type) kosong
31. Verifikasi baris `356938035643101` (Self-Purchased) tetap di staging dengan nilai snapshot Template (Device Name `Queclink GV300`, Brand `Queclink`, Model/Type `GV300`)
32. Verifikasi halaman Activate TAG tidak tertutup
33. Verifikasi tidak ada dialog konfirmasi
34. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### TC-GS-TAG-58: Edit Template sesudahnya tidak mengubah baris

35. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
36. Isi Template Device Name `Queclink GV300` dan Brand `Queclink`
37. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
38. Ubah Brand Template menjadi `Teltonika`
39. Kosongkan seluruh Template lalu tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643102`
40. Isi kembali Template dengan Device Name `Queclink GV300` dan Brand `Queclink`
41. Verifikasi baris `356938035643101` tetap `Self-Purchased` dengan Brand `Queclink` (snapshot)
42. Verifikasi baris `356938035643102` tetap `Needs Info` walau Template diisi belakangan
43. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### TC-GS-TAG-53 (lanjutan): Brand `NovaTrack` tidak membuat record di Global Settings > Brand

44. Buka Global Settings > Brand
45. Verifikasi sedikitnya satu baris Brand tampil, termasuk `Zebra`
46. Ketik Search `NovaTrack`, tekan Enter
47. Verifikasi empty state `No results found` tampil sehingga `NovaTrack` tidak ada di Global Settings > Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (validasi Template).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah: semua blok satu kelas harness (Template di halaman Activate GPS) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Total 47 langkah, dengan empat langkah `Mulai sesi` dan empat `Kembali ke List` yang merupakan prefix berulang; blok yang hanya mengetik tanpa menambah baris (TC-55, TC-53, TC-54) memakai satu sesi (butir halaman yang sama dipakai berulang, bagian 3).
- Urutan: TC-55 (diblok) lebih dulu, lalu TC-53, TC-54, dan sesi terpisah untuk TC-56, TC-57, TC-58 karena ketiganya memakai identifier `356938035643101` pada baris baru. TC-53 lanjutan (membaca Global Settings > Brand) paling akhir karena meninggalkan halaman Activate.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Buka section` Template mengikuti TC langkah 4; `Kosongkan field Brand dan Model/Type` (langkah 7) memulihkan field sebelum TC-53; penambahan IMEI `356938035643101` pada TC-54 (langkah 16) adalah langkah penghubung untuk mengamati baris yang dibentuk dari Template (Expected b TC-54); `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-54 Expected b ("baris yang dibentuk dari Template berstatus `Needs Info`") tidak memiliki langkah menambah identifier; spec menambahkan `356938035643101` sebagai langkah penghubung (langkah 16).
  - TC-53 Expected b ("tidak membuat record baru di Global Settings > Brand") tidak memiliki langkah observasi dan permukaan Brand milik spec lain; spec mengamatinya di langkah akhir (Search `NovaTrack` di Global Settings > Brand) tanpa mengarang selektor (disediakan tim FE).
  - TC-53 Brand `zebra` dan `NovaTrack`, TC-54, TC-55, dan TC-57: field Brand adalah input pencarian/tambah; tindakan yang menyimpan nilai (Enter) hanya disebut TC-53; spec memakai Enter di TC-53 dan mengetik langsung di TC lain sesuai TC.
  - TC-58 langkah 7 memakai "Kosongkan seluruh Template" tanpa menyebut kontrol; spec memakai `Clear Field` (kontrol yang diuji TC-57).
