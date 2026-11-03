---
id: TC-AC-DS-E2E-059-edit-opsi-device-name-brand-dan-suggestion
title: "Edit SKU: Opsi Device Name Dibatasi Category, Dropdown Brand, dan Suggestion Model/Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-189
  - TC-AC-DS-190
  - TC-AC-DS-191
  - TC-AC-DS-606
coverage:
  web: automated
---

# Edit SKU: Opsi Device Name Dibatasi Category, Dropdown Brand, dan Suggestion Model/Type

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC; SKU hanya dibuka di popup Edit tanpa disimpan sehingga tidak diubah dan Last Modified tidak berubah): SKU inti #29 `HHR-ARC-200` (UHF Handheld, Arcturus, Model/Type `H200`, stok 0) beserta Model/Type SKU lain (`H100`, `T-OBJ`, `T-USR`); pohon Category #25; Device Name #26 (`UHF Handheld Reader`, `UHF Handheld Reader Pro`, `Pemindai Ujung`, `Rugged Handheld Reader`, `4-Port Fixed Reader`, `Asset TAG`); Brand Principal #27 (`Arcturus`, `International Scanner Solutions`, `Kinetia`, `Veltrix`, `Zephyr`); file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data hierarki mendalam (Data Pre-setup #42, rancangan yang disiapkan lewat seed atau Fixture BE di hook `before` dan dihapus di hook `after`): Subcategory `UHF Handheld Gudang` di bawah `UHF Handheld` dan Device Name `Pemindai Gudang` (Category `UHF Handheld Gudang`). Ketersediaannya di environment belum diverifikasi.
- Data Dinamis: tidak ada. Spec tidak menyimpan perubahan sehingga tidak membuat SKU.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Ketik Search `HHR-ARC-200`, tekan Enter
2. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`

### TC-AC-DS-189: Opsi Device Name pada Edit dibatasi ke Category terkunci beserta descendant-nya

3. Klik field Device Name
4. Verifikasi opsi hanya `UHF Handheld Reader`, `UHF Handheld Reader Pro` (Device Name berkategori `UHF Handheld`), dan `Pemindai Gudang` (Device Name berkategori `UHF Handheld Gudang`, descendant tingkat ke-4)
5. Verifikasi Device Name berkategori lain (`Pemindai Ujung`, `Rugged Handheld Reader`, `4-Port Fixed Reader`, `Asset TAG`) tidak tampil
6. Tekan Esc untuk menutup daftar opsi

### TC-AC-DS-190: Dropdown Brand pada Edit memuat Brand milik entitas login secara flat dan alfabetis

7. Klik field Brand
8. Verifikasi opsi Brand berurutan alfabetis: `Arcturus`, `International Scanner Solutions`, `Kinetia`, `Veltrix`, `Zephyr`
9. Verifikasi Brand terpilih `Arcturus` ditandai pada daftar
10. Tekan Esc untuk menutup daftar opsi

### TC-AC-DS-191: Suggestion Model/Type pada Edit mengikuti prefix case-insensitive dari SKU yang dapat dilihat

11. Kosongkan isi field Model/Type lalu ketik `t-`
12. Verifikasi suggestion memuat `T-OBJ` dan `T-USR`
13. Verifikasi nilai `H200` (Model/Type tersimpan SKU ini) tidak tampil sebagai suggestion karena tidak berawalan `t-`

### TC-AC-DS-606: Suggestion Model/Type pada Edit memuat nilai milik SKU yang berawalan sama

14. Kosongkan isi field Model/Type lalu ketik `h2`
15. Verifikasi suggestion memuat `H200` (berawalan `h2` tanpa membedakan huruf besar-kecil)
16. Verifikasi suggestion tidak memuat `H100` karena tidak berawalan `h2`
17. Klik ikon close `[✕]` pada popup Edit SKU
18. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
19. Klik `[Leave]`
20. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 dan 20 (Search untuk menemukan baris target lalu menutup Search, R-16); Esc menutup daftar opsi; langkah 17 sampai 19 menutup form dirty (Model/Type diubah) secara deterministik tanpa menyimpan, sehingga SKU `HHR-ARC-200` tidak berubah (S-08, S-09). Seluruh TC memakai satu pembukaan popup Edit `HHR-ARC-200` (bagian 3, halaman yang sama dipakai berulang).
- Anchor absence (bagian 8b butir 2): Verifikasi suggestion yang tidak tampil (`H200` pada TC-AC-DS-191, `H100` pada TC-AC-DS-606) didahului Verifikasi suggestion lain pada daftar yang sama.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-059` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Data hierarki mendalam (Data Pre-setup #42), termasuk Device Name `Pemindai Gudang`, adalah rancangan yang belum diverifikasi ada di environment; TC-AC-DS-189 Expected a bergantung padanya.
