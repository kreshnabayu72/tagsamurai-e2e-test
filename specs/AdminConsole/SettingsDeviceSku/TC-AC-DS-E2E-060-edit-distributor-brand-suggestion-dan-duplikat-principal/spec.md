---
id: TC-AC-DS-E2E-060-edit-distributor-brand-suggestion-dan-duplikat-principal
title: "Edit SKU oleh Distributor: Dropdown Brand, Suggestion Model/Type, dan Kode Duplikat SKU Principal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-219
  - TC-AC-DS-582
coverage:
  web: automated
---

# Edit SKU oleh Distributor: Dropdown Brand, Suggestion Model/Type, dan Kode Duplikat SKU Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Data Pre-setup #10) `totalControlDist_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`), password dari `Spectra.env.AC_DS_DIST_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, `Spectra.env.AC_DS_TC_PASSWORD`).
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC; SKU hanya dibuka di popup Edit tanpa disimpan sehingga tidak diubah dan Last Modified tidak berubah): SKU lokal Distributor Cakra #31 `LOC-NOR-01` (Brand `Nordik`, Model/Type `R-01`) dan `LOC-NOR-02`; Brand Distributor #28 (`Nordik`, `Orbitron`) dengan Brand Principal #27 (`Arcturus`, `Veltrix`, `Kinetia`) yang tidak boleh tampil; SKU Principal inti #29 `HHR-ARC-100` (Model/Type `H100`); SKU Distributor lain `NUS-LOC-01` (Model/Type `NM-01`) dan `MAN-LOC-01` (Model/Type `MN-01`, rancangan yang disiapkan lewat seed dan belum diverifikasi ada di environment); pohon Category #25, Device Name #26, dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak menyimpan perubahan sehingga tidak membuat SKU.
- Kemampuan teknis: jeda nyata 1 detik pada langkah 4 memenuhi debounce pemeriksaan keunikan SKU (sekitar 500 ms) dan disebut eksplisit.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-219: Distributor mengubah SKU miliknya menjadi kode SKU Principal ditolak sebagai duplikat

1. Ketik Search `LOC-NOR-02`, tekan Enter
2. Klik ⋯ pada baris `LOC-NOR-02` lalu pilih `Edit`
3. Ganti isi field SKU dengan `HHR-ARC-100`
4. Tunggu 1 detik
5. Verifikasi pesan inline "SKU already exists" tampil karena Distributor diperiksa terhadap SKU Principal dan SKU miliknya
6. Klik ikon close `[✕]` pada popup Edit SKU
7. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
8. Klik `[Leave]`

### TC-AC-DS-582: Edit SKU oleh Distributor: dropdown Brand dan suggestion Model/Type bercakupan entitas

9. Ganti isi kotak search dengan `LOC-NOR-01`, tekan Enter
10. Klik ⋯ pada baris `LOC-NOR-01` lalu pilih `Edit`
11. Klik field Brand
12. Verifikasi opsi Brand hanya `Nordik` dan `Orbitron`
13. Verifikasi `Nordik` ditandai sebagai Brand terpilih
14. Verifikasi Brand Principal (`Arcturus`, `Veltrix`, `Kinetia`) tidak tampil sebagai opsi
15. Tekan Esc untuk menutup daftar opsi
16. Kosongkan isi field Model/Type lalu ketik `R`
17. Verifikasi suggestion memuat `R-01` (SKU milik Distributor)
18. Kosongkan isi field Model/Type lalu ketik `H1`
19. Verifikasi suggestion memuat `H100` (SKU Principal)
20. Kosongkan isi field Model/Type lalu ketik `NM`
21. Verifikasi tidak ada suggestion `NM-01` karena SKU `NUS-LOC-01` milik Distributor lain
22. Kosongkan isi field Model/Type lalu ketik `MN`
23. Verifikasi tidak ada suggestion `MN-01` karena SKU `MAN-LOC-01` milik Distributor lain
24. Klik ikon close `[✕]` pada popup Edit SKU
25. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
26. Klik `[Leave]`
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1, 9, dan 27 (Search untuk menemukan baris target lalu menutup Search, R-16); Esc menutup daftar opsi; langkah 6 sampai 8 dan 24 sampai 26 menutup form dirty tanpa menyimpan, sehingga SKU Pre-setup tidak berubah (S-08, S-09).
- Anchor absence (bagian 8b butir 2): Verifikasi tidak ada suggestion `NM-01` dan `MN-01` didahului Verifikasi suggestion `R-01` dan `H100` yang tampil pada daftar yang sama; "daftar saran kosong" bukan anchor sehingga anchor diambil dari Verifikasi sebelumnya.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-060` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - SKU Distributor lain (`NUS-LOC-01` Model/Type `NM-01`, `MAN-LOC-01` Model/Type `MN-01`) pada TC-AC-DS-582 belum terverifikasi ada di environment (catatan TC).
