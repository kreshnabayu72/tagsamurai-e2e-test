---
id: TC-FA-RP-E2E-156-tab-read-only-search-filter-sort-download-setup-column-dan-1
title: "Tab Read Only: Search, Filter, Sort, Download, Setup Column, dan menu baris (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-532
  - TC-FA-RP-533
  - TC-FA-RP-534
coverage:
  web: automated
---

# Tab Read Only: Search, Filter, Sort, Download, Setup Column, dan menu baris (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #37 (Tab Read Only empat baris: Dewi Anggraini, Maya Anggraeni, Yoga Pratama, Gilang Prakoso). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`. Pre-setup #36 disebut Precondition TC sumber tetapi tidak dipakai langkah.
- Tabel Search per kelas (TC-FA-RP-532):

| Kolom | Keyword | Baris yang tampil |
|---|---|---|
| Name | `dewi` | hanya Dewi Anggraini |
| Position | `COMPLIANCE` | hanya Maya Anggraeni (Compliance Analyst) |
| Division | `internal audit` | Dewi Anggraini dan Gilang Prakoso |
| Modified By | `prasetyo` | hanya Maya Anggraeni |
| Status | `inactive` | hanya Yoga Pratama |

## Test Steps

### Search per kelas teks dan badge (TC-FA-RP-532)

1. Klik Tab `Read Only`
2. Klik ikon Search
3. Untuk setiap baris pada Tabel Search per kelas, lakukan langkah 4 sampai 6
4. Ketik Search `<Keyword>`, tekan Enter
5. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
6. Kosongkan isi kotak search, tekan Enter

### Filter Status dan Activation Status (TC-FA-RP-533)

7. Klik ikon Filter
8. Pilih opsi `Inactive` pada field Status, klik `[Apply]`
9. Verifikasi hanya baris Yoga Pratama yang tampil
10. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`
11. Klik ikon Filter, pilih opsi `Pending Activation` pada field Activation Status, klik `[Apply]`
12. Verifikasi hanya baris Gilang Prakoso yang tampil
13. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

### Sort default dan siklus tiga state (TC-FA-RP-534)

14. Verifikasi urutan awal: Dewi Anggraini, Gilang Prakoso, Maya Anggraeni, Yoga Pratama
15. Klik header Name sekali
16. Verifikasi klik 1 ascending (urutan sama): Dewi Anggraini, Gilang Prakoso, Maya Anggraeni, Yoga Pratama
17. Klik header Name sekali lagi
18. Verifikasi klik 2 descending: Yoga Pratama, Maya Anggraeni, Gilang Prakoso, Dewi Anggraini
19. Klik header Name sekali lagi
20. Verifikasi klik 3 kembali ke default: Dewi Anggraini, Gilang Prakoso, Maya Anggraeni, Yoga Pratama

## Notes

- Langkah yang diulang: 4 sampai 6 (lima iterasi menurut Tabel Search per kelas); `Verifikasi` tiap iterasi satu per klausa Expected a sampai e (S-01). Jumlah langkah nominal 20; ekspansi blok ulang ke lima iterasi menjadi 32.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik Tab `Read Only` dan ikon Search (langkah 1 dan 2); membuka Filter Panel dan membersihkan Filter (langkah 7, 10, 11, 13); langkah 6 mengosongkan Search sebelum iterasi berikut; klik header Name pada langkah 15, 17, 19 membangun siklus sort.
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-532 langkah 2 "Buka Search" tanpa Enter; spec membuka kotak Search lewat ikon Search (langkah 2) lalu mengetik pada langkah 4.
  - Precondition ketiga TC menyebut Pre-setup #36 yang tidak dipakai langkah maupun Expected; spec tidak memakainya.
  - TC tidak menyebut apakah Filter Panel menutup setelah `[Apply]`; spec mengasumsikan panel menutup dan membukanya ulang lewat ikon Filter sebelum `[Clear Field]`.
  - TC-FA-RP-534 Expected b "klik 1 ascending (urutan sama)" memakai urutan default sebagai ascending Name; spec mengasersi urutan sama dengan default.
