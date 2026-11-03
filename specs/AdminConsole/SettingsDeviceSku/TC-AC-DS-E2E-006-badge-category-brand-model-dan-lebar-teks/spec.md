---
id: TC-AC-DS-E2E-006-badge-category-brand-model-dan-lebar-teks
title: "Badge Category, Brand, dan Model/Type: Teks Penuh, Pemotongan di Atas 25 Karakter, serta Device Name dan SKU Panjang"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-18
  - TC-AC-DS-19
  - TC-AC-DS-20
  - TC-AC-DS-21
  - TC-AC-DS-22
  - TC-AC-DS-23
  - TC-AC-DS-24
  - TC-AC-DS-25
coverage:
  web: automated
---

# Badge Category, Brand, dan Model/Type: Teks Penuh, Pemotongan di Atas 25 Karakter, serta Device Name dan SKU Panjang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100`: Category `UHF Handheld`, Brand `Arcturus`, Model/Type `H100`; `HHR-BIG-01`: Device Name `Industrial Handheld Reader`, Category `Perangkat Pemindai Kode Batang Industri` 39 karakter, Brand `International Scanner Solutions` 31 karakter, Model/Type `Industrial Handheld Reader Series Alpha` 39 karakter) dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Tabel "Badge yang diuji" (aturan pemotongan: lebih dari 25 karakter ditampilkan 12 huruf pertama + `..` + 12 huruf terakhir):

| Kolom | SKU | Teks badge | Teks tooltip |
|---|---|---|---|
| Category | `HHR-ARC-100` | `UHF Handheld` | `Hardware > Handheld Reader > UHF Handheld` |
| Category | `HHR-BIG-01` | `Perangkat Pe..ang Industri` | `Hardware > Handheld Reader > Perangkat Pemindai Kode Batang Industri` |
| Brand | `HHR-ARC-100` | `Arcturus` | `Arcturus` |
| Brand | `HHR-BIG-01` | `Internationa..er Solutions` | `International Scanner Solutions` |
| Model/Type | `HHR-ARC-100` | `H100` | `H100` |
| Model/Type | `HHR-BIG-01` | `Industrial H..Series Alpha` | `Industrial Handheld Reader Series Alpha` |

- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-18 sampai TC-AC-DS-23: Badge Category, Brand, dan Model/Type

1. Untuk setiap baris tabel "Badge yang diuji", lakukan langkah 2 sampai 8
2. Ketik Search dengan SKU pada baris tabel, tekan Enter
3. Verifikasi badge pada kolom baris tabel menampilkan teks pada kolom "Teks badge"
4. Hover badge pada kolom baris tabel
5. Verifikasi tooltip dengan teks pada kolom "Teks tooltip" tampil saat hover
6. Pindahkan fokus keyboard ke badge pada kolom baris tabel
7. Verifikasi tooltip dengan teks pada kolom "Teks tooltip" tampil saat fokus keyboard
8. Klik `(←)` pada kotak Search

### TC-AC-DS-24: Device Name dan SKU yang panjang

9. Ketik Search `HHR-BIG-01`, tekan Enter
10. Verifikasi teks Device Name `Industrial Handheld Reader` dan SKU `HHR-BIG-01` tampil utuh, kolom menyesuaikan konten
11. Verifikasi teks Device Name dan SKU tidak memuat tanda `..`
12. Hover sel Device Name
13. Verifikasi tidak ada tooltip pada sel Device Name
14. Hover sel SKU
15. Ganti isi kotak search dengan `HHR-`, tekan Enter
16. Verifikasi tinggi baris `HHR-BIG-01` sama dengan tinggi baris `HHR-ARC-100` karena kolom bernilai tunggal tidak membungkus ke baris kedua

### TC-AC-DS-25: Header kolom tidak membungkus

17. Klik `(←)` pada kotak Search
18. Verifikasi label header `Current Stock` tampil dalam satu baris dengan tinggi header tetap
19. Verifikasi label header `Last Modified` tampil dalam satu baris dengan tinggi header tetap

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Baris tabel "Badge yang diuji" memetakan: Category pendek TC-18, Category panjang TC-19, Brand pendek TC-20, Brand panjang TC-21, Model/Type pendek TC-22, Model/Type panjang TC-23. Urutan TC dalam spec: TC-18 sampai TC-23, TC-24, TC-25.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 (perulangan), 2, 9, 15 (Search untuk menemukan baris target, R-16), 4 dan 6 (hover dan fokus yang hasilnya diasersi pada langkah berikutnya), 8, 12, 14, 17 (hover atau mengosongkan Search). Langkah 14 (hover SKU) mengikuti langkah TC-24; Expected b TC hanya menyebut sel Device Name, sehingga tooltip sel SKU tidak diasersi.
- Langkah 2 sampai 8 diulang untuk enam baris tabel "Badge yang diuji" (8b butir 7). Langkah 15 memakai Search `HHR-` agar baris `HHR-BIG-01` dan `HHR-ARC-100` berada pada halaman yang sama untuk perbandingan tinggi baris.
- Spec melewati sekitar 35 langkah (ekspansi perulangan: 1 + 7 x 6 = 43 langkah ditambah 11 langkah lain = 54). Alasan pertahanan: seluruh blok memeriksa tampilan teks badge dan lebar kolom baris List yang sama dalam satu kelas (screening tampilan, tanpa seeding dan tanpa mengubah data); langkah berulang per kolom badge diperlukan karena parameter tiap iterasi ada di tabel Prerequisites; kegagalan satu iterasi tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal dan nilai Pre-setup #29/#30 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 di environment belum diverifikasi.
  - Judul TC-24 menyebut "tanpa tooltip" untuk Device Name dan SKU, tetapi Expected b hanya menyebut sel Device Name; spec mengikuti Expected.
  - TC-24 dan TC-25 tidak menyebut lebar viewport; ukuran tinggi baris dan header diasersi pada viewport default test.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
