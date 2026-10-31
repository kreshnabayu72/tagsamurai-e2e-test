---
id: TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance
title: "Used By (Items) = Total Item pada Instance Client, Principal, dan Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-368
  - TC-GS-UOM-369
  - TC-GS-UOM-370
coverage:
  web: automated
tags: [principal]
---

# Used By (Items) = Total Item pada Instance Client, Principal, dan Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1 (awal spec): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before`. Dipakai untuk TC-GS-UOM-368.
- Akun aktor 2 (ganti akun di langkah 9 sampai 11): Total Control Principal (Hendra Wijaya) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`). Dipakai untuk TC-GS-UOM-369.
- Akun aktor 3 (ganti akun di langkah 18 sampai 20): Total Control Distributor (Bayu Pratama) `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`). Dipakai untuk TC-GS-UOM-370. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`) karena spec berakhir di Distributor. Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, dan `GS_DISTRIBUTOR_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup (hanya dibaca, spec tidak membuat atau mengubah data). Pre-setup Principal dan Distributor adalah data environment tetap.
  - Client A (dicari lewat Search `<Unit Name>` karena baris bisa berada di halaman selain halaman 1; Accordion Device Name List tidak dirender pada instance Client):

    | Unit Name | Used By (Items) | Baris Item Type List | Referensi (Data Uji TC) |
    |---|---|---|---|
    | Pieces | 3 | 3 | Laptop, Monitor, Printer Ink |
    | Dozen | 2 | 2 | Egg Tray, Egg Carton |
    | Gram | 1 | 1 | Gold Bar |

  - Principal (instance berisi tiga unit Pre-setup Principal sehingga baris ada di halaman 1 tanpa Search):

    | Unit Name | Used By (Items) | Item Type List | Device Name List | Referensi (Data Uji TC) |
    |---|---|---|---|---|
    | Ampere | 3 | 2 baris | 1 baris | Item Type: Power Meter, Battery Pack; Device Name: Fixed Reader |
    | Watt | 2 | empty state `No item types linked` | 2 baris | Device Name: BLE Gateway, Handheld Reader |
    | Volt | 0 | empty state `No item types linked` | empty state `No device names linked` | bebas relasi |

  - Distributor: Hertz (Used By (Items) `0`, bebas relasi); instance berisi unit Pre-setup Distributor sehingga baris ada di halaman 1 tanpa Search.
- Guided Tooltip: flag halaman Measurement untuk ketiga akun aktor mengikuti pernyataan hook suite di `suite.md`.
- Layar awal akun default dibuka hook `beforeEach` suite; untuk Principal dan Distributor layar dibuka lewat langkah spec setelah login.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-UOM-368: Angka Used By (Items) sama dengan jumlah baris Detail pada instance Client (tanpa Device Name)

Untuk setiap baris tabel Client A pada Prerequisites (Pieces, Dozen, Gram) lakukan langkah 1 sampai 8:

1. Ketik Search `<Unit Name>`, tekan Enter
2. Verifikasi Used By (Items) baris `<Unit Name>` sesuai kolom Used By (Items) tabel Client A
3. Klik `⋯` baris `<Unit Name>` > Detail
4. Verifikasi jumlah baris Accordion Item Type List di Detail sesuai kolom Baris Item Type List tabel Client A
5. Verifikasi Accordion Device Name List tidak dirender
6. Verifikasi angka Used By (Items) sama dengan `Total Item` di header Detail unit yang sama
7. Tutup Modal Unit Detail lewat `[✕]`
8. Klik `(←)` pada kotak Search

### Ganti akun ke Principal

9. Logout dari Total Control Client A
10. Login sebagai Total Control Principal
11. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-369: Angka Used By (Items) pada instance Principal = baris Item Type + baris Device Name

Untuk setiap baris tabel Principal pada Prerequisites (Ampere, Watt, Volt) lakukan langkah 12 sampai 17:

12. Verifikasi Used By (Items) baris `<Unit Name>` sesuai kolom Used By (Items) tabel Principal
13. Klik `⋯` baris `<Unit Name>` > Detail
14. Verifikasi Accordion Item Type List di Detail sesuai kolom Item Type List tabel Principal
15. Verifikasi Accordion Device Name List di Detail sesuai kolom Device Name List tabel Principal
16. Verifikasi angka Used By (Items) sama dengan `Total Item` di header Detail unit yang sama
17. Tutup Modal Unit Detail lewat `[✕]`

### Ganti akun ke Distributor

18. Logout dari Total Control Principal
19. Login sebagai Total Control Distributor
20. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-370: Instance Distributor: Used By (Items) bernilai 0 dan Device Name List kosong dihitung nol

21. Perhatikan Used By (Items) baris Hertz
22. Verifikasi Used By (Items) Hertz tampil `0`
23. Klik angka `0` pada baris Hertz
24. Verifikasi Modal Unit Detail Hertz terbuka
25. Verifikasi Total Item `0`
26. Verifikasi Accordion Device Name List dirender dengan empty state `No device names linked`
27. Verifikasi Accordion Item Type List menampilkan empty state `No item types linked`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang: langkah 1 sampai 8 diulang untuk tiga baris tabel Client A (ekspansi 24 langkah) dan langkah 12 sampai 17 untuk tiga baris tabel Principal (ekspansi 18 langkah); parameter tiap iterasi ada di tabel Prerequisites. Dengan ekspansi, spec sekitar 55 langkah, di atas batas 35 langkah. Alasan: ketiga blok satu kelas harness (baca UI) dengan topik yang sama (kesamaan Used By (Items) dan Total Item), tidak membuat data, dan memakai Step ganti akun eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, ganti akun kasus b).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (Search nama unit untuk menemukan baris Client A), 7 dan 17 (menutup Modal Unit Detail), 8 (mengosongkan Search), 9 sampai 11 dan 18 sampai 20 (ganti akun dan membuka layar Measurement).
- Hitungan Device Name pada Principal dan Distributor (Used By (Items) = baris Item Type + baris Device Name) mengikuti TC-GS-UOM-369; baris Item Type List dan Device Name List pada tabel Prerequisites memakai kolom "Referensi" hanya sebagai keterangan data Pre-setup (nama referensi tidak diasersi karena Expected TC hanya menyebut jumlah baris dan empty state).
- Temuan untuk QA: TC-GS-UOM-369 dan TC-GS-UOM-370 tidak menyebut apakah instance Principal dan Distributor berisi unit lain di luar Pre-setup; spec mengasumsikan tidak ada sehingga baris ada di halaman 1 tanpa Search.
